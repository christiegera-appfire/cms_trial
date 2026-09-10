# Set

## Description

Use the Set sub-function with the Create a Linked Issue post function to set the value of a selected field on the new issue. You can add any number of Set configurations.

## Configuration

![contentId-12518116](/cms_trial/assets/ac63d3af-f380-4520-8696-731c6916c231.png)

Select **Add** **Configuration** to add more field settings.

### Field value

Make sure that the value you enter is valid for the datatype of the selected field. Also verify, that the context configuration for the project using this workflow will allow for modifying the selected field. Typically you will use text, dates, or numbers as values. User fields should be set to the account ID.

### Issue field

Select the field you want to update.

### Overwrite / append / prepend

For text fields and other fields that can accept multiple values (like checkboxes), you can choose to overwrite, append, or prepend the new value to any existing value. For a text field, you can also choose a separator to place between the values (not shown in the screenshot above).

### Create version if necessary

Imagine your origin issue has a version you want to copy to the linked issue. If the destination field is 'Fix Version/s', 'Affects Version/s', or some custom field of type 'Version Picker', you can define that a new version will be created in the target project if it does not exist. If you don't choose this option and that version does not exist, the user receives an error message and the transition completes.

A user needs the Administer Projects permission to be able to create a new version.

### Create component if necessary

Imagine your origin issue has a component you want to copy to the linked issue. If the destination field is *Components*, you define that a new component is created in the target project, if it does not yet exist. If you don't choose this option and that component does not yet exist, the user receives an error message and the transition completes.

A user needs the Administer Projects permission to create a new component.

### Special sources

- `*** empty ***`:  The destination field will be cleared.
- `*** last comment ***`**:**The last comment from the source issue will be copied. In some cases, that might be the comment from the transition screen, which the user just entered while performing the current transition.

### Special destinations

- `*** new comment ***`: A new comment will be created with the copied value. When you choose to overwrite to new comment, a new comment is created, enabling you to add multiple comments in one post function.  
  **Examples**:  
  `Copy Description to New Comment, overwrite`**→** creates a new comment with the description.  
  `Copy Summary to New Comment, append with separator ", "` **→** appends the summary to the previously created comment, so the comment will look like <Description>, <Summary>.  
  `Copy Assignee to New Comment, overwrite` → creates a new comment.  
  This configuration will result in two comments being created: one with the description and summary, and one with the assignee.