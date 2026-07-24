#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json, os, re
from datetime import date
from pathlib import Path
import numpy as np, requests, yaml
TTL={"Security":30,"TechStack":90,"Framework":90,"Architecture":180,"Domain":365,"Product":365,"Process":0}
def parse(text):
 m=re.match(r"^---\s*\n(.*?)\n---\s*\n?(.*)$",text,re.S)
 if not m: raise ValueError("missing YAML frontmatter")
 return yaml.safe_load(m.group(1)) or {},m.group(2).strip()
def chunk(body,size=1200,overlap=180):
 ps=[p.strip() for p in re.split(r"\n\s*\n",body) if p.strip()]; out=[]; cur=""
 for p in ps:
  if cur and len(cur)+len(p)+2>size: out.append(cur); cur=cur[-overlap:]+"\n\n"+p
  else: cur=(cur+"\n\n"+p).strip()
 if cur: out.append(cur)
 return out
def hash_embed(texts,dims=384):
 a=np.zeros((len(texts),dims),dtype=np.float32)
 for i,t in enumerate(texts):
  for tok in re.findall(r"[\w-]+",t.lower()):
   h=int(hashlib.sha256(tok.encode()).hexdigest()[:16],16); a[i,h%dims]+=1 if (h>>8)&1 else -1
 n=np.linalg.norm(a,axis=1,keepdims=True); n[n==0]=1
 return a/n
def embed(texts,provider,model):
 if provider=="hash": return hash_embed(texts)
 if provider=="local":
  try: from sentence_transformers import SentenceTransformer
  except ImportError as e: raise SystemExit("Install sentence-transformers or use --provider openai/hash") from e
  return np.asarray(SentenceTransformer(model).encode(texts,normalize_embeddings=True),dtype=np.float32)
 if provider=="openai":
  key=os.getenv("OPENAI_API_KEY"); base=os.getenv("OPENAI_BASE_URL","https://api.openai.com/v1")
  if not key: raise SystemExit("OPENAI_API_KEY is required")
  r=requests.post(base.rstrip("/")+"/embeddings",headers={"Authorization":"Bearer "+key},json={"model":model,"input":texts},timeout=120); r.raise_for_status()
  return np.asarray([x["embedding"] for x in r.json()["data"]],dtype=np.float32)
 raise SystemExit("unknown provider")
def ingest(base,provider,model):
 pages=base/"pages"; rag=base/".rag"; rag.mkdir(parents=True,exist_ok=True); items=[]; texts=[]; ids=[]
 for path in sorted(pages.glob("*.md")):
  meta,body=parse(path.read_text(encoding="utf-8"))
  for req in ("title","category","last_updated"):
   if not meta.get(req): raise ValueError(f"{path}: missing {req}")
  for n,c in enumerate(chunk(body)):
   cid=f"{path.stem}#{n}"; ids.append(cid); texts.append(" ".join([str(meta["title"])," ".join(meta.get("tags",[]) or [])," ".join(meta.get("keywords",[]) or []),c]))
   items.append({"id":cid,"document_id":path.stem,"chunk":n,"title":meta["title"],"path":str(path.relative_to(base)),"tags":meta.get("tags",[]),"keywords":meta.get("keywords",[]),"category":meta["category"],"last_updated":str(meta["last_updated"]),"ttl_days":TTL.get(meta["category"],90),"text":c})
 vec=embed(texts,provider,model) if texts else np.empty((0,0))
 (rag/"index.json").write_text(json.dumps({"version":"2.0","updated_at":date.today().isoformat(),"embedding":{"provider":provider,"model":model,"dimensions":int(vec.shape[1]) if vec.size else 0},"items":items},ensure_ascii=False,indent=2))
 (rag/"vectors.json").write_text(json.dumps({"version":"1.0","vectors":{k:v.tolist() for k,v in zip(ids,vec)}},separators=(",",":")))
 print(f"Indexed {len(items)} chunks")
def query(base,text,topk):
 idx=json.loads((base/".rag/index.json").read_text()); vs=json.loads((base/".rag/vectors.json").read_text())["vectors"]; cfg=idx["embedding"]; q=embed([text],cfg["provider"],cfg["model"])[0]; scored=[]
 for item in idx["items"]:
  v=np.asarray(vs[item["id"]],dtype=np.float32); scored.append((float(np.dot(q,v)/(np.linalg.norm(q)*np.linalg.norm(v)+1e-12)),item))
 for s,i in sorted(scored,key=lambda x:x[0],reverse=True)[:topk]: print(json.dumps({"score":round(s,4),**i},ensure_ascii=False))
p=argparse.ArgumentParser(); sub=p.add_subparsers(dest="cmd",required=True); a=sub.add_parser("ingest"); a.add_argument("base",type=Path); a.add_argument("--provider",choices=["local","openai","hash"],default="local"); a.add_argument("--model",default="sentence-transformers/all-MiniLM-L6-v2"); q=sub.add_parser("query"); q.add_argument("base",type=Path); q.add_argument("text"); q.add_argument("--top-k",type=int,default=5); x=p.parse_args(); ingest(x.base,x.provider,x.model) if x.cmd=="ingest" else query(x.base,x.text,x.top_k)
