# Script Debugger (Beta)

The SIL Manger and debugger are identical between Data Center and Cloud.

See the video for an example of using the SIL Manager debugger feature:

## Opening the debugger

To open the debugger, select the debugger button next to the **Run** button in the SIL manager menu bar. The debugger button is displayed only when a SIL script is open.

The debugger can only be used inside a SIL script. You can have any file type in the SIL manager. However, the debugger can only be run by a SIL script.

The script must be saved to run the debugger.

## Debugger overview

![Power Scripts for Jira Cloud breakpoints demonstration](/cms_trial/assets/00aca5e1-5a4f-408f-ac28-d4daa17bcea5.png)

1. **Run** button.
2. Break point(s)/execution pointer.
3. Debugger controls.
4. Status information.
5. **Variables/Values** tab.
6. **Context** tab.
7. **Modified objects** tab.
8. **Debug stack** pane.
9. **Breakpoints** pane.

## Execution pointer

The execution pointer is the line in the script that is currently evaluated. In the screen recording below, the execution pointer is the line of code highlighted in green. As the debugger moves through the lines of code, stopping at breakpoints, the execution pointer moves as well.

![Power Scripts for Jira Cloud debugger variables panel](/cms_trial/assets/83be0549-9dec-4baf-aa71-06a64b3ce85b.gif)

## Breakpoints

Breakpoints are one of the most important debugging techniques in your developer's toolbox. You set breakpoints wherever you want to pause debugger execution. For example, you may want to see the state of code variables at a certain breakpoint.

To set a breakpoint, click in the white margin next to the line number in the code editor pane.

![Power Scripts for Jira Cloud debug execution interface](/cms_trial/assets/9ce6661e-0e30-4b54-afab-ac777ecac210.gif)

## Actions

The following actions are available in the SIL Manager menu bar:

- Resume
- Step over
- Step into
- Step out
- Terminate

![Power Scripts for Jira Cloud debug console display](/cms_trial/assets/f94cea0a-e28e-49f3-9716-09abbd3873cb.png)

### Resume

The debugger runs the program and “breaks” only on user-defined breakpoints (indicated by red dots). The **Resume** action restarts the debugger on the next line of code.

### Step over

When using this action, the debugger runs the program statement by statement within the current execution context (scope).

### Step into

When using this action, the debugger runs the program statement by statement.

The debugger runs the function body if the statement is a function call (a new execution context is displayed in the **Call stack** tab). Otherwise, the debugger continues to the following statement, as in the case of the **Step over** control.

### Step out

If the debugger is within a nested scope, this action proceeds until the function returns (exits the current execution context).

If the debugger is within the global scope, this action runs the program to the end.

### Terminate

This action causes the debugger to stop running so that you can edit the code again.

## Main section

### Variables/Values tab

This tab contains the values of variables used in the script.

The contents of this section are dynamic and are updated as the script runs. This is a useful tool when combined with breakpoints to see if the script is working as expected.

![Power Scripts for Jira Cloud debugger call stack interface](/cms_trial/assets/db8ffd77-b179-4223-9f46-5ca0a747b46e.png)

### Context tab

The **Context** tab contains useful information about the “context” the script is running in. For example, you can find information such as whether the script is running against an issue context using the **Run** **Configuration** setting. In the screenshot below you can see that the script is running in the context of issue TP-1089.

![Power Scripts for Jira Cloud debug interface overview](/cms_trial/assets/327a42b8-c2d6-4131-b23c-c771fe10498a.png)

### Modified objects tab

The **Modified objects** tab displays objects such as Jira issues or Confluence pages, that are modified as part of the script. This is useful to keep track of what changes when the script runs.

![Power Scripts for Jira Cloud scripted fields configuration interface](/cms_trial/assets/53f5f5b0-27b3-4706-812a-e64ede407304.png)

### Debug stack pane

Use the **Debug stack** pane to view the function or procedure calls that are currently on the stack.

This pane displays the order in which methods and functions are called. The call stack is a good way to examine and understand the execution flow of an app.

### Breakpoints pane

The **Breakpoints** pane displays a list of all the breakpoints used in the script.

Click a breakpoint to jump to the respective breakpoint in the script.

![Power Scripts for Jira Cloud field configuration panel](/cms_trial/assets/5348c422-df5a-441f-8674-18b8c97bd33c.png)

To remove a breakpoint from the script, click the **Trash can** next to the respective breakpoint.

Note that, in the example above, two breakpoints are displayed in the pane, but only one can be seen in the script. The second breakpoint belong to the other file included in the first line of the SIL code. Keep this in mind to better manage the locations of all the breakpoints when debugging scripts comprised of multiple files.