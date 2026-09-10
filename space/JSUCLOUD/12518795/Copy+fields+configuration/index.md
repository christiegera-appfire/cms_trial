# Copy fields configuration

In some post functions, you can copy the value of a source field to a destination field. You can configure these fields in the Copy Value From Other Field post function and with the optional operations of the Create a Linked Issue and the Linked Transition post functions.

Although the source and destination fields can be different data type, not all conversions from source to destination field are supported nor feasible.

### Overwrite / append / prepend

For text fields and other fields that can accept multiple values (like checkboxes), you can overwrite, append, or prepend the new value to any existing value. For a text field, you can also choose a separator between the values.

### Create version if necessary

Imagine your origin issue has a version that you want to copy to the linked issue. If the destination field is *Fix Version/s*, *Affects Version/s,* or some custom field of type version picker, you can define that a new version will be created in the target project if it does not yet exist. If you don't choose this option and that version does not exist, the user receives an error message and the transition completes.

A user needs the Administer Projects permission to to create a new version.

### Create component if necessary

Imagine your origin issue has a component that you want to copy to the linked issue. If the destination field is *Components*, you define that a new component is created in the target project, if it does not yet exist. If you don't choose this option and that component doesn't exist, the user receives an error message, and the transition completes.

A user needs the Administer Projects permission to create a new component.

### Special sources

In addition to fields, you can select from the following special sources to copy to a destination issue. For example, you can copy the value of the previous user to the *Assignee* field of a new issue.

- `*** empty ***`: The destination field will be cleared.
- `*** last comment ***`**:**The last comment from the source issue will be copied. In some cases, that might be the comment from the transition screen, which the user just entered while performing the current transition.
- `*** transition comment ***`: The comment that the user entered on the transition screen will be copied to the destination field.
- `*** all comments ***`: All comments from the source issue will be copied to the destination field. This option is available only in the Create Linked Issue post function. If you use the **Copy as original author option**, the author must have comment permissions for the newly created issue.   
  `*** current user ***`: The user who triggered the post function will be copied to the destination field.
- `*** previous user ***`: The field is updated with the previous user assigned to the destination field. This is valid for single-user picker fields.
- `*** current datetime ***`: The current date and time will be copied to the destination field.

### Special destinations

- `*** new comment ***`: A new comment will be created with the copied value. When you choose to overwrite to new comment, a new comment is created, enabling you to add multiple comments in one post function.  
  **Examples**  
  `Copy Description to New Comment, overwrite`→ creates a new comment with the description.  
  `Copy Summary to New Comment, append with separator ", "` → appends the summary to the previously created comment, so the comment will look like <Description>, <Summary>.  
  `Copy Assignee to New Comment, overwrite` → creates a new comment.  
  This configuration will result in two comments being created: one with the description and summary, and one with the assignee.
- `*** new internal note ***`: Create a new internal note with the value from the source field (Jira Service Management only).

A **new internal note** is created only for Jira Service Management (JSM) project issues. For non-JSM projects, a regular comment is created with the value from the source field.