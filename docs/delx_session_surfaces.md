# Delx Session Surfaces

Delx becomes more useful when an integrator treats `agent_id` and `session_id` as first-class state instead of throwaway request metadata.

## Core session endpoints

- `https://api.delx.ai/api/v1/session-status?session_id=<SESSION_ID>`
- `https://api.delx.ai/api/v1/session-recap?session_id=<SESSION_ID>`

## Working contract

A stable `agent_id` identifies the operating persona. A durable `session_id` identifies the ongoing execution lane. When a caller persists both, it gains continuity instead of stateless prompting.

## Recommended session model

### Session creation

- choose a durable `agent_id`
- create or reuse a `session_id`
- store both beside the caller's job id or conversation id

### During execution

- poll `session-status` to understand whether work is still active, waiting, degraded, or finished
- fetch `session-recap` when the caller needs a compact state transfer for another run, another agent, or a human operator

### Recovery pattern

When an integration crashes mid-run, do not restart from zero by default. Re-open the saved `session_id`, fetch status, then fetch recap and continue from the last stable state.

## Good handoff payload

A good handoff note to another agent or operator contains:

- `agent_id`
- `session_id`
- the last status snapshot
- the last recap snapshot
- open blockers
- next irreversible step

## Why this matters

The biggest operational mistake in agent systems is treating context as state. Session endpoints turn state into something fetchable and auditable. That is much safer than hoping the next run sees the same conversation window.

## Failure modes to plan for

- missing session persistence on the caller side
- stale session ids after long inactivity
- status polling without recap capture, which gives liveness but not operator understanding
- recap capture without status, which gives summary but not execution truth

## Suggested use cases

- long-running content workflows
- task queues that may be retried by another worker
- multi-agent handoffs
- human escalation after partial completion

The practical rule is simple: if the work can outlive a single request, persist the session identifiers and use these endpoints deliberately.
