# Built-in field hasn't been mapped

The general field mapping on the host platform (for example, the Jira instance on which you have installed BigPicture) hasn't been done for a particular field.

The mapping of tasks in a particular Box is irrelevant. The check is performed just for the general mapping of the primary instance.

**Example**

BigPicture is installed on the "nostromo2" Jira instance. The host platform mapping is:

![image2021-6-14_13-17-17.png](/cms_trial/assets/ec4cbdf7-a7fe-44a2-b54a-ab09a8d043ec.png)

The general mapping is on the left:

![image2021-6-14_13-18-17.png](/cms_trial/assets/ba474cec-e374-4039-88ae-92aa4a2b41dd.png)

To avoid the error when sorting by "End date" or "Start date," the following fields have to be mapped:

![image2021-6-14_13-19-29.png](/cms_trial/assets/fffbbd3c-4c85-42b4-ba1e-66faf819aa16.png)

## Built-in fields

The mapping must be done if you want to sort tasks using the built-in field.