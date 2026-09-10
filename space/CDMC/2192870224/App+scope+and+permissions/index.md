# App scope and permissions

## Overview

Each app for Confluence Cloud (like Comala Document Management) has to be configured with a specific [scope](https://developer.atlassian.com/platform/forge/manifest-reference/scopes-forge/).

Scopes allow an app to request a particular level of access to an Atlassian product.

The app configures this automatically during installation. This adds the **Comala Document Management app user** as an individual user in **Global permissions**.

To manage global permissions:

1. Click the gear icon in the top-right corner of your Confluence site to open *Confluence Administration*.
2. In the left-hand navigation, under **Settings**, select **Permissions > Site permissions.**

   ![Site permissions page showing the Comala Document Management app user in the user permissions list.](/cms_trial/assets/fe22a026-5676-4df5-9d8e-854976ac5dad.png)

The automatic configuration also adds the **Comala Document Management** **app user** as an individual user for each space in the **Space permissions** screen**.** The app system user is assigned all individual user permissions for the space except **Restrictions Add/Delete**, **Archive**, **Delete own**, and **Space Export**.

![Space permissions page showing the Comala Document Management app user with assigned space permissions.](/cms_trial/assets/f0c83f33-6460-4cc7-badd-d0f86baaddf3.png)

Within an instance, a global administrator can limit the actions the app performs:

- Changes in scope by a global administrator can affect the global permissions for the app system user and the functioning of the app in the instance.
- Changes in the individual space permissions for the app system user (due to either the global change or a space administrator change) may affect the functioning of the app in that space.
- Page restrictions added to content prior to applying an app workflow to the content can cause an error.

## Pages with page-level restrictions

You need **view** and **edit** permissions on the page to use the applied workflow.

If page restrictions don’t include the **Comala Document Management app user**, the workflow won’t run on those pages, for example, when a page is created or updated.

You can configure how **Comala Document Management** handles restricted pages using the content restriction controls in [Global administration](/cms_trial/space/CDMC/2193129643/Global+administration/) and [Space administration](/cms_trial/space/CDMC/2192776249/Space+administration/).

## Permissions message

Space or page-level restrictions can prevent the app from working correctly. When this occurs, the following message is displayed when the app attempts to initialize the state byline on the page.

![Comala initialization message showing required permissions](/cms_trial/assets/330896fe-5c71-4ac2-9d45-fa105a833d00.png)

To resolve this, ensure the Comala Document Management app add-on user (or, in some cases, the current user) is added to the space permissions and any page restrictions, then refresh the page.

**Related topics**

- [Global administration](/cms_trial/space/CDMC/2193129643/Global+administration/)

- [Space administration](/cms_trial/space/CDMC/2192776249/Space+administration/)