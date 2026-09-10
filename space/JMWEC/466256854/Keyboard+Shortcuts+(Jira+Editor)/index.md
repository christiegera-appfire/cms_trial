# Keyboard Shortcuts (Jira Editor)

There are numerous keyboard shortcuts available when using the Jira expression editor. Refer to the table below for the full list.

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
| `goGroupLeft` | Move to the left of the [group](#) before the cursor. | `Ctrl-Left` | `Alt-Left` |
| `goGroupRight` | Move to the right of the [group](#) after the cursor. | `Ctrl-Right` | `Alt-Right` |
| `delCharBefore` | Delete the character before the cursor. | `Shift-Backspace` | `Ctrl-H` |
| `delCharAfter` | Delete the character after the cursor. | `Delete` | `Ctrl-D` |
| `delWordBefore` | Delete up to the start of the word before the cursor. |  | `Alt-Backspace` |
| `delWordAfter` | Delete up to the end of the word after the cursor. |  | `Alt-D` |
| `delGroupBefore` | Delete to the left of the [group](#) before the cursor. | `Ctrl-Backspace` | `Alt-Backspace` |
| `delGroupAfter` | Delete to the start of the [group](#) after the cursor. | `Ctrl-Delete` | `Ctrl-Alt-Backspace or Alt-Delete` |
| `indentAuto` | Auto-indent the current line or selection. | `Shift-Tab` | `Shift-Tab` |
| `indentMore` | Indent the current line or selection by one indent unit. | `Ctrl-]` | `Cmd-]` |
| `indentLess` | Dedent the current line or selection by one indent unit. | `Ctrl-[` | `Cmd-[` |
| `defaultTab` | If something is selected, indent it by one indent unit. If nothing is selected, insert a tab character. | `Tab` | `Tab` |
| `transposeChars` | Swap the characters before and after the cursor. |  | `Ctrl-T` |
| `newlineAndIndent` | Insert a newline and auto-indent the new line. | `Enter` | `Enter` |
| `toggleOverwrite` | Flip the overwrite flag. | `Insert` | `Insert` |

**Group**

A group is a stretch of word characters, a stretch of punctuation characters, a newline, or a stretch of *more than one* whitespace character.