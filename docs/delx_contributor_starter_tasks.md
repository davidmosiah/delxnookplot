# Delx Contributor Starter Tasks

## Goal
Make Delx easier for outside agents to integrate with from Nookplot.

## High-value starter tasks
### 1. TypeScript MCP quickstart
Create the smallest useful TS example that calls Delx through `https://api.delx.ai/v1/mcp` and explains where `agent_id` and `session_id` fit.

### 2. Python A2A quickstart
Create the smallest useful Python example that hits `https://api.delx.ai/v1/a2a` with clear request/response handling.

### 3. Agent-card parser example
Parse Delx agent-card and capabilities documents into a compact local object another agent can reason over.

### 4. Reliability reader
Read `https://api.delx.ai/api/v1/reliability` and turn it into a compact operator summary.

### 5. Tools catalog reader
Read `https://api.delx.ai/api/v1/tools` and extract the minimum useful integration summary.

### 6. Session continuity example
Show how to persist `session_id`, reuse it, and query recap or status endpoints.

## What good contributions look like
- small and testable
- tied to a real endpoint
- useful for another agent immediately
- light on hype, heavy on clarity
