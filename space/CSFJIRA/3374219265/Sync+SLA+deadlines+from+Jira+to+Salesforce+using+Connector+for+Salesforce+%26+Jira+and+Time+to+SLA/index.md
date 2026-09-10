# Sync SLA deadlines from Jira to Salesforce using Connector for Salesforce & Jira and Time to SLA

## Overview

When support teams use Salesforce and engineering teams use Jira, critical deadlines can easily get lost. This guide walks you through setting up a seamless integration between Salesforce and Jira using the Connector for Salesforce & Jira app, combined with Time to SLA, to ensure both teams always know exactly the SLA deadlines, regardless of which tool they're working in.

![SLA deadlines examples](/cms_trial/assets/a45cf9db-4343-4b2e-b067-3f64bde1fa2c.png)

## Benefits

- Unified SLA visibility: Both teams see critical deadlines in their own tools without switching platforms.
- Automated data synchronization: Cases and work items sync automatically; no manual copy-pasting.
- Instant escalations: Jira work items are created directly from Salesforce, with context and priority already in place.
- Consistent priority mapping: Priority levels mean the same thing across both platforms.

## Video guide

Video script

When support and engineering work in different tools, it's easy for deadlines to fall through the cracks. In this video, we'll fix that using Connector for Salesforce and Jira to integrate the two platforms, along with Time to SLA Cloud, so your support and engineering teams always know exactly how much time is left before a deadline, whichever tool they're working in.

At the end, when a support agent creates a Case in Salesforce and escalates it to engineering, a Jira work item is created, and an SLA timer starts. Finally, the deadline appears in the Salesforce Case without anyone having to copy and paste anything.

Before you start, you need to have already set up the Connector for Salesforce and Jira and have installed Time to SLA on the same Jira instance.

First, you need to create two date fields in Jira. These are the fields that Time to SLA will populate with SLA deadlines.

Click Settings, go to Work items, click Fields, and click Create new field.

For the field type, select Date Time Picker.

Name the first field: SLA Target Date - First Response. Click Create, and add the field to your screens. Select the Default JSM work item Screens.

Now create another Date Time Picker field. Name this one: SLA Target Date - Resolution and add it also to your screens.

If you open a Jira work item now and scroll down to **More fields**, you can already see both fields listed; you can pin them. They're empty for now. Time to SLA will fill them in once you configure it.

Next, before creating any SLAs, go to Salesforce and create matching custom fields there.

Go to Setup, open Object Manager, find Case, and select Fields and Relationships. Click New.

Select **Date Time** fielddata type.

For the first field, set the label to: SLA First Response Deadline. The field name will auto-fill. Go through the next screens and click **Save and New**.

Create the second **Date Time** field labeled SLA Resolution Deadline. Then Save.

Finally, go to Lightning Record Pages, open the Case Record Page, and drag both new fields into the page area. Put them right next to the Priority field so they're easy to spot. Save the layout.

These fields will stay empty until the Connector pushes data into them from Jira.

Now we can switch to Jira to configure Time to SLA.

First, you need a working calendar.

In Jira, go to Apps, Time to SLA, Calendars, and click Add new Calendar. Set your time zone and working days (for example, Monday to Friday), working hours (8 to 4), and add your public holidays. Save it.

You can now create the first SLA. Go to  SLA’s, then create an SLA. Name it: Time to First Response.

Next, add the first goal. Set the name to P1 – Critical, select the calendar you just created, set the duration to 1 hour, and scope it to work items with priority set to highest.

Add a second goal for P2 – High: 4 hours, where priority equals High. And a third: with Medium and Low priority for 8 hours.

Click Next to SLA Conditions. Set Start to Issue is Created, End when the Assignee makes a public comment, and Pause when the status is Waiting for Customer.

This is the key step. Scroll to SLA Custom Field, tick Update date field in issue, and from the dropdown select SLA Target Date – First Response, the custom field you’ve created in Jira earlier. Click Save.

Now create the second SLA: Time to Resolution. Goals are 4 hours for Critical, 24 hours for High, 72 hours for everything else. Start on Created, end when the resolution is set, and pause on Waiting for Customer. Link SLA Custom Field to SLA Target Date – Resolution. Click Save.

Now you can configure the Connector. Go to Apps, Connector for Salesforce, and click Bindings. Find your binding that connects your Jira space to your Salesforce platform and click Mapping.

Click Add Entity Mapping. For the Jira work item Type, select Bug. And for the Salesforce Object, select Case. Add it.

This lets you create Jira work items directly from Salesforce and keep the values in sync.

Click Mappings on the Case to Bug row to define field sync.

Map bidirectionally to ensure the fields can be updated on both platforms.

- Summary to Subject.
- Description to Description.
- Priority to Priority.

Other fields need to sync only from Jira to Salesforce so that Salesforce cannot accidentally overwrite them.

- Status to Status
- SLA Target Date to Resolution to SLA Resolution Deadline.
- SLA Target Date to First Response to SLA First Response Deadline.

Click Configure on the Priority field to set value mappings. Map Highest to Critical, High to High, Medium to Medium, and Low to Low.

Now let's see the apps in action.

Create a new Case in Salesforce.

Subject: Critical Bug in Login Flow. Priority: Critical. Description: User cannot log in after password reset. Save it.

Back on the Case record, use the Jira Issue panel to create a Jira work item. Select your mapped Jira space, and select Jira work item type Bug, and click Create.

Switch to Jira. The work item is already there. Summary and description came through. Priority is showing as Highest, which is correct for our Critical mapping. And over in the Time to SLA panel, both SLA timers are running. Showing minutes remaining to first response and resolution.

Under your pinned Fields — SLA Target Date – First Response and SLA Target Date – Resolution both now show a timestamp.

Push the update to Salesforce. And there we go — SLA Resolution Deadline and SLA First Response Deadline values are populated in the Case record. The support agent can see when engineering needs to have this resolved, without opening Jira.

This setup works best as a one-to-one association: one Salesforce Case syncing with one Jira work item. If you link a second Jira work item to the same Case and sync it, the field values will overwrite each other.

If you need to associate multiple Jira work items with a single Case, don't sync them. Instead, use the Jira Issue panel in Salesforce to view those additional work items. You can still see their details and SLA timers there, without any risk of data being overwritten.

To recap, the Connector for Salesforce and Jira synchronizes fields, including priority and SLA dates, so both teams can work in their respective tools while sharing a single source of truth.

---

## Before you start

Make sure you have:

- Installed Connector for Salesforce and Jira and configured to connect your Salesforce org and Jira instance.
- Installed Time to SLA Cloud on your Jira instance.
- Administrative access to both Salesforce and Jira.

---

## Steps

### 1. Create custom fields in Jira

You need to create the custom fields in Jira to display the SLA deadline information generated by Time to SLA.

1. In Jira, go to **Settings** > **Work items** > **Fields**.
2. Click **Create new field**.
3. Select **Date Time Picker** as the field type.
4. Create two fields:

   - SLA Target Date - First Response
   - SLA Target Date - Resolution
5. Click **Create**.
6. Add the fields to your work items screens.

   ![Custom SLA fields in Jira](/cms_trial/assets/617bfac1-73a8-4879-a06e-23199472c40e.png)

   Open any Jira work item and scroll down to *More fields*. You should see both SLA fields listed. You can pin them for easy access. They'll remain empty until Time to SLA populates them.

---

### 2. Create matching custom fields in Salesforce

Salesforce needs corresponding fields to receive the SLA deadline data from Jira.

#### 2.1. Add custom fields

1. In Salesforce, go to **Setup**.
2. Open **Object Manager** and search for **Case**.
3. Click **Case** and select **Fields and Relationships**.
4. Click **New**.
5. Select **Date Time** as the field data type.
6. Set the label to SLA First Response Deadline.
7. Click through the remaining screens and click **Save and New**.
8. Create a second Date Time field: SLA Resolution Deadline.
9. Click **Save**.

#### 2.2. Add fields to the case record page

1. Go to **Lightning Record Pages**.
2. Open **Case Record Page**.
3. Drag both new fields into the page area.
4. Position them next to the **Priority** field for easy visibility.
5. **Save** the layout.

   ![Custom SLA fields in Salesforce](/cms_trial/assets/214d4456-780c-4221-b159-39ccaaaf6688.png)

   These fields will populate automatically once the Connector pushes data from Jira.

---

### 3. Configure Time to SLA in Jira

#### 3.1. Create a working calendar

Time to SLA needs a calendar to track business hours and holidays.

1. In Jira, go to **Apps** > **Time to SLA** > **Calendars**.
2. Click **Add new Calendar**.
3. Configure:

   - **Time zone**: select your organization's time zone.
   - **Working days**: for example, Monday to Friday.
   - **Working hours**: for example, 8 AM to 4 PM.
   - **Public holidays**: add your organization's holidays.
4. Click **Save**.

#### 3.2. Create the first response SLA

1. Go to *SLAs.*
2. Click **Create SLA**.
3. Name it: **Time to First Response**.
4. Add the following goals:

| Name | Duration | Scope |
| --- | --- | --- |
| P1 - Critical | 1 hour | Priority = Highest |
| P2 - High | 4 hours | Priority = High |
| P3 - Medium/Low | 8 hours | Priority = Medium or Low |

1. Click **Next**.
2. Configure*SLA Conditions*:

   - **Start Condition**: `Issue is Created`
   - **End Condition**:`Public comment by a user in field Assignee`
   - **Pause Condition**: `Status is equal to Waiting for customer`
3. Scroll to **SLA Custom Field**:

   - Check the **Update date field in the issue**.
   - From the dropdown, select **SLA Target Date - First Response**.
4. Click **Save**.

   ![SLA Time to first response](/cms_trial/assets/6f3f1e5e-31ca-45a8-801b-9cb481dfc9f7.png)

#### 3.3. Create the resolution SLA

1. Click **Create SLA** again.
2. Name it: **Time to Resolution**.
3. Add the goals:

| Name | Duration | Scope |
| --- | --- | --- |
| P1 - Critical | 4 hours | Priority = Highest |
| P2 - High | 24 hours | Priority = High |
| P3 - Medium/Low | 72 hours | Priority = Medium or Low |

1. Click **Next**.
2. Configure*SLA Conditions*:

   - **Condition**: `Issue is Created`
   - **End Condition**: `Resolution is set`
   - **Pause Condition**: `Status is equal to Waiting for customer`
3. Scroll to **SLA Custom Field**:

   1. Check the **Update date field in the issue**.
   2. From the dropdown, select **SLA Target Date - Resolution**.
4. Click **Save**.

   ![SLA Time to Resolution](/cms_trial/assets/4d27bf32-c3bf-4c6e-98e4-ec12aa99b1bb.png)

---

### 4. Configure mapping in Connector for Salesforce and Jira

#### 4.1. Create the entity mapping

1. Go to **Apps** > **Connector for Salesforce and Jira**.
2. Click **Bindings**.
3. Find the binding that connects your Jira space to your Salesforce platform.
4. Click **Mapping**.
5. Click **Add Entity Mapping**.
6. Select:

   - **Jira work item type:** Bug
   - **Salesforce Object:** Case
7. Click **Add**.

   ![Bug to Case mapping](/cms_trial/assets/a321d571-8d2e-40f5-8a5a-0aefc822ed4d.png)

   This mapping lets you create Jira work items directly from Salesforce cases and keep data in sync.

#### 4.2. Configure field mappings

1. Click **Mappings** on the case to Bug row.
2. Set up bidirectional mappings for shared fields:

   - Summary ↔ Subject (bidirectional)
   - Description ↔ Description (bidirectional)
   - Priority ↔ Priority (bidirectional)
3. Set up unidirectional mappings (Jira to Salesforce only) for SLA fields:

   - Status → Status
   - SLA Target Date - Resolution → SLA Resolution Deadline
   - SLA Target Date - First Response → SLA First Response Deadline

     ![Field mappings](/cms_trial/assets/2ea46bf1-d98b-422f-9506-fa82c31d3a0f.png)

#### 4.3. Map priority values

1. Click **Configure** on the Priority field.
2. Set up value mappings:

   - Jira Highest → Salesforce Critical
   - Jira High → Salesforce High
   - Jira Medium → Salesforce Medium
   - Jira Low → Salesforce Low
3. Click **Save**.

   ![Value mappings](/cms_trial/assets/3916cc6a-cc52-4998-8b8a-007cb290434a.png)

---

## Test the integration

### Create a test case in Salesforce

1. In Salesforce, create a new case:

   - **Subject:** Critical Bug in Login Flow
   - **Priority:** Critical
   - **Description:** User cannot log in after password reset
2. **Save** the case.

### Create a Jira work item from the case

1. On the case record, locate the Jira Issue panel.
2. Click **Create new Jira issue**.
3. Select your mapped Jira space.
4. Select **Bug** as the work item type.
5. Click **Create**.

The work item appears with the correct summary and description:

- Priority shows as *Highest* (correctly mapped from *Critical*).
- The **Time to SLA panel** shows both SLA timers running with minutes remaining.
- The pinned **SLA Target Date** fields display timestamps.

![Jira bug with SLA timers](/cms_trial/assets/e800075b-6097-4e76-9149-e7f81e73828b.png)

**In Salesforce:**

- Return to the case record.
- Both **SLA First Response Deadline** and **SLA Resolution Deadline** fields are now populated.
- These values came automatically from Jira without any manual action.

  ![Salesforce custom fields with values filled](/cms_trial/assets/2d6ba6cd-1af1-4124-940b-b2516a821404.png)

---

This integration works best with a **one-to-one association**: one Salesforce case syncing with one Jira work item. This prevents data conflicts and ensures clean synchronization.

### Handling multiple work items

If you need to associate multiple Jira work items with a single Salesforce case, use the Jira Issue panel in Salesforce to view and link additional work items. You can still see their details and SLA timers in the panel without risking data overwrites.

---

## Troubleshooting

### Fields not syncing

- Verify the Connector binding is active and configured correctly.
- Check that field mappings are properly defined in the Binding's Mapping section.
- Review Connector logs for any sync errors.

### SLA timers not appearing

- Verify that you've created the SLA Target Date fields in Jira.
- Confirm that SLA Custom Field is configured to update the date fields.

### Values not mapping correctly

- Double-check priority value mappings in the Connector configuration.
- Ensure priority values exist in both systems before mapping.
- Verify that work items have a priority set before syncing.

---

## Related resources

- [Configure mappings with Connector for Salesforce and Jira Documentation](/cms_trial/space/CSFJIRA/1854180614/Configure+entity%2C+field+and+value+mappings/)
- [Time to SLA Cloud user guide](https://appfire.atlassian.net/wiki/spaces/TTSC/pages/1678575285)