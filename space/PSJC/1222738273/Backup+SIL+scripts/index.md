# Backup SIL scripts

A utility that will archive and compress the all the files in the main silprograms directory into a tar file.

```text
/**
* Creates a backup tar file of the silprograms directory.
* The tar file is then attached to a newly created Jira ticket to allow for download.
* @author Tim Reiking
* @date   2019/04/22
*/

string projectKey = "TRASH";        // The Jira project to create a new ticket
string type = "Task";               // Ticket type to create
string prefix = argv[0];            // Prefix the saved file name
string issueKey = argv[1];          // Generated Jira issue that contains backup

function backup(string env) {
    string fileName = prefix+replace(env, ".", "")+"DirBackup.tar.gz";
    string path = silEnv(env);
    string filePath = path+"/../"+fileName;
    //string command = "cd "+path+" && tar -czf "+filePath+" "+path;
    string command = "tar -czf "+filePath+" "+path;
     
    runnerLog(command);
    runnerLog("-------------");
    runnerLog(system(command));
     
    if(fileExists(filePath)) {
        if(isNull(issueKey)) { issueKey = createIssue(projectKey, "", type, "Created "+env+" backup"); }
        attachFile(filePath, issueKey);
        deleteFile(filePath);
    }
}
prefix = isNull(prefix) ? "" : prefix;
string cleanPath = silEnv("sil.home")+"/~";
if(directoryExists(cleanPath)) { system("rm -R "+cleanPath); }

backup("sil.home");
backup("kepler.home");

return issueKey;
```