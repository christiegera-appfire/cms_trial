# copy-page

## Overview

The **copy-page** trigger action enables you to automatically create a copy of an existing page.

You can configure the destination of the copied page to be one of the following:

- A child of the current page
- A child of a specified (named) page
- The homepage of a selected space

You can choose the **Target** **type** for the action as either

- **Page** - copies the page as a child of the current page or as a child of a selected page
- **Space** - copies the page as a child of the homepage in a selected space

The copied page retains the same name by default, but you can assign a new **Title** if needed.

The copied page includes the following:

- content properties
- page restrictions
- labels
- attachments
- custom content

![Comala copypage trigger action configuration dialog](/cms_trial/assets/c71a86fb-1eb6-4d67-8407-3729af70a950.png)

You can use this feature to keep public content separate from drafts, track changes with multiple versions, or quickly create similar pages for different projects or clients.

For example, you can copy the last approved version of a page to keep as a reference while continuing to edit the current draft using the copy-page trigger action.

## Copy page action parameters

| **Action Parameter** | **Value** | **Notes** |
| --- | --- | --- |
| **Target type** MANDATORY | The destination **Target type** is either:   - **Space** - **Page** | When **Space** is selected, the page is copied as   - a child of the homepage of a specified space   When **Page** is selected, the page is copied either as   - a child of the current page (default) - a child of a specified page   You must add a value for the **Target** parameter to set the destination parent page. |
| **Target** MANDATORY | **Target** value for the copied page:  When the **Target type** is **Space**,   - **The Select space** menu displays recently created spaces and lets you search for spaces by name. Matching results are shown as you type. Comala copypage trigger target space selection   When the **Target type** is **Page**   - empty value (default)    - sets the current page as the parent page - The **Select page** menu displays recently created pages and lets you search for pages by name. Matching results are shown as you type.  Comala copypage trigger action with destination settings | Use the box to search and add the destination value.  When searching, the box displays the options by the   - space key if **Space** is selected - page **contentId** if **Page** is selected   When **Space** is selected, and the homepage does not exist, the page is copied to the root of the destination space. |
| **Title** | Add a name for the copied page   - empty value (default) copies the page with the same name | By default, the copied page retains the same name as the source page.  When a page with the same name already exists in the target space, the copied page's name is appended with a number in brackets, for example, **Wellbeing policy (2).** Comala copied page in Confluence sidebar with appended number When the same trigger and **Copy Page** action are executed again, the first copy is updated without changing its page name rather than creating a new page.  A new page is created if a different trigger or **Copy Page** action is used to copy the page to the same space.  This lets you control page copies and prevents unnecessary duplication of pages. |
| **Copy properties** | Toggle option   - **Enabled**  (default) - **Inactive** | By default, the option is **Enabled,** and the page properties are retained when the page is copied. |
| **Copy restrictions** | Toggle option   - **Enabled**  (default) - **Inactive** | The option is **Enabled by default**, and page-level restrictions are retained when the page is copied.  When this option is **Enabled**, the addon user must have the Confluence **Add Restriction** permission in the destination space for the copied page. |
| **Copy attachments** | Toggle option   - **Enabled**  (default) - **Inactive** | By default, the option is **Enabled**, and page attachments are retained when the page is copied. |
| **Copy labels** | Toggle option   - **Enabled**  (default) - **Inactive** | By default, the option is **Enabled**, and the page labels are retained when the page is copied. |
| **Copy custom content** | Toggle option   - **Enabled**  (default) - **Inactive** | By default, the option is **Enabled**, and page custom content is retained when the page is copied. |

You can add one or more **Copy Page** actions to a single trigger. When the workflow trigger event occurs, the trigger checks that any required conditions are met, and if they are, the **Copy Page** action copies the page to the specified location.

This lets you automatically copy a page to different locations to keep track of changes by maintaining different versions or to generate separate copies for different projects or clients.

The **Copy Page** action can only be used to copy pages.

## “copy-page” JSON code

A **copy-page** workflow trigger action added using the visual editor is automatically displayed as a `“copy-page”` trigger action in the workflow code editor.

![Comala code editor copypage trigger action with space target](/cms_trial/assets/ab91a35a-aee6-46a2-9acc-905193b77d15.png)

You can also use the code editor to add the workflow trigger and the `“copy-page”` action.

## "copy-page" parameters and workflow trigger code example

### `"copy-page"` parameters

The trigger action `"copy-page"` copies a page to a specified location

- **action (*****copy-page*****)**

  - **target** **❗️** Only one of the following must be specified

    - **space:** The target space where you want to create the copy. The page is, by default, copied as a child of the target space's homepage.

      - value is the **space key** of the target space
    - **page:** The target parent page for the copied page. The parent page, by default, is the current page.

      - value is the **contentID** of the target parent page
  - **title:** The name for the page copy. *This is optional*.

    - If no title is defined, the copy is created with the same title as the source page
    - If a page with the same title already exists, the copy is created with a title that includes a number appended in brackets: **My Page (1)**
    - When executing subsequent copies of the page with the same trigger and trigger action, the original copied page is updated, and there is no change in the title
  - **copy-properties:** Copy content properties of the page when the page is copied

    - boolean value

      - **true** (default value)
      - **false**
    - default value is **true**
  - **copy-restrictions:** Copy the page-level restrictions of the page when the page is copied\*

    - boolean value

      - **true** (default value)
      - **false**
  - **copy-attachments:** Copy the page attachments of the page when the page is copied

    - boolean value

      - **true** (default value)
      - **false**
  - **copy-labels:** Copy the Confluence labels on the page when the page is copied

    - boolean value

      - **true** (default value)
      - **false**
  - **copy-custom-content:** Copy the custom content of the page when the page is copied

    - boolean value

      - **true** (default value)
      - **false**

\*When `“copy-restrictions”: true`, the app add-on user must have the Confluence **Add Restrictions** permission in the destination space for the copied page.

---

### ❗️ Mandatory parameters

**target**

The **target** parameter is mandatory and must include a value for either the target **space** or the target parent **page** parameter. This is either a **space key** for a different space or a page **contentID** in the current space.

The values are validated, and an error is logged if the target value (space key or parent page) does not exist.

---

### Trigger code example

```text
"triggers": [
    { "event": "on-change-state",
          "conditions": [{ "state": "Accepted" }],
          "actions": [
            {
              "action": "copy-page",
                "target":
                    {
                      "space": "STORE"
                    },
                "copy-properties": false,
                "copy-restrictions": false,
                "copy-attachments": true,
                "copy-labels": true,
                "copy-custom-content": false
          }
          ]
    }
]
```

The above `“trigger"` listens for a state change event to the **Accepted** state and copies the page to the space with the space key **STORE**:

- The page attachments and the page labels are included (each of these parameter values is `true`)
- The content properties, page restrictions, and custom content are not included on the copied page (each of these parameter values is `false`)

If one of these content parameters is not specified in the JSON code, the default value is assumed to be true, and the content is included on the copied page.