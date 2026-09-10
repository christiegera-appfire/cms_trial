# Export existing SIL aliases

Export a CSV formatted list of all existing SIL aliases

```text
struct _alias {
    string name;
    string id;
}

runnerLog("name,id");

string fileContent = readFromTextFile("../kepler/sil.aliases");
string [] fc = split(fileContent, "\r");

for(string a in fc) {
    if(!startsWith(a, "#")) {
        if(contains(a, "=")) {
            string line = replace(a, "\n", "");
            line = replace(line, "\r", "");
            
            _alias a = split(line, "=");
            runnerLog(a.name + "," + a.id);
        }
    }
}
```