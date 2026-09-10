# Set approver in Jira Service Desk

Call this script from a workflow transition action to set the approver based on the value of a custom field.

Using a SIL alias is the best practice for accessing custom field data. In the script below, the SIL alias is represented by the keyword “fruit”. For more information, go to the [custom fields aliases documentation](/cms_trial/space/PSJC/496206057/Custom+fields+aliases/).

```text
if(fruit == "Apple") {
    customfield_10700 = "jmuse";
}
else if(fruit == "Orange") {
    customfield_10700 = "efoulkes";
}
else if(fruit == "Peach") {
    customfield_10700 = "jwang";
}
```