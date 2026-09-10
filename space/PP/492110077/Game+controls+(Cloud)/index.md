# Game controls (Cloud)

This page is about **Planning Poker for Jira Cloud**. Using **DC**? [**Click here**](/cms_trial/space/PP/1144061984/Planning+Poker+for+Jira+Data+Center/).

In Planning Poker for Jira Cloud, understanding game controls is crucial for facilitating smooth gameplay and effective project estimation. This guide outlines the game controls available to both the game administrator (scrum master) and participants.

## Admin controls

![image-20241105-194152.png](/cms_trial/assets/4a70c028-f8b0-4e60-98f8-8ee0242f82c7.png)

1. **Issue information –** All the information about the issue chosen for estimation is displayed in this section. You can view the issue’s description, details, attachments, and comments.

You can expand the image attachments within the description field and comments to full-screen size by clicking on them.

![contentId-492110077](/cms_trial/assets/c5d61b5b-d354-4a36-a4d3-4676f5fea564.gif)

You can also easily send comments to the issue.

![2024-07-28_23-29-25 (1)-20240728-202951.gif](/cms_trial/assets/d6eb86e7-beb4-4156-8800-2cc38239fcbf.gif)

1. **Edit backlog/game –** Use these buttons to edit your game configuration during the session.
2. **Settings –** The admin can use this menu to perform the following actions:

   ![Screenshot 2024-07-28 at 23.33.03.png](/cms_trial/assets/4a28b981-4485-4a4b-9a11-adc754cc9b89.png)
   - **Restart game –**  Click this to replay the game from scratch.
   - **Finish game –** To conclude the game, select this option. This action will end the game, regardless of whether all the issues have been estimated and all rounds have been played. Once the game is finished, both the estimated and non-estimated issues will stay in the backlog list, and the estimated issues will be archived exactly as they were when the game was concluded.

     - Once the game is finished, the *Finish game* button will transform into the **Restart game** button. Feel free to reopen the game whenever you like by clicking this button. Reopening a game won't remove any previously saved estimations from the backlog. To re-estimate issues in a reopened game, the game's administrator will need to manually replay rounds and re-enter estimations for each issue.
   - **Delete game –** This will permanently delete the game, its progress, and all of its data.
   - **Contact us –** If you encounter problems, please use this option to reach out to our support team.
3. **Participants list –** Click the arrow to reveal the list of participants. Here you can view all the estimators and the spectators. The admins have the ADMIN tag next to their names.

   ![image-20240728-204708.png](/cms_trial/assets/47e1893b-b07a-446d-88eb-ac6a1c922c72.png)

   When the admin clicks next to the three-dot icon next to a participant’s name, two options are revealed:

   - **Switch to spectator –** The admin can make a participant a spectator or a spectator estimator.
   - **Remove from game –** Admins can kick estimators and spectators during the backlog, voting, or discussion phases with this feature. Removal is reversible, so players can reconnect via the Planning Poker dashboard or an invitation link. Admins can also remove themselves. If each player who hasn't played their card is removed, the voting phase would be over and the round would go to its discussion phase.
4. **Admin controls –** Here, the estimators only see the chosen card deck. Meanwhile, the admins can commit the following actions**:**

   - **Reveal cards –** Instantly reveal played cards, concluding the voting phase and initiating the discussion phase. Estimations from participants who haven't played their cards won't be considered during the discussion.
   - **Select next issue –** Admins can decide to skip the current issue for later estimation rounds without initiating the discussion phase.
   - **Remove issue from game –** Admins can remove the current issue from the game backlog. If it's the last issue to estimate, the game ends. When an issue is removed from the game backlog, it remains in the Jira backlog. The removed issue can be brought back to the game backlog by clicking *Add* issues.
   - **Timer –** In case the voting phase lasts too long or game participants have to be hurried up in order to make their decisions faster, the admin can start the countdown. Once the countdown timer runs to its end, all cards are opened and the round goes to the discussion phase. Click the timer button to start the countdown. Admins can configure the timer through this dropdown. The options are:

     - **Timer duration –** Choose between 10, 60, or 120 seconds. You can also set a custom time duration. This setting applies to both the autostart timer (if enabled) and the timer started manually by the admin.
     - **Timer autostart –** Enable the *Start timer automatically* toggle to have the timer start automatically for each issue.
   - **Sound on/off –** When enabled, there will be sound notifications at the start and end of the timer.
5. **Estimated issues/Story points estimated –** When an estimated value is saved at the end of a discussion phase, it is added to the sum of estimated points counter. This allows a scrum master to consider how many story points have been already generated by the issues estimated during the game, to compare the sum of estimated points with the team's velocity, and to consider a sprint to come.

   ![Screenshot 2024-07-28 at 23.38.36.png](/cms_trial/assets/28764dec-8535-4a08-9238-2315e7962008.png)
6. **Hide issues estimated during this game –** As the users estimate during the game, the estimated issues will be hidden in the backlog.
7. **Add issue to backlog –** You can quickly add individual issues to the game backlog using this option. Simply search for the issue key, and click the **Add issue to backlog** button.
8. **Add issues –** The backlog list is accessible to the game admin throughout all phases. The admin can quickly add an issue to the game backlog by using this button. The added issue is placed at the bottom of the backlog list.

## Player controls

![image-20240728-212554.png](/cms_trial/assets/6111b36b-f66c-4618-8711-c86a1fd2090a.png)

1. **Issue summary –** This is where you'll find information about the issue being estimated. If the issue summary is taking up too much space, you can click the modals to collapse them. Here is what you can do:

   - **View issue –** You can open the issue in a new window and reload it to view the most current information. Works for administrators, players, and spectators with the right access to a Jira project.
   - **Description/Attachments/Details –** All the available information about the issue are displayed here.
   - **Comments** – Displays the comments on the issue. Click the model to reveal the comments, and use the **+ New comment** button to add new comments.
2. **Card deck –** Each player (except spectators) receives a number of cards, depending on the card deck type selected during the game configuration. The timer's duration is also displayed. Use the sound toggle to turn on/off the sound of the estimation timer.

1. **Game backlog –** This section allows you to keep track of the issues being estimated, the number of estimated issues, and the story points estimated.
2. **Participants list –** Click the arrow to reveal the list of participants. Here you can view all the estimators and the spectators. The number of online participants is displayed, and the offline players are greyed out.

   ![Screenshot 2024-07-29 at 00.43.11.png](/cms_trial/assets/e60c621c-b0be-483e-9431-c0d26d81484d.png)
   - You can use the icon shown with the arrow above or the **Become spectator/estimator** button to switch between being a spectator and an estimator. If you're the last participant to play your card and switch to spectator, the voting phase ends.

## Related articles

To learn more about your responsibilities during the game flow, check out the documentation below:

[**Game flow (Cloud)**](/cms_trial/space/PP/1149501468/Game+flow+(Cloud)/)