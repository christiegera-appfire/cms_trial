# Conditional Execution Samples

The following are a few examples of how to use Conditional Execution, including the Nunjucks templates that should be used within a post-function utilizing the sample.

Some of the examples below include additional project configurations or custom fields.

## Assign ‘Bug’ issues to the Product Owner

1. Create a **Product Owner** project role, with your product owner as the only member.
2. Add the [Assign to role member](https://appfire.atlassian.net/wiki/pages/createpage.action?spaceKey=jmwec&title=Assign%20to%20role%20member&linkCreation=true&fromPageId=998440999) post-function to the Create transition of the issue workflow.
3. In the post-function configuration, select **Product Owner** for the **Project Role** field.
4. Select the checkbox under **Conditional execution**.
5. In **Condition**, enter `{{ issue.fields.issuetype.name == "Bug" }}`

## Assign ‘Bug’ issues to Product Manager when priority is ‘Critical’

1. Add the [Assign to role member](https://appfire.atlassian.net/wiki/pages/createpage.action?spaceKey=jmwec&title=Assign%20to%20role%20member&linkCreation=true&fromPageId=998440999) post-function to the **Create** transition of the issue workflow.
2. In the post-function configuration, select **Product Manager** for the **Project Role** field.
3. Select the checkbox under **Conditional execution**.
4. In **Condition**, enter `{{ issue.fields.issuetype.name == "Bug" and issue.fields.priority.name == "Critical" }}`

## Copy value from ‘Affects versions’ to ‘Fix versions’ when resolution is ‘Fixed’

This example is only applicable to Jira Service Management (JSM), unless you have customized your project to include similar fields.

1. Add the [Copy issue fields](/cms_trial/space/JMWEC/466323304/Copy+issue+fields/) post-function to the **Close** transition of the issue’s workflow.
2. Under **Fields to copy**, select **Affects versions** for **Source field**.
3. Also under **Fields to copy**, select **Fix versions** for **Destination field**.
4. Select the checkbox under **Conditional execution**.
5. In **Condition**, enter `{{ issue.fields.resolution.name == "Fixed" }}`

## Automatically transition High priority issues to ‘In Progress’

1. Add the [Transition issue(s)](/cms_trial/space/JMWEC/465242612/Transition+issue(s)/) post-function to the **Create** transition of the issue workflow.
2. Under **Transition(s)**, select the transition name or ID for the transition that points to ‘In Progress’ (e.g. **Start Progress**).
3. Select the checkbox under **Conditional execution**.
4. In **Condition**, enter `{{ issue.fields.priority.name == "High" or issue.fields.priority.name == "Highest" }}`

## Automatically transition issues created by ‘Service Desk Customer' project role

1. Add the [Transition issue(s)](/cms_trial/space/JMWEC/465242612/Transition+issue(s)/) post-function to the **Create** transition of the issue workflow.
2. Under **Transition(s)**, select the transition name or ID for the transition that points to ‘In Progress’ (e.g. **Start Progress**).
3. Select the checkbox under **Conditional execution**.
4. In **Condition**, enter `{{ issue.fields.reporter | isInRole("Service Desk Customers") }}`