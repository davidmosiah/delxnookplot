# Delx Error Taxonomy

A production integration should classify Delx failures by operator action, not just by HTTP code.

## Operator-oriented buckets

### Auth and policy errors

Examples:

- missing auth header
- invalid token or expired credential
- capability blocked by policy

Operator action:

- rotate or restore credentials
- verify scope and permission model
- do not retry blindly until auth state is fixed

### Caller contract errors

Examples:

- malformed request body
- missing required fields
- invalid `session_id`
- unsupported capability or version mismatch

Operator action:

- fix request construction
- validate against public specs before re-sending
- add schema validation on the caller side

### Rate and quota pressure

Examples:

- burst beyond quota
- concurrency saturation
- gateway throttling

Operator action:

- exponential backoff
- queue smoothing
- degrade non-critical features first

### Dependency or downstream failures

Examples:

- model provider timeout
- tool dependency unavailable
- upstream MCP/A2A dependency degraded

Operator action:

- check reliability surface
- mark the workflow degraded
- switch to reversible or read-only behavior when possible

### State and continuity failures

Examples:

- caller lost `session_id`
- recap unavailable when needed
- status stale after a crash

Operator action:

- treat state recovery as a first-class recovery path
- fetch status and recap before restarting work
- avoid duplicate irreversible actions

## Retry guidance

### Safe to retry

- transient 5xx
- network timeout
- temporary dependency failure
- rate limiting with explicit wait/backoff

### Unsafe to retry without inspection

- auth failures
- request contract failures
- irreversible tool actions with unknown completion state
- stale session state after crash

## Logging contract

Every caller should log at least:

- endpoint called
- request class
- status code
- retry count
- `session_id` if present
- whether the action was reversible or irreversible

## Why this taxonomy helps

A raw `500` is not an operator plan. A failure bucket tells the next agent or human what to do next and whether retrying is safe.
