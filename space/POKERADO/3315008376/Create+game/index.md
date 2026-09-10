# Create game

1. Click **+ Create game** in the main Planning Poker window to start a new estimation session. Use the table below to configure the game.

![contentId-3315008376](/cms_trial/assets/2a8612a2-6d55-4519-b68b-4feb2d18064b.png)

| **Field** | **Description** |
| --- | --- |
| **Game name** | Name your session, or use the auto-generated default. |
| **Work item type mappings** | Shows which estimation type (Story Points, Hours, T-shirt sizes) and card deck apply to each work item type. Expand **Settings preview** to view current mappings, or edit the defaults on [Configure game settings and card decks](/cms_trial/space/POKERADO/3562700831/Configure+game+settings+and+card+decks/). |
| **Suggested final estimate** | Choose how the app proposes a final score once votes are revealed. This takes effect the moment the moderator clicks Reveal during the game:   - **Consensus**: requires all estimators to agree on the same value. If votes differ, the group discusses and votes again on the same item, there's no limit on how many rounds an item can go through. - **Average**: exact mathematical average of all submitted estimates - **Average (rounded)**: average rounded to the nearest value in the active deck - **No suggestion**: moderator sets the value manually |
| **Async mode** | Toggle for asynchronous sessions.   - **Disabled (default):** real-time voting, cards revealed dynamically - **Enabled:** each participant estimates at their own pace; the moderator sets the final estimate once all submissions are in. This mode is ideal for distributed teams across time zones. See [Use async estimation for distributed teams](/cms_trial/space/POKERADO/3560898577/Use+async+estimation+for+distributed+teams/). |
| **Coffee card** | Optional checkbox that adds a coffee-break card to the deck, letting estimators signal they need a pause or that discussion has stalled. |
| **Roles and Permissions** | Assign users to roles by typing their names into the people-picker fields:   - *Moderators*: Control the session: start and flip rounds, reset rounds if a re-vote is needed, and submit the final estimate to Azure DevOps. - *Estimators*: Core team members who vote on work items using the configured card deck. - *Spectators*: Can view the session but not vote. Typically Product Owners, Scrum Masters, or stakeholders who want visibility without influencing the estimate. |

1. Click **Next** to proceed to work item selection.

## Work item selection

Select the work items to estimate. Once you're done, click **Create game** to launch the session.

#### By Sprint

Pick a team and sprint to load its backlog items. Use the refresh icon to reload after changes made elsewhere. An **Empty sprint** message appears if the sprint has no items.

#### By Query

Import items from an existing Azure DevOps query. If none exist, click **New Query** to build one.

#### Work Items

Add items directly by ID or title using **+ Add items**, or select items in your ADO backlog, open the context menu, and choose **Estimate in Planning Poker**. Click **Clear** to reset your selection.

![contentId-3315008376](/cms_trial/assets/4c6ccb4f-f8d9-4726-9a5a-4eda1ab5a5ae.png)