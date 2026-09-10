# Document Metadata Get

## Overview

The **Document Metadata Get** macro displays metadata, workflow parameters, and page parameters directly on a Confluence page or blog post, making important document information easily accessible and visible.

It retrieves metadata values defined on a page, including those set using the [Document Metadata Set](/cms_trial/space/CDMC/2510750404/Document+Metadata+Set/) and [Document Metadata List](/cms_trial/space/CDMC/2513797193/Document+Metadata+List/) macros, as well as those set by the [set-metadata trigger action](/cms_trial/space/CDMC/2193723026/set-metadata/). The retrieved values can be displayed on the page, referenced from other pages, or accessed in workflow definitions.

**When to use this macro:**

Use Document Metadata Get to display a single metadata value inline on a page.

To display all metadata on a page, refer to the [Document Metadata Values](/cms_trial/space/CDMC/2513862720/Document+Metadata+Values/) page.

To learn more about how to pull metadata from another page, refer to [Document Metadata From](/cms_trial/space/CDMC/2513600585/Document+Metadata+From/).

### Migration compatibility

The following metadata migrated from the hosted app can also be retrieved using this macro:

- Metadata set with the [metadata macro](https://appfire.atlassian.net/wiki/spaces/COMALACM/pages/655988203) and [metadata-list macro](https://appfire.atlassian.net/wiki/spaces/COMALACM/pages/655758458) of the [Comala Metadata app](https://marketplace.atlassian.com/apps/5295/comala-metadata?hosting=datacenter&tab=overview)
- Metadata set with Comala Document Management Data Center [set-metadata macro](https://appfire.atlassian.net/wiki/spaces/CDML/pages/650251172)
- Page-level workflow parameters

## Parameters

| **Parameter** | **Required** | **Description** |
| --- | --- | --- |
| Metadata Name | Yes | The name (key) of the metadata value to retrieve. Must match a metadata name that has been set on the page. |

## Add the macro

To add the Document Metadata Get macro:

1. On a draft page, type `/document metadata get`.

   ![Comala Document Metadata Get macro output on a page](/cms_trial/assets/deb5471d-6de7-4df9-bce5-775b3f71c6db.png)
2. Choose the **Document Metadata Get** macro. Click to edit and enter the **Metadata Name**.

   ![Document Metadata Get macro with the name of the metadata to get.](/cms_trial/assets/d4eac37b-ea98-4fc6-aa2c-a17228ba337c.png)

Make sure to enter a valid metadata name. The metadata name must exactly match a name set on the page. If the name does not match any existing metadata, the macro will not display a value.

1. **Publish** the page to retrieve and render the metadata value.

For example,

If a page has metadata set with the name `approver` and the value `John Smith`:

- **In the editor,** the macro appears as a placeholder block displaying the metadata name.
- **On the published page,** the macro renders the value **John Smith** inline where the macro was placed.

- The metadata name is case-sensitive. It must exactly match the name used in the Document Metadata Set or the workflow definition.

- The macro only renders values on a published page. If you’ve added or updated metadata, publish the page to see the result.

- If the metadata name doesn’t match any existing metadata on the page, the macro will not display a value.

- When working with migrated metadata from the hosted app, verify that the original metadata key name carried over correctly.

**Related macros**

- [Document Metadata Set](/cms_trial/space/CDMC/2510750404/Document+Metadata+Set/)
- [Document Metadata List](/cms_trial/space/CDMC/2513797193/Document+Metadata+List/)
- [Document Metadata Values](/cms_trial/space/CDMC/2513862720/Document+Metadata+Values/)
- [Document Metadata From](/cms_trial/space/CDMC/2513600585/Document+Metadata+From/)
- [Document Metadata Report](/cms_trial/space/CDMC/2508096484/Document+Metadata+Report/)