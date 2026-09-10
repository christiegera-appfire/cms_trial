# Export custom fields

Export a CSV formatted list of all custom field names and IDs.

```text
string csv = "Name,ID\n";
runnerLog("Name, ID");

for(JCustomField cf in getAllCustomFields()) {
    string temp = cf.name + "," + cf.id;
    runnerLog(temp);
    csv += temp + "\n";
}

printInFile("customFieldList.csv", csv);
```