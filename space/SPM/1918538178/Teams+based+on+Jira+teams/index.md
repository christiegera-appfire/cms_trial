# Teams based on Jira teams

## Initial setup

Setup must be done by a **Jira admin**.

Configuration is done once for the entire instance.

In the Teams module:

1. Go to **App Configuration** > **Integrations**
2. Navigate to the **Jira Teams** tab

   Image — asset pipeline pending  
   The app configuration page.
3. Generate an API token and add it to the app:

   1. Log in to [Atlassian account](https://id.atlassian.com/manage-profile/security/api-tokens).
   2. Click **Create API token.**
   3. In the dialog that appears, enter a memorable **Label** for your token and click **Create.**
   4. Click **Copy** to clipboard.
   5. Add it to the app.
4. Enter the Organization ID

   1. Open URL [https://admin.atlassian.com](https://nostromo11.atlassian.net/admin/users)
   2. If you have access to more than one Organization, select the one associated with your BigPicture instance

      Image — asset pipeline pending  
      Jira settings page.
   3. The ID can be found in the URL  
      <https://admin.atlassian.com/o/>**my-organization-id-xxxxx-xxxxxxx-xxxxxx**/overview

      Image — asset pipeline pending  
      image-20250127-121738.png
   4. Copy the ID from the URL and paste it into the required field

      Image — asset pipeline pending  
      fields where you can enter organization's ID.
5. Enter the email address
6. Click **Save**

You will see a confirmation message:

Image — asset pipeline pending  
Connection confirmation message.

Organization ID is listed on the page:

Image — asset pipeline pending  
successful sync confirmed on the app configuration page.

## Expiration of tokens

Jira tokens are valid for a limited period of time. To ensure that synchronization can continue, the token must be replaced periodically.

### What happens if synchronization fails? (for example, if the token stops working)

- Changes made to Jira teams can no longer be transferred to the app.
- Teams that already exist in the app remain unchanged (in the state corresponding to the last successful synchronization).

### Will replacing the token with a new one trigger another synchronization?

- No. Currently, synchronization is always triggered manually. There is no auto-synchronization

---

## Create app teams based on Jira teams

In the Teams module:

1. Click the **+** button.
2. Select **Create new team based on Jira team**

   Image — asset pipeline pending  
   Create new teams based on Jira team option in the app.
3. Select a Jira Cloud team and fill out the fields:

   1. **Jira cloud team** (required)
   2. **Team name** (required)
   3. **Team code and color** (required)
   4. Board (optional)
   5. **Start date of Team memberships** (required)

Image — asset pipeline pending  
Create new team based on Jira team screen.

1. Click **Create**.

**Result**: A new team appears on the list.

Image — asset pipeline pending  
New team based on Jira team listed in the Teams module.

### Memberships

- By default, the availability of team members is set to 100%.
- Memberships of team members and their availability can be modified as usual.
- When synchronization is triggered, based on a Jira team, new team members are added to the app:

  - the date of adding a person becomes the membership start date
  - availability is set to 100%
- When synchronization is triggered, based on a Jira team, team members are removed from BigPicture.

### Using the same Jira team in multiple boxes

You can’t create multiple box teams based on the same Jira team:

Image — asset pipeline pending  
Error message.

**You can assign the same app team to multiple boxes.**

Image — asset pipeline pending  
How to create team based on Jira in multiple boxes.

### Can I synchronize an existing app team with a Jira team?

No. The old team needs to be removed, and a new team (based on a Jira team) needs to be created.

## Synchronization

Synchronization between the app teams and the Jira teams has to be **triggered** **manually**.

Synchronization is **uni-directional**. Information from Jira is pulled into BigPicture.

### Where can synchronization be triggered

Synchronization must be triggered in the primary box of a team.

You can’t trigger synchronization in boxes that have inherited the team.

### Global synchronization

All app teams in a box (based on Jira teams) get synchronized.

**Exception**: If a team has been edited in the app, for example, team members have been added or removed, the team will **NOT** be synchronized during global synchronization to prevent the loss of information.

A pencil icon appears to teams that are excluded from the global synchronization.

**How to trigger a synchronization**

In a Teams module of a box:

1. Click **Synchronize**
2. Select Synchronize with Jira Cloud Teams

Image — asset pipeline pending  
Synchronize with Jira Cloud Teams option.

### Local synchronization (per team)

If a team has been edited in the app, for example, team members have been added or removed, the team will **NOT** be synchronized during global synchronization to prevent the loss of information.

A pencil icon appears to teams that are excluded from the global synchronization.

Image — asset pipeline pending  
Local sync of the teams based on Jira teams.

**How to trigger a synchronization**

To synchronize such a team, click the **re-synchronize button**:

- synchronization applies only to one team
- changes made in the app are overwritten with Jira team information

Image — asset pipeline pending  
How to resynchronize teams.