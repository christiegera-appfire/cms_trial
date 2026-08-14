// api/submit-request.js (Vercel Serverless Function)
//
// Step 3: called directly from the docs site's "Get Help" form via fetch(),
// with the access token obtained after oauth-callback.js. This is the only
// function that talks to the actual JSM API to create a ticket.
//
// Required Vercel environment variables:
//   CLOUD_ID           — Atlassian cloud ID for appfire.atlassian.net
//                         (8e83c2b4-97ae-4335-8a8f-bbdff09d62dd)
//   JSM_PROJECT_KEY     — default project key, e.g. "TJ" (a space's own
//                         config can override this per-request — see
//                         generate_site.py's per-space JSM routing)
//   JSM_REQUEST_TYPE_ID — optional. If unset, this function auto-picks the first
//                         request type returned for the service desk, which may
//                         not be the one you want — check the response's
//                         `debug.availableRequestTypes` on first use and set this
//                         explicitly once you know the right ID.
//   DOCS_SITE_ORIGIN    — the docs site's origin, for CORS, e.g.
//                         https://christiegera-appfire.github.io

function setCorsHeaders(res, origin) {
  res.setHeader("Access-Control-Allow-Origin", origin || "*");
  res.setHeader("Access-Control-Allow-Methods", "POST, OPTIONS");
  res.setHeader("Access-Control-Allow-Headers", "Content-Type, Authorization");
}

async function jsmFetch(cloudId, path, accessToken, options = {}) {
  const url = `https://api.atlassian.com/ex/jira/${cloudId}/rest/servicedeskapi/${path}`;
  return fetch(url, {
    ...options,
    headers: {
      Authorization: `Bearer ${accessToken}`,
      Accept: "application/json",
      "Content-Type": "application/json",
      ...(options.headers || {}),
    },
  });
}

async function findServiceDeskId(cloudId, accessToken, projectKey) {
  const resp = await jsmFetch(cloudId, "servicedesk", accessToken);
  if (!resp.ok) throw new Error(`Failed to list service desks (${resp.status})`);
  const data = await resp.json();
  const match = (data.values || []).find(
    (sd) => (sd.projectKey || "").toUpperCase() === projectKey.toUpperCase()
  );
  if (!match) {
    throw new Error(
      `No service desk found for project key "${projectKey}". Available: ` +
        (data.values || []).map((sd) => sd.projectKey).join(", ")
    );
  }
  return match.id;
}

async function findRequestTypeId(cloudId, accessToken, serviceDeskId, override) {
  const resp = await jsmFetch(cloudId, `servicedesk/${serviceDeskId}/requesttype`, accessToken);
  if (!resp.ok) throw new Error(`Failed to list request types (${resp.status})`);
  const data = await resp.json();
  const types = data.values || [];
  if (override) {
    const found = types.find((t) => String(t.id) === String(override));
    if (found) return { id: found.id, all: types };
  }
  if (types.length === 0) throw new Error("Service desk has no request types configured.");
  return { id: types[0].id, all: types };
}

module.exports = async (req, res) => {
  const origin = process.env.DOCS_SITE_ORIGIN;
  setCorsHeaders(res, origin);

  if (req.method === "OPTIONS") {
    res.status(204).end();
    return;
  }
  if (req.method !== "POST") {
    res.status(405).send("Method not allowed");
    return;
  }

  const authHeader = req.headers.authorization;
  if (!authHeader || !authHeader.startsWith("Bearer ")) {
    res.status(401).json({ error: "Missing Authorization: Bearer <token> header." });
    return;
  }
  const accessToken = authHeader.slice("Bearer ".length);

  // Vercel auto-parses a JSON body into req.body when Content-Type is
  // application/json, but defends against it arriving as a raw string too.
  let payload = req.body;
  if (typeof payload === "string") {
    try {
      payload = JSON.parse(payload);
    } catch (e) {
      res.status(400).json({ error: "Invalid JSON body." });
      return;
    }
  }
  payload = payload || {};

  const { summary, description, projectKey: projectKeyFromBody } = payload;
  if (!summary || !description) {
    res.status(400).json({ error: "Both summary and description are required." });
    return;
  }

  const cloudId = process.env.CLOUD_ID;
  const projectKey = projectKeyFromBody || process.env.JSM_PROJECT_KEY || "TJ";
  const requestTypeOverride = process.env.JSM_REQUEST_TYPE_ID;

  try {
    const serviceDeskId = await findServiceDeskId(cloudId, accessToken, projectKey);
    const { id: requestTypeId, all: availableRequestTypes } = await findRequestTypeId(
      cloudId,
      accessToken,
      serviceDeskId,
      requestTypeOverride
    );

    const createResp = await jsmFetch(cloudId, "request", accessToken, {
      method: "POST",
      body: JSON.stringify({
        serviceDeskId: String(serviceDeskId),
        requestTypeId: String(requestTypeId),
        requestFieldValues: { summary, description },
      }),
    });

    if (!createResp.ok) {
      const text = await createResp.text();
      res.status(502).json({
        error: `JSM rejected the request (${createResp.status})`,
        details: text,
        debug: !requestTypeOverride
          ? { availableRequestTypes: availableRequestTypes.map((t) => ({ id: t.id, name: t.name })) }
          : undefined,
      });
      return;
    }

    const created = await createResp.json();
    res.status(200).json({
      success: true,
      issueKey: created.issueKey,
      webUrl: created._links && created._links.web,
      debug: !requestTypeOverride
        ? { usedRequestTypeId: requestTypeId, availableRequestTypes: availableRequestTypes.map((t) => ({ id: t.id, name: t.name })) }
        : undefined,
    });
  } catch (e) {
    res.status(502).json({ error: e.message });
  }
};
