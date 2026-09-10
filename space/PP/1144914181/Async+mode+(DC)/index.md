# Async mode (DC)

This page is about **Planning Poker for Jira Data Center**. Using **Cloud**? [**Click here**](/cms_trial/space/PP/9568359/Game+configuration+(Cloud)/).

It's possible to estimate each Jira issue in the Async mode, which is useful for distributed teams that can't have an "on-line" session. Currently, there is no unified "session" concept, as in the classical game version. Instead, all participants are invited to estimate directly in the issues directly through the Async mode tab.

The only thing the “admin” needs to do is simply share the JQL filter with the participants. Then, they can go over the issues and estimate them one by one. After voting, the participants refresh the page and the estimates appear. Then, everyone can see who voted for which, and the estimate is saved before moving on to the next issue.

Here is a concise overview of the available functionalities and guidance on configuring the game.

## How to configure the Async mode

1. Click the Jira cog icon, then **Manage apps** > OTHER > **Planning Poker Configuration**.
2. Find Planning Poker in the apps list, and click **Configure**.
3. Select the deck type and the estimation field you want to save the estimates to. For more details, refer to this [documentation](/cms_trial/space/PP/511967561/Game+configuration+(DC)/).
4. Click **Save**.

Then, you can continue creating the game itself. Here is how:

1. Create a JQL (Jira Query Language) filter that includes the issues you want to estimate. Consult Jira documentation to learn more about JQL.
2. Share the JQL filter with team members.
3. To get the estimation process started, open the first issue.
4. Scroll down to the Activity section, and click the **Estimate (async mode)** tab.

## Game flow

### Initial voting phase

1. In the **Estimate (async mode)** tab, participants vote using a deck of cards to estimate the issue.

   ![contentId-1144914181](/cms_trial/assets/f11b770c-57f0-4c83-8069-7ee02af0c9d9.png)
2. To view results, refresh the page and click **Show all estimates**.

### Summary phase

1. The summary of all estimates from all users will be grouped by the Story Points values. You can click **Cancel my estimate** to remove your card.
2. Reach a consensus and click the suggested card to assign the estimation value.

   ![contentId-1144914181](/cms_trial/assets/412dcdd8-0674-4fd6-8e57-85ff6ec3b1b7.gif)
3. To start fresh, you can use the **Reset all estimates** button, which clears previous estimates and restarts the estimation.

That’s it! This provides a flexible and convenient way for teams who want to keep things at the issue level. However, if you don’t need this feature, you can remove the Async mode tab from your issue view by opening the app’s global settings, as described above, and checking the **Hide "Async mode" tab on issue details page** box.