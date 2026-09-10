# Release notes July 2024

**Release date**: July 27, 2024

Our team is thrilled to announce the latest release of [Planning Poker](https://marketplace.atlassian.com/apps/1212495/planning-poker?hosting=cloud&tab=overview) for Jira Cloud.

---

## New Planning Poker version 2.0

Appfire is thrilled to announce the release of the completely refactored version of the beloved Planning Poker for Jira Cloud!

## Video overview

Watch this [three-minute video](https://www.loom.com/share/8092f574596645a19fc57f2c92de8635?sid=708e6cf8-7dbc-44b7-a3b6-6f3103df6af1) instead of reading.

## Enhancements

This new version boasts significant performance and security enhancements to follow the highest Appfire standards, along with a fresh, intuitive interface.

## Dark theme

Planning Poker now fully supports Jira's dark mode theme for improved visual comfort and user preference alignment.

![image-20240729-093327.png](/cms_trial/assets/4df4c886-13df-4513-99d9-666d9c5d721f.png)

![image-20240729-093519.png](/cms_trial/assets/98aeea14-79ec-4851-9d10-099bc092b63d.png)

## New Planning Poker game

![Screenshot 2024-07-16 at 10.34.07.png](/cms_trial/assets/1761ccad-9cf4-4eef-8380-905c6172648a.png)

### Issue details

The Planning Poker game now has a much sleek interface. The default issue details are:

- **Descriptions**
- **Details**
- **Attachments**
- **Comments –** You can easily view the latest comments and add new ones.

  ![2024-07-29_12-45-22 (1)-20240729-094630.gif](/cms_trial/assets/34b1eaaa-bc8e-475b-a559-d9fc9dd113d6.gif)

All issue details can be easily collapsed or expanded. Their states will be remembered per user.

In addition, game admins can add large text fields (Custom fields of Paragraph type) below the description field. They can also add short custom fields (like numeric values, short text fields, single select fields, etc.) on the right side of the issue details.

### Voting panel and reference issues

The voting area has received a complete UI update while retaining the familiar and beloved user experience.

- The **Timer** feature has been completely reworked. It is now possible to configure it on-the-go, located to the right of the voting panel.

  ![Screenshot 2024-07-29 at 12.54.57.png](/cms_trial/assets/4403c9de-5f40-4d74-b002-db5185a7a997.png)
- The **Reference issues panel** is now cached, so it loads faster for repeated issues. It can now be collapsed (personal setting) or disabled (game configuration).

  ![Screenshot 2024-07-29 at 12.59.20.png](/cms_trial/assets/616253e5-ac20-453a-aa40-e2c2d797d7c9.png)

### Participants and Moderators

The Participants panel is collapsed by default, but users can expand it to access more features. The admin can switch participants from spectator to estimator, and vice versa, or remove them from the game. Offline participants and their votes will be shown after they disconnect.

![image-20240729-100520.png](/cms_trial/assets/74e5c684-8730-448f-83da-d8cc45711e27.png)

Multiple game admins can now be specified during the game creation or configuration.

### Game backlog

The game backlog now features a single issue list with estimated issues now pushed to the "Estimated" backlog.

![image-20240729-101712.png](/cms_trial/assets/fbf76fdb-5474-4f6b-ab05-ee2a735f650f.png)

- The column with the custom field that is being estimated is located on the left and is highlighted whenever the value has been saved during the game.
- There is new UI for custom fields.
- There is a new quick-add option called **+ Add issues**.

### Game navigation

The new navigation is there to make any transitions quick and easy.

## Updated game creation and configuration

### Edit game

![image-20240729-104354.png](/cms_trial/assets/1b101cc2-8b09-4a50-a454-ec7e389f6fb2.png)

![image-20240729-104539.png](/cms_trial/assets/50419c8b-aa1c-4fc0-836a-6e985022c1a0.png)

- New **Advanced configurations** tab
- New **Private game** settings have been introduced – now, only the invited participants can see the private game on their Dashboard and join it.
- Ability to specify Spectators and Estimations before the game
- New Issue details customization experience
- Ability to disable **Reference issues** panel

### Edit backlog

- New filtering experience

  ![bc536f69-4c4b-45fb-baa3-097a9a7985c4.png](/cms_trial/assets/93a4856e-ac16-4764-abd7-ae374f285af8.png)
- Use multiple consecutive searches to add issues to the backlog
- Easy backlog column customization
- New backlog experience during the game creation:

  - Remembered JQL/filter choice
  - Remembered JQL/filter from the previous game creation   
    or
  - Pre-set **Project** and **Status** filters for first-time creators

## Improved Game dashboard

![305d33b6-3b37-4fcf-9c5c-7b24d2720690.png](/cms_trial/assets/b83814b4-0027-4eca-8a65-40c6973146a9.png)

The game dashboard received new experience and features:

- Click the session name to join the game.
- Easily copy the game URL using the button next to the game name.

  ![image-20240729-105128.png](/cms_trial/assets/c09c3b7d-7901-49f6-a6ba-c906877dd28d.png)
- You can now delete multiple games at once using the **Delete game** button.
- **Export** game feature works for active games, not only for finished ones.

## Estimation from Issue details

Planning Poker in issue details has been moved to the Issue context view (panel on the right). It received real-time updates and a new UI:

![Screenshot 2024-07-16 at 10.39.02.png](/cms_trial/assets/783335eb-5b09-46e4-9888-21d157a20f66.png)

![Screenshot 2024-07-16 at 10.39.38.png](/cms_trial/assets/412b4910-c674-4ba6-91bd-aab3482ef0ff.png)

## Project level configuration

From now on, Project admins can configure values for Planning Poker in *Issue details* without the need for Global Admin permissions. Different projects now can have different settings.

![image-20240726-135558.png](/cms_trial/assets/58677e35-7243-484a-a5e0-8d3849a55750.png)

## Unsupported features

The latest version doesn’t support the legacy ***Mobile view*** feature. [Kindly inform us](https://appf.re/support) if this poses any inconvenience for you.

---

**Questions and feedback**

- Explore exciting features, pricing updates, reviews, and more on the [Marketplace](https://marketplace.atlassian.com/apps/1212495/planning-poker?hosting=cloud&tab=overview).
- Stuck with something? Raise a ticket with our [support team](https://appf.re/support).
- Do you love using our app? Let us know what you think [here](https://marketplace.atlassian.com/apps/1212495/planning-poker?hosting=cloud&tab=reviews).

**Credits**

A heartfelt thank you to our valued customers! Your incredible support and feedback inspire us to improve our apps and products continually. You are the driving force behind why we create software. We appreciate your trust in [Planning Poker](https://marketplace.atlassian.com/apps/1212495/planning-poker?hosting=cloud&tab=overview)!