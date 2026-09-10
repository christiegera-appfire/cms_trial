# Create a new issue in a different Jira Cloud instance

This article provides the code snippet to create a new issue in a different Jira Cloud instance using [callRest](/cms_trial/space/JMWEC/465242995/callRest/) filter and [Atlassian Jira REST API](https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issues/#api-rest-api-3-issue-post)

## \uD83D\uDCD8 Instructions

1. Navigate to the intended workflow to make the necessary changes in the edit mode.
2. Select the required transition.
3. Select the *Post functions* tab and click `Add post function`.
4. Add the <https://appfire.atlassian.net/wiki/pages/createpage.action?spaceKey=jmwec&title=Build-your-own%20%28scripted%29%20Post-function&linkCreation=true&fromPageId=465242767> post-function with the below template:

   ```java
   {{ "https://<URL>/rest/api/3/issue" | callRest(verb=("post"),
                  body= {
                       "fields": {
                      		"project": {
                           	"key":"JSM"
                               },
                           "summary": "From JMWE post-function",
                            "issuetype": {
                                     "id": "10006"
                                     },
                                     "customfield_10064": "val 1"
   					}
                  },
                  options= {
   					headers: {
   						"authorization": "Basic XXXXXXXXXX"
   					}
   				}) | dump(2) }}
   ```

Replace:

- `<URL>` in line #1 with the target Jira Cloud instance URL
- `JSM` in line #5 with the target project key
- `From JMWE post-function` in line #7 with the desired summary
- `10006` in line #9 with the target issue type id
- `10064` and `val 1` in line #11 with the id and value of a customfield that you want to set in the new issue. Add other fields as needed (check [this](https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issues/#api-rest-api-3-issue-post-example))
- `XXXXXXXXXX` in line #16 with your API token - check [this](https://developer.atlassian.com/cloud/jira/service-desk/basic-auth-for-rest-apis/).

![JMWE for Jira Cloud configuration for creating issues in different Jira Cloud instances](/cms_trial/assets/b4ad20d4-0945-4d71-8774-2496689e7be3.png)

### References

- [callRest](/cms_trial/space/JMWEC/465242995/callRest/)

## \uD83D\uDCCB Related articles