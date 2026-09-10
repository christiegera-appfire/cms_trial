# Planning Poker tab estimation (Cloud)

This page is about **Planning Poker for Jira Cloud**. Using **DC**? [**Click here**](/cms_trial/space/PP/1144061984/Planning+Poker+for+Jira+Data+Center/).

It's possible to estimate each Jira issue in the Async mode, which is useful for distributed teams that can't have an "on-line" session. Currently, there is no unified "session" concept, as in the classical game version. Instead, all participants are invited to estimate directly in the issues directly through the Planning Poker tab tab on the right side of the issue screen.

The only thing the admin needs to do is simply share the JQL filter with the participants. Then, they can go over the issues and estimate them one by one. After voting, the participants refresh the page and the estimates appear. Then, everyone can see who voted for which, and the estimate is saved before moving on to the next issue.

Below is a brief overview of the available functionality, as well as how to configure the game.

### Prerequisites

- The Jira admin must check the toggle for **Enable estimation from issue details** in global settings.
- The project admin must check the toggle for **Show Planning Poker in board menu** and **Enable estimation from issue details** in project settings.

For more information, refer to the [Settings documentation](/cms_trial/space/PP/661454980/Settings+(Cloud)/).

### Configure the tab

1. Navigate to **Apps** > **Manage your apps**.
2. Find Planning Poker in the apps list, and click **Configure**.
3. Select the deck type and the estimation field you want to save the estimates to. For more details, refer to this [documentation](/cms_trial/space/PP/9568359/Game+configuration+(Cloud)/).

   ![Screenshot 2024-07-29 at 14.58.01.png](/cms_trial/assets/16011858-e2a3-479e-a8f6-74b474a71071.png)
4. Click **Save**.

Then, you can continue creating the game itself. Here is how:

1. Create a JQL (Jira Query Language) filter that includes the issues you want to estimate. Consult Jira documentation to learn more about JQL.
2. Share the JQL filter with team members.
3. To get the estimation process started, open the first issue.
4. Click the **Planning Poker** tab on the right side of the screen.

   ![image-20240729-112000.png](/cms_trial/assets/cadf701f-91d4-40ae-ad8d-6b76d489b5ae.png)

This will reveal the card deck and start the initial voting phase.

### Initial voting phase

1. In the Planning Poker tab, participants vote using a deck of cards to estimate the issue.
2. To view results, refresh the page and click **Reveal**.

   ![5fb8ab42-2ad3-4df7-9b7a-c37f6438f88c.png](/cms_trial/assets/f43152df-d0f7-4147-a695-7448a549cb13.png)

### Summary phase

The summary of all estimates from all users will be grouped by the Story Points values.

1. Reach a consensus and click the suggested card to assign the estimation value.

   ![03bfee05-3ded-41f2-bbe3-5816e6e9941e.png](/cms_trial/assets/5ca0a04a-fd6d-4140-8f09-f43d18e9298f.png)
2. Pick the final estimate, or set the final estimate and click **Save estimate**.
3. To start fresh, you can use the **Reset** button, which clears previous estimates and restarts the estimation.

That’s it! This provides a flexible and convenient way for teams who want to keep things at the issue level. However, if you don’t need this feature, you can remove the Planning Poker tab from your issue view by opening the app’s project settings, and unchecking the **Enable estimation from issue details** box.