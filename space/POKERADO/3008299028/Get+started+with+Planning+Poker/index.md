# Get started with Planning Poker

## Run your first estimation game in Planning Poker

**Estimated time**: about 5 minutes

**No admin access needed.** Once Planning Poker is installed on your organization, any user can create or join a game.

> In this guide, you'll create your first Planning Poker estimation game, invite participants, estimate work items, and complete your first estimation session.

Planning Poker turns work item estimation into a live, consensus-based team activity, right inside Azure DevOps, no separate tool or spreadsheet.

![PPADO.gif](/cms_trial/assets/a9e46c2c-152b-46e1-b4b0-25c877e32590.gif)

## Before you begin

Before you start, make sure that:

- You have access to an Azure DevOps project.
- Planning Poker is installed for your Azure DevOps organization. See [Install Planning Poker in Azure DevOps](/cms_trial/space/POKERADO/3341353014/Install+Planning+Poker+in+Azure+DevOps/).
- Your project already contains the work items you want to estimate.
- Anyone participating in the estimation session has access to the same project.

## Create your first estimation game

1. 1

   Open Planning Poker. In your Azure DevOps project's left-hand menu, click **Planning Poker**.
2. 2

   Click **+ Create Game**, give it a name, and select one or more backlog work items to estimate.
3. 3

   Click **Share game** to invite your team to vote.

   ![image-20260820-195114.png](/cms_trial/assets/d36f68a2-5101-4dbe-8542-671c842e097b.png)
4. 4

   Pick a card from your deck (Fibonacci, T-shirt sizes, or whatever your team has configured) to vote for the first item.

   ![contentId-3008299028](/cms_trial/assets/d067b941-ff80-4c7f-b9b9-4ba4a32a08d4.png)

   **Playing solo right now?** Open the game's participant link in a second browser window (or hand it to a teammate). The reveal step is more meaningful with a second vote to compare against.
5. 5

   Click **Reveal** to see everyone's card side by side. If votes match, click **Accept** to save the estimate straight to the work item. If they don't match, discuss and vote again until you agree!

   ![contentId-3008299028](/cms_trial/assets/13fb8c4e-2afc-4173-a0dd-cc0f8ba13f09.png)

   Repeat for each remaining item in the game. Once everything's estimated, the moderator can end the game.

   #### Re-voting and re-estimating

   If votes don’t line up, the moderator can reset the round so that the team votes again, as many rounds as it takes to reach agreement. The same flow works for re-estimating work: reopen a game (or start a new one) on items that rolled over from a previous sprint and re-vote so the estimate reflects what the team now knows.

---

**Distributed team?** Async games let people vote on their own schedule instead of needing everyone live at once. See [Use async estimation for distributed teams](/cms_trial/space/POKERADO/3560898577/Use+async+estimation+for+distributed+teams/) to learn how this may be the best feature in Planning Poker!

**Pro-tip!**

Skip the full game next time. Estimate directly from a work item's detail view using the embedded Planning Poker section.

![contentId-3008299028](/cms_trial/assets/4c9ef229-933d-4ea7-8a47-2ba4d9c09d50.png)