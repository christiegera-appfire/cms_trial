# Teams based on Jira teams

## Initial setup

Setup must be done by a **Jira admin**.

Configuration is done once for the entire instance.

In the Teams module:

1. Go to **App Configuration** > **Integrations**
2. Navigate to the **Jira Teams** tab

   ![The app configuration page.](/cms_trial/assets/595bf3aa-0b47-458c-be19-3d37cd5af174.png)
3. Generate an API token and add it to the app:

   1. Log in to [Atlassian account](https://id.atlassian.com/manage-profile/security/api-tokens).
   2. Click **Create API token.**
   3. In the dialog that appears, enter a memorable **Label** for your token and click **Create.**
   4. Click **Copy** to clipboard.
   5. Add it to the app.
4. Enter the Organization ID

   1. Open URL [https://admin.atlassian.com](https://nostromo11.atlassian.net/admin/users)
   2. If you have access to more than one Organization, select the one associated with your BigPicture instance

      ![Jira settings page.](/cms_trial/assets/2ff442ed-7621-4564-b676-30633ba3e8e9.png)
   3. The ID can be found in the URL  
      <https://admin.atlassian.com/o/>**my-organization-id-xxxxx-xxxxxxx-xxxxxx**/overview

      ![image-20250127-121738.png](/cms_trial/assets/d4866451-e6a6-433e-b179-a76c1890dd05.png)
   4. Copy the ID from the URL and paste it into the required field

      ![fields where you can enter organization's ID.](/cms_trial/assets/159f87b8-bc48-43d4-8e6d-ab52b8044abc.png)
5. Enter the email address
6. Click **Save**

You will see a confirmation message:

![Connection confirmation message.](/cms_trial/assets/9207d1c3-bda6-4e40-8b80-aca2f7742bf0.png)

Organization ID is listed on the page:

![successful sync confirmed on the app configuration page.](/cms_trial/assets/9c1a1112-fcac-4808-9caf-1f2932f18fca.png)

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

   ![Create new teams based on Jira team option in the app.](/cms_trial/assets/a52af3d9-b2b5-4f03-8413-970143b35b6d.png)
3. Select a Jira Cloud team and fill out the fields:

   1. **Jira cloud team** (required)
   2. **Team name** (required)
   3. **Team code and color** (required)
   4. Board (optional)
   5. **Start date of Team memberships** (required)

![Create new team based on Jira team screen.](/cms_trial/assets/83e96579-b894-459f-bdbf-b75a171c75a2.png)

1. Click **Create**.

**Result**: A new team appears on the list.

![New team based on Jira team listed in the Teams module.](/cms_trial/assets/4e30cc30-4a9d-453a-ac3e-ceaff8608e44.png)

### Memberships

- By default, the availability of team members is set to 100%.
- Memberships of team members and their availability can be modified as usual.
- When synchronization is triggered, based on a Jira team, new team members are added to the app:

  - the date of adding a person becomes the membership start date
  - availability is set to 100%
- When synchronization is triggered, based on a Jira team, team members are removed from BigPicture.

### Using the same Jira team in multiple boxes

You can’t create multiple box teams based on the same Jira team:

![Error message.](/cms_trial/assets/8942a07c-4b00-4da6-8816-9fa3fe775f12.png)

**You can assign the same app team to multiple boxes.**

![How to create team based on Jira in multiple boxes.](/cms_trial/assets/e55d8605-7965-4e1e-9369-05480e50c556.mp4)

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

![Synchronize with Jira Cloud Teams option.](/cms_trial/assets/f116cafb-5583-4984-977d-264d509421f3.png)

### Local synchronization (per team)

If a team has been edited in the app, for example, team members have been added or removed, the team will **NOT** be synchronized during global synchronization to prevent the loss of information.

A pencil icon appears to teams that are excluded from the global synchronization.

![Local sync of the teams based on Jira teams.](/cms_trial/assets/9926d397-dc25-420d-bf07-0423cfcc1f55.png)

**How to trigger a synchronization**

To synchronize such a team, click the **re-synchronize button**:

- synchronization applies only to one team
- changes made in the app are overwritten with Jira team information

![How to resynchronize teams.](/cms_trial/assets/dfe77d1f-25cf-486c-96af-dae8c1c4ac7a.mov)