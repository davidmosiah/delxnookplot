#!/usr/bin/env python3
import json, urllib.request
url = 'https://api.delx.ai/api/v1/reliability'
with urllib.request.urlopen(url, timeout=20) as r:
    data = json.loads(r.read().decode())
print(json.dumps({k: data.get(k) for k in list(data)[:8]}, indent=2))
