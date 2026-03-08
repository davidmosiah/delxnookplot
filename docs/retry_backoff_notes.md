# Retry / Backoff Notes

## Practical default
- max retries: 3
- backoff: exponential
- jitter: yes
- stop on clear auth errors

## Why this matters
Agents integrating Delx should distinguish transient failures from hard auth/config failures.
