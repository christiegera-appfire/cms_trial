# Printing Output

There are several functions which print output. Each one prints to a different place in Jira. This article details each.

## Printing to the SIL Manager Console or SIL Runner Gadget

- runnerLog()

**Sample Code**

|  |
| --- |
| ```text runnerLog("TEST"); ``` |

Example output from the SIL Manager:

![Power Scripts for Jira Cloud queued tasks interface](/cms_trial/assets/472a28dd-04e5-4e60-8ffd-0600d3096e6e.png)

Example output from the SIL Runner Gadget:

![Power Scripts for Jira Cloud scheduled job templates panel](/cms_trial/assets/5a4d7163-8b8d-4c07-b835-9d5ed6b6a0fd.png)

The SIL Engine ignores the runnerLog() function when script are run from other methods other than the SIL Manager.

## Printing to the Jira System Logs

- print()
- printLog()

**Sample Code**

|  |
| --- |
| ```text print("TEST"); logPrint("INFO", "TEST"); ``` |

Example output:

**Example Output**

|  |
| --- |
| ```text 2020-08-13 02:01:23,619-0600 pool-387-thread-1 INFO admin 765x13039x1 1jpmc0 0:0:0:0:0:0:0:1 /rest/keplerrominfo/refapp/latest/async-script/runScriptFromEditor [c.k.s.lang.functions.LogPrintFunction] TEST ``` |

## Printing to a file on the host system

- printInFile()

  **Printing to the silprograms folder**

  ```text
  printInFile("debug.txt", "Sample Output");
  ```

  **Printing to the silprograms folder**

  ```text
  printInFile("path/to/file/debug.txt", "Sample Output");
  ```

  **Printing to a system file**

  ```text
  printInFile("/path/to/system/file/debug.txt", "Sample Output");
  ```

  **Printing to a system file - Windows**

  ```text
  printInFile("C:/path/to/system/file/debug.txt", "Sample Output");
  ```

Remember to click on the Refresh button!

Whenever changes are made outside the SIL Manager window, click on the "Refresh" button to view the changes.

## Additional Help

Need help implementing this script? Talk to me directly to me by clicking on the bot on this page.