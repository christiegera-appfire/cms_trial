# Associate, push, and pull actions with REST API

You can configure and run an API call that associates a Jira issue with a Salesforce object and pushes the data to Salesforce. The API allows associating, auto push, and auto pull for created Salesforce objects.

The old API (`<BASE-URL>/rest/api/2/issue/<KEY>/properties/com.servicerocket.jira.cloud.issue.salesforce.associations`), which used Jira entity properties for storing associations, is no longer supported due to storage limitations. You can use the Associate API below instead to achieve the same functionality.

There are several REST APIs available for your integration; check the pages below to learn more details:

- [Associate API](/cms_trial/space/CSFJIRA/1684308828/Associate+API%3A+POST+%2Fexternal%2Fapi%2Fassociation/)
- [Push API](/cms_trial/space/CSFJIRA/1685258704/Push+API%3A+POST+%2Fexternal%2Fapi%2Fpush%2Fproject/)
- [Bulk associations: GET /external/api/associations](https://appfire.atlassian.net/wiki/spaces/470745117/pages/1831928784/Bulk+associations+GET+external+api+associations?atlOrigin=eyJpIjoiNTg0OGE3ZmUyZDQ4NGU5ZmE5Y2FmZmQ0ODY0NDQ3NDEiLCJwIjoiYyJ9)
- [Bulk associations: POST /external/api/associations](https://appfire.atlassian.net/wiki/spaces/470745117/pages/1832615937/Bulk+associations+POST+external+api+associations?atlOrigin=eyJpIjoiMWE2Njg0NDRlZTQxNDhkNzhhZWQ4NmM1ZWRlMjZkZGYiLCJwIjoiYyJ9)

## Use case

### Scenario

A customer has migrated their Salesforce instances, recreated their data on a new instance, and now requires an automated solution to associate and push the newly created Salesforce objects.

### Solution

Use the script below to automate the association and push mechanism of Salesforce objects in the new instance.

## Before you start

Make sure you have:

- [set up a connection to Salesforce](https://appfire.atlassian.net/wiki/spaces/CSFJIRA/pages/470754669)
- [bound a project to a connection](https://appfire.atlassian.net/wiki/spaces/CSFJIRA/pages/470754674)

## Instructions

1. Copy the script and install dependencies using `npm install atlassian-jwt moment`.
2. For the `const token`, replace `FILL_ME_IN` with the REST API access token**.** The token is available on the *Connections* configuration page of the Connector for Salesforce & Jira app:

- Choose your **Connection**, then click menu▢ > **API Access Token.**

  ![API access token.png](/cms_trial/assets/cb34094a-0d1e-4186-b89a-50d114464b41.png)
- Select the token lifespan and copy the **REST API token**.

  ![image-20250224-142516.png](/cms_trial/assets/f28c8718-8b3c-443c-a8f8-52dd240f9488.png)

1. For `const projectId`, replace `FILL_ME_IN` with the project ID for the issues you want to associate with.
2. At line 73 hardcode the **Jira issue ID**, **Salesforce Object Name,** and the **Salesforce Object ID.**

   1. To do this in bulk, use the [Bulk associations: POST /external/api/associations](https://appfire.atlassian.net/wiki/spaces/470745117/pages/1832615937/Bulk+associations+POST+external+api+associations?atlOrigin=eyJpIjoiMWE2Njg0NDRlZTQxNDhkNzhhZWQ4NmM1ZWRlMjZkZGYiLCJwIjoiYyJ9).
3. Set up API details.  
   Modify the script to call the `POST/external/api/association` endpoint with the `allowUpsert` query parameter set to `true` if upserting is required.
4. Run the script.

   1. You can use Visual Studio Code to run the script.
5. Verify that the association was created and pushed. Ensure the object you are linking to has a different summary so that a simple association only creates a link, while the push actually replaces the summary.

## Example script

Below is an example script in Node.js that demonstrates how to associate a Jira issue with a Salesforce object and push the issue data to Salesforce using the provided REST APIs.

```text
// API Access Token from authorized connection on the configuration page
const TOKEN = "FILL_ME_IN";

// The Connector's URL
const APP_BASE_URL = "https://sfjc.integration.appfire.app";

// Project ID for the Jira issues ( can't be the project key )
const PROJECT_ID = "FILL_ME_IN";

// Function to associate a single Jira issue with a Salesforce object
async function associateSingleCase(issueIdString, salesforceObjectName, salesforceObjectId) {
    const payload = {
        "jiraIssueId": issueIdString, // ID of the Jira issue
        "son": salesforceObjectName, // Salesforce object name eg: Case, Opportunity, etc.
        "soid": salesforceObjectId,  // Salesforce object ID
        "viewOnly": false, // Whether the association is view-only
        "autoPush": false, // Whether to automatically push changes
        "autoPull": false // Whether to automatically pull changes
    }

    const url = `${APP_BASE_URL}/external/api/association`;
    console.log('Associating single object...');
    const r = await fetch(url, {
        method: 'POST',
        body: JSON.stringify(payload),
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': 'JWT ' + TOKEN,
        }
    })
    if ((r.status !== 200) && (r.status !== 201)) {
        console.error(r.status);
        let data = await r.text();
        console.error(data);
        throw new Error(data);  // Throw an error if the request fails
    } else {
        const result = await r.json()
        console.log('associateSingleIssue complete: ', result);
        return result;
    }
}

// Function to push a single Jira issue to a Salesforce object
async function pushSingleIssue(projectIdString, issueIdString, salesforceObjectName, salesforceObjectId) {
    const url = `${APP_BASE_URL}/external/api/push/project/${projectIdString}/issue/${issueIdString}/to/${salesforceObjectName}/${salesforceObjectId}`;
    console.log('Pushing issue to object...');
    const r = await fetch(url, {
        method: 'POST',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': 'JWT ' + TOKEN,
        }
    })
    const result = await r.json();
    console.log('pushSingleIssue complete: ', result);
    return result;
}

// Function to associate a Jira issue and then push it to Salesforce
function associateThenPush(projectIdString, issueIdString, salesforceObjectName, salesforceObjectId) {
    return associateSingleCase(issueIdString, salesforceObjectName, salesforceObjectId)
        .then(() => pushSingleIssue(projectIdString, issueIdString, salesforceObjectName, salesforceObjectId));
}

// Main function to execute the script
async function main() {
    const issueIdOrKey = "TEST-5" // Replace this with your Jira issue ID or Key
    const salesforceObjectName = "Case" // Replace this with the salesforce SON you'd like to associate
    const salesforceObjectId = "500J80000019IF9IAM" // Replace this with the SOID you'd like to associate with

    await associateThenPush(PROJECT_ID, issueIdOrKey, salesforceObjectName, salesforceObjectId);  // Example issue and Salesforce object
    console.log('Done!');
}

main();
```