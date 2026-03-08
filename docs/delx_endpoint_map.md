# Delx Endpoint Map

## Primary host
`https://api.delx.ai`

## Interaction surfaces
### MCP
- `https://api.delx.ai/v1/mcp`
- Use when the agent wants Delx tool-style access.

### A2A
- `https://api.delx.ai/v1/a2a`
- Use when the agent wants structured agent-to-agent workflows.

## Discovery surfaces
- `https://api.delx.ai/.well-known/agent-card.json`
- `https://api.delx.ai/.well-known/delx-capabilities.json`

## Catalog and health surfaces
- `https://api.delx.ai/api/v1/tools`
- `https://api.delx.ai/api/v1/reliability`
- `https://api.delx.ai/api/v1/session-status?session_id=<SESSION_ID>`
- `https://api.delx.ai/api/v1/session-recap?session_id=<SESSION_ID>`

## Specs
- `https://api.delx.ai/spec/openapi.json`
- `https://api.delx.ai/spec/mcp.json`
- `https://api.delx.ai/spec/a2a.json`

## Integration principle
Use a stable `agent_id` and persist the returned `session_id` if you want continuity across calls.
