# Authenticate REST APIs

To authenticate API requests for the Connector for Salesforce & Jira, follow these general guidelines for using a REST API token. The API is available for the Jira Cloud version only.

## Before you start

Make sure you have:

- [Set up a connection to Salesforce](/cms_trial/space/CSFJIRA/1873379599/Set+up+a+connection+to+Salesforce+(Jira+Cloud)/)
- [Configured a binding between a project to a connection](/cms_trial/space/CSFJIRA/1873379785/Bind+a+space+to+a+connection+(Jira+Cloud)/)

## Steps

1. Select **Apps** from the left sidebar in Jira.
2. Next to *Connector for Salesforce,* click **Menu** (▢) > **App settings**.
3. Under *Connector for Salesforce*, click **Connections**.
4. Choose your **Connection**, then click the **three dot menu** (▢) > **API Access Token.**

   ![API access token.png](/cms_trial/assets/b7909149-751e-4beb-93fc-e858122a3cf6.png)
5. For the REST API token, select the token lifespan. (**15 minutes to 365 days**).

   ![image-20250224-142516.png](/cms_trial/assets/91c0b66c-9b06-4f32-87db-ce501f85aff5.png)
6. Copy the generated **REST API token**.
7. Use the REST token for API requests.

Make sure you use the proper Connector for Salesforce and Jira Cloud instance URL:  
 <https://sfjc.integration.appfire.app> or <https://eu-sfjc.integration.appfire>, depending on your data residency location.

1. Check your Connector’s URL.

   1. Open Web Developer Tools

      - Windows/Linux: F12 or Ctrl+Shift+I
      - macOS: Command+Option+I
   2. In Jira, go to **Apps** > **Connector for Salesforce Menu** (▢) > **App settings** > **Connections**.  
      Make sure you do this *after* opening the developer tools in the previous step. The tools only capture network traffic from the moment they're opened, so opening them beforehand is essential.

      ![connect.png](/cms_trial/assets/a3a9c349-81a5-4942-8ae5-6c9ac703ca18.png)
   3. Go to the **Network** tab, and search for `/addon/api/connection` in the **Filter** field.
   4. Look for the **Requests URL** to find either:

      - sfjc.integration.appfire.app
      - eu-sfjc.integration.appfire.app
   5. Copy the URL you found and use it for your API authentication setup.

      ![developer tools.png](/cms_trial/assets/79cc8083-0859-4062-91c8-d1f55e0df0bd.png)

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

## Related pages

[pagetree macro — dynamic multi-level tree, not yet built]