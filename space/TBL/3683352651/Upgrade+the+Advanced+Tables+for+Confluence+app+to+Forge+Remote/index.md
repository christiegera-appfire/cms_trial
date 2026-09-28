# Upgrade the Advanced Tables for Confluence app to Forge Remote

## Overview

Appfire's Advanced Tables for Confluence app has moved to Atlassian Forge Remote, Atlassian’s most advanced cloud development platform.

- At Appfire, we are committed to maintaining the highest standards of security, reliability, and performance across our solutions. As part of this commitment, we developed and deployed the **Advanced Tables for Confluence** cloud app on **Atlassian Forge Remote**.
- The Advanced Tables for Confluence app on Forge Remote now offers an improved macro editor experience. [Read more](/cms_trial/space/TBL/2766798931/Release+notes+February+2026/).

Atlassian is [ending support for the Connect framework](https://www.atlassian.com/blog/development/announcing-connect-end-of-support-timeline-and-next-steps) in late 2026. As a result, the Connect version of Advanced Tables for Confluence is retired, and legacy macros will not load. Upgrade the appto restore functionality and avoid disruption.

### **Why Forge Remote?**

- Moving to Forge ensures your data is protected within Atlassian’s trusted infrastructure, leveraging its built-in security, compliance, and scalability.
- This advancement represents our ongoing dedication to delivering solutions that meet Level 3 (Forge) and Level 4 (Runs on Atlassian – RoA) technical and security standards.
- By embracing Forge, Appfire continues to deliver on its promise to offer secure, enterprise-grade apps that evolve with Atlassian’s platform, giving you confidence that your workflows are supported by the strongest foundation available.

## How to upgrade to Forge Remote?

To upgrade the app to the Forge Remote version, you need administrative privileges.

1. Log in to <https://admin.atlassian.com/> and select your **organization**.
2. In the left navigation pane, go to **Apps** and under **Sites**, click the **Site** name to open **Site settings**.

   ![Navigate to Sites under Apps.png](/cms_trial/assets/7455aa6d-7c12-4864-a582-91a4257d89b7.png)
3. Under **Site settings**, click **Connected apps**. On the **Connected apps** page, you can view, update, configure, and uninstall installed apps.
4. The Advanced Tables for Confluence app displays an **Update** label. Click **View app details**.

   ![Advanced Tables_connected apps.png](/cms_trial/assets/2deffb4e-5031-44d1-b79b-e4c3a84210c4.png)
   1. To upgrade the app, click **Update**.

      ![Advanced Tables app update screen in Confluence administration](/cms_trial/assets/0dee3e88-f0a2-40d7-89d7-81894fc3b256.png)
   2. The *Confirm app update* dialog opens. You can review the permissions and click **Update**.

      ![Advanced Tables confirm app update dialog](/cms_trial/assets/7384444e-4d8a-4d22-a2d2-25e357faedf2.png)

**Do not access the app** in the cloud **until the upgrade is complete and a few minutes have passed** to allow the cloud processing to finish.

After the upgrade, if any Advanced Tables macros do not display content on your Confluence page, edit the macro and save the configuration to refresh it.

## Support

If you have questions or need assistance with the upgrade process, contact our [support team](https://appf.re/support).

## References

- [Atlassian’s Connect end of support announcement](https://www.atlassian.com/blog/development/announcing-connect-end-of-support-timeline-and-next-steps)
- [Data recovery for apps with hosted storage](https://developer.atlassian.com/platform/forge/runtime-reference/storage-api/#data-recovery-for-apps-with-hosted-storage).
- [Migration from Data Center to cloud](/cms_trial/space/TBL/74814073/Migration+from+Data+Center+to+cloud/)