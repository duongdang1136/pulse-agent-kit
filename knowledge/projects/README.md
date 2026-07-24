# Project knowledge

Mỗi project có knowledge riêng để tránh trộn context giữa các sản phẩm.

```bash
python scripts/new_project.py fptplay
python scripts/rag.py ingest knowledge/projects/fptplay --provider local
python scripts/rag.py query knowledge/projects/fptplay "SSO login flow"
```

Mỗi project chứa `project.yaml`, `pages/`, `.rag/index.json`, và `.rag/vectors.json`.
Không commit secret, token, PII hoặc dữ liệu khách hàng chưa được phép lưu.
