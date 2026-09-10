# Transitions activity tab on issue view page

The JMWE app provides an overview of the transitions triggered on the issue on the issue view page under the Activity section. To view this tab:

1. Enable **Show "Transitions" Activity Tab on Issue View** on JMWE Configuration page
2. Go to the Issue View screen
3. Locate the *Transitions* tab under **Activity**

![contentId-466256308](/cms_trial/assets/264fc2dd-877f-4999-b43a-c28606637ebd.png)

The tab includes the following information:

1. **Transition** - `To` and `From` statuses of the transition. Note that JMWE does not show auto-transitions (the transition leading to the same status)
2. **When** - Timestamp at which the transition was triggered. You can hold the pointer over the date to see the full timestamp value (which is especially useful for relative date/time values)
3. **By** - Author of the transition
4. **Time in Status** - How long the issue spent in the "from" status (left of the arrow) before being transitioned.