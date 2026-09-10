# Managing aliases in the sil.aliases file

Creating aliases is a simple task of editing the 'sil.aliases' properties file in the Kepler Home directory. This file must contain pairs in the following form: alias=customfield\_id.   
For our example above, we should edit it and put an entry like this:

#### **sil.aliases**

```text
# custom fields aliases
reportedUser=customfield_10001
```

The **sil.aliases** file is NOT a SIL language file. It does not require a semi-colon and the end of each line. SIL syntax checker will not run for this file.

The **sil.aliases** file is located in the *kepler* directory inside of *<JIRA\_HOME>*. This directory can be accessed from the SIL Manager by changing the View to be **Kepler Home**

You can rewrite the script in another way and use alias instead of the custom field ID or name:

```text
if(isNotNull(reportedUser)) {
  assignee=reportedUser;
}
```

  Now the code looks clean and the script function creator is clear even without comments.

The SIL Manager interface also uses the sil.aliases file. Saving changes from the SIL Manager will cause the sil.aliases file to be overwritten.

**See More**