# Arguments (argv variable)

The argv variable is a [standard array field](/cms_trial/space/PSJC/434602568/Variable+types+and+reference+methods/) provided by the language to pass arguments into a script. It is predefined in all executions of the SIL scripts.

## Where it is used

There may be situations where a single script is used in such a way that the argv variable is truly needed, so you may want to differentiate between calls:

- [SIL Runner Gadget](/cms_trial/space/PSJC/490998486/SIL+Runner+Gadget/) scripts
- Live Fields scripts (DataCenter only)
- [call function](/cms_trial/space/PSJC/435028557/call/)
- [SIL Scheduler](/cms_trial/space/PSJC/490998807/SIL+Scheduler/) configuration
- Listeners
- Postfunctions
- etc

Refer to each item documentation to see the parameters passed onto the argv variable

## How to use it

Just like any other standard field, the argv variable can be called directly in any script. For example, the following script would print all the arguments in the argv variable in the log file.

```text
logPrint("INFO", argv);
```

Since the argv variable is an array it can also work with index operators:

```text
string firstArg = argv[0];
//or, provided that the invoking protocol defines a map array
string summaryValue = argv["summary"];
```

Or, since the argv variable is an array it can be iterated over using a loop:

```text
for(string argument in argv) {
    //do something with the value of the argument variable
}
```

## Examples

## SIL Runner Gadget Example

While it is usually better to use a [parameter script](/cms_trial/space/PSJC/490998740/Parameters+in+SIL+Runner+Gadget/) to create input fields, generic parameters can be used and passed to the script.

![Power Scripts for Jira Cloud script editor showing argv variable configuration](/cms_trial/assets/386fdec4-5aea-47ec-905f-aff28ee1dd9c.png)

The values of the parameters can be accessed using the argv variable:

```text
runnerLog("I love to eat " + argv[0] + " and " + argv[1] + ".");
runnerLof("I don't like eating " + argv[2] + " unless they are over ripe.");
```

## Call function example

This script is designed to be used by the call() function as reusable code. It is a function that derives the file name from the full file path.

**getFileName.sil - reusable function**

```text
string filePath = argv[0];
int start = lastIndexOf(filePath, "\\");
return trim(substring(filePath, start+1, length(filePath)));
```

**Some other script**

```text
call("", "Functions/getFileName.sil", "C:/Jira/someFile.txt")
```

## SIL Scheduler example

For this example we have a scheduled script that will check the weather for several US ZIP codes and create new issues with the weather information.

![Power Scripts for Jira Cloud arguments variable configuration panel](/cms_trial/assets/a3d8cbed-ef3f-49aa-86b0-3fa3792f6cff.png)

The following code excerpt shows how the arguments can be iterated over to perform the action for each ZIP code:

```text
...
for(string zipCode in argv) {
  weatherData wd = getForcast(zipCode);
  string newIssue = createIssue("WTHR", "", "Forcast", wd.summary);
  %newIssue%.description = wd.description;
  %newIssue%.temperature = wd.temp;
}
...
```