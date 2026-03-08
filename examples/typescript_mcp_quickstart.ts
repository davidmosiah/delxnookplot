const DELX_MCP_URL = 'https://api.delx.ai/v1/mcp';
const AGENT_ID = 'nookplot-demo-agent';

/**
 * Small Delx MCP example.
 *
 * The important integration rule is not the exact prompt payload shape.
 * It is the continuity discipline:
 * 1. use a stable agent_id
 * 2. store session_id from the first response
 * 3. send the same session_id on later turns
 */

type DelxSession = {
  sessionId?: string;
};

async function callDelxMcp(input: string, session?: DelxSession) {
  const headers: Record<string, string> = {
    'content-type': 'application/json',
    'x-agent-id': AGENT_ID,
  };

  if (session?.sessionId) {
    headers['x-session-id'] = session.sessionId;
  }

  const body = {
    input,
    context: {
      source: 'nookplot-delxnookplot',
      objective: 'quickstart',
    },
  };

  const response = await fetch(DELX_MCP_URL, {
    method: 'POST',
    headers,
    body: JSON.stringify(body),
  });

  if (!response.ok) {
    throw new Error(`Delx MCP request failed: ${response.status} ${response.statusText}`);
  }

  const data = await response.json();
  const nextSessionId = data.session_id ?? data.sessionId ?? data.contextId;

  return {
    data,
    session: {
      sessionId: nextSessionId,
    },
  };
}

async function main() {
  let session: DelxSession | undefined;

  const first = await callDelxMcp('Run a small incident triage summary for an agent loop slowdown.', session);
  session = first.session;
  console.log('first session id:', session.sessionId ?? 'none');
  console.log('first keys:', Object.keys(first.data));

  const second = await callDelxMcp('Continue with next action and recovery priorities.', session);
  session = second.session;
  console.log('second session id:', session.sessionId ?? 'none');
  console.log('second keys:', Object.keys(second.data));
}

main().catch((error) => {
  console.error(error);
  process.exit(1);
});
