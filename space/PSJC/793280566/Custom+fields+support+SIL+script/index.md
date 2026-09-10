# Custom fields support SIL script

Product Discovery hides some custom fields from Jira's standard interface, making them difficult to reference in scripts. This page explains how to use a diagnostic SIL script that discovers hidden custom fields in Product Discovery projects.

The script:

- Finds all custom field IDs in your Product Discovery projects.
- Automatically generates [SIL aliases](/cms_trial/space/PSJC/496206057/Custom+fields+aliases/) for the discovered fields.
- Creates aliases directly in your `sil.aliases` file.
- Displays manual alias code and links to documentation if automatic creation fails.

For additional details, see the [How the script works](/cms_trial/space/PSJC/793280566/Custom+fields+support+SIL+script/) section.

---

## How to run the script

This script works on any Jira Cloud instance without modifications.

1. Create a new file in the SIL Manager.
2. Copy the script code from the code section below.
3. Click **Run**.
4. Monitor progress in the console tab at the bottom.

### What to watch for when monitoring the script

|  |  |
| --- | --- |
| **Check your** `sil.aliases` **file after running the script.** | Occasionally, line breaks can be missing at the end of the file (usually from manual editing), causing new aliases to merge with existing ones incorrectly. When aliases get combined this way, they become malformed and won't work properly. Power Scripts for Jira Cloud SIL aliases file configuration |
| - **Review error messages** **in the console output.** | If the alias creation fails, the script displays the exact alias code to add manually and links to documentation for instructions. Power Scripts for Jira Cloud manual alias creation interface For manual alias creation instructions, see the [Managing aliases in the sil.aliases file](/cms_trial/space/PSJC/496206151/Managing+aliases+in+the+sil.aliases+file/) page. |
| **Check known limitations**. | Some behaviors and restrictions are documented in the [Other known limitations](/cms_trial/space/PSJC/797638671/Other+known+limitations/) page. |

### Script code

The code below is longer than most SIL scripts because it works on any Product Discovery configuration without modifications. Don't let the complexity discourage you; most SIL automation is much simpler than this diagnostic tool.

Click to expand the SIL script code

```text
struct _pdField {
    string name;
    string id;
    string alias;
}

function camelCase(string name) {
    string [] words = split(name, " ");
    string cc = toLower(words[0]);
    
    for(int x=1; x<size(words); x++) {
        string nextWord;
        for(int l=0; l<length(words[x]); l++) {
            if(l==0) {
                nextWord = toUpper(words[x][l]);
            } else {
                nextWord += words[x][l];
            }
        }
        cc += nextWord;
    }
    return cc;
}

_pdField [] allPDFields;
string dots = ".";
runnerLog("Starting dynamic search of Jira Product Discovery fields:", true);

for(string proj in allProjects()) {
    JProject p = projectObject(proj);
    
    if(p.projecttype == "product_discovery") {
        runnerLog(dots + " Scanning project <strong>" + proj + "</strong>", true);
        dots += ".";
        for(string issue in selectIssues("project = " + proj, 100)) {
            for(string af in arrayKeys(getIssueFields(issue, true))) {
                if(startsWith(af, "custom")) {
                    string name = getCustomFieldNameById(af);
                    allPDFields[name] = {name, af, camelCase(name)};
                }
            }
        }
    }
}

runnerLog("Dynamic scan complete, <strong style=\"color:blue;\">" + trim(size(allPDFields)) + "</strong> fields found in scan.", true);
runnerLog("<hr>", true);

//--new section--

runnerLog("");
runnerLog("Starting heuristic search of Jira Product Discovery fields:", true);

string [] knownFields = "Category|Customer segments|Documents|Goal|Idea archived|Idea archived on|Idea short description|Product Area|Rank|Request participants|Roadmap|Teams";
int added = 0;

for(string k in knownFields) {
    _pdField test = allPDFields[k];
    
    if(isNull(test.name)) {
        allPDFields[k] = {k, null, camelCase(k)};
        runnerLog(k);
        added ++;
    }
}

runnerLog(".", true);
runnerLog("..", true);
runnerLog("...", true);
runnerLog("Heuristic scan complete, <strong style=\"color:blue;\">" + trim(added) + "</strong> field(s) found in scan.", true);
runnerLog("<hr>", true);

//--new section--

runnerLog("");
runnerLog("Creating SIL aliases for Jira Product Discovery fields:", true);
int success_count = 0;
int error_count = 0;

for(_pdField f in arrayStructSort(allPDFields,"name")) {
    boolean result = admAddCustomFieldAlias(f.name, f.alias);
    
    if(result) {
        runnerLog("<strong style=\"color:green;\">Success</strong>: SIL alias created for \"" + f.name + "\": <i>" + f.alias + "</i>", true);
        success_count ++;
    } else {
       string message = "<strong style=\"color:red;\">Error</strong>: The SIL alias for " + f.name + ": " + f.alias + " was not able to be created for an unknown reason.";
       message += " It's possible this occurred because the alias already exists.";
       if(isNotNull(f.id)) {
           message += " The SIL alias will need to be created manually. See <a href=\"https://appfire.atlassian.net/wiki/spaces/PSJC/pages/496206151/Managing+Aliases+in+the+sil.aliases+File\">this page</a> for instructions.";
           message += " Insert the following text into the sil.aliases file:";
           message += "<div style=\"width:25%;background: #b3bac5;margin-left: 25px;padding: 0.25em 5px;\">" + f.alias + "=" + f.id + "<div>";
           error_count ++;
       }
       runnerLog(message, true);
    }
}

runnerLog("Done! <strong>" + trim(success_count) + "</strong> SIL aliases were created with " + trim(error_count) + " errors.", true);
```

---

## How the script works

The script follows a two-step process: first, it discovers all custom field IDs in your Product Discovery projects, then automatically creates SIL aliases for those fields.

### Step 1: Field discovery

The script uses two methods to discover fields, with progress and results displayed separately in the SIL Manager console for each method.

![Power Scripts for Jira Cloud search monitoring dashboard](/cms_trial/assets/d3776039-555b-4335-b969-2d4f082269cc.png)

|  |  |  |
| --- | --- | --- |
| number 1a.png | **Dynamic search** | This scans all Product Discovery projects and examines every idea to find populated custom fields. It automatically picks up new fields that Atlassian adds without requiring script updates.  This method works because custom fields only appear in API responses when they contain data. By examining every idea across all Product Discovery projects, the script maximizes the chances of finding each field in at least one populated instance. |
| number2a.png | **Static search** | Also known as heuristic, this search uses a predefined list of known Product Discovery fields as a backup method to catch fields that weren't found in the dynamic search. |

### Step 2: Alias creation

Once field IDs are discovered, the script generates camelCase aliases and adds them directly to your `sil.aliases` file. For example, 'Idea short description' becomes `ideaShortDescription`.

If alias creation fails, first check if the alias already exists in your `sil.aliases` file since this is the most common cause of errors. For manual creation instructions, see the [Managing aliases in the sil.aliases file](/cms_trial/space/PSJC/496206151/Managing+aliases+in+the+sil.aliases+file/) page.