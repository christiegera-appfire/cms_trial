# Issue can be assigned only active or future sprints

![contentId-1918832646](/cms_trial/assets/be7e0d61-48d9-4ffb-b1a5-e24336ad8305.png)

You can't add issues to Jira sprints that are already closed.

If you have synchronized your sub-boxes (such as Iterations) with a Jira sprint field by assigning a task to a sub-box, you may inadvertently assign a task to a closed sprint.View the use case below to see how this situation may occur.

![contentId-1918832646](/cms_trial/assets/384d5036-7403-49c9-bf0e-bbf93753ad88.png)

## Use case

You have a Program-type Box with Iteration sub-boxes in it.

![image2021-5-24_10-22-15.png](/cms_trial/assets/72e50523-592a-499d-9a4e-873525361385.png)

In the OMEGA Program-type box configuration, you can see that Iterations (sub-boxes in the Program-type box) are **synchronized with Jira sprints**.

![image2021-5-24_10-24-12.png](/cms_trial/assets/8943af55-d623-4130-b696-9f2ba259a53a.png)

Sync works both ways:

- Assigning a task to a sprint automatically puts it in an appropriate Iteration Box;
- Assigning a task to an Iteration Box automatically assigns it to a Jira sprint.

So, for example, when you use the Board module to assign tasks to Boxes, even though the tasks are shown under Iteration 1 in the Board module, the app will return an error if Iteration 1 is synced with a closed sprint.

![image2021-5-24_10-28-31.png](/cms_trial/assets/2703a2a5-8452-431d-9b1e-b50981c50541.png)

In this case, Iteration 1 is synced with a sprint that is already closed in Jira:

- On the one hand, Jira doesn't let you modify closed sprints (you can't add tasks to them);
- On the other hand, the app is trying to assign a task to a sprint because of your actions in the Board module.

![contentId-1918832646](/cms_trial/assets/65e0d831-6911-4a6d-a976-9a99d59662f2.png)![contentId-1918832646](/cms_trial/assets/35d99833-abf9-453d-a932-28698ce7ee3c.png)

### Closed sub-box status

Changing the box status to "Closed" is helpful after the associated sprint has been closed in Jira. The box color will change to green - the app won't let you assign a task to a closed box, and the Box status will be easy to see.

![contentId-1918832646](/cms_trial/assets/c2f90e59-6109-4fcb-aef1-75553a5f66cd.png)![contentId-1918832646](/cms_trial/assets/e2f72000-0828-466a-a6fc-e779e0acce59.png)

## Solutions

You have two ways of addressing the issue:

- Assign tasks to different sub-boxes (Iterations synced with sprints that aren't closed)
- Re-open the sprints → assign tasks to Iterations → close sprints after tasks have been successfully assigned.

### Assign tasks to boxes synced with sprints that are NOT "closed"

This is the recommended option. If a sprint has been closed in Jira, you probably don't want to associate new tasks with it. Assign tasks to sub-boxes (such as "Iterations") that are NOT "Closed."

Also, make sure that the sub-box status reflects the sprint status. Once you close a box, the app won't let you assign new tasks. This limits the chances of this error appearing.

**How do I know which tasks should be moved because they don't belong to a closed sprint?**

1. Check which boxes are synced with which sprints.
2. Check the Sprint Reports of closed sprints. Completed sprint issues that haven't been carried forward to the following sprint are listed on the report. Only those issues should be in a Box associated with a closed sprint. Other issues should not be added to a box.

Pick a sprint report to view:

![image2021-5-24_11-32-44.png](/cms_trial/assets/581a39c7-3a5b-49ae-9e90-c1bb38042715.png)

Only those issues should be in a box synced with this sprint:

![image2021-5-24_11-33-38.png](/cms_trial/assets/dfb03a4b-9d5f-4a35-8aad-227cf0e94d07.png)

Move the tasks accordingly.

![image2021-5-24_11-34-35.png](/cms_trial/assets/372f352c-cf9e-4fc4-9f84-04c81b8730d4.png)

Then, clear the warning logwhen it appears.

### Re-open sprints

Technically, it is possible to re-open a sprint and make changes if you need to do it.

To view closed sprints, go to "Reports":

![contentId-1918832646](/cms_trial/assets/2fe5b360-11e5-4c28-b7aa-548fe098b7ea.png)

Select "Sprint Report: on the left:

![image2021-5-24_10-43-20.png](/cms_trial/assets/f246702a-a339-48e7-b47a-5aae1050a6d5.png)

To "Re-open" a sprint, use the button on the right:

![contentId-1918832646](/cms_trial/assets/48505bc5-2770-4b82-b6e7-37d31d9f628a.png)

Go back to the app → refresh → clear the log

![contentId-1918832646](/cms_trial/assets/d6234475-2641-4da3-836f-e1fadc2cdd9c.png)

Now, you can go back to Jira and close the sprint. The error won't appear again.