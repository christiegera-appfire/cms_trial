# FAQ: Calendars

Below are some answers to questions we're commonly asked about creating calendars. If you need help with something we haven't addressed, [please contact us](https://appfire.atlassian.net/servicedesk/customer/portals).

#### ***How can I use the Custom Duration function?***

Answer:

Custom Duration is used to format SLA durations such as remaining time and overdue. You can use it if you want the time you dedicate to a task to differ from your actual working hours. When TTS calculates how much time you spend on work items, it will consider the new duration as 1 day. Check out the example below:

**Example:**

Let's imagine you are assigned 3 tasks. Each will take you 3 hours, and you work 9 hours a day. You have 1 working day to complete everything.

If you pick **Calculate from calendar** and you finish all 3 tasks in 1 working day, the result will be as if you spent 9 hours on each activity, which equates to 27 hours for 3 tasks. That wouldn’t make any sense.

To fix this, you can enter 3h for **Custom Duration** and show that you've worked for 9 hours in total. This would provide a more logical result in showing how much time was spent on a task, especially when getting a report.

***I have different teams in different time zones. How will this affect the SLA calculation and the SLA Panel?***

Answer:

The information on the SLA Panel is calculated according to the time zone selected on the calendar. To see how users in different time zones are affected, let’s examine an example:

**Example:**

Let's imagine you live in Istanbul (GMT+3). Your team in Dublin utilizes a calendar set to its time zone, which is GMT+1. When it is 3 pm in Istanbul, it is 1 pm in Dublin.

Assume you created a new work item. This work item will not start counting until the start date matches the time in the selected time zone. So, if the work item’s start date is set to 9 am Dublin time, counting won't begin until 9 am Dublin time. When it is 9 am in Istanbul, you will see the SLA panel in your work item with the start date and target date calculated according to your time zone. However, the elapsed duration won't start counting until it’s 9 am in Dublin.

#### ***Are the calculations based on the assignee's or the reporter's time zone?***

Answer:

Time to SLA bases its calculations on neither. SLA start date, end date, and target date are displayed according to the user's own time zone. When performing the calculation, Time to SLA uses the time zone that is selected in the calendar for the SLA configuration.

#### ***Can I delete a calendar that's already been used by an SLA?***

Answer:

No, you can't. When you attempt to delete an SLA that's already in use by another SLA, you will receive an error that displays the names of the SLAs that are utilizing that calendar.