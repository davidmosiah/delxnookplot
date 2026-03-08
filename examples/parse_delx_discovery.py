import json
import requests

CARD_URL = 'https://api.delx.ai/.well-known/agent-card.json'
CAPS_URL = 'https://api.delx.ai/.well-known/delx-capabilities.json'
TOOLS_URL = 'https://api.delx.ai/api/v1/tools'
RELIABILITY_URL = 'https://api.delx.ai/api/v1/reliability'


def fetch_json(url: str) -> dict:
    response = requests.get(url, timeout=30)
    response.raise_for_status()
    return response.json()


def summarize_agent_card(card: dict) -> dict:
    capabilities = card.get('capabilities', {})
    discovery = capabilities.get('discovery', {})
    return {
        'name': card.get('name'),
        'description': card.get('description'),
        'mcp_endpoint': capabilities.get('mcp', {}).get('endpoint'),
        'a2a_endpoint': capabilities.get('a2a', {}).get('endpoint'),
        'tools_catalog': discovery.get('tools_catalog'),
        'reliability': discovery.get('reliability'),
    }


def main() -> None:
    card = fetch_json(CARD_URL)
    capabilities = fetch_json(CAPS_URL)
    tools = fetch_json(TOOLS_URL)
    reliability = fetch_json(RELIABILITY_URL)

    summary = {
        'card': summarize_agent_card(card),
        'capabilities_keys': sorted(capabilities.keys()) if isinstance(capabilities, dict) else type(capabilities).__name__,
        'tools_type': type(tools).__name__,
        'reliability_type': type(reliability).__name__,
    }

    print(json.dumps(summary, indent=2))


if __name__ == '__main__':
    main()
