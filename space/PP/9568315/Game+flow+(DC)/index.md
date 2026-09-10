# Game flow (DC)

This page is about **Planning Poker for Jira Data Center**. Using **Cloud**? [**Click here**](/cms_trial/space/PP/1144061974/Planning+Poker+for+Jira+Cloud/).

This page provides a comprehensive overview of the game flow.

## How to join the game

Users can easily join a game once it’s been created. Here’s how:

1. **Using the Planning Poker Dashboard**

The primary method is through the Planning Poker dashboard. To access it, click the app logo either in the Jira Apps menu or the project sidebar. On the dashboard, you'll find a list of recent games created within your Jira.

From there, you can:

- Join a game as a player by clicking **Join**.
- Share or join the game by using the copy link option.

  ![image-20240731-170005.png](/cms_trial/assets/760a12fc-c08c-4dbf-8b8e-7e2fdbca1475.png)

1. **Via Invitation Email**

Another way to join a game is by following a game link from an invitation email sent by the administrator. When you join a game through an invitation link, you'll always start as a participant (not a spectator).

![contentId-9568315](/cms_trial/assets/929a6707-c76f-4540-8d58-c83e3ffabef1.png)

**Before starting the game, it’s crucial that you establish your team’s communication method.** While Planning Poker is an effective tool for team estimation, it doesn't include built-in communication features, as different teams prefer different methods.

To ensure effective communication, the person responsible for estimation to gather all players in a meeting room, Slack channel, Zoom conference, or another suitable tool. Strong communication will lead to successful estimations!

---

## Estimation process

The main purpose of a Planning Poker game is to estimate the issues you've added to it. This estimation process is broken down into organized rounds. Each round focuses on one issue and aims to decide its fate – whether it gets postponed, removed, or assigned a final estimation value. Typically, the number of rounds matches the number of issues for estimation.

Each round consists of three phases:

- Backlog Phase
- Voting Phase
- Discussion Phase

Let's delve into each phase for a deeper understanding.

### **Backlog phase**

#### Purpose

The Backlog Phase serves as the initial step of each round, where participants await instructions from the game admin.

#### Progression

| 👤 **Game Admin** |
| --- |
| The admin's main task in this phase is selecting an issue for estimation, but can perform many other specific actions: image-20240731-173451.png  1. **Estimate the first backlog issue –** The admin can select a specific issue or simply click here to start estimating from the first backlog issue. 2. **Quick add –** The admin can add an issue to the game backlog by typing its key (e.g., JRCS-10) and clicking **Quick add**. The added issue is placed at the top of the backlog list. 3. **Re-import backlog for current JQL –** The admin can search Jira projects for issues using JQL and add them to the game's backlog. The JQL-query, used to filter and add issues, is saved as a game parameter. If issues were added or removed during the game, the admin can restore the initial backlog list using this feature. This feature can be used without affecting any issues that have already been estimated in the game, regardless of whether they were quick-added during the game or not. 4. **Estimate now –** The admin can select issues to estimate in any order. Clicking this button initiates the voting phase for the selected issue.   The backlog list is accessible to the game admin throughout all phases. In addition to providing a quick overview of issue details, the backlog enables the admin to swiftly estimate an issue by clicking on it and selecting **Estimate now**. Clicking this button concludes the current round and initiates the voting phase for the new round to estimate the selected issue. The current issue is then moved to the top of the game's backlog list. image-20240731-173737.png Additionally, the estimated items archive allows game admins to review estimation history and make changes to the game's backlog. When you click on an issue in the archive, a window appears showing its estimation history and two buttons: image-20240731-175046.png  1. **Estimate now –** Clicking this ends the current round and starts a new round's voting phase immediately. The selected issue is moved to the top of the game's backlog for re-estimation. 2. **Delete –** Clicking this removes the issue from the estimated issues archive. It doesn't impact the current round, but the issue will no longer be in the archive. The deleted issue's estimation value is subtracted from the estimated points displayed in the sidebar. |

| 👥 **Estimators/Spectators** |
| --- |
| Theycan observe the list of issues to estimate, participants' information, and previous estimations. The main task is to wait for a game admin to choose an issue to estimate. |

When the game admin chooses an issue to estimate, the Backlog Phase ends, and the round proceeds to the Voting Phase.

The Backlog Phase can be performed automatically in the background without the game admin's interference. If you prefer this, enable [**Round Autostart**](/cms_trial/space/PP/9568359/Game+configuration+(Cloud)/) in the game configuration. In this case, the issue to be estimated in the next voting phase is picked from the top of the backlog list. If you're expecting to select the next issue to estimate manually and have missed your backlog phase, check your game configuration.

---

### **Voting phase**

#### Purpose

The Voting Phase is the core of the estimation round. Its process varies based on roles, but the goal remains simple: participants and the admin provide their estimates for the current issue.

#### Progression

Each player (except spectators) receives a number of cards, depending on the card deck type selected during the game configuration. Typically, the cards in your hand will look like this:

![image-20240731-175259.png](/cms_trial/assets/00ad4f14-5e29-476a-96ff-a792702bc2ad.png)

| 👤 **Game Admin** |
| --- |
| Admins estimate the issue just like estimators but have additional responsibilities. They are provided with a group of additional controls, available to them during the voting phase. These controls allow the game admin to commit the following actions: contentId-9568315  1. **Reveal cards –** Instantly reveal played cards, concluding the voting phase and initiating the discussion phase. Estimations from participants who haven't played their cards won't be considered during the discussion. 2. **Skip & postpone –**  Admins can decide to postpone the current issue for later estimation rounds without initiating the discussion phase. The issue being voted on will be moved to the bottom of the game backlog list. 3. **Skip & remove –** Admins have the authority to skip and remove the current issue from the game backlog. If it's the last issue to estimate, the game ends. When an issue is removed from the game backlog, it remains in the Jira backlog. The removed issue can be brought back to the game backlog by re-importing JQL. |

| 👥 **Estimators/Spectators** |
| --- |
| - Estimators are responsible for providing estimates for the current issue. - They choose a card that best matches their estimation of the issue, considering factors like deadline, difficulty, and complexity. - They play their cards face down, keeping their estimations private.   If you change your mind before revealing the cards, you can switch cards by clicking a different one or confirming the "Take it back" action. |

The Voting Phase concludes when all game participants have played their cards or in the following circumstances:

- The admin uses their **Reveal cards** privilege.
- The round timer's countdown reaches its end, whether initiated by the game admin's **Start countdown** privilege or the **Timer auto-start** game configuration option.
- The participants haven't played their cards and have gone spectators.

In any of these scenarios, once the Voting Phase ends, all played cards are revealed to all game participants and spectators. Additionally, certain phase statistics are presented, and the round transitions to the Discussion Phase.

---

### **Discussion phase**

#### Purpose

The Discussion Phase is the final stage of the round, focusing on reaching a consensus regarding the estimation for the current issue through team collaboration.

#### Progression

In this phase, all played cards are unveiled to every participant. Estimations are visually represented in cards, facilitating easy sharing and discussion.

| 👤 **Game Admin** |
| --- |
| In this phase, estimations by participants are organized based on the game's deck type and serve as active controls for the game admin. Hovering over an estimation button triggers the estimation context section. They are provided with a group of additional controls, available to them during the voting phase. These controls allow the game admin to commit the following actions: contentId-9568315  1. **Save –** Enter and save the final estimation value during the discussion phase—the key action in the game. All participants need to agree on the estimation value for the current issue. Once an estimation value is entered and this button is clicked, it becomes a parameter for that issue and moves the game to the next round if there are more issues in the backlog. If an estimation value is saved for the last unestimated issue, the game ends.     - **Suggested/Average –** You can use this overview to simplify decision-making. It presents the estimation value chosen by most players and an average estimation value based on all estimations from the round's voting phase.   **Keep in mind that you need to match your deck type with a storage field.** To accurately save an estimation, understanding the data type is crucial for proper storage within the designated Jira issue field. Ensure that the export field in your game's configuration matches the data type of the deck you intend to use. If there's a mismatch between the deck type and the export field's data type, be sure to configure a suitable deck mapping.   1. **Replay –**  Admins can restart the voting phase of the current round, discarding all participants' estimations for that round. 2. **Skip & postpone/remove –** These buttons function similarly to how they did during the voting phase.. |

| 👥 **Estimators/Spectators** |
| --- |
| - Participants engage in discussions under the guidance of the scrum master to arrive at a mutual consensus regarding the estimation for the current round's issue. |

Once a consensus is reached, the game administrator submits the estimation value, and the game advances to the next round or concludes.

---

### **End of the game**

A Planning Poker game ends when:

1. No rounds remain, and all issues are estimated.
2. The game admin uses the **Finish Game** privilege.

Upon the game's conclusion, a cheerful notification informs players. Finished games can be reopened if needed by clicking **Re-open game** from the top app menu. Estimated issues are also accessible in the “Advanced Issue Search” for further editing or bulk editing.

![image-20240731-175657.png](/cms_trial/assets/30d8484c-aa00-4a39-829f-1831f05707e3.png)

When the game is finished, you can export it to CSV format with summarised estimation data through the dashboard.

![image-20240731-175753.png](/cms_trial/assets/773b7ebe-936b-4c0c-a5d7-b2f59a993338.png)

---

## Next steps

[**Game controls (DC)**](/cms_trial/space/PP/1159561645/Game+controls+(DC)/)