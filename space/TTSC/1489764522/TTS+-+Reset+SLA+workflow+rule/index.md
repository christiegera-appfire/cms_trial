# TTS - Reset SLA workflow rule

Time to SLA provides a single rule (previously, post function) called **TTS - Reset SLA**, which enables you to reset SLA timers based on specific workflow transitions in Jira.

Here’s how to configure and use this post function:

1. Go to **Work items** > **Workflows** for the relevant project and select the workflow where you’d like to add the post function.
2. Click the actions icon next to it and select **Edit**.
3. Select the transition where you want the SLA reset to occur. For example, if you want the SLA to reset when transitioning from `To Do` to `In Progress`, locate the specific transition within the workflow.
4. Click **Add rule**.

   ![Time to SLA reset SLA workflow rule configuration page](/cms_trial/assets/3dd7c39c-0d05-420c-a14f-af9eb0464780.png)
5. Select `TTS - Reset SLA` from the list.

   ![Time to SLA reset SLA workflow rule action dialog](/cms_trial/assets/06617f0f-cdeb-42e7-8ccd-f6e0d3da85c0.png)
6. After selecting *TTS - Reset SLA*, you’ll have several options to configure its behavior:

   ![Time to SLA reset SLA workflow rule final configuration screen](/cms_trial/assets/6caafe73-3250-4ded-8f70-c163374d3ac2.png)
   - **Reset type:**

     - **Restart current SLA**: Resets the SLA timer, starting it from the beginning.
     - **Invalidate current SLA**: Puts the SLA on hold until the next start condition is met.
   - **Behavior on finished SLAs** (only applies if the SLA has already completed):

     - **Do nothing**: Leaves the SLA as-is.
     - **Reset SLA durations and restart SLA**: Resets the timer and starts the SLA from scratch.
     - **Reset SLA durations and invalidate previous cycles**: Resets the timer and marks the previous cycle as invalid.
   - **Select SLA(s)**:

     - **All SLAs**: Applies the reset to all SLAs associated with the issue.
     - **Selected SLAs**: Allows you to choose specific SLAs to apply the reset to.
7. Click **Add**.
8. Click **Update workflow** to save your changes.