# Unselect an option in a multi-select field using JMWE post-function

This article provides the code snippet to unselect an option in a multi-select field using [Set issue fields](/cms_trial/space/JMWEC/465504849/Set+issue+fields/) post-function.

## \uD83D\uDCD8 Instructions

1. Navigate to the intended workflow to make the necessary changes in the edit mode.
2. Select the required transition.
3. Select the *Post functions* tab and click `Add post function`.
4. Add the [Set issue fields](/cms_trial/space/JMWEC/465504849/Set+issue+fields/) post-function.
5. Select the issues, for which the field should be set, under “Target Issue(s)”.
6. Select the desired field and add the below Nunjucks template:

   ```java
   {{ issue.fields.customfield_10067 | filter(["value","Item 3"],true) | join(',',"value") }}
   ```

Replace `10067` with the id of the desired field and `Item 3` with the option to be removed.

With this, the option “Item 3” will be removed from the selected options (if it exists).

![JMWE for Jira Cloud multiselect field configuration for option deselection](/cms_trial/assets/cf232a94-8ee1-4fd3-b213-a8225336dd69.png)

If this post-function is added on the create transition, select the checkbox *“Delay the execution of this post-function”* under *“Delayed execution”* and select a delay of 3 seconds.

### References

- [filter](/wiki/spaces/JMWEC/pages/78482118/Custom+Filters#filter)
- [join filter](/cms_trial/space/JMWEC/465373240/Nunjucks+Filters/)