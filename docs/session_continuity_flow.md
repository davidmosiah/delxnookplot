# Delx Session Continuity Flow

## Why continuity matters
Delx is more useful when the caller keeps the same context across turns instead of treating every call like a fresh session.

## Minimal rule set
1. Choose a stable `agent_id`.
2. Make the first request to `https://api.delx.ai/v1/mcp` or `https://api.delx.ai/v1/a2a`.
3. Capture the returned `session_id`.
4. Reuse that `session_id` on later turns.
5. Query recap or status endpoints when you need a compact summary:
   - `https://api.delx.ai/api/v1/session-status?session_id=<SESSION_ID>`
   - `https://api.delx.ai/api/v1/session-recap?session_id=<SESSION_ID>`

## Example call flow
- turn 1: ask Delx for incident triage
- turn 2: ask Delx for recovery priorities using the same `session_id`
- turn 3: query recap and persist it in your own memory layer

## What breaks continuity
- changing `agent_id` between calls
- failing to persist `session_id`
- opening parallel sessions without tracking which `session_id` belongs to which thread

## What a contributor can improve here
- tiny client wrappers
- helper utilities for storing session ids
- docs showing where session id can live in a real agent runtime
