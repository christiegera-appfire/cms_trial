# Remove a SIL directory

Remove a directory and recursively delete the files within.

Note: this script uses PowerShell based commands. If running on a Linux operating system the compatible PowerShell package will need to be installed.

```text
/**
* Deletes a directory within silprograms and all the containing files.
* @author Tim Reiking
* @date   2020/4/10
*/

string dirName = ""; // Name of the directory

// Determine if the directory contains the silprograms path
if(!startsWith(dirName, silEnv("sil.home"))) { dirName = silEnv("sil.home")+"/"+dirName; }

// Deletes the directory recursively
if(directoryExists(dirName)) { 
    runnerLog("Deleting... "+dirName);
    if(system("rm -R "+dirName)[0] == "-1.0") {
      system("powershell -command \"Remove-Item '"+dirName+"' -Recurse -Force\"");
    }
} else {
    runnerLog("Cannot find "+dirName);
}
```