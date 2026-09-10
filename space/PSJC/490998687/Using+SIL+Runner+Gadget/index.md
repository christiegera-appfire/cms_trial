# Using SIL Runner Gadget

When you select a script from the list, the **Description** field will automatically be filled in.

The **Parameters** field is used to pass values **into** your SIL™ program. To add a parameter click the **Add Parameter** button.

### Notes

- Parameter names must be unique, otherwise the most recent definition will overwrite the previous ones. This includes parameters with no name.
- You can customize the gadget to be more user friendly, by asking **parameters** in a different way. You can find more details [here](/cms_trial/space/PSJC/435028593/Parameter+Functions/).

![Power Scripts for Jira Cloud gadget execution display](/cms_trial/assets/db310b57-1e3e-4ecb-af0a-97d1251fbb8f.png)![Power Scripts for Jira Cloud webhook configuration dialog](/cms_trial/assets/8f5d14f1-7107-461f-8258-11e4a19d5ce8.png)

The parameters will be passed into the program using the **argv** variable. The values will be available using a construct like **argv["parameter\_name"]** or **argv[position].** For the above example, the number of rockets can be retrieved using **argv["groupname"]** or **argv[2]**. You can reorder the parameters using drag and drop.

Once you run the script, the program console will be displayed.

![Power Scripts for Jira Cloud webhooks management interface](/cms_trial/assets/d8a3b465-6d62-4adc-b1ca-8f32978c43a0.png)

You can use the [RunnerLog](/cms_trial/space/PSJC/433000617/runnerLog/) function to print info in the console as the program runs. Note that the console buffer is limited to 512 lines every ~0.5 sec and the console will only display the latest 512 lines.

#### **Example code**

```text
runnerLog("Preparing to start a war...");

runnerLog("Building tanks...");
runnerLog("Built " + argv["tanks"] + " tanks.");

runnerLog("Gathering infantry...");
runnerLog("Gathered " + argv["infantry"] + " brave men.");

runnerLog("Fueling rockets...");
runnerLog(argv["rockets"] + " ready.");

runnerLog("Dispatching orders...");
return "Good job! The world is now at war!";
```

### Tip

You can return as many values as you need, regardless of their type.

**See more**