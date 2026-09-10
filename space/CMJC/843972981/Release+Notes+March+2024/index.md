# Release Notes March 2024

**Release date**: March 20, 2024

Our team is thrilled to announce the latest release of Configuration Manager for Jira (CMJ) Cloud.

---

## Enhancements

We’ve made improvements to how Configuration Manager for Jira (CMJ) Cloud handles different problems during the analysis phase of deployment.

## Improved handling of duplicate tabs on a screen

Now, CMJ Cloud detects tabs with the same name on a single screen and shows an error during the analysis phase of deployment. The tabs in a screen must have unique names. To avoid the conflict, you need to ensure the tabs have different names in the source Jira screen. You can’t continue with the deployment before resolving the problem.

## Improved handling of read-only workflows

CMJ Cloud is now able to detect if the deployment tries to update system workflows on the destination Jira Cloud site. System workflows can’t be edited in Jira Cloud as they’re read-only. In this case, you’ll see an error during the analysis phase advising you to rename the workflow. The rename will lead to the creation of a new workflow in the destination. You can’t continue with the deployment before resolving the problem.

## New release notes design

Starting today, Configuration Manager for Jira (CMJ) Cloud will be using a new release notes design. This change will occur throughout all of Appfire’s products, and it’s intended to bring a more unified look to all supported products.

---

## Bug fixes

The following bugs are fixed in this release:

- Board card layout items are created in reversed order.
- Migration failure during an update of a workflow.
- Migration performance issues with a huge number of custom fields.

---

**Questions and feedback**

- Explore exciting features, pricing updates, reviews, and more on the [Marketplace](https://marketplace.atlassian.com/apps/1211611/configuration-manager-for-jira-cmj?hosting=cloud&tab=overview).
- Stuck with something? Raise a ticket with our [support team](https://appf.re/support).
- Do you love using our app? Let us know what you think [here](https://marketplace.atlassian.com/apps/1211611/configuration-manager-for-jira-cmj?hosting=cloud&tab=reviews).

**Credits**

A heartfelt thank you to our valued customers! Your incredible support and feedback inspire us to improve our apps and products continually. You are the driving force behind why we create software. We appreciate your trust in Configuration Manager for Jira (CMJ) Cloud!