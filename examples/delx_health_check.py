#!/usr/bin/env python3
import json
import urllib.request

URLS = [
    'https://api.delx.ai/.well-known/agent-card.json',
    'https://api.delx.ai/.well-known/delx-capabilities.json',
    'https://api.delx.ai/spec/openapi.json',
]

for url in URLS:
    try:
        with urllib.request.urlopen(url, timeout=20) as r:
            data = json.loads(r.read().decode())
            print(f'OK {url} keys={list(data)[:5]}')
    except Exception as e:
        print(f'ERR {url} {type(e).__name__}: {e}')
