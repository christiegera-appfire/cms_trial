# Power Scripts for Jira Cloud Product tour

When you install Power Scripts for Jira Cloud, **Power Scripts** appears in the left-hand pane after clicking **Settings** > **Marketplace Apps**. This page walks you through the key navigation elements:

- The **SIL Manager** menu contains the tools used to write and store scripts.
- The **Script Templates** page offers out-of-the-box scripts you can customize and use without writing code.

- The **Settings** menu gives you access to the Power Scripts configuration options.
- The **Self-Help** menu provides system management tools to monitor status, restart the engine, manage backups, and request additional resources.

![Power Scripts for Jira Cloud main navigation menu](/cms_trial/assets/026cdf84-7067-4f83-b03a-e90558861c02.png)

Let’s look at each menu section and learn more about the core functionalities of the Power Scripts app.

---

## The SIL Manager

The **SIL Manager** is a scripting console where you write, modify, organize, test, debug, and execute scripts. To access the SIL Manager, go to **Apps** > **Marketplace Apps** > **SIL Manager** in the left-hand pane.

![Power Scripts for Jira Cloud editor console display](/cms_trial/assets/ab1a2ae6-2a86-469f-94a3-be4d394e0ca0.png)

The **SIL Manager** is straightforward and easy to navigate. It consists of several components.

---

|  |  |  |
| --- | --- | --- |
| number 1a.png | In the left side of the SIL Manager, you have the **Files** panel, which contains two main directories:   - **silprograms**, where you organize and store your scripts and related files; - a settings folder called **kepler**. | - Create file folders. - Organize your scripts, files, and programs by grouping them in different folders. - Open the scripts you want to modify or run. - Save the script you’re working on. Alternatively, you can use the **Save** (▢) icon located on the main menu toolbar. - Use the **Search** field to locate specific scripts. - Collapse or expand the **Files** panel by clicking the vertical*Files*icon. |
| number2a.png | The Power Scripts editor is the largest panel in the SIL Manager. This is where you write scripts. | - Create or modify scripts. - The name of the file you’re working on is shown in the top-left corner of the editor. - When you start typing, the SIL Manager offers scripting suggestions. Power Scripts for Jira Cloud SIL Manager suggestions |
| number3a.png | When working in the editor, you use the main menu toolbar to perform various actions and complete tasks. | - Use the **File** drop-down menu to create new folders and files and access the SIL Manager settings. - Use the **Edit** drop-down menu to search for specific text in the script, find and replace it, or navigate to a specific row and column. - Use the **Insert** drop-down menu to add a condition in your script. - Use the **Snippets** drop-down menu to insert a snippet into your script. Snippets are small ready-to-edit sections of code that can be inserted into a larger script. - Use the **Window** drop-down menu to switch between full-screen and regular mode. - Use the **Run** drop-down menu to set the **Default Script Context**, which can be a specific Jira issue or global. The **Run** menu also lets you check, run, or debug the script you’re working on. To do this, you can also use the **Check** (▢), **Run** (▢ ), and **Debug** (▢) icons on the main menu toolbar. |
| number4a.png | The tabs at the bottom of the SIL Manager display scripts-related data. | - The **Editor** **console** displays output for some of the scripts that you run.  Power Scripts for Jira Cloud event viewer display  - The **Server log** tab opens the actual Jira server log, where you can view Power Script errors.  Power Scripts for Jira Cloud script templates page  - The **Event viewer** displays event data for the scripts you run or check. For more information about an event, click its **Show details** link.  Power Scripts for Jira Cloud template editing interface As you can see in the screenshots above, each tab you open contains additional menu icons in the panel's right corner. Use these icons to perform actions specific to the panel you’ve opened. For example, in the **Editor console** you can copy the output, download it to a file, or clear the results. |
| number5a.png | The vertical tabs on the right provide access to additional panels where you can create and manage SIL-specific variables and aliases and access the Power Scripts documentation. | - You can use the **Persistent variables** panel to create and assign values to variables that are not part of Jira, but are stored in the database. - You can use the **SIL Aliases** panel to create aliases for custom fields created in Jira. You can then use the aliases instead of the Jira issue keys.   Persistent variables and SIL aliases are part of the advanced Power Scripts functionality.   - In the **SIL Help** panel, you can open the online Power Scripts product documentation or use the search field to access the in-product help content. |

---

## Script Templates

Script templates are customizable scripts that you can use immediately without any coding. A simple interface generates the script based on your needs. Script templates are designed to support beginner Power Script users with some of the most commonly used script types. For ease of use, script templates are organized into categories.

To browse the Script Templates:

1. Go to **Apps** > **Marketplace Apps** > **Power Scripts** > **Script Templates**.
2. Select a category.
3. Click a script template to open it.

![Power Scripts for Jira Cloud settings configuration page](/cms_trial/assets/eea4d8d5-c2fe-4f11-9001-4d5682bc43c1.png)

If you are just starting with Power Scripts, you can browse and read through the available script templates. All script templates follow a similar structure.

![Power Scripts for Jira Cloud SIL engine operations interface](/cms_trial/assets/b2ca41d5-c0f0-4aee-9a08-62bb0f3e71db.png)

1. Under the template's name, you can see a short description of the script action.
2. Use thedrop-down menus to set the context for the script, where and how it will be applied.
3. Some script templates require additional values or parameters.
4. The **SIL code preview** displays the script based on the options, parameters, and values you provide.
5. Once the script is generated in the **SIL code preview** panel, you can run it immediately by clicking **Apply Action**.  
   Alternatively, copy and paste the code into the **SIL Manager**.

To learn how and when to use script templates, see the [Script Templates documentation](/cms_trial/space/PSJC/1165525018/Automation+(Script)+Templates/).

---

## Settings

In some cases, your scripts require additional configuration to run properly on the Jira instances you manage. You can access and manage these configurations on the *Settings* page.

![Power Scripts for Jira Cloud print output icon](/cms_trial/assets/d5b7ca48-a2aa-4e93-8027-c5b7580f633b.png)

1. Go to **Marketplace Apps** > **Power Scripts** > **Settings**.
2. Select a specific configuration from the menu.
3. To create a configuration, provide the required values and parameters in the configuration settings panel.

---

## Self-Help

The *Self- Help* dashboard is your central hub for system control and maintenance where you can:

- Monitor real-time system status and performance metrics
- Restart the engine when needed
- Configure system settings and parameters
- Allocate additional resources to optimize performance
- Create and restore backups of critical `silprograms` and `kepler` directories
- Request engine resizing to meet changing demands
- Access system notifications and support messages

![Power Scripts for Jira Cloud console output display](/cms_trial/assets/4fb57d98-7198-4900-9ba4-a36a885668d3.png)

1. Go to **Apps** > **Marketplace Apps** > **Power Scripts** > **Self Help**.
2. Select a system management menu and perform the required actions.

To learn how to use the Self Help dashboard, see [this page](/cms_trial/space/PSJC/516456599/Managing+your+solution%3A+Self-Help/).