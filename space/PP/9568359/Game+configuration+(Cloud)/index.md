# Game configuration (Cloud)

This page is about **Planning Poker for Jira Cloud**. Using **DC**? [**Click here**](/cms_trial/space/PP/1144061984/Planning+Poker+for+Jira+Data+Center/).

## Overview

A Planning Poker game allows teams to cast their votes in story points, T-shirt sizes, or time estimates. This fosters active discussions and consensus-building among team members.

You can easily manage your game's backlog, invite teammates, view and edit task details or comments during estimation, and save the estimates in a designated Jira field. Additionally, you can estimate on your preferred device, host private or password-protected sessions, and fine-tune your game using advanced settings.

We highly recommend reviewing the [game basics](/cms_trial/space/PP/9568521/Game+basics/) before you start configuration.

## Requirements

- Before you start your very first Planning Poker game you should provide the app with content to estimate. To do this, you have to:

  - Create at least one Jira project.
  - Create at least one issue that you want to estimate in any Jira project.

**Project access management**

Always check user access rights in the project you're estimating and ensure that you've set up permissions in a way that allows all intended participants in your Planning Poker game to view the project's issues. Misconfigured access can prevent some users from seeing issues during the game, especially when voting. Refer to Jira’s [Configure projects](https://confluence.atlassian.com/adminjiracloud/configuring-projects-776636280.html) and [Manage project permissions](https://confluence.atlassian.com/adminjiracloud/managing-project-permissions-776636362.html) articles for details.

## How to start a Planning Poker game

### Step 1: Start a game

If you have a project with issues to estimate, you can start your game. You can initiate your game either from the Planning Poker app dashboard or the Jira Backlog view.

| **If you haven’t created any games yet:** | **From the Planning Poker app dashboard**: | **From Jira Backlog view:** |
| --- | --- | --- |
| Your dashboard will look like this: contentId-9568359 Simply click **New game** to start configuring your game. | Open the Planning Poker dashboard (**Apps** > **Planning Poker**), click **New Game**. image-20240722-180549.png | To start a game from Jira Backlog View, **you need to have started a sprint in a project**. The sprint must include issues you want to estimate.  This feature is currently available **only** in **Company-managed** projects. image-20240722-185010.png Go to Backlog view in your project sidebar, and click **Open in Planning Poker** from the options dropdown.  Can’t see the *Open in Planning Poker* option? This could be because you have the **Enhance my board and backlog** toggle enabled. Disable it, and try again. contentId-9568359 |

---

### Step 2: Configure the Planning Poker game

After selecting to create a game, Planning Poker will navigate you to the game configuration menu, which is divided into two sections: **New game setup** (Basic settings, Advanced settings), and **New game backlog setup**. It will help you customize the game, making estimations as close to your project's traits as possible.

#### **New game setup:**

Here you need to enter the most essential parameters of your game. This includes:

![image-20250717-201558.png](/cms_trial/assets/3a96a7ec-5867-4e7b-9e89-b3817facc01d.png)

1. **Game name –** Name your session or go with a preset one. Be creative to avoid confusion when viewing the game list in the Planning Poker dashboard.
2. **Private game –** If checked, your game will be hidden on the Planning Poker Dashboard for all project participants, except the game administrator. You will be able to add users to a private game only by sending them an email notification with the game’s URL, as described in the “Notify participants” section. Private games can be seen and accessed only by invited Estimators and Spectators.

**Basic settings**

1. **Estimation field –** Select a field from the issue object where the estimated points value will be stored once the issue is estimated. We show you both the field name and its ID, making it easy to distinguish between default fields and fields you've created yourself. You can use the following fields:

   - **Story Points**: This field stores integers and is suitable for saving numerical estimations like Fibonacci deck-type cards or custom numerical deck cards. It's the default estimation field for Company-managed Jira projects and is recommended.
   - **Story Point Estimate**: Similar to the previous field, this one also stores integers and serves as the default estimation field for Company-managed projects.
   - **Comments**: This field stores string values, making it ideal for abstract estimations such as t-shirt sizes or custom deck non-numerical estimation values. It's available by default in all project types.
   - **Original Estimate**: This field stores time units like 1h, 30m, 5m, etc. It works well with an hours deck type or a custom deck containing cards with time unit estimation values.
   - **Custom fields:**

**IMPORTANT:**

Please note that only the Comments field is accessible for all issue types in both team and company-managed projects by default. For Story Points, Story Point Estimate, and Original Estimate, you need to manually add them to the issue types you plan to estimate. To learn how, please watch [this video](https://www.youtube.com/watch?v=8kFACfQJHug&feature=youtu.be). Additionally, explore our [FAQ section](/cms_trial/space/PP/9568458/FAQ%3A+Planning+Poker+for+Jira/) for further guidance.

Furthermore, when you attach a custom field to an issue type, and the field's name includes the words "story" or "point," it will appear as a custom field in the "Estimation Field" dropdown menu.

1. **Card deck –** Choose the front values on cards that players will use to vote when estimating an issue. You can select from predefined card deck templates or customize them as needed. You can also employ labels to conceal specific values, allowing you to focus on relative sizes rather than fixating on exact numerical values during estimation.

   - **Fibonacci:** Includes cards with values 1, 2, 3, 5, 8, 13, 21, 34, and 55.
   - **T-shirt:** Features cards labeled as XXS, XS, S, M, L, XL, and XXL.
   - **Labeled T-Shirt:** Combines labels with values, such as XXS=0.5, XS=1, S=2, M=3, L=5, XL=8, and XXL=13.
   - **Hours:** Consists of cards marked as 1h, 2h, 3h, 4h, 5h, 6h, 7h, 8h, 9h, 10h, 11h, and 12h.
   - **Custom:** Whenever you customize a card deck template using special input, it switches itself to a *Custom* card deck. When you customize the card deck, use commas to separate different values. This tells you what type of card it is and how many of them there are. If you put in three values separated by commas, players get only three cards for estimating issues in the game.

To use text or abstract values for estimating numeric custom fields, employ value mapping in the format: `LABEL=VALUE`. For instance, the Labeled T-Shirt deck uses this format: XXS=0.5, XS=1, S=2, M=3, L=5, XL=8, XXL=13.

1. **Add "?" and "coffee" cards to the deck –** If enabled, this adds two extra cards to your deck:

   ![Screenshot 2024-07-22 at 22.16.24.png](/cms_trial/assets/a7bc8679-58fd-48be-9b35-f220658fc548.png)
   - **"?" –** Allows a player to express uncertainty when estimating the current issue.
   - **"coffee" –** Allows a player to inform other game participants that they need a break.
2. **Game administrators –** Select who will manage the session. By default, the game creator has full administrative control. Here you can also add multiple game admins by simply selecting their names from the dropdown. This list will also display users who currently have administrative privileges regarding the game. To take away their admin privileges, simply click the red cross icon next to the user's name.  
   **Estimators –** Select the estimators.   
   **Spectators –** If there are any, select the spectators.

**All game administrators have the same level of privileges** – so there are no master or regular game admin roles. This means that each game admin can control the list of game administrators by adding or removing users. Mind it to use additional admins feature wisely.

1. **Invite participants via email –** Notify project participants about their involvement in a Planning Poker game via email. This is useful if the estimation session is being held remotely or you’ve set the game type to be Private. Notification email(s), which contain a URL for seamless access to the game, will be sent in bulk to all the users in the list.

   ![contentId-9568359](/cms_trial/assets/62ec2979-8bb0-457c-a1c4-7b566d5233c1.png)
2. **Allow players to update their personal estimates after revealing them –** By default, this option is enabled, allowing participants to change their estimates after the initial reveal. If you disable it, participants will no longer be able to edit their votes once the estimates are revealed. Instead, you’ll need to initiate a re-estimation round if you want to collect new estimates from the team.

Once you've covered the basics, you can click ***Next step*** to start editing the game backlog. Or you can switch to the **Advanced settings** to continue configuring.

**Advanced settings**

![image-20250226-192700.png](/cms_trial/assets/fb90811b-2237-4eac-af4e-0bcb45ce2c5e.png)

**Layout**

1. **Add custom fields to game layout –** Custom fields will be automatically distributed by the order of selection.

**Estimation context**

1. **Enable estimation context –** This powerful feature in Planning Poker helps you make better estimations in a Scrum approach. When the voting phase starts and you hover over a card with a value (e.g., 3), Planning Poker will search for all previous issues in the project that were estimated as 3. This helps you see how similar issues were estimated in the past:

   ![image-20240728-223434.png](/cms_trial/assets/a90f5f45-17c3-4421-9bd5-eceaac2846bd.png)

   **Limit issues pool for estimation context** – Here you can control the context to fit your needs. Use this to reduce the default scope of the estimation context JQL. This will be an additional query command merged as `AND` condition. For example, you could set the Estimation context to display only issues with specific labels, like `design` and `UX`, by entering the following JQL query into the Estimation context settings input: `labels IN (design, UX)`.

To build JQL queries different from the one shown above, you have to be familiar with [Jira Query Language (JQL).](https://www.atlassian.com/blog/jira-software/jql-the-most-flexible-way-to-search-jira-14)

**How?** The logic of estimation context is closely tied to game configurations. Here's how it works behind the scenes:

- Planning Poker looks for previous estimations within the project's current issue.
- It only queries previous estimations based on the field you've chosen in the "Export estimates to" dropdown during the current game setup.
- If you've set up Deck mapping, Planning Poker will look for previous estimations equal to the value mapped to the card front.

1. **Labels –**

   - **Add labels after estimation –**  To tag estimated issues, just enter the label you want. When you save the estimation, the label will be added to the issue.
   - **Add labels to skipped issues –**  To tag issues that are postponed or canceled, enter the desired label. The label will be added to an issue when the admin clicks either the "Skip and postpone" or "Skip and remove" button.

**Label names cannot contain spaces**, so format them like this: `label-name` or `label_name`. Later on, you can view and delete labels when browsing issues. They are also used for advanced issue searches via Jira Issues and filters service.

1. **Change issue status after estimation to –** Here you can choose a state (`To Do`, `In Progress`, etc.) to transition the issue after estimating it. Enter the "transition name" to the needed state.
2. **Move issue to sprint after estimation –** You can move an issue to a specific sprint by selecting the board and then the sprint.

Click **Next step** to configure the backlog.

---

### Step 3: Configure backlog

Here, the admin searches for specific issues within Jira projects, adds them to the game's backlog, and arranges them in the desired order.

First, filter the issues to add them to the game backlog. You can add multiple issues one by one with different searches:

![image-20241105-190724.png](/cms_trial/assets/f9e60d77-241e-4b36-af40-b38f23d57926.png)

1. **Issue name –** Search for specific issues using this search box.
2. **Project –** Choose specific Jira projects from which the issues will be sourced for estimation.
3. **Issue Type –** Filter issues based on their type, such as Change, Incident, Bug, Epic, Problem, Service request, and more.
4. **Status –** Select issues based on their current status within the workflow. Options could include Authorize, Draft, Awaiting approval, and more.
5. **Sprint –** Filter issues associated with a particular sprint.
6. **+ More –** Use this dropdown to add additional filters to your filter bar. Once the filter is selected in the dropdown, it will be added to your filters bar and you will be able to use it along with the default filters.
7. **Order by –** This option enables you to organize items in the game backlog effectively. You can sort items based on various criteria, including Jira rank, priority, and status, with the flexibility to arrange them in either ascending or descending order. When sorting by a single field, you have the option to toggle between filter mode and JQL mode. By default, the order by rank is set to ascending, consistent with JQL settings.

In JQL mode, you can sort by two fields simultaneously, but this is not available in filter mode. If you switch from JQL mode (where two fields are selected) to filter mode, ordering by multiple fields will be disabled.

1. **JQL –** For advanced users, this button offers the option to switch to Jira Query Language (JQL) for more complex and customized queries. If you're a seasoned Jira user, you can write your own JQL query into input to find issues you want to add to your Planning Poker game. Building a custom JQL query is a flexible approach to commence search in your Jira projects, but to master it you have to know how to deal with operators, expressions, and other features of JQL. Feel free to surf [Jira tutorials](https://www.atlassian.com/blog/jira-software/jql-the-most-flexible-way-to-search-jira-14) to learn more about JQL.

The JQL query you use to add issues to the game **is saved** **as one of the game parameters**. If any issues are deleted or added during the game, the admin can quickly restore the backlog by using the **Re-importing backlog for current JQL** feature. This will add issues from the JQL query that are missing and remove issues that are no longer in the query.

Then, further refine the issues and order them accordingly.

![image-20240723-094818.png](/cms_trial/assets/cd2085e4-cbb1-4546-9cb4-256de05a2c5c.png)

1. **Add issues –** Click to add extra issues to the backlog.
2. **Columns –** Use this dropdown to add extra columns to your backlog.
3. **Remove –** Click to remove the issues you don’t want from the backlog.
4. **Checkbox column –** To further filter the issues, use this column. Checked issues will be added to the game; unchecked will be ignored.

#### **Ordering the backlog:**

Once you've added all the issues you want to include in your Planning Poker game, it's time to arrange them in the desired order. The order of the issues is important not only for keeping the game organized but also for when the next round starts automatically as it selects the top issue from the backlog list. Here's how you can edit your backlog:

- **Drag & Drop –** Just click and hold the issue you want to move, drag it to the place you want it in the list, and drop it.
- **JQL –** You can also use `order by ...` in JQL in the *Add issues to game backlog* dialog.

---

### Step 4: Start the game

Once you have tailored your backlog to best suit your needs, click **Start game** to start the Planning Poker session. For a breakdown of the game process, refer to the [**Game flow**](/cms_trial/space/PP/9568315/Game+flow+(DC)/) page.

You can always modify the session configuration even after it's begun. To do this, simply click **Edit game** or **Edit backlog** on the session page.

![image-20240723-100501.png](/cms_trial/assets/23d1df1e-83c2-437c-aaaa-67abe42fffe5.png)

Planning Poker remembers the settings you've saved before! When you begin a new game, it will use the last saved settings as the default configuration. For example, if you previously selected "Story Points" in the "Estimation fields" dropdown and saved your configuration, the next time you start a new game, "Story Points" will automatically appear as the default choice in the "Estimation fields" dropdown.

## Next steps

Once you've completed configuring your game, refer to the following documentation to assist you during gameplay:

[**Game controls (Cloud)**](/cms_trial/space/PP/492110077/Game+controls+(Cloud)/)

[**Game flow (Cloud)**](/cms_trial/space/PP/9568315/Game+flow+(DC)/)