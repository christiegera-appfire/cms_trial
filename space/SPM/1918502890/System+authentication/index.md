# System authentication

The system authentication mechanism provides in-app authentication and is based on JWT.Cookie-based authentication is replaced with JWT-based authentication transferred by the Authorization header.

The authentication token expires in 15 minutes. When the authentication token expires, a refresh token is used to query for a new authentication token.

## Impact

An additional authorization step is required to use automation successfully (and communicate with our API).

## Instructions

When any client starts using the service, it should authenticate under **/system/auth** endpoint (e.g., <https://yourjira.com/rest/softwareplant-bigpicture/1.0/system/auth>)

### Step one - authentication request

1. Use the *GET/* ***system/auth*** **request** (cookie: JSESSIONID, which represents a session in Jira where BP/BG/BT is working).
2. As a response, you will receive either:

   1. **two tokens**

      1. **authentication**(valid for 15 min)
      2. **refresh**(valid for seven days)
   2. HTTP 401 → If Jira doesn't prohibit it, you can use basic authentication instead of using cookie JSESSIOND  - forward to request username and password.

```text
{
    "authentication": "$authenticationJWT",
    "refresh": "$refreshJWT"
}
```

**/system/auth** endpoint is accessible to the authentication filter for the application.

### Step two - implementation

1. A valid **authentication token** should be **attached to the Authorization header** for every BigPicture request - the authorization header must contain the value of the authentication field (received as a response from *system/auth).*
2. Because our applications function in the Jira environment, the **JSESSIONID cookie must still be forwarded to our endpoints**.

### Step three - token refresh

An authentication token is valid for a limited time. The query for an authentication token refreshes when it expires.

1. When the **token expires**, the API will respond with an HTTP 401.
2. Query **/system/reauth** endpoint using refresh token in Authorization header. Use the **refresh token**(the value of the refresh field received as a response from *system/auth)* for authorization → *GET* ***/system/reauth***request.
3. The response will contain a new authentication token. Use it as described in step two above.

```text
{
    "authentication": "$authenticationJWT"
}
```