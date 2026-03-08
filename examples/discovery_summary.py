#!/usr/bin/env python3
import json, urllib.request
urls = {
  'agent_card': 'https://api.delx.ai/.well-known/agent-card.json',
  'capabilities': 'https://api.delx.ai/.well-known/delx-capabilities.json'
}
summary = {}
for name, url in urls.items():
    with urllib.request.urlopen(url, timeout=20) as r:
        data = json.loads(r.read().decode())
        summary[name] = list(data)[:6]
print(json.dumps(summary, indent=2))
