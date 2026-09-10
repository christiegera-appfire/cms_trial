# Custom fields aliases

Aliases represents a powerful tool to refer custom fields indirectly making your scripts function obvious.

## The Case for the Aliases

Addressing fields by their Jira internal name is not useful. Nobody likes to write 'customfield\_12067' instead of a meaningful variable name. Thus, we allowed to address the fields by name. Though you should keep in mind that certain errors might still appear because the field name resolution does not take into account that there can be more than one custom field with that name.

Look into the following code:

```text
if(isNotNull(customfield_10001) // or #{The Reported User)} if accessed by name
{
  assignee=customfield_10001; // assign the report to him or her
}
```

This code is meaningless without comments because the whole script purpose evades from the programmer's eye. A better option would be the following one:

```text
if(isNotNull(#{Reported User}) // or customfield_10001 if accessed by number
{
  assignee=#{Reported User}; // assign the report to him or her
}
```

Such coding style has the disadvantage that there might be more than one custom field with the **Reported User** name. In such cases SIL™ takes into account the first custom field resolved by name. Therefore, SIL™ has created its own custom field naming system, one that is independent of the IDs attributed by Jira to custom fields and one that can provide a much better distinction of the custom fields names. The feature is called SIL™ aliases, and allows you to alias any custom field with a friendly name. Let's see how this example looks with aliases.

## Managing Aliases

Find details on how to create and modify SIL aliases from the links below:

- [Managing aliases from the SIL Manager](/cms_trial/space/PSJC/496206102/Managing+aliases+from+the+SIL+Manager/)
- [Managing aliases in the sil.aliases file](/cms_trial/space/PSJC/496206151/Managing+aliases+in+the+sil.aliases+file/)

**Important:**

After each manual modification of the `sil.aliases` file, go to the *SIL Aliases* panel in SIL Manager and click the **Reload aliases** icon to refresh the data. Alternatively, you can use the `admReloadCustomFieldAliases()` function to programmatically reload aliases.

The `admReloadCustomFieldAliases()` function should only be called immediately after modifying the `sil.aliases` file. Do not use it frequently or unnecessarily, as it can impact performance.

**Important:** After each manual modification of the sil.aliases file, go to "SIL Aliases" panel and click "Reload aliases" to refresh the data.

Alternatively, you can use the `admReloadCustomFieldAliases()` routine to programmatically reload aliases. **This routine should only be called immediately after modifying the sil.aliases file** - do not use it frequently or unnecessarily as it can impact performance.

## Summary

Using SIL™ aliases instead of custom fields IDs and names is supreme. There are important results when maintaining a complex Jira install:

1. When and if a custom field gets deleted and recreated, its ID changes. Using SIL™ aliases allows you to keep your code unchanged, you just need to point in the sil.aliases file the new custom field ID for that alias.
2. Simpler syntax and clearer meaning of the scripts
3. Aliases provide independence of the Jira instance

Since 1 and 2 are obvious, let's discuss the 3rd point: the independence of the Jira instance. Think of two Jira systems, for instance test environment and a production one. You do not want to work directly into production so normally you develop your new workflow on the test environment and you add a new custom field. Now, everything is ready and you want to publish changes into production system, so:

- You create a custom field with the same name on the production system. But Jira assigns its own ID, that may be different from the ID on the test system.
- You move over the SIL™ scripts.
- You import the workflow, with the paths changed to the above SIL™ scripts if necessary.

Now, if you referred your custom field by its ID, you need to go through every script and do a search and replace the old ID with the new one. If you referred it by name, maybe your colleague just added a custom field, used in some other project, that has the same name.

However, if you used the alias, you just place your alias in that file, and everybody is happy.

It is important to keep aliases names unique. If more than one alias with the same name exists, the last one is taken into account, the rest are discarded.

## Another Example

If you're still not convinced, let's take a look at another example. Look into this workflow action (post function):

#### **test.sil**

```text
 if(customfield_10000 < currentDate() && customfield_10001 > currentDate()) {
	assignee = customfield_10002;
 }
```

From the code above, it is quite clear that customfield\_10000 and customfield\_10001 are dates; customfield\_10002 is a user picker. But their meaning is unknown. However, if we define the following aliases:

#### **sil.aliases**

```text
 initialDate=customfield_10000
 finalDate=customfield_10001
 contact=customfield_10002
```

Then we use them in our SIL™ program.

#### **test.sil**

```text
 if(initialDate < currentDate() && finalDate > currentDate()) {
 	assignee = contact;
 }
```