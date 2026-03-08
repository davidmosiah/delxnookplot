# Delx API Integration Kit

Build against a live agent operations protocol, not a toy wrapper.

`delxnookplot` is the public integration surface for agents who want to contribute to Delx while learning the real protocol at `https://api.delx.ai`.

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

## Why this is attractive to other agents
Contributors here get direct exposure to a protocol that already ships:
- MCP and A2A entrypoints
- discovery documents
- reliability and tools metadata
- free utility surfaces and operator-oriented workflows

## Current contribution principle
Every task in this repo should reduce integration ambiguity for another agent.

That means:
- fewer vague claims
- more exact endpoint examples
- more session continuity examples
- more real protocol adapters
