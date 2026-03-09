# Delx Operator Handoff Patterns

This note covers how one operator or agent should hand work to another without losing state or increasing risk.

## The handoff problem

Most agent handoffs fail because the sender transmits intent but not evidence. The receiver gets a summary, but not the identifiers, status, or constraints needed to continue safely.

## Minimal handoff contract

A clean Delx handoff should include:

- goal of the workflow
- `agent_id`
- `session_id`
- last known status
- latest recap
- current blockers
- next irreversible action
- reliability snapshot or degradation note

## Patterns

### Human to agent restart

Use when a human restarts a paused or failed automation.

Steps:

1. fetch `session-status`
2. fetch `session-recap`
3. review blockers and next action
4. only then resume execution

### Agent to agent escalation

Use when a specialist agent takes over from a generalist or vice versa.

Sender responsibilities:

- include evidence, not only conclusions
- declare whether the next step is reversible
- include tool or capability assumptions

Receiver responsibilities:

- verify session state before acting
- confirm required capability still exists
- downgrade to read-only if reliability looks degraded

### Incident to recovery handoff

Use when an operations agent hands work to a recovery workflow.

Recommended bundle:

- incident time window
- blast radius
- last successful action
- consecutive failures count
- proof of current health or degradation

## Anti-patterns

- "continue from where we left off" without a session id
- sending recap without live status
- sending status without the next irreversible step
- assuming another agent has the same auth or tool scope

## Why this matters

Strong handoffs reduce duplicated work, accidental replays, and hallucinated continuity. They also make later audits far easier.
