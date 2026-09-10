# Identifying all deprecated post functions

There is a method by which you can identify all deprecated post functions within all workflows; however, this method requires running a Python script against the [Jira Cloud Workflow REST API](https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-workflows/#api-rest-api-3-workflows-search-get). If you are not comfortable with this method, the only alternative is to work through all of your workflows one at a time using the [JMWE workflow extensions](/cms_trial/space/JMWEC/466321411/JMWE+workflow+extensions/) Administration page.

To generate a list of all JMWE workflow extensions across all of your workflows, use the following Python script. A few things to note:

- You must supply a few variable values:

  - Your base Jira Cloud domain for the `JIRA_BASE_URL` variable.
  - The email address with which you log into Jira Cloud, for the `EMAIL` variable.
  - An API token for the `API_TOKEN` variable. If you need to generate an API token, see <https://support.atlassian.com/atlassian-account/docs/manage-api-tokens-for-your-atlassian-account/>.

The example script only returns JMWE extensions that have been added to Workflows - it does not scan any Actions for deprecated post functions. You will need to check [Shared actions](/cms_trial/space/JMWEC/466288975/Shared+actions/), [Scheduled actions](/cms_trial/space/JMWEC/466321868/Scheduled+actions/), and [Event-based actions](/cms_trial/space/JMWEC/465473524/Event-based+actions/) separately.

### Python script

```python
import requests
from collections import defaultdict

# === CONFIGURATION ===
JIRA_BASE_URL = "https://example.atlassian.net"  # Replace with your Jira Cloud domain
EMAIL = "name@example.com"                       # Replace with your Jira email
API_TOKEN = "your_api_token"                     # Replace with your Jira API token

AUTH = (EMAIL, API_TOKEN)
HEADERS = {"Accept": "application/json"}
JMWE_KEY = "com.innovalog.jmwe"
MAX_RESULTS = 50

# List of specific JMWE post-functions to look for
TARGET_JMWE_FUNCTIONS = {
    "AssignToLastRoleMemberFunction": "Assign to last role member (Deprecated)",
    "AssignToRoleMemberFunction": "Assign to role member (Deprecated)",
    "ClearFieldsOfLinkedIssuesFunction": "Clear fields of linked issues (Deprecated)",
    "CommentLinkedIssuesFunction": "Comment linked issues (Deprecated)",
    "CopyFieldValueFromLinkedIssuesFunction": "Copy field value from linked issues (Deprecated)",
    "CopyFieldValueFromParentFunction": "Copy field value from parent issue (Deprecated)",
    "CopyFieldValueToLinkedIssuesFunction": "Copy field value to linked issues (Deprecated)",
    "CopyFieldValueToParentFunction": "Copy field value to parent issue (Deprecated)",
    "CopyValueFromFieldToFieldFunction": "Copy value from field to field (Deprecated)",
    "SetFieldValueOfLinkedIssuesFunction": "Set field value of linked issues (Deprecated)",
    "TransitionLinkedIssuesFunction": "Transition linked issues (Deprecated)",
    "TransitionParentIssueFunction": "Transition parent issue (Deprecated)",
}

def match_jmwe_postfunction(post_function: dict):
    """Check if the post-function matches one of the target JMWE functions"""
    if not post_function.get("type", "").startswith(JMWE_KEY):
        return None
    type_id = post_function["type"].split("__")[-1]
    return TARGET_JMWE_FUNCTIONS.get(type_id)

def get_grouped_jmwe_data():
    grouped_data = defaultdict(list)
    start_at = 0

    while True:
        url = (
            f"{JIRA_BASE_URL}/rest/api/3/workflow/search"
            f"?expand=transitions.rules&startAt={start_at}&maxResults={MAX_RESULTS}"
        )

        response = requests.get(url, auth=AUTH, headers=HEADERS)
        if response.status_code != 200:
            raise Exception(f"API error: {response.status_code} - {response.text}")

        data = response.json()
        workflows = data.get("values", [])

        for wf in workflows:
            wf_name = wf.get("id", {}).get("name", "Unknown")
            for t in wf.get("transitions", []):
                transition_name = t.get("name", "Unnamed Transition")
                jmwe_matches = []

                for pf in t.get("rules", {}).get("postFunctions", []):
                    match = match_jmwe_postfunction(pf)
                    if match:
                        jmwe_matches.append(match)

                if jmwe_matches:
                    grouped_data[wf_name].append({
                        "transition": transition_name,
                        "jmwe_functions": jmwe_matches
                    })

        start_at += MAX_RESULTS
        if start_at >= data.get("total", 0):
            break

    return grouped_data

if __name__ == "__main__":
    print("🔍 Scanning workflows for specific JMWE post-functions...\n")
    grouped_results = get_grouped_jmwe_data()

    if grouped_results:
        print(f"✅ Found transitions using targeted JMWE post-functions in {len(grouped_results)} workflows:\n")
        for wf_name, transitions in grouped_results.items():
            print(f"• Workflow: {wf_name}")
            for t in transitions:
                print(f"  ↳ Transition: {t['transition']}")
                for func in t['jmwe_functions']:
                    print(f"    - {func}")
            print()
    else:
        print("❌ No transitions using the targeted JMWE post-functions were found.")
```

The script returns something like the following:

```none
🔍 Scanning workflows for specific JMWE post-functions...

✅ Found transitions using targeted JMWE post-functions in 2 workflows:

• Workflow: Software Simplified Workflow for Project JMWE
  ↳ Transition: Selected for Development
    - Transition parent issue (Deprecated)
    - Transition linked issues (Deprecated)
    - Set field value of linked issues (Deprecated)
    - Copy value from field to field (Deprecated)
    - Copy field value to parent issue (Deprecated)
    - Copy field value to linked issues (Deprecated)
    - Copy field value from parent issue (Deprecated)
    - Copy field value from linked issues (Deprecated)
    - Comment linked issues (Deprecated)
    - Clear fields of linked issues (Deprecated)
    - Assign to role member (Deprecated)
    - Assign to last role member (Deprecated)

• Workflow: Software Simplified Workflow for Project MU
  ↳ Transition: transition 1
    - Copy field value from parent issue (Deprecated)
  ↳ Transition: transition 2
    - Set field value of linked issues (Deprecated)
    - Clear fields of linked issues (Deprecated)
  ↳ Transition: transition 3
    - Transition parent issue (Deprecated)
```