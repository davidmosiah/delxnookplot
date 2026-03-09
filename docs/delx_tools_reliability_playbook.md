# Delx Tools and Reliability Playbook

This note treats the Delx API as an operator surface, not only a demo endpoint.

## Core surfaces

- `https://api.delx.ai/api/v1/tools`
- `https://api.delx.ai/api/v1/reliability`
- `https://api.delx.ai/.well-known/agent-card.json`
- `https://api.delx.ai/.well-known/delx-capabilities.json`

## Why separate tools from reliability

The tools catalog answers "what can this agent do right now?" The reliability surface answers "how safe is it to depend on it for a real workflow?" Operators need both before wiring one agent into another.

## Recommended operator checks

1. Pull the tools catalog and record the tool names, categories, and obvious side effects.
2. Pull reliability data and record the current status, dependency health, and any degradation notes.
3. Compare both with the public agent card so the public claim and the live surface stay aligned.
4. Save the evidence links in the same incident or integration note so another agent can audit the decision later.

## Minimal evidence bundle

A lightweight evidence bundle for an integration review should contain:

- timestamp of the fetch
- tools endpoint response summary
- reliability endpoint response summary
- agent-card version or hash
- any mismatch between public claim and live state

## Practical workflow

### Pre-integration gate

Use the reliability endpoint before first use or after a meaningful outage. If reliability shows degraded state, treat the target agent as read-only or avoid irreversible actions.

### Post-change gate

After an agent owner adds tools or changes auth rules, fetch tools and reliability again and diff the responses. Do not assume compatibility across silent changes.

### Incident support gate

During incidents, use the tools endpoint to answer capability scope and the reliability endpoint to answer blast radius. This avoids guessing what the dependent agent can still do safely.

## Common mistakes

- Using the tools catalog as a health signal.
- Reading the agent card only once and never comparing it with live surfaces.
- Treating a healthy root endpoint as proof that every tool behind it is healthy.
- Forgetting to capture evidence, which makes future handoff or review weak.

## Suggested automation

A useful recurring job is a drift detector that fetches tools, reliability, and the agent card together, then flags:

- new tools without documentation
- removed tools without migration note
- reliability degradation without operator annotation
- mismatch between public capabilities and live tools

That job is valuable because most integration failures are not hard outages. They are silent drift.
