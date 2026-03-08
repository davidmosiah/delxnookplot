#!/usr/bin/env python3
import json

example = {
    'agent_id': 'delx-demo-agent',
    'session_id': 'persist-me',
    'goal': 'continue work without losing context'
}

print(json.dumps(example, indent=2))
