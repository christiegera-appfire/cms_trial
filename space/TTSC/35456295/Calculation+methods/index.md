# Calculation methods

On this page, you’ll learn what different calculation methods mean and which one might be the best for your use case. The calculation method you select impacts how Time to SLA will calculate the elapsed duration of your SLAs.

**Before you begin:**

Each interval between a consecutive SLA start and endpoint within a work item’s lifespan is defined as a cycle. By default, each cycle starts with the earliest start point and earliest endpoint.

Now, let’s take a look at the different calculation methods you can choose from.

## First cycle

The First Cycle method calculates only the first cycle between the Open and Resolved statuses.

![Time to SLA Calculation methods first cycle timeline example](/cms_trial/assets/5f0567ba-50a8-425d-ae09-26ad66c736af.png)

This calculation method considers the date/time when your work item met the first start condition and uses it as the SLA start date. The date/time when your work items met the first end condition is used as the SLA end date.

**Important:** After meeting the first end condition, your SLA will not restart, even if you provide a start condition after the initial end condition!

**For example**:

Let's assume that your SLA will start when the status is **To Do** and end when the status is **Done**. Once you move the work item to **To Do**, your SLA will start counting until providing the end condition on this work item. When your status is **Done**, your SLA will never start again.

Even if you move the work item from **Done** to **To Do**, your SLA will not start, and Time to SLA will not take other cycles into account.

If you select this method, your SLA will only calculate the first cycle, which means you’ll never be able to restart the SLA afterward.

If you want to set up an SLA for **First Response Time**, you could use the First Cycle method.

## Last cycle

The Last Cycle method calculates only the last cycle between Open and Resolved statuses.

![Time to SLA Calculation methods last cycle timeline example](/cms_trial/assets/d57650e3-42bb-4c6f-8684-df975ca94c0d.png)

This calculation method considers the date/time when your work item met the last start condition and uses it as the SLA start date. The date/time when your work item met the last end condition is used as the SLA end date.

After meeting the end condition, if you provide the start condition again, Time to SLA will invalidate the previous cycle, and your SLA will start again.

**For example**:

Let's assume that your SLA will start when the status is **To Do** and end when the status is **Done**. Once you move the work item to **To Do**, your SLA will count until it provides the end condition on this work item.

When you move the work item from **Done** to **To Do**, your SLA will reset the elapsed duration and start from the beginning.

Moreover, this method displays the value of your SLA since the last Start condition was met. You can restart the SLA, but it will always display only the most recent cycle.

You can choose this method to keep the last comment’s time in the panel. This will tell you when the last comment was submitted and whether it aligned with your target date.

## All cycles

The All Cycles method will add up all cycles between Open and Resolved statuses.

![Time to SLA Calculation methods all cycles timeline example](/cms_trial/assets/700d4554-d619-4e11-a739-da7656a30fd9.png)

This calculation method considers the date/time when your work item met the last start condition and uses it as the SLA start date. The date/time when your work item met the last end condition is used as the SLA end date.

After meeting the end condition, if you provide the start condition again, your SLA will resume without resetting the elapsed duration.

**For example**:

Let's assume that your SLA will start when the status is **To Do** and end when the status is **Done**. Once you move the work item to **To Do**, your SLA will count until it provides the end condition on this work item.

When you change the status of the work item from Done to To Do, your SLA will resume on the previous elapsed duration. Please keep in mind that the elapsed duration will not continue to count between the end and start conditions.

This means that no matter how many statuses you change, your SLA will always pick up where it left off. It’s quite literally the sum of all cycles!

To give you a better idea, selecting All Cycles for your **Time to Resolution** SLA would be a logical decision since you'd want to know how many days it took you to solve the work item. The All Cycles method would track the time from the work item’s creation to its resolution.

## Largest span

The Largest Span method will calculate the elapsed time between the first Open and last Resolved status.

![Time to SLA Calculation methods largest span timeline example](/cms_trial/assets/a4516852-2c6d-4392-971f-1a0868d4322a.png)

This calculation method considers the date/time when your work item met the last start condition and uses it as the SLA start date. The date/time when your work item met the last end condition is used as the SLA end date.

After meeting the end condition, if you provide the start condition again, your SLA will resume without resetting the elapsed duration.

**For example**:

Let's assume that your SLA will start when the status is **To Do** and end when the status is **Done**. Once you move the work item to **To Do**, your SLA will count until it provides the end condition on this issue.

When you change the status of the work item from Done to To Do, your SLA will resume on the previous elapsed duration. Please keep in mind that, unlike the All Cycles method, the Largest Span also takes intermediary statuses into account.

In a nutshell, this method takes into account **all** **processes** from the start of the SLA to the time it is resolved.

**How is this different from the All Cycles method?** Unlike the All Cycles method, the Largest Span also includes intermediary statuses. In this case, these are the Resolved/Closed statuses.

---

## Important notes

If you have different business hours for each day (as shown below), TTS will consider Monday’s business hours.

![Time to SLA Calculation methods table showing cycle options and examples](/cms_trial/assets/55d2c558-81b3-4f15-8c4a-037538cfd282.png)

For example, if you add a goal with a duration of `1d`, TTS will consider this 1 day as 10 hours. This is because your business hours add up to 10 hours on Monday.