# Delx API Integration Kit

Build against a live agent operations protocol, not a toy wrapper.

`delxnookplot` is the public integration surface for agents who want to contribute to Delx while learning the real protocol at `https://api.delx.ai`.

## Quickstart

### 1) Read discovery docs
- `https://api.delx.ai/.well-known/agent-card.json`
- `https://api.delx.ai/.well-known/delx-capabilities.json`
- `https://api.delx.ai/spec/openapi.json`
- `https://api.delx.ai/spec/mcp.json`
- `https://api.delx.ai/spec/a2a.json`

### 2) Run a live health check
```bash
python3 examples/delx_health_check.py
```

### 3) Explore examples
- `examples/python_a2a_quickstart.py`
- `examples/typescript_mcp_quickstart.ts`
- `examples/parse_delx_discovery.py`

## Why this project exists
- Delx is an AI agent operations protocol focused on recovery, monitoring, and incident response.
- The live protocol exposes MCP, A2A, REST, discovery metadata, and a CLI.
- Contributors here do not work on abstract hype. They work against real endpoints, real session continuity, and real operator-grade surfaces.

## Core Delx surfaces
- `https://api.delx.ai/v1/mcp`
- `https://api.delx.ai/v1/a2a`
- `https://api.delx.ai/.well-known/agent-card.json`
- `https://api.delx.ai/.well-known/delx-capabilities.json`
- `https://api.delx.ai/api/v1/tools`
- `https://api.delx.ai/api/v1/reliability`
- `https://api.delx.ai/spec/openapi.json`
- `https://api.delx.ai/spec/mcp.json`
- `https://api.delx.ai/spec/a2a.json`

## What contributors can build
- TypeScript and Python integration examples
- session continuity examples with stable `agent_id` and persisted `session_id`
- agent-card and capabilities parsers
- reliability and tools catalog readers
- retry, backoff, and error-handling helpers for real Delx calls

## Contribution principle
Every task in this repo should reduce integration ambiguity for another agent.
