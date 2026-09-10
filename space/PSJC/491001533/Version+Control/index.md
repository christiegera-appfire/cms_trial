# Version Control

Making backups and carefully creating a repository that maintains version control is a good thing. This Knowledge Base article will show you how to set that up.

## Git Repository

Because SIL code is stored in text files, it is totally possible to create a git repository directly in the silprograms folder. Once the repository has been set up, use the SIL code below to make commits from the SIL Gadget Runner. See this [Atlassian documentation on creating a git repository](https://support.atlassian.com/bitbucket-cloud/docs/create-a-git-repository/).

|  |
| --- |
| ```text persistent string gitPath;   string baseCommand = "git --git-dir=\"" + gitPath + "\\.git\" --work-tree=\"" + gitPath + "\" ";   string [] folders = gadget_getMultiValues(argv, "Folders"); string [] files = gadget_getMultiValues(argv, "Files"); string commitMessage = arrayGetElement(argv, "Commit Message");   for(string f in folders) {     string command = baseCommand + "add --all \"" + gitPath + "\\" + f + "\"";     runnerLog("Running git command: " + command);     runnerLog(system(command));  }   for(string f in files) {     string command = baseCommand + "add \"" + gitPath + "\\" + f + "\"";     runnerLog("Running git command: " + command);     runnerLog(system(command));  }   string command = baseCommand + "commit -a -m \"" + commitMessage + "\""; runnerLog("Running git command: " + command); runnerLog(system(command)); command = (baseCommand + "push origin \nusername: jmuse \n "); runnerLog("Running git command: " + command); runnerLog(system(command)); Params Script:   persistent string gitPath = "C:\\Program Files\\Atlassian\\Application Data\\JIRA_versions\\silprograms";   function getFiles(string dir) {           string [] dirs = findDirectories(dir, ".*");     string [] silFiles;     string [] files;           for(string dir in dirs) {         if(contains(dir, ".git") == false) {             silFiles += findFiles(dir, ".*");         }     }           silFiles = arraySort(silFiles, false);           for(string b in silFiles) {         string temp = replace(b, dir, "");         temp = replace(temp, "/", "");         temp = substring(temp, 1, length(temp));         files += temp;     }           return arraySort(files, false); }   function getFolders(string dir) {           string [] folders = findDirectories(dir, ".*");     string [] subFolders;     string [] folderNames;           for(string f in folders) {         if(contains(f, ".git") == false) {             folderNames += substring(replace(f, dir, ""), 1, length(dir));             string [] subfold = findDirectories(f, ".*");             for(string sf in subfold) {                 folderNames += substring(replace(sf, dir, ""), 1, length(dir));             }                       }     }           folderNames += folderNames;     return arraySort(arrayToSet(folderNames), false); } ``` |

Code for SIL Runner Gadget

|  |
| --- |
| ```text gadget_createMultiSelectList("Folders", getFolders(gitPath), "", false, ""); gadget_createMultiSelectList("Files", getFiles(gitPath), "", false, ""); gadget_createTextArea("Commit Message", "", 10, true, ""); ``` |

[unmapped inline: placeholder]