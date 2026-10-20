# Field support

Product Discovery uses fields differently than standard Jira projects to create specialized tables and views for idea management. This unique field structure can cause compatibility issues with Power Scripts.

## Supported fields

The following fields work with Power Scripts in Product Discovery projects:

|  |  |
| --- | --- |
| **Standard fieds** | Standard Jira fields work normally when present in Product Discovery projects, including Summary, Description, Assignee, and others. For a complete list of supported standard fields, see [this page](/cms_trial/space/PSJC/434962565/Supported+custom+field+types/). |
| **Custom fields** | Most Product Discovery custom fields work with SIL code like any other custom field. These include fields like Category, Customer segments, Documents, Goal, and others discovered by the [Custom fields support SIL script](/cms_trial/space/PSJC/793280566/Custom+fields+support+SIL+script/).  [Unmapped block: nestedExpand] |
| **Date fields** | Use the [JPDInterval SIL type](/cms_trial/space/PSJC/435028065/Predefined+structure+types+reference/) to manipulate custom date type fields, such as Project start and Project target. |

## Unsupported fields

The following fields return null values from the REST API and cannot be accessed through Power Scripts:

- Delivery progress
- Delivery status
- Insights

Some Product Discovery fields use ranking-style values (similar to 5-star ratings) that may require special handling in your scripts. If you need to work with ranking-style fields, use the [Custom fields support SIL script](/cms_trial/space/PSJC/793280566/Custom+fields+support+SIL+script/) to discover the current field IDs and test accessibility.