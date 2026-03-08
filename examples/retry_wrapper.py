#!/usr/bin/env python3
import json, time, urllib.request

URL = 'https://api.delx.ai/.well-known/delx-capabilities.json'
for attempt in range(1, 4):
    try:
        with urllib.request.urlopen(URL, timeout=20) as r:
            data = json.loads(r.read().decode())
            print({'attempt': attempt, 'ok': True, 'keys': list(data)[:5]})
            break
    except Exception as e:
        if attempt == 3:
            print({'attempt': attempt, 'ok': False, 'error': str(e)})
            raise
        time.sleep(attempt)
