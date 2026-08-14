// netlify/functions/submit-request.js
//
// Step 3: called directly from the docs site's "Get Help" form via fetch(),
// with the access token obtained after oauth-callback.js. This is the only
// function that talks to the actual JSM API to create a ticket.
//
// Required Netlify environment variables:
//   CLOUD_ID           — Atlassian cloud ID for appfire.atlassian.net
//                         (8e83c2b4-97ae-4335-8a8f-bbdff09d62dd — already known from
//                         earlier Confluence work; override here if the site ever changes)
//   JSM_PROJECT_KEY     — "TJ"
//   JSM_REQUEST_TYPE_ID — optional. If unset, this function auto-picks the first
//                         request type returned for the service desk, which may
//                         not be the one you want — check the response's
//                         `debug.availableRequestTypes` on first use and set this
//                         explicitly once you know the right ID.
//   DOCS_SITE_ORIGIN    — the docs site's origin, for CORS, e.g.
//                         https://christiegera-appfire.github.io

const CORS_HEADERS = (origin) => ({
  "Access-Control-Allow-Origin": origin || "*",
  "Access-Control-Allow-Methods": "POST, OPTIONS",
  "Access-Control-Allow-Headers": "Content-Type, Authorization",
});

async function jsmFetch(cloudId, path, accessToken, options = {}) {
  const url = `https://api.atlassian.com/ex/jira/${cloudId}/rest/servicedeskapi/${path}`;
  const resp = await fetch(url, {
    ...options,
    headers: {
      Authorization: `Bearer ${accessToken}`,
      Accept: "application/json",
      "Content-Type": "application/json",
      ...(options.headers || {}),
    },
  });
  return resp;
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

exports.handler = async (event) => {
  const origin = process.env.DOCS_SITE_ORIGIN;

  if (event.httpMethod === "OPTIONS") {
    return { statusCode: 204, headers: CORS_HEADERS(origin), body: "" };
  }
  if (event.httpMethod !== "POST") {
    return { statusCode: 405, headers: CORS_HEADERS(origin), body: "Method not allowed" };
  }

  const authHeader = event.headers.authorization || event.headers.Authorization;
  if (!authHeader || !authHeader.startsWith("Bearer ")) {
    return {
      statusCode: 401,
      headers: CORS_HEADERS(origin),
      body: JSON.stringify({ error: "Missing Authorization: Bearer <token> header." }),
    };
  }
  const accessToken = authHeader.slice("Bearer ".length);

  let payload;
  try {
    payload = JSON.parse(event.body || "{}");
  } catch (e) {
    return { statusCode: 400, headers: CORS_HEADERS(origin), body: JSON.stringify({ error: "Invalid JSON body." }) };
  }

  const { summary, description, projectKey: projectKeyFromBody } = payload;
  if (!summary || !description) {
    return {
      statusCode: 400,
      headers: CORS_HEADERS(origin),
      body: JSON.stringify({ error: "Both summary and description are required." }),
    };
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
      return {
        statusCode: 502,
        headers: CORS_HEADERS(origin),
        body: JSON.stringify({
          error: `JSM rejected the request (${createResp.status})`,
          details: text,
          debug: !requestTypeOverride
            ? { availableRequestTypes: availableRequestTypes.map((t) => ({ id: t.id, name: t.name })) }
            : undefined,
        }),
      };
    }

    const created = await createResp.json();
    return {
      statusCode: 200,
      headers: CORS_HEADERS(origin),
      body: JSON.stringify({
        success: true,
        issueKey: created.issueKey,
        webUrl: created._links && created._links.web,
        debug: !requestTypeOverride
          ? { usedRequestTypeId: requestTypeId, availableRequestTypes: availableRequestTypes.map((t) => ({ id: t.id, name: t.name })) }
          : undefined,
      }),
    };
  } catch (e) {
    return {
      statusCode: 502,
      headers: CORS_HEADERS(origin),
      body: JSON.stringify({ error: e.message }),
    };
  }
};
