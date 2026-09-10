# File tree

The file tree on the left side of the SIL Manager displays your scripts and folders in an organized hierarchy. Files are organized in folders and show their type with icons:

![Power Scripts for Jira Cloud file types icon display](/cms_trial/assets/25bfca41-39b7-4f9c-90b7-8d688458fb72.png)

SIL script files must use the `.sil` extension to be recognized and executed properly by the system.

You can navigate, search, and manage your files directly from this panel.

| **To…** | **Do this** |
| --- | --- |
| Open a file in the editor | Double-click any file in the tree. |
| Search for a file in a folder | Select the folder and use the search box to quickly find files by name. The search looks through the selected folder and all its nested subfolders, making it easy to locate files in large directory structures. |
| Open the context menus for a folder | Right-click on any folder to access available actions: Power Scripts for Jira Cloud file menu options  - **Refresh**: Updates the view to show new files added to the folder outside of the SIL Manager. - **Rename**: Changes the folder name. - **Delete**: Removes the folder.   Only empty folders can be deleted. Remove all files and subfolders before attempting to delete a folder.   - **New**: Creates new files or subfolders within the selected folder. - **Download**: Downloads the folder and its contents. - **Upload file**: Uploads a file to the selected folder. |
| Open the context menus for a file | Right-click on any folder to access available actions: Power Scripts for Jira Cloud file context menu interface  - **Rename**: Changes the filename. - **Delete**: Removes the file. - **Storage Type**: Select where the file is stored.    - **Disk**: File stored on the file system.   - **Database**: File stored in the database.   Changing a file's storage type will automatically migrate the file to the new location. For bulk migrations, a [bulk storage change utility](/cms_trial/space/PSJC/490996090/Script+Storage+configuration/) is available to transfer all SIL scripts between storage locations at once. Note that this utility affects only SIL scripts, not supplementary files (HTML, JavaScript, CSV, text files).   - **Find usages**: Searches for references to this file across all scripts and configurations.   This option is particularly useful for understanding dependencies before deleting or renaming a file. It helps you avoid breaking existing workflows or scripts that depend on it.   - **Download**: Downloads the file. |

The **Delete** and **Rename** actions are performed without checking for existing usage. If your script is already used in workflows, post-functions, or other automations, deleting or renaming it will break those implementations. Always verify usage before performing these operations.