# Import directory from BitBucket

A utility that will download files from a Bitbucket repository.

```text
/**
* Downloads files from a Bitbucket repository into a local silprograms directory
* @author Tim Reiking
* @date   2019/8/20
*/

// silprograms Info
string directory = "";                                                  // Folder or file to download from repository
string path = silEnv("sil.home")+"/"+directory;                         // Location to put the downloaded file or folder

// Bitbucket Info
string bitbucketURL = "https://bitbucket.cprime.io/";                   // Base Bitbucket URL
string repoURL = "projects/CIA/repos/cprimejirasil/raw/silprograms/";   // Bitbucket path of the head directory
string branch = "";                                                     // Bitbucket branch to pull info

// Bitbucket Credentials
string user = "";                                                       // Bitbucket username used to pull
string pass = "";                                                       // Bitbucket password used to pull

/**
* Recursively downloads a file from URL
* @param urlBase - The url containing the required files
* @param request - HTTP information used to pull files
* @param downloadDir - The destination for new files
* @return 'true' if download successful, otherwise 'false'
*/
function getFiles(string urlBase, HttpRequest request, string downloadDir) {
    string values = httpGet(urlBase+branch, request);
    number statusCode = httpGetStatusCode();
    if (statusCode < 200 || statusCode >= 300 || endsWith(urlBase, "//")) {
        return false;
    }
 
    string[] fileList = split(values, "\n");
    for(string f in fileList) {
        string[] breakUp = split(f, "\t");
        string fileName = breakUp[1];
 
        string p = downloadDir+"/"+fileName;
        runnerLog(p);
        if(contains(fileName, ".")) {
            if(fileExists(p)) {
                deleteFile(p);
            }
            createFile(p);
            values = httpGet(urlBase+"/"+replace(fileName, " ", "%20")+branch, request);
            printInFile(p, trim(values));
        } else {
            createDirectory(p);
            if(!getFiles(urlBase+"/"+fileName, request, p)) {
                return false;
            }
        }
    }
    return true;
}


branch = branch != "" ? "?at="+branch : "";
HttpRequest request;
HttpHeader authHeader = httpBasicAuthHeader(user, pass);
request.headers += authHeader;

getFiles(bitbucketURL+repoURL+directory, request, path);
```