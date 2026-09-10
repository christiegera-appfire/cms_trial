# The Action script

## Basic usage

The Action script contains instructions that will be executed when calling an action.

To learn more about SIL, see the [Simple Issue Language documentation](https://appfire.atlassian.net/wiki/spaces/PSJ/pages/15489652).

If the action requires certain input from the user via the [Screen Script](/cms_trial/space/PSJC/1839235307/The+Screen+script/), the values are placed in the **argv** variable. This is a string array containing the ordered sequences of label and value(s) for the fields shown on the screen.

When a user interacts with a screen created by the Screen script, their input is stored in the `argv` variable — a string array containing an ordered sequence of field labels and their corresponding values.

- For single-value fields, the array contains the field label followed by the value entered.
- For multi-value fields:

  - If no values are selected, the label is followed by an empty value.
  - If one or more values were selected, the label is followed by the number of values selected, then the selected values themselves.

To simplify accessing these values, Power Actions provides specialized helper functions:

| **Function** | **Used With** | **Description** | **Return Value** |
| --- | --- | --- | --- |
| `BA_getSingleValue(argv, label)` | Text fields, select lists, radio groups, text areas, single checkboxes | Retrieves a single value for the given label | String representing the entered/selected value (for checkboxes: "checked" if selected, empty string if not) |
| `BA_getMultiValues(argv, label)` | Multi-select lists, checkbox groups, file upload | Retrieves multiple values for the given label | String array of selected options (for file uploads: pairs of original filename and uploaded path) |
| `BA_isChecked(argv, label)` | Single checkbox | Provides a boolean check for checkbox state | Boolean: true if checked, false if not |
| `BA_getDateValue(argv, label)` | Date picker, date time picker | Retrieves date values (converts from user's time zone to server time zone) | Date value |

### Example

Consider this Screen script:

```text
BA_createCheckboxGroup("checkbox group", {"o1", "o2", "o3"}, {"o1", "o2"}, false);
```

If the user does not change the default values:

- The `argv` variable will contain: `"checkbox group", "2", "o1", "o2"`
- `BA_getMultiValues(argv, "checkbox group")` would return an array with two values: `o1` and `o2`

If the user unchecks all values:

- The `argv` variable would contain: `"checkbox group", ""` (empty string)

You can use these helper functions with array-specific functions like [arrayGetElement](https://appfire.atlassian.net/wiki/spaces/PSJ/pages/15488868) and [arrayElementExists](https://appfire.atlassian.net/wiki/spaces/PSJ/pages/15488771). For a list of available functions that manipulate arrays, see [Array Functions](https://appfire.atlassian.net/wiki/spaces/PSJ/pages/15488052).

## Validation and error handling

The Action script is responsible for validating user input and providing appropriate feedback. This validation ensures data quality and prevents processing invalid or incomplete information. Two types of errors can be returned: generic and field validation errors.

### Generic errors

Generic errors display at the top of the screen as a general message. These are useful for overall validation issues or when the error is not specific to a single input field.

To create a generic error that appears at the top of the screen, simply return a string from your Action Script:

```text
string fruit = getElement(argv, 1);

if(isNull(fruit)){
    return "What? You don't like fruits?";
}
```

In this example:

1. The script retrieves the value of the fruit field from the `argv` array (at position 1).
2. It checks if the fruit value is null or empty using the `isNull()` function.
3. If the user didn't select a fruit, it returns an error message as a string (see screenshot below).
4. This message will appear at the top of the screen as a general error notice.
5. The action execution will stop at this point and return to the screen.

![Power Scripts for Jira Cloud thread pool configuration interface](/cms_trial/assets/f8fbcf17-fcea-4e0c-8cf6-00477b523a9f.png)

### Field validation errors

Field validation errors display next to specific input fields on the screen, creating a better user experience by clearly indicating which fields need correction. This approach is particularly useful when validating multiple fields simultaneously.

To create field-specific error messages that appear next to their respective input fields, return an array containing pairs of values (field label and error message) from your Action Script:

```text
string fruitLabel = getElement(argv, 0);
string fruit = getElement(argv, 1);
string chocolateLabel = getElement(argv, 2);
string chocolate = getElement(argv, 3);

string[] errors;

if(isNull(fruit)){
    errors = addElement(errors, fruitLabel);
    errors = addElement(errors, "What? You don't like fruits?");
}

if(chocolate != "yes" && chocolate != "of course"){
    errors = addElement(errors, chocolateLabel);
    errors = addElement(errors, "No way!");
}

return errors;
```

In this example:

1. The script retrieves both the labels and values for two fields (fruit and chocolate).
2. It creates an empty array to hold potential errors.
3. For each validation check:

   - If the check fails, it adds the field's label to the array.
   - Immediately after the label, it adds the error message for that field.
4. The array is structured as pairs of values: `[field1_label, field1_error, field2_label, field2_error, ...]`
5. The script returns the complete array of errors.
6. Each error will appear next to its corresponding field on the screen (see screenshot below).
7. Multiple validation errors can be displayed simultaneously.

![Power Scripts for Jira Cloud time configuration settings](/cms_trial/assets/45b4ba46-0bd7-407f-af4f-0592b8af3941.png)

## Advanced return features

Power Actions supports redirecting to other pages and preventing automatic page refresh through a structured return object.

### Using BActionReturn

The `BActionReturn` structure provides advanced control options:

| **Field** | **Type** | **Purpose** |
| --- | --- | --- |
| `errors` | Array of BActionError | Field-specific or general error messages |
| `location` | String | URL to redirect to (leave empty to avoid redirection) |
| `disableRefresh` | Boolean | When true, it prevents automatic page refresh |

Each `BActionError` contains:

- `field`: String identifying the field (leave empty for general errors).
- `message`: String containing the error message.

Example usage:

```text
BActionReturn ret;

if(thereAreErrors()) {
    BActionError e;
    e.message = "There are errors!"; // global error
    ret.errors += e;
} else if(mustRedirect()) {
    ret.location = "https://google.com?q=SIL";
} else {
    ret.disableRefresh = true;
}

return ret;
```

In this example:

- The script creates a `BActionReturn` object and follows a simple decision path.
- If errors exist, it adds a global error message.
- If there are no errors but the redirection is needed, it sets the redirect URL.
- Otherwise, it prevents page refresh.
- The system then processes the return object accordingly.

While the previous error-handling approaches are still supported, using `BActionReturn` is recommended for new scripts as it provides more control over the post-action behavior.

## Practical example: working with uploaded files

When a user uploads files through a file upload field created with `BA_createFileUpload()`, you must process these files in your Action Script. The uploaded files are available as pairs of values (original filename and server path) in the `argv` array.

The following script demonstrates how to process each uploaded file:

```text
string[] files = BA_getMultiValues(argv, "file");
for(int i = 0; i < size(files); i += 2){
    number ORIGINAL_NAME = i;
    number NEW_PATH = i + 1;
    desc += "File " + files[ORIGINAL_NAME] + " was uploaded to " + files[NEW_PATH] + "\n";
}
```

In this example:

- The script retrieves file information using `BA_getMultiValues()`.
- The loop processes each filename/path pair by stepping through the array.
- It builds a description of all uploaded files for reporting or logging.