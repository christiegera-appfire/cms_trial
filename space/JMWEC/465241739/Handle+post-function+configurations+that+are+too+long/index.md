# Handle post-function configurations that are too long

Due to a limitation of Jira Cloud, which passes the post-function configuration in a GET URL that is limited to 8000 characters in total, JMWE cannot support long post-function configurations. The most affected are post-functions with more functionalities such as the Transition post-functions.

## Problem

For example, you have a Transition issue post-function with a lengthy template to calculate the transition to be triggered:

```text
{% if issue.fields.customfield_12332 == "A" and issue.fields.customfield_11312 == "a" %}
"To Department A"
{% elif issue.fields.customfield_12332 == "B" and issue.fields.customfield_11312 == "b" %}
"To Department B"
.....
....
```

When you try to save the post-function you will see this error:

![JMWE for Jira Cloud configuration panel with text handling options](/cms_trial/assets/0a081224-3753-4a1d-9962-c3fd3af24c80.png)

## Workaround

To reduce the post-function configuration length you need to replace the Nunjucks template in the post-function with a Shared Nunjucks template.

1. Create a [Shared Nunjucks template](/wiki/spaces/JMWEC/pages/78480866/Shared+Nunjucks+Templates#Creating-a-shared-Nunjucks-template) “Calculated transitions” in the Shared Nunjucks templates page
2. Input the template in the Nunjucks editor
3. Go back to the post-function
4. Remove the existing template
5. Input the following template under “Calculated transitions”

   ```text
   {% include "Calculated transitions" %}
   ```
6. Save the post-function and publish the workflow

## Related articles