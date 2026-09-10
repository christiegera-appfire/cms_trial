# Parent issue status scripted field

## Problem

You would like to display the status of the issues parent in a custom field.

### Display comment text only

```text
if(isNotNull(parent)) {
    return parent.status;
}
```

Make sure that the “Child update” trigger is enabled in the [scripted field configuration](/cms_trial/space/PSJC/856361791/Scripted+Fields+Configuration/) to ensure that the scripted field on the child gets updated when the parent issue is updated.

Also, make sure that the issue type of the parent issue is added to the configuration so that scripted fields will be triggered when the parent is updated.