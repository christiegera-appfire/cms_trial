# Lag time

## About the lag time

You can set the Lag time to add time to the start or finish of a predecessor task which creates a gap in timing. The Lag time delays the start of the successor task, although you can set it as a negative value as well.  If the value is a positive number the tasks will be separated by the given number of days. If on the other hand, the Lag time is a negative value then the tasks will 'overlap'. The working and non-working days are both included in the Lag time calculation. Parent tasks can start/finish on non-working days when Lag time is applied.

## Set lag time

To set the Lag time create a dependency first and click on the created link to open the details dialog. Next, enter the Lag time.

For example, a period almost always exists between sending out a Request for Quote for a service and receiving the quote. When you show a lag, you show the plus (+) sign and then the amount of lag. For example, a lag of one week is shown as +5.

![contentId-1918406747](/cms_trial/assets/352bc130-a383-4326-a09a-9be4fbd57e5b.png)

As a result, a 5-day gap will be maintained by the App and when the ASAP mode is enabled the tasks will be scheduled such that the gap is reduced to the set minimum:

![contentId-1918406747](/cms_trial/assets/afd14481-4114-4b69-a217-2267ce3a6e5b.png)

Another common case is sequential tasks starting on the same date or a couple of days before the end date of the predecessor. Let's set a negative Lag time (-1):

![contentId-1918406747](/cms_trial/assets/6a772511-9aa8-4dd2-a205-f8c7f8803128.png)

As a result, both tasks can start on the same date while having the 'End to start' dependency:

![contentId-1918406747](/cms_trial/assets/fde0e1d0-66cf-4443-9921-e054720dce69.png)

## Lag time and non-working days

When you set the Task Period to one of the auto-modes the App will move the linked task such that it does not start on a non-working day.

For example: You can set the Lag time to +1, +2 or +3 but as the task there are non-working days the result position of the tasks remains unchanged:

![contentId-1918406747](/cms_trial/assets/9803f8f5-027e-40cb-a3d7-1101f06566bc.png)

## Lag time and scheduling mode

The Scheduling mode has priority over the Lag time. When the task is set to Manual or Locked mode, the dependencies do NOT work then with no Lag time being applied.

For example: The Lag time between the OA-36 and OA-135 is set to 10 days but as the OA-135 is in manual mode, the Lag time is not effective.

![contentId-1918406747](/cms_trial/assets/a26c24cb-fc73-4398-9661-29a9845a20c2.png)