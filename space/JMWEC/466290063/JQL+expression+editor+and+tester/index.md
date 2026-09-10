# JQL expression editor and tester

This document describes the JQL expression editor and tester. It is available from the *Link issues to current issue* post-function only.

## **JQL expression editor**

#### **JQL expression features**

The JQL expression editor has the ability to:

- Check for syntax errors in the Nunjucks code
- Colorize keywords, comments, variables and so on

The editor also provides advanced features, such as find and replace, that are available through keyboard shortcuts.

#### **JQL expression editor keyboard shortcuts**

You can use the following shortcut keys as an alternative to the mouse when working in this editor, while the cursor is active in the editor:

| Command | Description | PC | Mac |
| --- | --- | --- | --- |
| `find` | Opens the search box. Use /re/ syntax for regexp search | `Ctrl-F` | `Cmd-F` |
| `findNext` | Post a search, finds the next occurrence of the search | `Ctrl-G` | `Cmd-G` |
| `findPrev` | Post a search, finds the previous occurrence of the search | `Shift-Ctrl-G` | `Shift-Cmd-G` |
| `replace` | Opens the *Replace* window. | `Shift-Ctrl-F` | `Cmd-Alt-F` |
| `replaceAll` | Opens the *Replace all* window | `Shift-Ctrl-R` | `Shift-Cmd-Alt-F` |
| `selectAll` | Select the whole content of the editor | `Ctrl-A` | `Cmd-A` |
| `singleSelection` | When multiple selections are present, this deselects all but the primary selection | `Esc` | `Esc` |
| `killLine` | Deletes the part of the line after the cursor. If that consists only of whitespace, the newline at the end of the line is also deleted. |  | `Ctrl-K` |
| `deleteLine` | Deletes the whole line under the cursor, including newline at the end. | `Ctrl-D` | `Cmd-D` |
| `delWrappedLineLeft` | Delete the part of the line from the left side of the visual line the cursor is on to the cursor. |  | `Cmd-Backspace` |
| `delWrappedLineRight` | Delete the part of the line from the cursor to the right side of the visual line the cursor is on. |  | `Cmd-Delete` |
| `undo` | Undo the last change | `Ctrl-Z` | `Cmd-Z` |
| `redo` | Redo the last undone change | `Ctrl-Y` | `Shift-Cmd-Z` or `Cmd-Y` |
| `undoSelection` | Undo the last change to the selection, or if there are no selection only changes at the top of the history, undo the last change. | `Ctrl-U` | `Cmd-U` |
| `redoSelection` | Redo the last change to the selection, or the last text change if no selection changes remain. | `Alt-U` | `Shift-Cmd-U` |
| `goDocStart` | Move the cursor to the start of the document. | `Ctrl-Home` | `Cmd-Up` or `Cmd-Home` |
| `goDocEnd` | Move the cursor to the end of the document. | `Ctrl-End` | `Cmd-End` or `Cmd-Down` |
| `goLineStart` | Move the cursor to the start of the line. | `Alt-Left` | `Ctrl-A` |
| `goLineStartSmart` | Move to the start of the text on the line, or if we are already there, to the actual start of the line (including whitespace). | `Home` | `Home` |
| `goLineEnd` | Move the cursor to the end of the line. | `Alt-Right` | `Ctrl-E` |
| `goLineRight` | Move the cursor to the right side of the visual line it is on. |  | `Cmd-Right` |
| `goLineLeft` | Move the cursor to the left side of the visual line it is on. If this line is wrapped, that may not be the start of the line. |  | `Cmd-Left` |
| `goLineUp` | Move the cursor up one line. | `Up` | `Ctrl-P` |
| `goLineDown` | Move down one line. | `Down` | `Ctrl-N` |
| `goPageUp` | Move the cursor up one screen and scroll up by the same distance. | `PageUp` | `Shift-Ctrl-V` |
| `goPageDown` | Move the cursor down one screen and scroll down by the same distance. | `PageDown` | `Ctrl-V` |
| `goCharLeft` | Move the cursor one character left, going to the previous line when hitting the start of the line. | `Left` | `Ctrl-B` |
| `goCharRight` | Move the cursor one character right, going to the next line when hitting the end of the line. | `Right` | `Ctrl-F` |
| `goWordLeft` | Move the cursor to the start of the previous word. |  | `Alt-B` |
| `goWordRight` | Move the cursor to the end of the next word. |  | `Alt-F` |
| `goGroupLeft` | Move to the left of the [group](https://appfire.atlassian.net/wiki/spaces/MWECS/pages/448235270/JQL+expression+editor+and+tester#grouDefinition) before the cursor. | `Ctrl-Left` | `Alt-Left` |
| `goGroupRight` | Move to the right of the [group](https://appfire.atlassian.net/wiki/spaces/MWECS/pages/448235270/JQL+expression+editor+and+tester#groupDefinition) after the cursor. | `Ctrl-Right` | `Alt-Right` |
| `delCharBefore` | Delete the character before the cursor. | `Shift-Backspace` | `Ctrl-H` |
| `delCharAfter` | Delete the character after the cursor. | `Delete` | `Ctrl-D` |
| `delWordBefore` | Delete up to the start of the word before the cursor. |  | `Alt-Backspace` |
| `delWordAfter` | Delete up to the end of the word after the cursor. |  | `Alt-D` |
| `delGroupBefore` | Delete to the left of the [group](https://appfire.atlassian.net/wiki/spaces/MWECS/pages/448235270/JQL+expression+editor+and+tester#groupDefinition) before the cursor. | `Ctrl-Backspace` | `Alt-Backspace` |
| `delGroupAfter` | Delete to the start of the [group](https://appfire.atlassian.net/wiki/spaces/MWECS/pages/448235270/JQL+expression+editor+and+tester#groupDefinition) after the cursor. | `Ctrl-Delete` | `Ctrl-Alt-Backspace or Alt-Delete` |
| `indentAuto` | Auto-indent the current line or selection. | `Shift-Tab` | `Shift-Tab` |
| `indentMore` | Indent the current line or selection by one indent unit. | `Ctrl-]` | `Cmd-]` |
| `indentLess` | Unindent the current line or selection by one indent unit. | `Ctrl-[` | `Cmd-[` |
| `defaultTab` | If something is selected, indent it by one indent unit. If nothing is selected, insert a tab character. | `Tab` | `Tab` |
| `transposeChars` | Swap the characters before and after the cursor. |  | `Ctrl-T` |
| `newlineAndIndent` | Insert a newline and auto-indent the new line. | `Enter` | `Enter` |
| `toggleOverwrite` | Flip the overwrite flag. | `Insert` | `Insert` |

#### Group

A group is a stretch of word characters, a stretch of punctuation characters, a newline, or a stretch of *more than one* whitespace character.

#### **Lookup user**

By 29 April 2019, Atlassian will remove personal data from the API that is used to identify users, such as `username` and `userKey`, and instead, use the Atlassian account ID (`accountId`). These are the impacts on JMWE:

- If the JQL in your existing "Link issue to current issue" post-functions are using the `username` or the `userkey` they need to be replaced with the `accountId`.
- If you are adding/modifying the JQL in the Link issues to current issue post-function you should not anymore specify the `username` or `userkey` but only the `accountId`. For example, JQL return the issues assigned to a specific user

However, the `accountId` is not obvious in Jira. You can use this **Lookup user** feature in the Nunjucks editor to find the `accountId` of a user. To know the `accountId` of a user:

1. Click on the **Lookup user** button
2. Select the user from `Search for user`
3. Click on **Insert accountId**

### **JQL expression tester**

The JQL expression tester lets you test your expression against any issue. You can quickly test and debug your expression and make changes without having to actually trigger the transition and/or look at the JMWE logs to see the result.

#### **Using the JQL expression tester**

After writing your JQL expression in the editor, click on `Test JQL expression.`A window opens, asking you to input an issue to run the JQL expression against. The [issue](/cms_trial/space/JMWEC/465503811/Using+Nunjucks+Templates/) variable used in your annotations will point to this issue.

The [transition](/cms_trial/space/JMWEC/465503811/Using+Nunjucks+Templates/) variable will not reflect transition information during testing.

#### Testing your JQL expression

After selecting an issue against which the JQL expression should be tested, click on `Test.`The following information will be displayed. This information can be used for debugging.

1. **Message**: Success/error message based on the test result.
2. **Parsed JQL query**: The parsed JQL query
3. **Issues:** The result of the JQL query which is an array of issues.

**Example:**

*Test a JQL expression that fetches issues in a project that are assigned to the current user.*

- Add the *Link issues to current issue* post-function to a transition.
- In the JQL editor, write the following lines of code:

  ```javascript
  project = TEST and assignee = {{currentUser.accountId}}
  ```
- Select maximum number of issues in `Max. Issues`.
- Click on `Test JQL expression`
- Type the Issue key of an issue.
- Click on `Test.`
- The following result is displayed:

  ![JMWE for Jira Cloud JQL expression editor showing query configuration options](/cms_trial/assets/2352cfa1-2b27-4a07-86e2-1abc4427012c.png)

#### **Debugging your JQL expression**

If you encounter an error during testing or your JQL expression doesn't seem to fetch expected results, you will need to debug your expression. The information displayed in the result panel aids in debugging the expression.

In the above example if you provided `"=="` instead of `"="`:

```javascript
project = TEST and reporter == {{currentUser.accountId}}
```

- **Test the JQL expression,** as explained above. The following result will be displayed.

  ![JMWE for Jira Cloud JQL testing interface with query validation](/cms_trial/assets/3a87b8df-94f5-4f41-bb95-e9fe7f6937c2.png)
- **Identify the problem**, from the `Message` that displayed an error that, there is an error in the JQL query
- **Correct the problem**, by modifying the expression

  ```javascript
  project = TEST and reporter = {{currentUser.accountId}}
  ```
- **Retest the expression,** by clicking on `Test again` and verify the result in the template test panel.

  ![JMWE for Jira Cloud JQL expression editor showing query configuration options](/cms_trial/assets/2352cfa1-2b27-4a07-86e2-1abc4427012c.png)