# Game flow (Cloud)

This page is about **Planning Poker for Jira Cloud**. Using **DC**? [**Click here**](/cms_trial/space/PP/1144061984/Planning+Poker+for+Jira+Data+Center/).

This page provides a comprehensive overview of the game flow.

## How to join the game

Users can easily join a game once it’s been created. Here’s how:

1. **Using the Planning Poker Dashboard**

The primary method is through the Planning Poker dashboard. To access it, click the app logo either in the Jira Apps menu or the project sidebar. On the dashboard, you'll find a list of recent games created within your Jira. From there, you can:

- Join a game as a player by clicking on the game title.
- Share or join the game by using the copy link option.

  ![image-20240723-151400.png](/cms_trial/assets/c52d80ba-cbd9-4355-96d1-b1b7c3b43b07.png)

1. **Via Invitation Email**

Another way to join a game is by following a game link from an invitation email sent by the administrator. When you join a game through an invitation link, you'll always start as a participant (not a spectator).

![contentId-1149501468](/cms_trial/assets/1c41c6ab-4171-4ebd-a8fa-e3c5468a35f7.png)

**Before starting the game, it’s crucial that you establish your team’s communication method.** While Planning Poker is an effective tool for team estimation, it doesn't include built-in communication features, as different teams prefer different methods.

To ensure effective communication, the person responsible for estimation to gather all players in a meeting room, Slack channel, Zoom conference, or another suitable tool. Strong communication will lead to successful estimations!

---

## Estimation process

The main purpose of a Planning Poker game is to estimate the issues you've added to it. This estimation process is broken down into organized rounds. Each round focuses on one issue and aims to decide its fate – whether it gets postponed, removed, or assigned a final estimation value. Typically, the number of rounds matches the number of issues for estimation.

Each round consists of three phases:

- Backlog phase
- Voting phase
- Discussion phase

Let's delve into each phase for a deeper understanding.

### **Backlog phase**

#### Purpose

The Backlog Phase serves as the initial step of each round, where participants await instructions from the game admin.

#### Progression

| 👤 **Game Admin** |
| --- |
| The admin's main task in this phase is starting the game by selecting an issue for estimation, but they can perform many other specific actions: image-20241105-192947.png  1. **Edit backlog/game –** At any point in the game, you can use these buttons to edit the game’s backlog and the game configuration. 2. **Settings –** The admin can use this icon to restart, finish, or delete the game. If you encounter problems, please use the *Contact us* option. 3. **Hide issues estimated during this game –** As the users estimate during the game, the estimated issues will be hidden in the backlog. 4. **Add issue to backlog –** You can quickly add individual issues to the game backlog using this option. Simply search for the issue key, and click the **Add issue to backlog** button. 5. **Add issues –** The admin can quickly add issues to the game backlog using this button. The added issues are placed at the bottom of the backlog list. 6. **Start now –** Clicking this button initiates the voting phase. The admin can select issues to estimate in any order. Once you click the button, the first issue in your backlog list will be up for estimation.   The backlog list is accessible to the game admin throughout all phases. In addition to providing a quick overview of issue details, the backlog enables the admin to swiftly estimate an issue by clicking on it.  The admin and users can review the estimation history through the game backlog. Once saved, the final estimations are shown next to the issue with green background. The ones that haven’t been finalized yet are in grey. image-20240728-173510.png |

| 👥 **Estimators/Spectators** |
| --- |
| Theycan observe the list of issues to estimate, participants' information, and previous estimations. The main task is to wait for a game admin to choose an issue to estimate. image-20240728-181208.png |

When the game admin chooses an issue to estimate, the Backlog Phase ends, and the round proceeds to the Voting phase.

---

### **Voting phase**

#### Purpose

The Voting phase is the core of the estimation round. Its process varies based on roles, but the goal remains simple: participants and the admin provide their estimates for the current issue.

#### Progression

Each player (except spectators) receives a number of cards, depending on the card deck type selected during the game configuration. Typically, the cards in your hand will look like this:

![image-20240728-182054.png](/cms_trial/assets/fe738614-43e3-465c-8fb3-6c2d72aa6fa0.png)

| 👤 **Game Admin** |
| --- |
| Admins estimate the issue just like estimators but have additional responsibilities. They are provided with a group of additional controls, available to them during the Voting phase. These controls allow the game admin to commit the following actions: image-20240728-184652.png  1. **Reveal cards** – Instantly reveal played cards, concluding the Voting phase and initiating the discussion phase. Estimations from participants who haven't played their cards won't be considered during the discussion. **Please note**: Offline participants who haven’t made their estimations will not affect the final estimation, as their votes are not recorded in the game. 2. **Select next issue –** Admins can decide to skip the current issue for later estimation rounds without initiating the discussion phase. 3. **Remove issue from game –** Admins can remove the current issue from the game backlog. If it's the last issue to estimate, the game ends. When an issue is removed from the game backlog, it remains in the Jira backlog. The removed issue can be brought back to the game backlog by clicking *Add* issues. 4. **Timer –** Click the timer button to start the countdown. Admins can configure the timer through this dropdown. The options are:     - **Timer duration –** Choose between 10, 60, or 120 seconds. You can also set a custom time duration. This setting applies to both the autostart timer (if enabled) and the timer started manually by the admin.    - **Timer autostart –** Enable the *Start timer automatically* toggle to have the timer start automatically for each issue. 5. **Sound on/off –** When enabled, there will be sound notifications at the start and end of the timer. |

| 👥 **Estimators/Spectators** |
| --- |
| - Estimators are responsible for providing estimates for the current issue. - They choose a card that best matches their estimation of the issue, considering factors like deadline, difficulty, and complexity. - They play their cards face down, keeping their estimations private.   If you change your mind before revealing the cards, you can switch cards by clicking a different one or clicking the **Edit personal vote** button. |

The Voting phase concludes when all game participants have played their cards or in the following circumstances:

- The admin uses their **Reveal cards** privilege.
- The timer's countdown reaches its end.
- The participants haven't played their cards and have gone spectators.

In any of these scenarios, once the Voting phase ends, all played cards are revealed to all game participants and spectators. Additionally, certain phase statistics are presented, and the round transitions to the Discussion phase.

---

### **Discussion phase**

#### Purpose

The Discussion Phase is the final stage of the round, focusing on reaching a consensus regarding the estimation for the current issue through team collaboration.

#### Progression

In this phase, all played cards are unveiled to every participant. Estimations are visually represented in cards, facilitating easy sharing and discussion.

| 👤 **Game Admin** |
| --- |
| In this phase, estimations by participants are organized based on the game's deck type and serve as active controls for the game admin. Clicking on an estimation card triggers the *Issues already estimated as* section, where you can see the issues that have been estimated with the same number: image-20240728-192509.png Admins are provided with a group of additional controls. These controls allow the game admin to commit the following actions: image-20240728-192232.png  1. **Save & next –** Enter and save the final estimation value during the discussion phase—the key action in the game. All participants need to agree on the estimation value for the current issue. Once an estimation value is entered and this button is clicked, it becomes a parameter for that issue and moves the game to the next round if there are more issues in the backlog. If an estimation value is saved for the last unestimated issue, the game ends.   **Keep in mind that you need to match your deck type with a storage field.** To accurately save an estimation, understanding the data type is crucial for proper storage within the designated Jira issue field. Ensure that the export field in your game's configuration matches the data type of the deck you intend to use. If there's a mismatch between the deck type and the export field's data type, be sure to configure a suitable deck mapping.   1. **Save –** This option saves the current issue’s estimation but doesn’t proceed to the next issue. 2. **Replay –**  Admins can restart the Voting phase of the current round, discarding all participants' estimations for that round. 3. **Edit personal vote –** Click the button to edit your personal vote. 4. **Cards –** The cards with the estimation number of each estimator are displayed here. The users can click on their card to edit their personal vote. 5. **Select next issue/Remove issue from game –** These buttons function similarly to how they did during the Voting phase. |

| 👥 **Estimators/Spectators** |
| --- |
| - Participants engage in discussions under the guidance of the scrum master to arrive at a mutual consensus regarding the estimation for the current round's issue. |

Once a consensus is reached, the game administrator submits the estimation value, and the game advances to the next round or concludes.

---

### **End of the game**

A Planning Poker game ends when:

1. No rounds remain, and all issues are estimated.
2. The game admin uses the **Finish Game** privilege. When used, no further changes to the game will be possible without restoring it. All unfinished stories will remain in estimation backlog.

Upon the game's conclusion, a notification informs players. Finished games can be reopened if needed by opening the session and clicking **Restart game** from the three-dot icon.

![Screenshot 2024-07-28 at 22.36.58.png](/cms_trial/assets/63f1fe8d-5a24-4839-9ce7-72d369dc9705.png)

When the game is finished, you can export it to CSV format with summarised estimation data through the dashboard.

![image-20240728-193951.png](/cms_trial/assets/551c0817-1b7c-4b52-8543-eedcb8c360b4.png)

## Next steps

[**Game controls (Cloud)**](/cms_trial/space/PP/492110077/Game+controls+(Cloud)/)