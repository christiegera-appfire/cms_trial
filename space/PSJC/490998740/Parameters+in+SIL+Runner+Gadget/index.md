# Parameters in SIL Runner Gadget

You can customize the SIL™ Runner Gadget in a more user friendly way by setting up the following components:

- **Name**- name of the configuration
- **Description**- description of the configuration
- **Execution script** - script that will be executed
- **Parameter script** - optional script that will dynamically insert the advanced parameter fields on the configuration run screen.

If no parameter script is given, the user will be able to add simple input fields for the text parameters (we maintained the old functionality). In order to not show any kind of input for the parameters, use an empty script.

## Example

![Power Scripts for Jira Cloud gadget settings display](/cms_trial/assets/2d30d742-8e58-4e47-8b30-3ae85896e32a.png)

The execution script is the script that will be executed. If there are any parameters declared in the parameter script, their values will be received and interpreted here. In order to get the values of the parameters, use the [parameter retrieval functions](/cms_trial/space/PSJC/434507485/Parameter+Retrieval+Functions/).

In our case, the execution script uses the [runnerLog](/cms_trial/space/PSJC/433000617/runnerLog/) function and can return as many values as you need, regardless of their type.

#### **Example code**

```text
date start_date = gadget_getDateValue(argv, "Start Date");
string tanks = gadget_getSingleValue(argv, "Tanks");
string infantry = gadget_getSingleValue(argv, "Infantry");
string rockets = gadget_getMultiValues(argv, "Rockets");
runnerLog("Preparing to start a war...");
runnerLog("The war will start at this date: " + start_date);
runnerLog("Building tanks...");
runnerLog("Built " + tanks + " tanks.");
runnerLog("Gathering infantry...");
runnerLog("Gathered " + infantry + " brave men.");
runnerLog("Fueling rockets...");
runnerLog(rockets + " ready.");
runnerLog("Dispatching orders...");
return "Good job! The world is now at war!";
```

The parameter script contains the declaration of the parameters that will be used in the execution script. In order to declare the parameters, use the input type functions.

#### **Example code**

```text
gadget_createDatePicker("Start Date", currentDate(), true, "Choose a start date");
gadget_createInput("Tanks", "500", true, "The number of tanks");
gadget_createInput("Infantry", "1600", true, "The number of tanks");
gadget_createCheckboxGroup("Rockets", {"A big one", "A lot of small ones"}, "", false, "Do you want to use rockets?");
```

The parameters can be set to default values, which can be edited before running the execution script. Using the scripts above, the SIL™ Runner Gadget will look like this:

![Power Scripts for Jira Cloud getting started interface](/cms_trial/assets/f60ba18b-f52d-4dba-94c1-d76986d5654a.png)

The execution of the script above produces the following output:

![Power Scripts for Jira Cloud SIL Manager menus overview](/cms_trial/assets/1b2554c7-a808-4044-b747-d9474d529200.png)

**See More**