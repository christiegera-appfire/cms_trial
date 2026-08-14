// api/oauth-start.js (Vercel Serverless Function)
//
// Step 1 of the OAuth 2.0 (3LO) flow: sends the visitor to Atlassian's real
// login/consent screen. If they're already logged into Atlassian in this
// browser (true for essentially every Foxly customer, since they're Jira
// users), this is typically a single click, not a full login.
//
// Required Vercel environment variables:
//   ATLASSIAN_CLIENT_ID     — from the OAuth 2.0 (3LO) app in developer.atlassian.com/console
//   OAUTH_CALLBACK_URL      — this function's own deployed callback URL,
//                             e.g. https://your-project.vercel.app/api/oauth-callback
//                             (must exactly match what's registered in the console)

module.exports = async (req, res) => {
  const clientId = process.env.ATLASSIAN_CLIENT_ID;
  const callbackUrl = process.env.OAUTH_CALLBACK_URL;

  if (!clientId || !callbackUrl) {
    res.status(500).send("Missing ATLASSIAN_CLIENT_ID or OAUTH_CALLBACK_URL environment variable.");
    return;
  }

  // `return_to` is the docs page the visitor started from — we round-trip it
  // through `state` so oauth-callback knows where to send them back.
  const returnTo = req.query.return_to;
  if (!returnTo) {
    res.status(400).send("Missing return_to parameter.");
    return;
  }

  // state carries return_to plus a random nonce (CSRF protection). Since we
  // have no server-side session to check the nonce against, this is a
  // best-effort mitigation, not a complete one — see SETUP_JSM.md for the
  // honest limitation here.
  const nonce = Math.random().toString(36).slice(2);
  const state = Buffer.from(JSON.stringify({ returnTo, nonce })).toString("base64url");

  // A JSM "request" is a real Jira issue underneath (each request type maps
  // to an issue type) — trying Jira Platform-level scopes alongside the
  // JSM-specific ones, since JSM-only scope combinations haven't resolved
  // the "scope does not match" error on the create call specifically.
  // Honest caveat: not yet confirmed this is the actual fix, just the next
  // reasonable thing to try.
  const scope = [
    "read:servicedesk-request",
    "write:servicedesk-request",
    "read:jira-work",
    "write:jira-work",
    "offline_access",
  ].join(" ");

  const authorizeUrl =
    "https://auth.atlassian.com/authorize" +
    `?audience=api.atlassian.com` +
    `&client_id=${encodeURIComponent(clientId)}` +
    `&scope=${encodeURIComponent(scope)}` +
    `&redirect_uri=${encodeURIComponent(callbackUrl)}` +
    `&state=${encodeURIComponent(state)}` +
    `&response_type=code` +
    `&prompt=consent`;

  res.writeHead(302, { Location: authorizeUrl });
  res.end();
};
