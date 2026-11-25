# Lag time

## About the lag time

You can set the Lag time to add time to the start or finish of a predecessor task, which creates a gap in timing. The Lag time delays the start of the successor task, although you can also set it to a negative value.

If the value is positive, the tasks will be separated by the given number of days. If, on the other hand, the Lag time is a negative value, then the tasks will overlap.

The working and non-working days are both included in the Lag time calculation. Parent tasks can start/finish on non-working days when Lag time is applied.

## Set lag time

To set the Lag time, create a dependency first and click the created link to open the details dialog. Next, enter the Lag time.

For example, a period almost always exists between sending out a Request for Quote for a service and receiving the quote. When you show a lag, you show the plus (+) sign and then the amount of lag.

For example, a lag of one week is shown as +5.

![Dependency details modal. A lag time is set to five.](/cms_trial/assets/1616a31b-03f0-4ea2-aa61-249a32444fc7.png)

As a result, a 5-day gap will be maintained by the App, and when the ASAP mode is enabled, the tasks will be scheduled such that the gap is reduced to the set minimum:

![5-day-gap.png](/cms_trial/assets/9ed6842c-5029-4b28-ab0d-58a6ad9f7f7b.png)

Another common case is sequential tasks starting on the same date or a couple of days before the predecessor's end date. Let's set a negative Lag time (-1):

![edit-dependency-lag.png](/cms_trial/assets/e99503a1-360a-4140-8271-b4ae1c67877a.png)

As a result, both tasks can start on the same date while having the 'End to start' dependency:

![end-to-start.png](/cms_trial/assets/51f84f56-6851-43aa-8dc7-c5330f1ce06c.png)

## Lag time and non-working days

When you set the Task Period to one of the auto-modes, the App will move the linked task such that it does not start on a non-working day.

For example: You can set the Lag time to +1, +2, or +3, but if there are non-working days, the result position of the tasks remains unchanged:

![lag-time.png](/cms_trial/assets/c3e614ad-4515-4b84-94a3-cf478889bf27.png)

## Lag time and scheduling mode

The Scheduling mode has priority over the Lag time. When the task is set to Manual or Locked mode, dependencies do not work, and no Lag time is applied.

For example: The Lag time between Task 1 and Task 2 is set to 10 days, but because Task 2 is in Manual mode, the Lag time does not take any effect.