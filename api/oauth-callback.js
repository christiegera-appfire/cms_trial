// api/oauth-callback.js (Vercel Serverless Function)
//
// Step 2: Atlassian redirects here with a one-time authorization code. This
// function exchanges it for an access token, then bounces the browser back
// to the docs page with the token in the URL fragment (`#access_token=...`).
// Fragments never get sent to any server on the next request, which is why
// this pattern is used to hand a token to a purely static frontend without
// a shared backend session — the frontend JS reads it once, then scrubs the
// URL bar immediately.
//
// Required Vercel environment variables:
//   ATLASSIAN_CLIENT_ID
//   ATLASSIAN_CLIENT_SECRET   — set this as a Vercel secret, never commit it
//   OAUTH_CALLBACK_URL        — must exactly match the one used in oauth-start.js

module.exports = async (req, res) => {
  const clientId = process.env.ATLASSIAN_CLIENT_ID;
  const clientSecret = process.env.ATLASSIAN_CLIENT_SECRET;
  const callbackUrl = process.env.OAUTH_CALLBACK_URL;

  const { code, state, error } = req.query;

  if (error) {
    res.status(400).send(`Atlassian returned an error: ${error}`);
    return;
  }
  if (!code || !state) {
    res.status(400).send("Missing code or state parameter.");
    return;
  }

  let returnTo;
  try {
    const decoded = JSON.parse(Buffer.from(state, "base64url").toString("utf8"));
    returnTo = decoded.returnTo;
  } catch (e) {
    res.status(400).send("Invalid state parameter.");
    return;
  }
  if (!returnTo) {
    res.status(400).send("state did not contain a return_to URL.");
    return;
  }

  let tokenResp;
  try {
    tokenResp = await fetch("https://auth.atlassian.com/oauth/token", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        grant_type: "authorization_code",
        client_id: clientId,
        client_secret: clientSecret,
        code,
        redirect_uri: callbackUrl,
      }),
    });
  } catch (e) {
    res.status(502).send(`Token exchange request failed: ${e.message}`);
    return;
  }

  if (!tokenResp.ok) {
    const text = await tokenResp.text();
    res.status(502).send(`Token exchange failed (${tokenResp.status}): ${text}`);
    return;
  }

  const tokenData = await tokenResp.json();
  const accessToken = tokenData.access_token;
  if (!accessToken) {
    res.status(502).send("Token exchange response had no access_token.");
    return;
  }

  // Note: we deliberately do NOT persist tokenData.refresh_token anywhere.
  // Without a backend session store, there's nowhere safe to keep it — the
  // visitor will need to re-authorize (usually a single click) the next
  // time they submit a request. This is a real tradeoff of the no-session
  // design, not an oversight.

  const redirectUrl = `${returnTo}#access_token=${encodeURIComponent(accessToken)}`;
  res.writeHead(302, { Location: redirectUrl });
  res.end();
};
