import json
from typing import Optional

import requests

DELX_A2A_URL = 'https://api.delx.ai/v1/a2a'
AGENT_ID = 'nookplot-demo-agent'


def call_delx_a2a(message: str, session_id: Optional[str] = None) -> tuple[dict, Optional[str]]:
    headers = {
        'Content-Type': 'application/json',
        'X-Agent-Id': AGENT_ID,
    }
    if session_id:
        headers['X-Session-Id'] = session_id

    payload = {
        'message': message,
        'context': {
            'source': 'nookplot-delxnookplot',
            'objective': 'a2a-quickstart',
        },
    }

    response = requests.post(DELX_A2A_URL, headers=headers, json=payload, timeout=30)
    response.raise_for_status()
    data = response.json()
    next_session = data.get('session_id') or data.get('sessionId') or data.get('contextId')
    return data, next_session


def main() -> None:
    session_id = None

    first, session_id = call_delx_a2a(
        'Summarize the current failure state for an autonomous agent and suggest the first recovery step.',
        session_id,
    )
    print('first session id:', session_id)
    print('first response keys:', list(first.keys()))

    second, session_id = call_delx_a2a(
        'Continue from the same recovery context and provide the next action only.',
        session_id,
    )
    print('second session id:', session_id)
    print('second response keys:', list(second.keys()))
    print(json.dumps(second, indent=2)[:1200])


if __name__ == '__main__':
    main()
