# The Screen script

The Screen script lets you to determine if an action requires additional input and to build a dynamic form where the user can fill in the necessary data.

## Input types

The Forms and Wizards feature offers various field types designed to collect different kinds of data. Below is a structured table organizing these input types by their core functionality.

| **Category** | **Input Type** | **Description** |
| --- | --- | --- |
| **Content fields** | HTML content | Rich formatted content with HTML support |
| **Single value fields** | Text | Short text entry |
|  | Text area | Multi-line text entry |
|  | Single checkbox | Yes/No or True/False selection |
|  | Date picker | Calendar-based date selection |
|  | Date time [icker | Date with time selection |
|  | User picker | Select a single user from directory |
| **Multiple value Fields** | File upload | Upload one or more files |
| **Option selection - single** | Select list | Dropdown menu with single selection |
|  | Radio group | Visual selection of one option from a group |
| **Option selection - multiple** | Multi select list | Dropdown allowing multiple selections |
|  | Checkbox group | Visual selection of multiple options from a group |

## How to create a screen

Input fields are created using a specialized script library with dedicated functions for each field type. See [The input type functions](/cms_trial/space/PSJC/1839235499/The+input+type+functions/) page for detailed documentation on each input creation function.

## Screen customization functions

Beyond adding input controls, Forms and Wizards offers additional functions to control how your screen is displayed. These specialized functions allow you to customize key elements of the user interface.

- To customize the screen title that appears at the top of your screen, use [BA\_setActionTitle](/cms_trial/space/PSJC/1839235434/BA_setActionTitle/).
- To change the text displayed on the submit button (default is *Execute*), use [BA\_setExecuteButtonText](/cms_trial/space/PSJC/1839235467/BA_setExecuteButtonText/).

## Input fields example script

This script demonstrates all available input field types in Forms and Wizards, organized by category, with consistent configuration options. The script:

- Creates common variables for field configuration.
- Implements all input field types with appropriate parameters.
- Customizes the screen title and execute button text.

```text
// Common configuration variables
boolean isDisabled = false;     // Controls whether fields are interactive or read-only
boolean isRequired = true;      // Makes fields mandatory for form submission
string badesc = "This is a description";  // Default help text for all fields

//--- Content Fields ---//
BA_createHtmlContent("<h1>HTML Title Text</h1>");  // Displays formatted HTML content

//--- Single Value Fields ---//
BA_createInput("input", "asdf", isDisabled, isRequired, badesc);  // Simple text input with default value "asdf"
BA_createTextArea("ta", "some text", isDisabled, 3, isRequired, badesc);  // Multi-line text area with 3 rows
BA_createSingleCheckbox("cbx", true, isDisabled, isRequired, badesc);  // Checkbox pre-checked (true)
date d = currentDate();  // Gets current date for date pickers
BA_createDatePicker("date", d, isDisabled, isRequired, badesc);  // Date selection field
BA_createDateTimePicker("datetime", d, isDisabled, isRequired, badesc);  // Date and time selection field
BA_createUserPicker("userpicker", "admin", isDisabled, isRequired, badesc);  // User selection with default "admin"

//--- Multiple Value Fields ---//
BA_createFileUpload("File Upload", isDisabled, isRequired, badesc);  // Allows uploading one or more files

//--- Option Selection - Single Value ---//
BA_createSelectList("Select List", {"a", "b"}, "a", isDisabled, isRequired, badesc);  // Dropdown with options "a" and "b", "a" selected
BA_createRadioGroup("Radio Group", {"a", "b"}, "a", isDisabled, isRequired, badesc);  // Radio buttons with same options

//--- Option Selection - Multiple Values ---//
BA_createMultiSelectList("Multi Select List", {"a", "b", "c"}, {"a", "b"}, isDisabled, isRequired, badesc);  // Dropdown allowing multiple selections
BA_createCheckboxGroup("Checkbox Group", {"a", "b", "c"}, {"a", "b"}, isDisabled, isRequired, badesc);  // Multiple checkboxes

//--- Screen Customization ---//
BA_setActionTitle("Multiple options, multiple selectable values");  // Sets the screen title
BA_setExecuteButtonText("Example");  // Changes the submit button text from "Execute" to "Example"
```