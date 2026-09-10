# Define SLAs

Time to SLA lets you define and track an unlimited number of SLAs. On the **SLAs** page, you can define new SLAs, manage your existing SLAs, and manage notifiers.

## How to define an SLA

This documentation provides step-by-step instructions on creating an SLA using the Time to SLA app for Jira Cloud.

Watch this 2-minute video to get an overview:

Video script

Hi there! In this video, we’ll show you how to create your first SLA in the Time to SLA app for Jira Cloud. Let’s get started.

First, open the **SLAs** screen, then click on **SLA** or **Create your first SLA**.

Give your SLA a clear name so your team knows what it’s for. Optionally, add a description for more details. After that, select the project this SLA will apply to. You can further refine the issues by specifying additional details like issue type, request type, assignee, and JQL in the next step. When you're ready, hit **Next** to move forward.

Now, let’s set the goals for your SLA. Think of SLA goals as the timeframes or deadlines for tasks. You can set these as specific durations—like days or hours—or tie them to a custom field, such as a due date.

Want to add multiple goals? Just click the Add Goal button. For example, you might create an SLA goal for issues tagged as High Priority or based on certain issue types or request types. These goals will be prioritized from top to bottom.

The SLA will be applied to issues that match the filters or queries you set up.

Now, let's set when the SLA should start, pause, and stop. For example, you can start the SLA when an issue is assigned, pause it while you’re waiting for customer feedback, and stop it once the issue is resolved.

You can add multiple conditions and, if needed, group them using **AND** or **OR** operators for more complex scenarios.

For those who want to dive deeper, Time to SLA has advanced options like the Calculation Method, Critical Zone Percentage, and more. For example, these tools can help you track when an SLA is approaching its deadline and customize notifications to stay ahead of the curve.

And that’s it! Once you’re done, just hit **Save**, and your SLA is ready to go. Now you can track, manage, and meet your deadlines more efficiently in Jira.

To see your SLA in action, create a new issue and open it. This is the SLA panel, where you’ll see a live countdown tracking the time, along with key metrics to help you monitor progress. When the start condition is met, the SLA panel will start ticking. If you want your SLA to apply to existing issues, just run a recalculation within the SLA's scope. There’s more info on that in the documentation.

Once the SLA starts, you’ll automatically receive notifications when it reaches 50% and 75% of its duration to help you stay on top of deadlines.

Thanks for watching! Now that you know the basics, dive into the app and start creating SLAs that help your team deliver results on time, every time. Happy tracking!

### **Steps**

1. Log in to your Jira Cloud account.
2. Click **Apps** in the header menu and open the **Time to SLA** app.
3. Go to **SLAs** in the header menu.
4. Upon installation, the **SLAs** page appears empty if no SLAs are imported. Click **+ SLA** or **Create your first SLA** to define your first SLA.

   ![A screenshot showing the SLAs screen and the button placement on the Time to SLA app.](/cms_trial/assets/34383697-cba4-41fb-b343-b2840efd9eba.png)

#### Step 1: Set up your SLA definition

1. Enter a clear and concise name for your SLA that reflects its purpose.

   ![A screenshot showing the SLA definition, step 1. ](/cms_trial/assets/e75c083d-4d1f-4c23-b4ad-fb515878e3e8.png)
2. Optionally, add a description.
3. Select the project(s) to which the SLA will be applied. As you select the projects, the work items under those projects will be listed below. If you want to narrow down the scope of the SLA even more, you can do so in the **SLA Goals** step.

#### Step 2: Select your SLA goals

Set your SLA goals, which are time limits or deadlines set within your specified context. They are tracked according to your working hours.

Each goal can be a specific timeframe (days, hours, minutes) or a fixed deadline, such as a due date or custom field in Jira work items. If your SLA includes multiple goals, they are prioritized from top to bottom. The remaining work items will be handled under a default goal.

1. Use the **+ Add goal** button to configure goals. *Add* *SLA goal* screen opens.

   ![A screenshot showing the SLA goal creation, step 2.](/cms_trial/assets/a44b8eaa-cea9-4ce7-b802-a0cf76480093.png)
2. **Goal Name:** Enter the name of the goal.
3. **Goal Calendar:** Select the goal calendar. You can also use the *Select calendar via Jira issue* feature to ensure teams can dynamically select their calendar based on their geographical location.
4. **Goal Target Type:** There are five you can choose from. Refer to the [related documentation](/cms_trial/space/TTSC/35390901/SLA+goals/) to learn more about each type.
5. **Goal Issues:** Select the work items the goal will apply to. If you select *Only specific issues in selected projects*, a dropdown will be revealed, and you’ll need to perform a set of configurations to narrow down the SLA scope. You can directly select the work item types the SLA will be applied to, or click **+ More** to select work items based on:

   - **Request Type –** Tailor the SLA to the unique needs of that type of request. For instance, you might want different SLAs for bug fixes, feature requests, or support queries.
   - **Issue Type –** Each project can have different Issue Types (for example, Bug, Task, Story). Choosing an Issue Type ensures that the SLA is applicable to work items falling under that specific category.
   - **Issue Priority –** Assigning an SLA to a particular Priority ensures that the defined service levels are applied based on the criticality of the work item (for example, Highest, High).
   - **Issue Filter –** Allows you to apply the SLA to a subset of work items based on a predefined filter, giving you extra flexibility.
   - **JQL (Jira Query Language) –** Allows you to create sophisticated queries to filter and retrieve specific sets of work items and apply the SLA to matching the criteria defined in the JQL query. This is particularly useful for advanced users who want to create dynamic and customized SLA conditions.

Add other goals as needed to reflect all SLA requirements. Once you’re done, proceed to SLA conditions.

#### Step 3: Set your SLA conditions

1. Select your SLA conditions. Time to SLA lists the most widely used conditions inspired by real-world scenarios to save time; however, you can click **+ More Condition Types** to reveal many other options. For example, you might start time when a work item is created, pause time while you wait for the customer to respond, and stop time when the work item is resolved. You can add more than one condition.   
   Check out the screenshots below to see some examples:

![A screenshot showing the SLA condition creation, step 3.](/cms_trial/assets/d6658156-c690-46bb-acdc-15585b910730.png)

![A screenshot showing SLA condition creation, with another example.](/cms_trial/assets/4eaa34f6-ade4-4009-a362-4ea172f097c7.png)

Conditions can be connected using logical operators, with the default being the OR (“Any of the following conditions”) operator, meaning the SLA starts when any of the conditions are met. Alternatively, you can use the AND (“All of the following conditions”) operator. In this case, the SLA will start only when all conditions within a group are met.

![A screenshot showing the differences between OR and AND operators.](/cms_trial/assets/ed522403-b163-4e56-9a6b-a37afcf9d84b.png)

You can also create Grouped Conditions to construct intricate SLA use cases by organizing conditions into logical groups with specific connectors.

For more information about SLA conditions, refer to the [related documentation](/cms_trial/space/TTSC/35456221/SLA+conditions/).

Once you click **Save**, your SLA will be created.

#### (Optional) Step 4: Dive into advanced configurations

1. If you want to dive into more advanced configurations, click **Edit**. The advanced configurations are:

   - **Calculation Method –** Select the calculation method for the elapsed duration. Your options are **All Cycles**, **First Cycle**, **Largest Span**, and **Last Cycle**.

     ![A screenshot showing the different calculation methods an SLA can use in the Time to SLA app. ](/cms_trial/assets/25fca42c-ef2f-4d0b-9293-046e26116081.png)

     By default, All Cycles are selected. For example, if the SLA starts with an Open status and ends with a Resolved status, the All Cycles method will add up all the cycles between Open and Resolved statuses. [Click here](/cms_trial/space/TTSC/35456295/Calculation+methods/) to learn more about calculation methods.
   - **Critical Zone Percentage –** This is a parameter that you can set to signal when an SLA has reached what you would describe as a critical status. When an SLA enters this zone, the SLA panel’s color will change from **blue** to **orange**.

     ![A screenshot showing the critical zone percentage selection in the Time to SLA app.](/cms_trial/assets/46c0e112-6fb8-4a2b-88a0-59e7454a2f48.png)

     ➡️ *You can create notifications that will alert you and your team when an SLA is in the critical zone. Learn how* [*here*](/cms_trial/space/TTSC/35881090/Actions/)*.*
   - **SLA Custom Field –** Add this custom field to screens where you would like to see SLA target date information. Only date/time custom fields can be selected as the target date, hence why only these custom fields are available within the drop-down menu. Please note that this is an optional custom field that will need to be added to the relevant screens. The installation of Time to SLA does not automatically add it to work items. To learn how, [refer to this documentation](/cms_trial/space/TTSC/35684678/SLA+custom+field/).

     ![A screenshot showing the SLA Custom Field ](/cms_trial/assets/30392d32-224d-40c3-85ce-5159db2f114d.png)
   - **Linked Issue SLA –** You can select whether to display this SLA in linked work items and specify which link types it’ll be displayed in. When you link two work items, you’ll be able to see the SLA panel on both of them.

     ![A screenshot showing the Linked Issue SLA configuration options.](/cms_trial/assets/12caf78c-62f0-4935-b815-71bf0aacacd6.png)

**Example:**

Assume there are two work items: Work 1 in "Space 1" and Work 2 in "Space 2". The link created between these work items is as follows:

"Work 1 blocked by Work 2" hence "Work 2 blocks Work 1 ". The SLA configuration only has "Space 1" defined for the SLA scope **Projects** and is configured to display Linked Work Items **Blocks**.

With this configuration, the expectation is that you should be able to see the SLA of the linked work item "Work 1" on "Work 2".

Don’t forget to click **Save**.

## SLA management

![The SLAs screen, with different actions you can take on the screen highlighted.](/cms_trial/assets/222e101e-b6c3-49b5-aeba-f375e9bd6dac.png)

1. **SLAs –** Click to access all of your SLAs.
2. **Search bar –** Choose a filter from the dropdown, like `Priorities`, and then use the search box to find specific elements within that category. For example, search for `Blocker` to target SLAs with that priority.

   ![A screenshot showing how to use the search bar on SLAs screen.](/cms_trial/assets/8f6bdb7b-393c-43f2-901f-113874be99d6.png)

   The limits in the search bar are based on the values added in the SLA context.
3. **Hide disabled SLAs –** Check this box to hide disabled SLAs from view. To disable an SLA, click the three-dot icon next to it and select **Disable**.
4. **List of SLAs –** All of the SLAs in your instance are listed here. Clicking on the name of any SLA will take you to its configurations, allowing you to edit it. By clicking on the arrow next to them, you can reveal the details about the SLA, and then use *Columns* on the right-hand side to filter which details you want to see in this view (Conditions, Goals, etc.).
5. **Columns –** Add or remove columns that display information about the selected SLA on the SLAs page. You can change their order by dragging and dropping them on the table.
6. **SLA Options Menu –** After expanding the details of an SLA by clicking the arrow next to it, you can click the three-dot icon on the right-hand side to reveal the options menu for the SLA.

   ![A screenshot showing the SLA options menu.](/cms_trial/assets/c33eadad-2ca2-49a4-90e0-2998ae322cc8.png)
   - **Edit –** Click here to modify the SLA by updating any field. Alternatively, click on the SLA name to open the editing screen.After editing, you must recalculate the SLA data for the work items; otherwise, you may run into miscalculations. Click here to find out [how to recalculate SLA data](/cms_trial/space/TTSC/35456416/Recalculation/).
   - **Manage notifiers –** This option lets you set up and manage notifications for your SLA.
   - **Clone –** Clicking this optionduplicates that SLA.
   - **Enable/Disable –** Click to enable or disable the SLA. When an SLA is disabled, all SLA actions are stopped. The SLA won’t appear in fields, reports, and other configurations. You can use this feature to hide SLAs that are irrelevant to your workflow but might be needed in the future. Disabling such SLAs preserves configurations for potential future use.
   - **Delete –** This action is irreversible and will permanently remove the SLA.

SLAs created using the old interface (created before June 20, 2024) cannot be cloned. You must create new ones using the new system.

## Next steps

[**SLA notifications**](/cms_trial/space/TTSC/35881090/Actions/)