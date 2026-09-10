# Game configuration (DC)

This page is about **Planning Poker for Jira Data Center**. Using **Cloud**? [**Click here**](/cms_trial/space/PP/1144061974/Planning+Poker+for+Jira+Cloud/).

## Overview

A Planning Poker game allows teams to cast their votes in story points, T-shirt sizes, or time estimates. This fosters active discussions and consensus-building among team members.

You can easily manage your game's backlog, invite teammates, view and edit task details or comments during estimation, and save the estimates in a designated Jira field. Additionally, you can estimate on your preferred device, host private or password-protected sessions, and fine-tune your game using advanced settings.

We highly recommend reviewing the [game basics](/cms_trial/space/PP/9568521/Game+basics/) before you start configuration.

## Requirements

- Before you start your very first Planning Poker game you should provide the app with content to estimate. To do this, you have to:

  - Create at least one Jira project.
  - Create at least one issue that you want to estimate in any Jira project.
- Ensure all team members can participate simultaneously.

**Project access management**

Always check user access rights in the project you're estimating and ensure that you've set up permissions in a way that allows all intended participants in your Planning Poker game to view the project's issues. Misconfigured access can prevent some users from seeing issues during the game, especially when voting. Refer to Jira’s [Configure projects](https://confluence.atlassian.com/adminjiraserver/configuring-projects-938847065.html) and [Manage project permissions](https://confluence.atlassian.com/adminjiraserver/managing-project-permissions-938847145.html) articles for details.

## How to start a Planning Poker game

### Step 1: Start a game

If you have a project with issues to estimate, you can start your game.

| **If you haven’t created any games yet:** | **From the Planning Poker app dashboard**: |
| --- | --- |
| Your dashboard will look like this: contentId-511967561 Simply click **New game** to start configuring your game. | Open the app dashboard by clicking **Planning Poker** from the Jira navigation bar, click **New Game**. contentId-511967561 |

### Step 2: Configure the Planning Poker game

After selecting to create a game, Planning Poker will navigate you to the game configuration menu, which is divided into three sections: Game basics, Game administration, and Game flow. It will help you customize the game, making estimations as close to your project's traits as possible.

#### **Game basics:**

Here you need to enter the most essential parameters of your game. This includes:

![contentId-511967561](/cms_trial/assets/a5b4b467-b3fb-4b9b-9e69-9dc573676b35.png)

1. **Game name –** Name your session. Be creative to avoid confusion when viewing the game list in the Planning Poker Dashboard.
2. **Export estimates to –** Select a field from the issue object where the estimated points value will be stored once the issue is estimated. We show you both the field name and its ID, making it easy to distinguish between default fields and fields you've created yourself. You can use the following fields:

   - **Story Points**: This field stores integers and is suitable for saving numerical estimations like Fibonacci deck-type cards or custom numerical deck cards.
   - **Comments**: This field stores string values, making it ideal for abstract estimations such as t-shirt sizes or custom deck non-numerical estimation values.
   - **Original Estimate**: This field stores time units like 1h, 30m, 5m, etc. It works well with an hours deck type or a custom deck containing cards with time unit estimation values.
   - **Remaining Estimate:** This field stores time units representing the remaining effort required to complete the task, e.g., 1h, 30m, 5m, etc.
   - **Custom fields:**

**IMPORTANT:**

To make Story Points, Story Point Estimate, Remaining Estimate, and Original Estimate fields accessible for all issue types, you need to manually add them to the issue types you plan to estimate. To learn how, please watch [this video](https://www.youtube.com/watch?v=8kFACfQJHug&feature=youtu.be). Additionally, explore our [FAQ section](/cms_trial/space/PP/9568458/FAQ%3A+Planning+Poker+for+Jira/) for further guidance.

Furthermore, when you attach a custom field to an issue type, and the field's name includes the words "story" or "point," it will appear as a custom field in the "Exports Estimates To" dropdown menu.

1. **Card deck –** Choose the front values on cards that players will use to vote when estimating an issue. You can select from predefined card deck templates or customize them as needed. You can also employ labels to conceal specific values, allowing you to focus on relative sizes rather than fixating on exact numerical values during estimation.

   - **Fibonacci:** Includes cards with values 1, 2, 3, 5, 8, 13, 21, 34, and 55.
   - **T-shirt:** Features cards labeled as XXS, XS, S, M, L, XL, and XXL.
   - **Labeled T-Shirt:** Combines labels with values, such as XXS=0.5, XS=1, S=2, M=3, L=5, XL=8, and XXL=13.
   - **Hours:** Consists of cards marked as 1h, 2h, 3h, 4h, 5h, 6h, 7h, 8h, 9h, 10h, 11h, and 12h.
   - **Custom:** Whenever you customize a card deck template using special input, it switches itself to a *Custom* card deck. When you customize the card deck, use commas to separate different values. This tells you what type of card it is and how many of them there are. If you put in three values separated by commas, players get only three cards for estimating issues in the game.

To use text or abstract values for estimating numeric custom fields, employ value mapping in the format: `LABEL=VALUE`. For instance, the Labeled T-Shirt deck uses this format: XXS=0.5, XS=1, S=2, M=3, L=5, XL=8, XXL=13.

1. **Add "?" and "coffee" cards to the deck –** If enabled, this adds two extra cards to your deck:

   ![contentId-511967561](/cms_trial/assets/fe3fd2bd-0d42-4aa1-8f8a-6a29bb71634d.png)
   - **"?" –** Allows a player to express uncertainty when estimating the current issue.
   - **"coffee" –** Allows a player to inform other game participants that they need a break.
2. **Round autostart –** If enabled, the game's next round will start automatically once the current issue's estimation is successfully saved or if the issue is skipped. The next issue to estimate will be automatically selected from the top of the game backlog.
3. **Notify participants –** Here you select the participants of the game and you can send invites from the **Edit game** screen after the game is created.

![contentId-511967561](/cms_trial/assets/87f25cd4-9d0f-48f8-98dc-435a21146c12.png)

To include a user in the notification list, simply click the "Select User" dropdown and search for the desired participant by typing their username. Notification email(s), which contain a URL for seamless access to the game, will be sent in bulk to all the users in the list:

![contentId-511967561](/cms_trial/assets/a04c6425-6213-40f2-9da0-154396caf0b2.png)

1. **Show advanced configuration –** Once you've covered the basics, you can click ***Next: Edit backlog*** to start editing the game backlog. Or you can click this option to continue configuring with further advanced settings.

### Step 3: Switch to advanced configuration (Optional)

#### **Game administration:**

![contentId-511967561](/cms_trial/assets/c6a8e03f-eaa2-48c4-aefd-e864538301ac.png)

1. **Game description –** Describe your game to make its purpose clear to all estimation participants.

   ![contentId-511967561](/cms_trial/assets/e4e66fc3-6c3b-47ff-915c-22f98a958bc0.png)
2. **Private game –** If checked, your game will be hidden on the Planning Poker Dashboard for all project participants, except the game administrator. You will be able to add users to a private game only by sending them an email notification with the game’s URL, as described in the #6 “Notify participants” section.
3. **Multiple admins –** By default, the game creator has full administrative control. Here you can also add multiple game admins by simply selecting their names from the dropdown. This list will also display users who currently have administrative privileges regarding the game. To take away their admin privileges, simply click the cross icon next to the user's name.

**All game administrators have the same level of privileges** – so there are no master or regular game admin roles. This means that each game admin can control the list of game administrators by adding or removing users. Mind it to use additional admins feature wisely.

1. **Admin password –** The admin can add more admins by editing the #10 “Multiple admins” section or the *Add additional game admin* button in the game's top bar. However, there may be instances when the current admin is unavailable. This feature allows other players to become additional game admins if they know the password set here, even if the current admin is unavailable. If the Admin Password field is not empty, a "Become Game Admin" button will appear in the game's top bar. By clicking it and entering the admin password, the user becomes a game administrator.
2. **Permission by group –** Here you can restrict the game for any user group.
3. **Custom fields above –** Add extra custom fields to appear above the issue description during the game for quick reference.

   ![contentId-511967561](/cms_trial/assets/50a7438a-7612-40a4-b094-55b09c8ab122.png)
4. **Custom fields above –** Add more custom fields to appear below the issue description.

   ![contentId-511967561](/cms_trial/assets/8863362e-130a-41fa-9cb1-58e492d1e0b7.png)

#### **Game flow:**

![contentId-511967561](/cms_trial/assets/0d8b516a-812b-4a7d-9a57-18afa6f80b36.png)

1. **Timer autostart –** When enabled, this feature initiates the countdown for the round timer at the start of the voting phase. If the timer reaches its limit, the voting phase concludes, regardless of whether all users have submitted their cards. The default timer duration is 45 seconds.

Timer autostart **won't** trigger on the very first round of the game. Planning Poker expects the scrum master to ensure the presence of all required participants for this initial round.

1. **Timer sound –** When enabled, there will be sound notifications at the start and end of the timer.
2. **Timer duration –** Change the round timer duration from the default 45 seconds to any other value. This will affect both the timer autostart (if enabled by the above option) and the timer started by the admin's actions.
3. **Labels (Estimated, Skipped, Removed) –**

   - **Estimated –** To tag estimated issues, just enter the label you want. When you save the estimation, the label will be added to the issue.
   - **Skipped –** To tag issues that are postponed or canceled, enter the desired label. The label will be added to an issue when the admin clicks either the "Skip and postpone" or "Skip and remove" button.
   - **Removed –** To remove a label from an estimated issue, enter the label values you want to remove. The label will be removed from the issue after the estimation is saved successfully.

**Label names cannot contain spaces**, so format them like this: label-name or label\_name. Later on, you can view and delete labels when browsing issues. They are also used for advanced issue searches via Jira Issues and filters service.

1. **Estimation context –** This powerful feature in Planning Poker helps you make better estimations in a Scrum approach. When the voting phase starts and you hover over a card with a value (e.g., 3), Planning Poker will search for all previous issues in the project that were estimated as 3. This helps you see how similar issues were estimated in the past:

   ![contentId-511967561](/cms_trial/assets/edc1c9bb-bafb-42bf-abd1-0b862fc10ce0.png)

Here you can control the context to fit your needs. For example, you could set the Estimation context to only display issues with specific labels, like “design” and “UX”, by entering the following JQL query into the Estimation context settings input: "labels IN (design, UX)".

To build JQL queries different from the one shown above, you have to be familiar with [Jira Query Language (JQL)](https://www.atlassian.com/blog/jira-software/jql-the-most-flexible-way-to-search-jira-14).

**How?** The logic of estimation context is closely tied to game configurations. Here's how it works behind the scenes:

- Planning Poker looks for previous estimations within the project's current issue.
- It only queries previous estimations based on the field you've chosen in the "Export estimates to" dropdown during the current game setup.
- If you've set up Deck mapping, Planning Poker will look for previous estimations equal to the value mapped to the card front.

1. **Issue status estimated –** Here you can choose a state (*To Do*, *In Progress*, etc.) to transition the issue after estimating it. Enter the"transition name" to the needed state.
2. **Issue status removed –** Here you can choose a state *(To Do, In Progress, etc.)* to transition the issue after it’s removed or skipped from the estimation.
3. **Move to Sprint –** You can move an issue to a specific sprint by selecting the board and then the sprint.

Click **Next: Edit Backlog** to move to the next step.

### Step 4: Configure backlog

Here the admin searches for specific issues within Jira projects, add them to the game's backlog, and arrange them in the desired order. The filter options are:

![contentId-511967561](/cms_trial/assets/364e0417-88b1-4624-94d9-e1ad013aceb2.png)

1. **Project –** Choose specific Jira projects from which the issues will be sourced for estimation. Once you click on a project, all the issues in it will be added to the game.
2. **Type –** Filter issues based on their type, such as Change, Incident, Bug, Epic, Problem, Service request, and more.
3. **Status –** Select issues based on their current status within the workflow. Options could include Authorize, Draft, Awaiting approval, and more.
4. **Assignee –** Select issues based on their current assignee.
5. **Fields –** Use this dropdown to add additional filters to your filter bar. Once the filter is selected in the dropdown, it will be added to your filters bar and you will be able to use it along with the default filters.
6. **My Filters –** You can also use your own custom filters. For more information on creating custom filters, refer to the [Jira documentation](https://confluence.atlassian.com/jirasoftwareserver0903/configuring-filters-1178870343.html).
7. **Search board and then sprint… –** Here you can select a board and also a sprint. Keep in mind that this section and the JQL are not synchronized, so we recommend using either these filters or the ones that come before them on their own.
8. **JQL –** This section displays the Jira Query Language (JQL) translation of your selected filters and offers a way to create more complex and customized queries. If you're a seasoned Jira user, you can write your own JQL query into input to find issues you want to add to your Planning Poker game. Building a custom JQL query is a flexible approach to commence search in your Jira projects, but to master it you have to know how to deal with operators, expressions, and other features of JQL. Feel free to surf [Jira tutorials](https://www.atlassian.com/blog/jira-software/jql-the-most-flexible-way-to-search-jira-14) to learn more about JQL.

   ![contentId-511967561](/cms_trial/assets/90cd038b-cbbf-462d-a0f1-64f64835e558.png)

The JQL query you use to add issues to the game **is saved** **as one of the game parameters**. If any issues are deleted or added during the game, the admin can quickly restore the backlog by using the **Re-importing backlog for current JQL** feature. This will add issues from the JQL query that are missing and remove issues that are no longer in the query.

1. **Columns –** Use this dropdown to add extra columns to your backlog.

   ![contentId-511967561](/cms_trial/assets/22212fe5-14c5-4516-bf03-a489eae99deb.gif)
2. **Checkbox column –** To further filter the issues, use this column. To remove any issues that you don’t want to have in the game, check the boxes next to them and remove the selected ones, or simply click the trash icon next to the issue.

#### **Ordering the Backlog:**

Once you've added all the issues you want to include in your Planning Poker game, it's time to arrange them in the desired order. The order of the issues is important not only for keeping the game organized but also for when the next round starts automatically (if #5 “Roud autostart” is enabled) as it selects the top issue from the backlog list. Here's how you can edit your backlog:

- **Drag & Drop –** This is the old-fashioned way: Just click and hold the issue you want to move, drag it to the place you want it in the list, and drop it.
- **Order by Columns –** You can also order issues by columns, ascending or descending. To do so, just pick a header of a column you want your issues to be ordered by and click it. Once clicked your issues will be ordered by a chosen column, ascending. If the same column is clicked once more, the order will be switched to descending, and so on.

  - You can easily add other columns to order your backlog by clicking the **Columns** button and selecting the column(s) you want.

### Step 5: Start the game

Once you have tailored your backlog to best suit your needs, click **Next: Start game** to start the Planning Poker session. A breakdown of the game process is provided in [**Game Flow**](https://appfire.atlassian.net/wiki/pages/createpage.action?spaceKey=pp&title=Game%20Flow&linkCreation=true&fromPageId=511967561) chapter of this documentation.

You can always modify the session configuration even after it's begun. To do this, simply click **Edit game** or **Edit backlog** on the session page.

![contentId-511967561](/cms_trial/assets/998ca679-5a20-41e0-87b7-e525b3a8a8bf.png)

Planning Poker remembers the settings you've saved before! When you begin a new game, it will use the last saved settings as the default configuration. For example, if you previously selected **Story Points** in the *Export estimates to* dropdown and saved your configuration, the next time you start a new game, **Story Points** will automatically appear as the default choice in the *Export estimates to* dropdown.

## Next steps

Once you've completed configuring your game, refer to the following documentation to assist you during gameplay:

[**Game controls**](/cms_trial/space/PP/492110077/Game+controls+(Cloud)/)

[**Game flow**](https://appfire.atlassian.net/wiki/pages/createpage.action?spaceKey=pp&title=Game%20Flow&linkCreation=true&fromPageId=511967561)