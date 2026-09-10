# Create presets in Rich Filter Controller

By the end of this tutorial, you will be able to create and use custom presets in the *Rich Filter Controller*. These presets allow you to save and quickly apply your most frequently used filter combinations with a single click.

Every dashboard user can now define their own presets in the controller. You can save any combination of quick filters as a preset. Presets appear as toggle buttons at the top of the controller and allow you to apply the corresponding filters with a single click. You can create multiple presets and switch between them easily. The configuration of your presets is saved in the user preferences in Jira. With this feature, every dashboard user can have their own presets available when working with the dashboard on different browsers and computers.

![Screenshot showing the Presets combination in Jira dashboard.](/cms_trial/assets/9674c351-19e3-40c3-885f-380816a962a8.png)

## Before you start

You need to have already created:

1. A rich filter - [Create and access rich filters](/cms_trial/space/RFCDOC/783941927/Create+and+access+rich+filters/)
2. A dashboard with *Rich Filter Controller* and *Rich Filter Results* gadgets - See [Build a simple interactive Jira dashboard](/cms_trial/space/RFCDOC/783941937/Build+a+simple+interactive+Jira+dashboard/).
3. Some static, dynamic, or smart filters are defined and visible in your *Rich Filter Controller*.   
   We have used the dashboard we worked with in [the smart filters tutorial](/cms_trial/space/RFCDOC/783941961/Add+smart+filters+and+smart+columns+to+your+dashboard/).

## Create your first preset

1. Open your dashboard with the defined *Rich Filter Controller*.
2. Click **Menu** (▢) > **Show presets** (▢).

   ![image-20260129-121022.png](/cms_trial/assets/61e6038f-3f85-41f1-95dc-eabd2877f707.png)
3. Configure your filters by applying the quick filters you want to save as a preset. For this example:

   1. Clickthe **Assigned to me** static filter.
   2. From the **Priority** dynamic filter, select **Highest**, **High,** and **Medium** priority.
   3. For the **Status** dynamic filter, select all statuses except for **Closed.**

      ![Screenshot showing the Apply filter combination.](/cms_trial/assets/6e152639-e659-4113-a345-a549ea5daf68.png)
4. Click **Apply**.  
   The dashboard now displays only issues matching your selected criteria.
5. Click **Create preset** to create your first preset.
6. Customize your preset:

   - Label your preset, for example, name it `My items`.
   - Change the display color to help you identify it quickly.![Screenshot showing the Save filter combination.](/cms_trial/assets/c7b6657f-983e-409b-ab8d-83e62ff5e88e.png)
7. Click **Save** to save your configuration.  
   Your new preset appears as a toggle button at the top of the *Rich Filter Controller*. It is automatically saved in your Jira user preferences, ensuring presets are available every time you access the dashboard.

   ![Screenshot showing the My items preset.](/cms_trial/assets/1280c07c-958a-4679-a7f7-c9fb36bcaf20.png)
8. Repeat the process above with different filter combinations to create more presets that suit your needs.   
   You can create multiple presets and switch between them easily by clicking on the corresponding toggle buttons at the top of the controller.

   ![Screenshot showing the My items and To do presets.](/cms_trial/assets/62e007b6-729b-4a57-bf96-0c057771168e.png)

To modify your existing presets, click the **Menu** icon that appears when hovering over the **Presets** (▢) icon and select the **Edit presets** option.

![Edit existing presets](/cms_trial/assets/9520eb43-a4b2-41d2-9531-532d76fbe22f.png)