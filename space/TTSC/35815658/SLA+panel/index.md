# SLA panel

The SLA panel presents SLA information and visualizes SLA status using colors and icons. If your work item meets the conditions for an SLA, the SLA panel will appear on the work item view:

![An SLA panel created by Time to SLA for Jira Cloud on the Jira work item view.](/cms_trial/assets/fb6c36c8-0917-4263-a9b7-1d7be587dde0.png)

If there are multiple SLAs within a work item, you will see a different panel for each SLA.

## Time to SLA’s SLA panel details

The SLA panel consolidates all SLA metrics into one customizable interface. It includes a live countdown and provides a clear, real-time view of SLA progress and status. Below are the key components of the SLA panel:

![Three SLA panels in different statuses - In progress, met, and breached.](/cms_trial/assets/d564b01b-242e-4253-98af-3c64ac8d1eef.png)

1. The name of the SLA being tracked.
2. Click to view detailed information about this SLA. Only users with access to the SLA configuration page can view this data.
3. Hold the pointer over these icons to see details like SLA goal and calendar name.
4. ⏳ SLA Start Date > ⌛ SLA Target Date.
5. The SLA status in **blue** means your SLA is progressing.
6. **Elapsed:** The time that has passed since the SLA started.

   - **Remaining:** The time left to meet the SLA goal.
7. SLA End Date.
8. The SLA status in **green**means your SLA has been successfully met.
9. The SLA status in **red**means your SLA is overdue/breached/violated.
10. If you miss your SLA deadline, this will show you the overdue duration.
11. The progress bar shows how far your SLA has progressed. It will continue to count after your SLA is overdue.

If you’d like to display the target date on a custom field, [learn how](/cms_trial/space/TTSC/35684678/SLA+custom+field/) here.

## Colors and icons

The SLA panel dynamically changes as the SLA progresses. Here’s what the different colors and icons indicate:

| **Color/Icon** | **What it means** |
| --- | --- |
| SLA panel status (blue) that shows 'SLA in progress'. | The SLA is in progress and on track. |
| SLA panel status (orange) that shows 'SLA is in critical zone'. | The SLA is in progress but in the **critical zone**, which means the deadline is approaching. You can change when the SLA will be in the critical zone in [SLA configuration](/cms_trial/space/TTSC/35651691/Define+SLAs/). |
| SLA panel status (green) that shows 'SLA has been met'. | The SLA goal has been met successfully. |
| SLA panel status (red) that shows 'SLA is breached'. | The SLA is exceeded/breached/violated. |
| SLA panel status (grey) that shows 'no target'. | The SLA doesn’t have a target. There can be three reasons:   1. `No target` is chosen as the goal. 2. `Negotiation date` is chosen as the goal, but it hasn't been set on the work item yet. 3. The JQL works, but the start condition hasn't been met yet. The SLA will start counting when the condition is met. |
| SLA panel status (blue with moon icon) that shows 'out of working hours'. | The SLA’s calendar is out of working hours. |

## How to customize the SLA panel

On the **Settings** > **SLA Panel** page, you can customize your SLA panel, such as where the panel appears and what’s shown on it. The settings include the following:

![Different configuration options available on the Time to SLA for Jira Cloud SLA Panel screen.](/cms_trial/assets/11c54eed-dae0-4c5e-8d15-5a91a8abf3f7.png)

1. **Display Options –** The SLA Panel can be displayed on the right, the left, or both.

   1. **Display “Where is my SLA” helper panel on issues missing an SLA –** This is enabled by default, but you can remove the helper panel if you’d rather not have it displayed.
2. **Shown in SLA panel –** Select which parts you want to display on the SLA panel.
3. **Duration Format –** Choose which units should be included in the duration format.
4. **SLA Context –** The SLA panel will display SLAs based on this selection.
5. **Completed SLAs** – Check this box to hide completed SLAs from the SLA panel.
6. **Out of working hours** **–** Check this box to hide SLAs from the SLA panel when their calendar is set to out of working hours
7. **Paused SLAs –** Check this box to hide paused SLAs from the SLA panel.
8. **Not started SLAs –** Check this box to hide not started SLAs from the SLA panel. New instances have this setting disabled by default.
9. **SLA Order –** You can order your SLA panels based on Urgency and Start Date. Or you can create a custom sorting option.

**SLA Order – Urgency:** SLAs will be ordered by their states (Running, Paused, Stopped) and then by remaining time.

If there are multiple SLAs in each SLA state, they will be placed in the following order:

1. Longest breach
2. Shortest breach
3. Shortest remaining time
4. Longest remaining time

**SLA Order – Start Date:** SLAs will be ordered based on their start date. It can be Ascending or Descending.

**SLA Order – Custom:** Order your SLAs as you wish. The world is your oyster.

1. **Live Preview –** As you select your options, watch the right-hand side to see a live preview of what the SLA panel will look like.