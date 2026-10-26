# Custom Keywords

## Basics of JQL Custom Keywords

A JQL keyword serves as metadata for an issue that has been evaluated and saved prior to performing a JQL search. The value associated with the JQL keyword is determined by running a function on the Power Scripts side.

In our case, the indexing function is implemented as a SIL script on the Power Scripts side. This script returns the value that will be used in Jira.

To enable custom properties indexing for this indexing process, follow these steps:

1. Access the Jira admin settings.
2. Locate and click **Apps** > **Manage apps**.
3. Locate and click **Power Scripts** in the left hand navigation to expand the menu.
4. Click **Configurations** in the left hand navigation.
5. Click the *Automations* tab.
6. Click the *JQL* tab in the configuration submenu.
7. Click the *Custom keywords* tab.
8. Click the **Enable Custom keywords Auto Synchronization** toggle to turn on that feature.

![Power Scripts for Jira Cloud custom JQL keywords interface](/cms_trial/assets/b47702b4-dd5e-4f0b-8d9c-3bc7b0f98054.png)

Next, you need to define an indexing function and the keyword to be used.

### The SIL Script as the Indexing Function

All indexing scripts run by Power Scripts are run in an issue context. This means that you may consider the indexing function one that takes as parameter the issue and returns a single value of type DATE, INTEGER, STRING or TEXT.

A good indexing function is:

1. **stable**, i.e. if you call it in two moments of time with the same input data, it will return the same result
2. **fast**, i.e. calculation should be as short as possible
3. **self-reliant**, i.e. calculation is based as much as possible only on the local, immediate, available data.

**Examples of indexing functions/scripts:**

A. The Good

```text
sl
```

B. The Bad

```text
//this is not stable. Tomorrow we will get another result!
return (integer)(((number)(currentDate() - created)) / (24 * 60 * 60 * 1000));
```

C. The Ugly

```text
include "chatgpt/functions.incl";
return derivedCustomerSatisfactionScore(subject, description, priority, getLastComment(key)["text"]);
```

This last example, although fully possible, it will be slow (and probably costly).

You may write your own indexing function in the SIL Manager editor.

![Power Scripts for Jira Cloud JQL keyword configuration panel](/cms_trial/assets/0a828b7a-e90f-4944-9192-a9549a203da9.png)

### The Keyword

The next step is to register the keyword you want to use with Jira. Click **Add JQL keyword**.

![Power Scripts for Jira Cloud add JQL keyword dialog](/cms_trial/assets/2c51a32f-0aac-4956-bf46-9737ca10616c.png)

When pressed, the above dialog will appear; you are required to provide a very simple name, no spaces and its data type (string, text, number or date).

Saving it will register it to Jira. For our example, we have the above stable function which we saved under *slen.sil*, and for simplicity we named our keyword ***slen*** too:

![Power Scripts for Jira Cloud JQL keyword usage example](/cms_trial/assets/ef0041fc-2dd2-4338-9afb-e90a685de72e.png)

The next step is to associate the keyword we just created with the script. Click on the **Edit** icon:

![Power Scripts for Jira Cloud string length JQL keyword configuration](/cms_trial/assets/2b46fca4-dbfd-4694-ab55-082131694bb2.png)

Script return should match or be convertible to the data type that Jira accepts. Incorrect types will yield incorrect results

Once you associated the script the screen will show you the keywords and their scripts:

![Power Scripts for Jira Cloud advanced JQL keyword settings](/cms_trial/assets/5c6a6d4a-e7f4-4824-85c6-954e86b49be4.png)

### Searching

Because we changed the configuration, we need to trigger the initial synchronization. After synchronization is completed, we will be able to search for the property we just defined in the normal JQL search box:

![Power Scripts for Jira Cloud JQL search results with custom keywords](/cms_trial/assets/5a68c485-0883-46b9-9d2b-cec551314328.png)

## Advanced Usage

The script that returns the values to be indexed actually may return more than the value. The accepted return is:

```text
VALUE, OPERATION, ISSUE_KEY
-or-
VALUE, OPERATION, ARRAY_OF_ISSUE_KEYS
```

This is because you might encounter situations in which you need to maintain the index value on a different issue (or a bunch of issues), and thus we offer the possibility of specifying where to put the value and how.

OPERATION may be one of the following:

| **Operation** | **Synonyms** | **Comments** |
| --- | --- | --- |
| + | add, plus | For strings, it adds the value separated by space, if not found previously in the indexed string.  For numbers it performs the addition.  For dates, the returned value must be an interval, and it performs the addition of the date already in place with the interval you provide |
| - | delete, remove, minus | For strings, it removes the value previously added; if not found does nothing.  For numbers it performs the normal subtraction  For dates, the returned value must be an interval, and it performs the subtraction of the date already in place with the interval you provide |
| = | set  equal | This is the default operation. It just sets the value you provided, which must be convertible as type to the target JQL type. |

### Examples

Of course, it is better to see some examples to master this feature.

#### Example 1

Let’s examine a simple example. Suppose we want to keep a list of keys of the subtasks on the parents of the issue, so that when we search for the key of the subtask, the parent is found instead:

```c
if(issueType == "Subtask") {
    //on subtasks, update the parent property, "+" (ADD operation) means to add 
    //the key string if it does not exist
    return key, "+", parent; //parent will store on the property subtasks keys
}
//on parents, we do not update the property
return;
```

If you install this on a property of type TEXT named ***sbt*** you may (after indexing) search for `sbt ~ SUBTASKKEY` and it will yield in search results the parent of the subtask you provided.

#### Example 2

Let’s see another example, this time a numeric one, maintaining a number on the parent issue, as the sum of the number of characters in their summaries:

```c
//calculates number of chars in the subject of the parent issue + no chars in 
//the children summaries as well.
//this is an example of an aggregator function.
 
persistent int lastCalc = 0; //keep it in a persistent var, per issue

int len = length(summary); //recalculate it

int diff = len - lastCalc; //create the difference
lastCalc = len; //save it in the persistent variable so we will know next time what quantity to update

if(issueType == "Subtask") { //if subtask, store it on the parent, not on the subtask
    return diff, "add", parent; //addition with negative elements is still addition, right ?
}
return diff, "plus"; //just store it for non-subtasks issues
```

In the above example we used the synonyms for the “+“ operation just to make it a bit more clear. Of course, the example is just an intellectual exercise, and you should come up with more useful aggregators.

#### Example 3

Last, an example that returns an array of issues as the last parameter:

```c
if(issueType != "Subtask") {
    return key, "+", subtasks(key); //update only on children of the current task 
}
//on subtasks, we still need to maintain the parent!
return parent, "set";
```

Here, you see two operations: one is from parent to child issues, the other is from the target issue itself. If you configure a STRING property with name ***childof*** afterwards you may search for it with the JQL `childof = "TEST-1234"`

### Additional Notes

To save on I/O note that if the property is not modified by the operation, no write operation is issued. Also, the “+“ and “-“ operations require an extra I/O operation (they will get the value which was pre-existing in the operation)

Old value from the index is not retrieved prior to the execution of the script because we cannot know in advance the target issues.

For type STRING or TEXT keywords: if there’s no value on the target, it is assumed an empty string. For NUMBER keywords, the missing value is considered 0 (zero). For DATE type keyword, you must set up a value (we do not assume anything).

Keep your indexer scripts tuned and cover all the corner cases. Avoid scripts yielding exceptions. Failure to do so may yield bad performance on PowerScripts side (and potential OOMs) and also will provide incorrect results in the Jira search.

## SIL Routines linked to JQL

You may manipulate the JQL value directly, although it’s not recommended because it may lead to inefficient I/O.

There are two functions you may use in any listener (for instance).

[getCustomKeywordIndexValue](/cms_trial/space/PSJC/734134284/getCustomKeywordIndexValue/)

[setCustomKeywordIndexValue](/cms_trial/space/PSJC/733775542/setCustomKeywordIndexValue/)

The usage is straightforward:

```c++
string value = getCustomKeywordIndexValue("TEST-2", "kcustomk");
setCustomKeywordIndexValue("TEST-2", "kcustomk", value + " change");
```

You will need to use the correct formatting for the data type you use.

## Legacy Keywords

In the past, JQL keywords had to be pre-registered with Jira and therefore the names can not be customized, only the values. Because of this, Power Scripts for Jira Cloud came with 3 sets of each keyword data type. This allows you to add custom values to these keywords through scripting.

![Power Scripts for Jira Cloud legacy JQL keywords management](/cms_trial/assets/fa213731-62d3-447b-b9b2-922616a71f8e.png)

It is recommended to move these configurations and give them more interesting names, since these may be very hard to use by your users.