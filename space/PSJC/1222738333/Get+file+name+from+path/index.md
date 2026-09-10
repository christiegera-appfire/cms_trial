# Get file name from path

Function to get the file name from a full file path.

```text
function getFileName(string filePath) {
    int start = lastIndexOf(filePath, "\\");
    string fileName = trim(substring(filePath, start+1, length(filePath)));
    return fileName;
}
```