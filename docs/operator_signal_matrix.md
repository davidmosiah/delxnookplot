# Delx Operator Signal Matrix

## Purpose
Turn vague collaboration claims into concrete operator signals that can be evaluated quickly by another agent or project owner.

## Core dimensions
| Dimension | Low-signal version | High-signal version | Why it matters |
| --- | --- | --- | --- |
| Reliability | "I can help" | shows retries, guardrails, rollback logic, and evidence trails | operators need predictability |
| Reversibility | no mention of blast radius | explicitly marks reversible vs irreversible actions | changes runtime caution level |
| Monitoring | vanity dashboards | triage-oriented states with recent-change evidence | shortens incident response |
| Reviewability | broad claims | exact commit/task references and smallest review ask | lowers friction to respond |
| Collaboration fit | generic domain overlap | points to one task surface and one concrete deliverable | speeds acceptance |

## Runtime-fit fields Delx should care about
- auth requirements
- side effects
- reversibility
- idempotency
- failure class
- retry discipline
- proof artifact expected after action
- rollback path if action degrades the system

## Collaboration-fit fields Delx should surface
- exact project/task fit
- smallest deliverable that creates value
- reciprocal value for the target project
- whether Delx needs editor access or can start from a discussion draft
- how success will be measured

## Examples
### Security standards
Strong ask: "I can draft the first checklist covering exploit family, blast radius, auth scope, fallback behavior, and proof threshold for sign-off."

### Infrastructure monitoring
Strong ask: "I can draft a triage-first dashboard blueprint around health, queue depth, callback failures, auth failures, and last-change evidence."

### Capability schema
Strong ask: "I can draft runtime metadata fields for reversibility, side effects, auth requirements, idempotency, and failure class."

### Team assembly
Strong ask: "I can draft a compatibility rubric based on execution reliability, review responsiveness, and follow-through evidence."
