# File Manipulation Functions

This section contains functions that enable users to handle directories and files.

Starting with **SIL Engine 5.8.0.0** we limit the directories you have access to. By default you will have unrestricted access to the following directories:

- sil.home (usually set on *silprograms*)
- kepler.home (usually set on *kepler*)
- <JIRA\_HOME>/tmp
- <JIRA\_HOME>/log
- <JIRA\_HOME>/export
- <JIRA\_HOME>/import
- <JIRA\_HOME>/data
- The directory announced by `java.io.tmpdir`variable
- The user home directory, if the user under which Jira runs has a home directory

Extra directories may be specified defining `sil.allowed.dirs` property. The Java process must be launched with `-Dsil.allowed.dirs=<path1>:<path2>` ('nix systems) or `-Dsil.allowed.dirs=<path1>;<path2>` (Windows). Attempting to access files outside designated directories will result in error.

## Functions summary

- [createDirectory](/cms_trial/space/PSJC/434962712/createDirectory/)
- [createFile](/cms_trial/space/PSJC/434799160/createFile/)
- [deleteDirectory](/cms_trial/space/PSJC/1293550706/deleteDirectory/)
- [deleteFile](/cms_trial/space/PSJC/435028345/deleteFile/)
- [directoryExists](/cms_trial/space/PSJC/435028361/directoryExists/)
- [fileClose](/cms_trial/space/PSJC/434507093/fileClose/)
- [fileContains](/cms_trial/space/PSJC/434602700/fileContains/)
- [fileCopy](/cms_trial/space/PSJC/434733426/fileCopy/)
- [fileExists](/cms_trial/space/PSJC/434930064/fileExists/)
- [fileInfo](/cms_trial/space/PSJC/434733442/fileInfo/)
- [fileMove](/cms_trial/space/PSJC/434635496/fileMove/)
- [fileOpen](/cms_trial/space/PSJC/434602716/fileOpen/)
- [fileRead](/cms_trial/space/PSJC/434374272/fileRead/)
- [fileReadByte](/cms_trial/space/PSJC/434374288/fileReadByte/)
- [fileReadLine](/cms_trial/space/PSJC/433654422/fileReadLine/)
- [fileSeek](/cms_trial/space/PSJC/434472643/fileSeek/)
- [fileSHA256Checksum](/cms_trial/space/PSJC/434864385/fileSHA256Checksum/)
- [fileSize](/cms_trial/space/PSJC/434962736/fileSize/)
- [fileTruncate](/cms_trial/space/PSJC/513900554/fileTruncate/)
- [fileWrite](/cms_trial/space/PSJC/434864401/fileWrite/)
- [findDirectories](/cms_trial/space/PSJC/434962752/findDirectories/)
- [findFiles](/cms_trial/space/PSJC/433654440/findFiles/)
- [printInFile](/cms_trial/space/PSJC/434995405/printInFile/)
- [readFromBinaryFile](/cms_trial/space/PSJC/434507159/readFromBinaryFile/)
- [readFromCSVFile](/cms_trial/space/PSJC/434831805/readFromCSVFile/)
- [readFromTextFile](/cms_trial/space/PSJC/434766059/readFromTextFile/)
- [renameFile](/cms_trial/space/PSJC/433654462/renameFile/)
- [writeToBinaryFile](/cms_trial/space/PSJC/434602733/writeToBinaryFile/)
- [zipFiles](/cms_trial/space/PSJC/434733459/zipFiles/)