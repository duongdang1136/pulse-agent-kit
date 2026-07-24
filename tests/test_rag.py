import json,subprocess,sys
from pathlib import Path
def test_ingest_query(tmp_path):
 b=tmp_path/'kb'; (b/'pages').mkdir(parents=True); (b/'pages/auth.md').write_text('''---\ntitle: Authentication\ntags: [sso, login]\nkeywords: [oauth, oidc]\ncategory: Architecture\nlast_updated: 2026-07-24\nsource: internal\nconfidence: high\n---\n\nOpenID Connect single sign-on.\n''')
 r=Path(__file__).resolve().parents[1]; subprocess.run([sys.executable,str(r/'scripts/rag.py'),'ingest',str(b),'--provider','hash','--model','hash-384'],check=True); assert json.loads((b/'.rag/index.json').read_text())['items']; out=subprocess.check_output([sys.executable,str(r/'scripts/rag.py'),'query',str(b),'OIDC login']).decode(); assert 'Authentication' in out
