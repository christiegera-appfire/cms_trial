# SLA goals

Each SLA has contracts regarding the agreed-upon aspects of the service to be provided. Each contract includes a set of goals to determine whether the SLA has been met or not. Each goal can be a specific timeframe (days, hours, minutes) or a fixed deadline, such as a due date or custom field in Jira work items. They are tracked according to your working hours.

You can add goals by using the **+ Add goal** button and arrange them by dragging and dropping as you please:

![Time to SLA SLA goals page with goal settings table](/cms_trial/assets/488c6772-8d6d-4f2d-86c8-8a809026cdac.png)

Each SLA goal must have all or specific goal work items, a goal calendar, and a goal target type. Here’s a breakdown of each section:

![Time to SLA SLA goals duration configuration dialog](/cms_trial/assets/bb0aff6e-d929-40fb-b7bd-50c0879a118c.png)

## Goal Name

Start by giving your SLA goal a meaningful name, for example, `Low priority work`.

## Goal Calendar

For the goal to be calculated according to your holidays and working hours, you need to pick a calendar for it. The default calendar is 7x24; however, you can select one of the calendars you've created from the Goal calendar list, or easily create a new one by clicking **+ Add New Calendar** on the list.

### **Select calendar via Jira issue**

The current Dynamic Calendar field has been replaced with a new Dynamic Calendar field created on Forge.

Because this field has a new field ID and now stores the calendar ID (instead of the calendar name), any automation rule, script, or integration that still references the old field ID or the old value format will stop working.

To learn how to fix this, read the related [documentation](/cms_trial/space/TTSC/2513797296/Changes+after+the+Forge+migration/).

Alternatively, you can select the **Select calendar via Jira Issue** option, enabling you to select your calendar dynamically. This empowers team members across different time zones to customize adjustments on a per-work-item basis, eliminating the need to generate multiple goals for various time zones.

To use this feature, you need to add the TTS - Dynamic Calendar field to your instance and make sure it’s available on all screens you need. To do that, follow these steps:

1. Open **Jira Settings** > **Work items**.
2. Click **Fields** in the side menu.
3. Search for `TTS - Dynamic Calendar`. When it appears, click the three-dot icon next to it to reveal the options.
4. Cick **Add field to screen**.

   ![Time to SLA SLA goals page with target duration options](/cms_trial/assets/d4493333-309b-4619-9e92-2eb033267bc9.png)
5. Select all the screens you want to see the field on.
6. Click **Update**. This will add the custom field to the screens you’ve selected.

## Goal Target Type

There are five goal target types you can choose from.

### Duration

Use this if the SLA has a fixed timeframe. Just type a duration (for example, `2d 5h`), which will be your SLA’s goal. Keep in mind that when the letter “d” is used in the duration, it is interpreted as a “calendar day,” which could be 8 hours, for example. The deadline is calculated as **Deadline Date** = **SLA Start Date + SLA Duration + Valid Paused Time (if any, before breach)**.

The SLA begins counting after the start date is met, and you’ll have exactly the amount of time you specify here, excluding any time the SLA is paused before a breach.

### Negotiation date

The Negotiation date goal type lets you use the value of a date or date-time field as the SLA deadline.

Unlike a [Duration goal](/cms_trial/space/TTSC/35390901/SLA+goals/), which defines how much SLA time is available, such as 8 working hours or 3 business days, a Negotiation date goal defines the exact date and time by which the SLA should be completed.

For example:

- **Duration goal:** Resolve the work item within 8 working hours.
- **Negotiation date goal:** Resolve the work item by August 18 at 17:00.

You might use a Negotiation date when:

- A customer provides a specific due date for a request.
- You have a contractual commitment with a fixed deadline.
- You need to assess or triage a work item before agreeing on a realistic resolution deadline.

#### How it works

When you select Negotiation date as the SLA goal type, you choose a date or date-time field to use as the deadline.

TTS compares the SLA's actual end date with the value in that field:

- If the SLA ends on or before the Negotiation date, the SLA is met.
- If the SLA ends after the Negotiation date, the SLA is breached.

For example, suppose:

- The SLA starts on Monday, August 17 at 09:00.
- The Negotiation date is Wednesday, August 19 at 17:00.
- The work item is resolved on Wednesday at 15:00 — the SLA is met.
- The work item is resolved on Wednesday at 18:00 — the SLA is breached.

#### Important considerations

- **Changes to the Negotiation date affect the SLA calculation**.   
  If you change the value in the selected field, TTS recalculates the SLA using the new deadline. Moving the date earlier or later can therefore change the SLA's remaining time and breach status.
- **A Negotiation date can already be in the past.**  
  If the selected date or time is earlier than the SLA start date, the SLA starts with a deadline that has already passed and is considered breached.
- **Pauses do not postpone the Negotiation date.**  
  The Negotiation date is a fixed deadline. If the SLA enters a paused state, the deadline does not move forward.  
  For example, if the Negotiation date is Friday at 17:00, pausing the SLA for several hours will not extend the deadline beyond Friday at 17:00.

#### Using a date picker field

If you select a date picker field instead of a date-time picker field, an additional offset setting appears. A date picker stores only a date and does not include a specific time. The offset lets you define the time that TTS should use when calculating the SLA deadline.

### Dynamic duration

Dynamic duration is a Jira custom field. When you enter a time string here, Time to SLA will set the SLA duration as the input entered in this field. This allows users to enter different SLA goals for each work item!

To set an SLA goal as a Dynamic duration, you need to create a custom field that will store the SLA duration **beforehand**. This custom field will appear only in the screens you select while creating the custom field, regardless of whether you designate the SLA goal as Dynamic duration or not.

First, you need to create the custom field. If you don’t know how, [refer to this page](https://appfire.atlassian.net/wiki/spaces/TTSC/pages/35881063). Then, you can set the SLA Goal as a dynamic duration.

### Next business day

`Next business day` refers to the next working day according to the company's regular business hours. For example, let’s say a company operates from Monday to Friday, from 8 AM to 6 PM. For an SLA that started counting at 9 AM, selecting this will give you time to work on the work item until 6 PM. You can pick as many business days as you'd like and not worry about break times, as the calculation will be done accordingly.

For example, if a customer creates a ticket outside of the company's working hours, such as at 8 PM on a Friday, the SLA will start counting from 9 AM on the following Monday and end at 6 PM on that same Monday. This is the standard practice for most companies when using this calculation.

If you select **Next business day** as the goal type, pausing the SLA **won’t postpone** the target date. Even if a pause condition is met, the deadline stays the same.

### No target

Use this option if you don’t have a target date. You can use this if you only want to see the elapsed duration in the SLA panel or see how long you worked on the work item. When you pick No target, the SLA panel will look like this:

![Time to SLA SLA goals compact target duration example](/cms_trial/assets/4570ef4c-fde0-45b9-a3a8-cb8c7db5d762.png)

## Goal Issues

Use this section to define the scope and conditions under which the SLA goal is applied. Initially, two options are available:

- **Remaining issues in selected projects –** This applies the SLA goal to all work items within the broader SLA context without any additional filtering.
- **Only specific issues in selected projects –** Lets you filter the work items the SLA goal will be applied to. Once selected, the **+ More** button will appear, allowing you to refine the goal’s scope further.

  ![Time to SLA SLA goals validation dialog for target duration](/cms_trial/assets/dbb6cf3d-bbd8-47ad-954e-b2b57cf1fb92.png)
  - **Issue Priority –** Categorizes SLA goals according to the priority level assigned to a work item.
  - **Issue Type –** Lists SLA goals according to the work item type assigned to a work item.
  - **Request Type –** Tailors the SLA goal based on the specific request type associated with a work item.
  - **Assignee –** Tailors the SLA goal based on the assignee of the work item.
  - **JQL –** Create queries to filter and retrieve specific sets of work items, allowing for precise control over which work items the SLA goals should apply to.
  - **Issue Filter –** You can create work item filters and then use them to filter the goal’s scope.