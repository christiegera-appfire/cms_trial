# Game basics

This page applies to both **Planning Poker for Jira Cloud** and **Jira Data Center**.

### **What is a game?**

In Planning Poker for Jira, a “game” refers to a collaborative effort among a group of individuals to estimate the effort and complexity of tasks or backlog items within an Agile project. This is a technique commonly used in Agile methodologies like Scrum.

During a game, team members typically use a set of predefined estimation values (e.g., Fibonacci numbers or T-shirt sizes) to assign estimates to the tasks being discussed. These estimates help in determining the effort required for each item, allowing the team to plan their work effectively. Planning Poker streamlines this process by offering a collaborative platform within Jira.

A game can be created in only two steps:

**Step 1: Create the game**

![contentId-9568521](/cms_trial/assets/895c7a2a-356f-49d6-a8ee-23e7a3a972b1.png)

**Step 2: Select the issues**

![Screenshot 2024-11-05 at 21.58.46.png](/cms_trial/assets/b3fe89e2-f326-4818-a48a-5fc4492217ef.png)

**Step 3: Start the game!**

![image-20241105-190029.png](/cms_trial/assets/3a9586bd-f80a-46e5-aa67-2e581ca0876c.png)

---

### **What are the estimation values in the card deck?**

In the Agile methodology, estimation values are used by teams to assess the effort required to complete specific tasks or stories. The most common approach is to utilize story points, which represent the relative complexity or effort involved. These story points are typically assigned using a [Fibonacci-like number format](https://en.wikipedia.org/wiki/Fibonacci_number): 0, 0.5, 1, 2, 3, 5, 8, 13, 20, 40, and 100.

In Planning Poker for Jira, you have several options on your card deck, including:

1. **Standard Fibonacci** – follows the traditional Fibonacci sequence for story point estimation.
2. **T-Shirt Size** – uses sizes like XXS, XS, S, M, L, and XL, providing a high-level estimation scale.
3. **Labeled T-Shirt** – stands for Small, Medium, and Large, enabling quick and simplified relative estimation.
4. **Hours** – allows teams to estimate in terms of time, such as hours or days, offering a more concrete understanding of effort.
5. **Custom** – enables teams to define their own set of estimation values that align with their specific requirements. When you select an option and change the values, you automatically create a new Custom value.

---

### **What are the game types?**

Planning Poker games are not tied to specific Jira projects or boards; they are available to everyone within the entire instance. They can be either **Public** or **Private**. By default, each game is public, but you can toggle **Private game** to hide the game from the list.

![image-20240728-220126.png](/cms_trial/assets/468a4440-730f-4db8-b125-cf4fdf32cc81.png)

- **Public** – provides unrestricted game access. Every Jira Software user can access a public session and update its configuration and participants list, including the roles. However, Jira restrictions still apply, meaning that users without access to the specific project, board, or issue will not be able to see restricted data. Nonetheless, they can still join and modify a public estimation session in Planning Poker.
- **Private** – restricts session access. Private games can be seen and accessed only by invited Estimators and Spectators. They can join it via email invitation.

---

### **What are the user roles?**

Following Jira architecture and Scrum plot, Planning Poker divides users into different roles:

- **Administrator –** The user with all the rights of the player and the spectator roles, combined with vast privileges to control the game. The admin is responsible for configuring the game options and editing its backlog. The user who started the game becomes its administrator initially and is considered a participant in the game.   
  More admins can be added at any time during the game by clicking **Edit game** and adding the names of the administrators:

![image-20240728-220621.png](/cms_trial/assets/63944a4e-0932-4bb5-9471-e262f30135d6.png)

![Screenshot 2024-07-29 at 01.07.36.png](/cms_trial/assets/abcb8d88-b0d8-4332-96f2-8bd16a9d61b4.png)

The admin can become a spectator by clicking **Switch to spectator** anytime during the course of the round, and once the admin returns, regains all administrative rights. The admin can also change a player's role from spectator to estimator, and vice versa..

![Screenshot 2024-07-29 at 01.08.55.png](/cms_trial/assets/a8099c9c-c3c1-40bc-ad8e-44e9584417b0.png)

- **Player –** This participant actively engages in each round's phases, primarily by strategically playing cards during the Voting phase to assess various issues. The player can become a spectator by clicking **Become spectator** anytime during the course of the round.
- **Spectator –** A spectator is limited to watching the game unfold, with no active participation in the round phases. They cannot play cards to assess issues and are not counted as participants in the game. Users can start as spectators but switch to participants by clicking **Become estimator** at any time during the round.

Let’s build on this by exploring the key responsibilities of each user role:

| **Administrator** |
| --- |
| The Admin’s role is essential to guiding the estimation process. Here are your key responsibilities:   1. **Configuring the Session** 2. **Starting the Estimation Process:** Initiate the session by picking an issue to estimate and guide participants through the estimation. 3. **Guiding the Session:** Start and manage the voting process, submit the final votes, and save estimates. 4. **Final Estimation:** Guide the discussion toward a consensus and make the final selection. 5. **Finishing the Session:** Conclude the session when all issues have been estimated. |

| **Player** |
| --- |
| As a Player, your active involvement is crucial for achieving accurate estimations. Here are your rules:   1. **Joining the Session:** Actively participate in the estimation process at the designated time. 2. **Providing Estimation Values:** Submit your estimation values for the selected issues based on your expertise. 3. **Engaging in Discussions:** Share your insights and reasoning during the discussion phase. 4. **Revising Personal Estimates:** Consider the discussion and revise your estimate if necessary. 5. **Following the Admin’s Guidance:** Adhere to the instructions provided by the administrator throughout the session. |

| **Spectator** |
| --- |
| Spectators can only watch the game unfold. Here are some rules to keep in mind:   1. **Engaged Observation:** Attentively follow the discussions, estimations, and decision-making process of the team. Those new to the team or the estimation process can use the session as a learning opportunity. 2. **Note-taking:** Optionally take notes during the session to capture important points, key insights, or any notable aspects of the discussion for later review. |

---

### **How can I access a game?**

Planning Poker games are available to everyone within the entire instance. To access the games on Jira Cloud, simply click **Apps** and then select **Planning Poker**, or alternatively, go to your project's sidebar and click **Planning Poker**. On Jira Data Center, you can simply click **Planning Poker** on the Jira navigation bar.

**Data center**

![image-20240731-185348.png](/cms_trial/assets/b81fed2f-fa92-427d-9249-44ec671f50b3.png)

For Data Center, you can search for a specific game, create a new game, share a game with others by copying the game URL (desktop only), or filter them based on their status or the creator's identity. Let’s look at the components in more detail:

1. **New Game –** A button that allows you to start a new game.
2. **Finished game –** You can either display finished games or hide them from view.
3. **Search –** A text input that allows you to filter games by description, owner, or state. Just start typing your desired filter, and the list will be affected immediately.  
   **Game state** and **Creator** filters **–** dropdown lists that allow you to filter estimation games.
4. **Join –** The button that allows you to join a game as a participant.
5. **Configuration –** Allows you to edit a game’s configuration.
6. **Clone game –** A button that allows you to clone the game, creating a new one with exactly the same configuration and backlog content. Once clicked, a modal will appear, prompting for the name of a new game. The user, who cloned the game, becomes its prodigy's admin automatically.
7. **Copy game URL –** A button that allows you to share an invitation link to a game. Once clicked, the game's invitation link will be copied to your buffer.
8. **Export –** When a game is finished, you can export it to CSV format with summarized estimation data.
9. **Delete –** Click to delete the game.
10. **Mobile version –** A button that allows accessing Planning Poker games from a mobile view, providing estimates. The estimation from mobile is optimized for in-room estimation when a moderator shares their screen.

**Cloud**

![image-20240728-221803.png](/cms_trial/assets/d9b4b8e1-5856-4a04-851e-f266b709e010.png)

In Cloud, you can search for a specific game, create a new game, share a game with others by copying the game URL (desktop only), or filter them based on their status or the creator's identity. To join, simply click on the game’s title.

Let’s look at the components in more detail:

1. **Create game –** A button that allows you to start a new game.
2. **Search –** A text input that allows you to filter by name. Just start typing, and the list will be affected immediately.
3. **State** and **Creator** filters **–** Dropdown lists that allow you to filter estimation games.
4. **Delete game –** You can individually delete games or select multiple games and click this button to delete in bulk.
5. **Game settings –** Click to reveal the options:

   - **Clone game configuration –** A button that allows you to clone the game, creating a new one with exactly the same configuration and backlog content. Once clicked, a modal will appear, prompting for the name of a new game. The user, who cloned the game, becomes its prodigy's admin automatically.
   - **Copy game URL –** A button that allows you to share an invitation link to a game. Once clicked, the game's invitation link will be copied to your buffer.
   - **Export results (CSV) –** When a game is finished, you can export it to CSV format with summarized estimation data.
   - **Finish game –** Click to finish the game.
   - **Delete game –** Click to delete the game.

---

### **How does a Planning Poker game unfold?**

The Planning Poker game revolves around estimation rounds, each dedicated to a specific issue and comprising three phases: the **Backlog**, **Voting**, and **Discussion**. Here's a concise overview of how a Planning Poker game unfolds:

1. After configuring session settings, the administrator kicks off the game.
2. Participants join as either players or spectators through the Planning Poker dashboard. If it's a private game, they can only join via email.
3. The session displays a backlog view with issues to be estimated. The admin selects the issue to be estimated.
4. Players provide their individual estimates. The cards are played face-down.
5. The voting phase ends when all players have played their cards or the admin intervenes. The session enters the discussion phase.
6. The players discuss their estimates and reach a consensus. They can update their personal estimates if needed.
7. The admin approves the final estimation for the selected issue.
8. The process repeats for each issue in the backlog.
9. The game ends when there are no more rounds to play or the admin finishes it.

To learn more about game flow, refer to the related documentation ([Cloud](/cms_trial/space/PP/1149501468/Game+flow+(Cloud)/), [DC](/cms_trial/space/PP/9568315/Game+flow+(DC)/)).

## 🖇️ Related Articles

[**Further reading**](https://appfire.atlassian.net/wiki/spaces/PP/pages/463636664)