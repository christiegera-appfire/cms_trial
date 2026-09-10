# Advanced configuration of the Create issue(s) post-function

This document explains how to get more out of the Create issue(s) post-function such as creating multiple issues, linking newly created issues together, setting the field values of the newly created issue from the iterator and so on.

## Creating multiple issues

Using the "Multiple issue creation" feature of the Create issue post-function you can create multiple issues at once during the execution of this post-function, optionally linking them to the current issue. The iterator template is a Nunjucks template that must return either a comma-separated list of values or an array of values, in JSON format. The post-function will iterate over this list or the array of values and create one new issue per value. The below sections explain some of the use cases.

### Create one issue per value and set a field of the newly created issue

**To create one issue each for the users**`jdoe,tblack and dcharlie`**and assign the newly created issues to the respective user**

1. In the Iterator section input

   ```javascript
   jdoe,tblack,dcharlie
   ```
2. Go to `Set fields of new issue` section
3. Under `Additional fields` select "**Assignee**"
4. Click on `Add`
5. Select `Set field value to` option from the drop-down
6. Input this template:

   ```javascript
   {{it}}
   ```

**To create one issue per user in a multi-user-picker field, and assign the issue to that user**

1. In the Iterator section input

   ```javascript
   {{ issue.fields["Multi user picker"] | join(",","accountId") }}
   ```
2. To assign the newly created issues to the respective user:

   1. Go to `Set fields of new issue` section
   2. Under `Additional fields` select "**Assignee**"
   3. Click on `Add`
   4. Select `Set field value to` option from the drop-down
   5. Input this template:

      ```javascript
      {{it}}
      ```

You can similarly create multiple issues for values in any multi-values field like Affects Version/s, Component/s etc.

### Build an iterator to create multiple issues and set fields of the newly created issues

Instead of a list of values or an array of values as in the examples above, each value in the list can be an arbitrary JavaScript object with multiple values and each object will be available through the `it` variable in the rest of the post-function configuration. For example, if the iterator returns the following:

```javascript
[ 
  {"assignee":"55usdhf7682njsio", "summary":"Issue for John Doe"},
  {"assignee":"53suf8683jskdh622e", "summary":"Issue for Tim Black"} 
]
```

then with the "Iterator returns JSON" option is set, two new issues will be created. Under the "Set fields of new issue" you can set the Summary of the newly created issue to:

```javascript
{{it.summary}}
```

and Assignee to:

```javascript
{{it.assignee}}
```

### Create issues from a *combination* of two custom fields

You can create multiple issues from a *combination* of two single-select custom fields and set the respective fields of the newly created issue. For this, you'll need to generate an array of all possible combinations and provide it in the iterator. One issue will be created for each combination. Let's assume you have two Multi-select fields *Resource* and *Environment*, then your iterator logic will be something like:

**Iterator logic**

```text
{% set arr = [] %}
{% for resource in issue.fields['Resource'] %}
  {% for env in issue.fields['Environment'] %}
    {% set unused = arr.push({resource:resource.value,environment:env.value}) %}
  {% endfor %}
{% endfor %}
{{ arr | dump(2)}}
```

Select the "Iterator returns JSON" option, since the iterator returns an array of objects.

**Setting fields**

In the "Set fields of new issue" section, set the Resource field to:

```text
{{it.resource}}
```

and the Environment field to:

```text
{{it.environment}}
```

### Cloning an issue and its linked issues

Using the Sequence of post-function post-function you can clone an issue and its linked issues too. Let's assume on the trigger of the transition "Clone now" you want to clone an Epic and its Stories to a different project.

**Create a sequence**

1. Add the "Sequence of post-functions" post-function to the transition
2. In the sequence add the "Create issue" post-function.

   1. Select the destination project in "Project"
   2. Select the "Issue type" as "Calculated" and input

      ```text
      {{ issue.fields.issuetype.name }}
      ```
   3. Select the "Link to new issue" as "clones"
   4. Configure the fields
   5. Click on Save
3. Add another "Create issue" post-function to clone the linked issues

   1. Select the destination project in "Project"
   2. Select the "Issue type" as "Calculated" and input

      ```text
      {{ it.fields.issuetype.name }}
      ```
   3. Select "Multiple issue creation" option and input the following template:

      ```javascript
      {{ issue | linkedIssues("blocks",['key']) | length }}
      ```
   4. Select “Linked Issues” under “Set fields of new issue”

      1. Select “Set field value to Groovy expression”
      2. Input the following code:

         ```text
         [
         {
           "type": {"name":"Blocks"},
           "inwardIssue": {"key":"{{transition.context.newIssueKey}}"}
         }
         ]
         ```
   5. Save the post-function.
4. Click on "Save"
5. Publish the workflow.

Now when you trigger the transition "Clone now" the Parent and its subtasks are cloned to the new project.

## Link newly created issues

When using the "Multiple issue creation" feature of the Create Issue post-function, you can link the newly created issues together. There are two approaches to this as explained below. Consider you are creating 3 issues and this is your iterator script:

```javascript
[
  {
    "summary":"A first issue"
  },
  {
    "summary":"A second issue"
  },
  {
    "summary":"A third issue"
  }
]
```

### Using the `newIssueKeys` variable

This is a very generic approach in which you can use the `newIssueKeys` global variable that exposes the array of the issue keys of the issues already created by the post-function during previous iterations. For example, if your iterator value is an array of three values (three issues will be created), during the creation of the third issue, `newIssueKeys` global variable array holds the first two issue keys. This way, you can add in your Iterator objects information about the links to create between issues.

For example:

- Add linking information to the above array as shown below with the "Iterator returns JSON" option selected, where

  - **linkTo:** represents an index pointing to the issue to be linked to. `0` for the first issue, `1` for the second issue and so on.
  - **linkTypeName:** represents the name of the link type to be created, like, `Blocks`
  - **direction:** represents the direction to be linked to, like, `outward`

    ```text
    [
      {
        "summary":"A first issue"
      },
      {
        "summary":"A second issue",
        "linkTo": 0,
        "linkTypeName": "Blocks",
        "direction": "inward"
      },
      {
        "summary":"A third issue",
        "linkTo": 1,
        "linkTypeName": "Blocks",
        "direction": "outward"
      }
    ]
    ```
- Under the "Set fields of new issue" select `Linked Issues` field
- Select "Set field value to" in the drop-down and input the following template:

  ```javascript
  [
  {% if it.linkTo != null %}
  {
    "type": {"name":"{{it.linkTypeName}}"},
    "{{it.direction}}Issue": {"key":"{{newIssueKeys[it.linkTo]}}"}
  }
  {% endif %}
  ]
  ```

Now when the transition is triggered

- 3 issues are created,
- the second issue is linked to the first one through "is blocked by" link and
- the third issue is linked to the second by the "blocks" link.

### Using the iterator

This is an easier approach in which you can specify the issue links to create in the iterator section, using the following syntax:

- Add the "Create issue" post-function
- Select the "Issue type"
- Select the link type (link from the current issue to the newly created issues)
- Select "Create multiple issues" under "Multiple issue creation"
- Add the following information under the "Iterator" selecting the "Iterator returns JSON" option

For each value, an `issueLinks` property can be specified, which contains an array of links to create. Each link is specified by:

- **linkName:** Indicates the link direction name as it appears on the issue (e.g. "blocks" or "is blocked by")
- **toIssue:** Indicates the issue link to. It contains the 1-based index of the issue to link to; `1` being the first issue created by the iterator, `2` the second, etc.. If `0` is specified, then the new issue is linked to the issue being transitioned.

**Iterator script**

```javascript
[
  {
    "summary":"A first issue"
  },
  {
    "summary":"A second issue",
    "issueLinks": [
      {"linkName":"blocks","toIssue":1}
    ]
  },
  {
    "summary":"A third issue",
    "issueLinks": [
      {"linkName":"relates to","toIssue":2}
    ]
  }
]
```

## Prevent issue creation when the transition is run the second time

To avoid creating a second issue when the transition is run a second time you can use the `jmwe.last.issue.created` property of the issue to check that there is no issue created already by the post-function. Select the conditional execution section and input the template:

```text
{{ issue | issueProperty("jmwe.last.issue.created") == null }}
```

This will avoid the creation of an issue by the post-function, the second time the transition is triggered. This approach only works if there is a single Create Issues post-function on the issue's workflow, and it creates only one issue.

## Prevent loop on the Create transition

When creating a new issue during the creation of an issue, it leads to a recursive loop. For example:

1. If you are creating subtasks to a Task on the Create transition then the post-function will try to create sub-tasks to each newly created sub-task and you will see the error: "Cannot create a subtask to a subtask".
2. If you are creating tasks linked to the Story on the Create transition then the post-function creates linked tasks to each newly created task thereby creating a loop. JMWE identifies the loop and stops the issue creation with an error message: "Identified a loop. Execution Stopped."

To avoid this you can use the conditional execution section and break the loop.

1. In the first example, add a condition in the conditional execution template to check that the main issue (issue from which multiples issues are created) is not a subtask.

   ```javascript
   {{ not issue.fields.issuetype.subtask }}
   ```
2. In the second example, identify the main issue by its issue type as follows.

   ```javascript
   {{ issue.fields.issuetype.name == "Story" }}
   ```
3. The best is to use the `jmwe-created-from` property of the issue; Using this approach check that the issue is *not created* from another issue.

   ```javascript
   {{ issue | issueProperty("jmwe-created-from") == null }}
   ```

## Workaround to move an issue and its linked issues

Moving issues to a new project is not supported by the Jira Cloud APIs, so it *cannot be implemented by JMWE or any other app*. A workaround is to re-create the task and its linked issues in the destination project and delete the main issue and its linked issues.