# Menu and toolbar items

This section explains the menu options and toolbar buttons available in the SIL Manager.

## The main menu bar

This section contains the main navigation menus that provide access to file management, editing functions, code insertion, snippets, and display options.

![Power Scripts for Jira Cloud outgoing mail configuration interface](/cms_trial/assets/9f2453b9-d672-4de0-a1b1-34bc2e080021.png)

|  | **Menu name** | **Menu options** |
| --- | --- | --- |
| number 1a.png | **File** | This menu provides basic file management and editor configuration options:   - **New file**: Creates a new blank file in the editor. - **New folder**: Creates a new folder in the file tree for organizing your scripts. - **New file from snippet**: Creates a new file using a predefined code snippet or template. - **Save**: Saves the currently open file. - **Settings**: Opens the SIL Manager configuration options, including:    - **Theme**: Choose editor appearance.   - **File type handling**: Set default behavior for files with no extension or unknown extensions.   - **Font size**: Adjust editor text size.   - **Placeholder text**: Customize the default "Code goes here..." text in new files.   - **Autocomplete settings**: Enable/disable autocomplete features and live autocomplete suggestions.   - **Editor display options**: Toggle various visual elements.   - **Code formatting**: Configure tab behavior and tab size.   For detailed information, see the [SIL Manager settings](/cms_trial/space/PSJC/490997655/SIL+Manager+settings/) page. |
| number2a.png | **Edit** | This menu provides standard text editing functions for working with your scripts:   - **Search**: Find text within the current file. - **Search and Replace**: Find and replace text throughout the file. - **Go to**: Jump directly to a specific line number. |
| number3a.png | **Insert** | This menu provides quick access to common SIL programming constructs, helping you insert properly formatted code templates without having to write the syntax from scratch.   - **FOR loop objects**: Inserts a `FOR` loop template for iterating over objects. - **FOR loop with index**: Inserts a `FOR` loop template that includes an index counter. - **IF - ELSE**: Inserts an `IF-ELSE` conditional statement template. - **WHILE**: Inserts a `WHILE` loop template. - **DO WHILE**: Inserts a `DO-WHILE` loop template. |
| number4a.png | **Snippets** | This menu provides access to pre-written code templates organized by category. These functional snippets help you quickly insert common Jira automation tasks without writing code from scratch.  For complete documentation, see: [Script Snippets](/cms_trial/space/PSJC/723320834/Script+Snippets/). |
| number5a.png | **Window** | This menu controls the SIL Manager’s display option.   - **Toggle Full Screen**: Expands the SIL Manager to use the entire browser window for maximum workspace. - **Split Screen**: Lets you view multiple files side by side (coming soon). |
| number6a.png | **Run** | This menu provides controls for executing and testing your scripts:   - **Run Configuration**: By default, scripts execute in the global context without any specific issue data. Use this option to set a specific Jira issue context for testing your script with real data. - **Check**: Validates the syntax of your script without executing it. Use this to catch errors before running. - **Run**: Executes the current script. Results appear in the console tab at the bottom of the screen. - **Debug**: Opens the Script Debugger (Beta) for step-by-step debugging of your scripts.   For complete documentation, see: [Script Debugger (Beta)](/cms_trial/space/PSJC/516653057/Script+Debugger+(Beta)/). |

## The toolbar

The toolbar contains action buttons that become available when you open a file, providing quick access to common development tasks.

![Power Scripts for Jira Cloud SIL Runner gadget parameters](/cms_trial/assets/5e021c33-685a-49e3-89f0-7752f16b85bb.png)

|  | **Action name** | **Description** |
| --- | --- | --- |
| number 1a.png | **Save** | Saves your script changes to storage. |
| number2a.png | **Check** | Performs syntax validation on the current script. |
| number3a.png | **Run** | Executes the script with your current run configuration. |
| number4a.png | **Debug** | Opens the Script Debugger (Beta) for step-by-step debugging of your scripts.  For complete documentation, see: [Script Debugger (Beta)](/cms_trial/space/PSJC/516653057/Script+Debugger+(Beta)/). |
| number5a.png | **Find usages** | Searches for references to selected text across all script files. Highlight any text in your script and click this button to find where it's used elsewhere in your codebase. |