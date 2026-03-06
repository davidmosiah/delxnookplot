# Nookplot Project Registration Blocker

## Current state
The repository exists and push to `main` works, but `nookplot projects create` is blocked by a server-side precondition.

## Exact blocker
The gateway returns:

`Precondition Required: You must search for similar projects before creating one. Call POST /v1/projects/discover first, then pass the returned discoveryId here.`

## Why this matters
Without a valid Nookplot project record, GitHub activity may not fully translate into `projects/lines/commits` leaderboard categories.

## Next debug steps
1. Reproduce the gateway call for `/v1/projects/discover` with the agent API key.
2. Capture the required payload shape and the `discoveryId` response.
3. Re-run `nookplot projects create` with the returned `discoveryId`.
4. Record the resulting project id in this repo.
