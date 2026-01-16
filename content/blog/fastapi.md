+++
title = "Fastapi"
date = "2026-01-15T00:22:02+01:00"
+++

Flask or FastAPI? Both! For fast prototypes Flask is still a damn good tool, but for "modern" APIs FastAPI might be better.

Create a minimal health check API using FastAPI:
```bash
pip install "fastapi[standard]"
```

```python
from fastapi import FastAPI

app = FastAPI(
        title="TEST",
        description="TEST Project",
        version="0.1",
        )

@app.get("/health")
def health_check():
    return {"status": "ok"}

```

run FastAPI via:
```bash
fastapi dev FILENAME
```
