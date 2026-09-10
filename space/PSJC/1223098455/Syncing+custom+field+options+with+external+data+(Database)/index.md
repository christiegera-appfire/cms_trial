# Syncing custom field options with external data (Database)

## Problem

Often the single source of truth for information does not lay in Jira. Many people resolve themselves to syncing this data manually which is time consuming and error prone.

## Solution

Using data from an external database we can create a script that syncs the data with options available in a custom field.

Configuration

The first step to achieving this is establishing the connection with the database. This is done in the configuration and the connection is given a unique name that is called within the script. See [configuring data sources](/cms_trial/space/PSJC/490996148/SQL+Datasource+configuration/) for more information.

## Full Scripts

#### **syncOptions.sil**

```javascript
struct _externalOptions {
    int id;
    string value;
}

/*------------------------------------------------------------------------------
Get options from external database
------------------------------------------------------------------------------*/

_externalOptions[] exOptions;
exOptions = sql("myDatabase", "SELECT id, value FROM myTable");

/*------------------------------------------------------------------------------
Get the curren list of options from the custom field and compare with new data
------------------------------------------------------------------------------*/

//prepare external data for comparison
string[] exLazyCheck;
for(_externalOptions ex in exOptions) {
    exLazyCheck[ex.value] = ex.value;
}

//get and prepare internal data for comparison
JCustomFieldOption[] customFieldOptions = admGetCustomFieldOptions("My Select List", {});
JCustomFieldOption[] customFieldOptionsMapped;
for(JCustomFieldOption option in customFieldOptions) {
    customFieldOptionsMapped[option.value] = option;
}

string[] intLazyCheck;
for(JCustomFieldOption option in customFieldOptions) {
    intLazyCheck[option.value] = option.value;
}

//compare the data
string[] newOptions = arrayDiff(exLazyCheck, intLazyCheck);
string[] oldOptions = arrayDiff(intLazyCheck, exLazyCheck);

/*------------------------------------------------------------------------------
Compare external options to see which options are new and need to be added
------------------------------------------------------------------------------*/

JCustomFieldOption[] addOptions;
for(string new in newOptions) {
    JCustomFieldOption option;
    option.value = new;
    option.disabled = false;
    
    addOptions += option;
}

//commit changes
admAddCustomFieldOptions("My Select List", addOptions);

/*------------------------------------------------------------------------------
Compare external options to see which options need to be removed
------------------------------------------------------------------------------*/

string[] removeOptions;
for(string old in oldOptions) {
    JCustomFieldOption option;
    option = customFieldOptionsMapped[old];
    
    removeOptions += option.id;
}

//commit changes
admDeleteCustomFieldOptions("My Select List", removeOptions, {});
```