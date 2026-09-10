# Move a SIL directory

A utility that will move a directory of SIL scripts to another directory.

Note: this script uses Linux based commands that may need to be modified for other operating systems.

```text
/**
* Moves a file(s)/directory to a new location
* @author Tim Reiking
* @date   2020/4/8
*/

string dirName = "";                    // The destination directory within the main directory
string[] sources = "";                  // An array of files and directories to move

string path = silEnv("sil.home")+"/";   // Main directory
string dest = path+dirName;             // The full path
runnerLog(dest);

for(string source in sources) {
    source = path+source;
    
    runnerLog(source);
    if(directoryExists(dest) && (directoryExists(source) || fileExists(source))) {
        runnerLog("Moving...");
        system("mv "+source+" "+dest);
    }
}
```