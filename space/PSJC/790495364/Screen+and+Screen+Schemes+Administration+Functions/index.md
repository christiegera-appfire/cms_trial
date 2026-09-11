# Screen and Screen Schemes Administration Functions

This section contains functions that enable users to handle screen and screen schemes administration.

## Functions Summary

- [admAddFieldToDefaultScreen](/cms_trial/space/PSJC/790530249/admAddFieldToDefaultScreen/)
- [admAddFieldToScreenTab](/cms_trial/space/PSJC/790497410/admAddFieldToScreenTab/)
- [admCreateScreenScheme](/cms_trial/space/PSJC/790758340/admCreateScreenScheme/)
- [admGetScreenTabFields](/cms_trial/space/PSJC/791969973/admGetScreenTabFields/)
- [admGetScreenTabs](/cms_trial/space/PSJC/790529764/admGetScreenTabs/)
- [admMoveFieldLastInTab](/cms_trial/space/PSJC/792297546/admMoveFieldLastInTab/)

Structures used:

### JScreenScheme

```text
int id; // the id
string name; // name of the scheme, must be not null
string description; // description
int  defaultScreenId; // default screen, must always be set
int createScreenId; //create screen
int editScreenId; //edit screen
int viewScreenId; //view screen
```

### JScreen

```text
int id; // screen id
string name; // name, must be not null
string description;
string scope; //TEMPLATE or PROJECT
string projectKey;
```

### Example usage

```c++
JScreenScheme [] sss = admGetAllScreenSchemes();
runnerLog("Screen Schemes (" + size(sss) + ") :" + sss);

JScreen [] screens = admGetAllScreens();
runnerLog("Screens(" + size(screens) + ") :" + screens);


JScreen s = admCreateScreen("My screen", "A screen for demo purposes");
s = admUpdateScreen(s.id, "Demo Screen", "A screen for demo purposes, but the title is rather dull");

runnerLog("Created screen id(" + s.id + ") :" + s);

int demoTabId = admCreateScreenTab(s.id, "My Tab");
admUpdateScreenTab(s.id, demoTabId, "Demo Tab");

int mainTab = 0;

int [] allTabs = admGetScreenTabs(s.id);
for(int i = 0; i < size(allTabs) && mainTab == 0; i++) {
    if(allTabs[i] != demoTabId) {
        mainTab = allTabs[i];
    }
}

runnerLog("You may add any of the following fields:" + admGetAllAvailableFieldsForScreen(s.id));

runnerLog("Tabs are now:" + allTabs);

admAddFieldToScreenTab(s.id, mainTab, "summary");
admAddFieldToScreenTab(s.id, mainTab, "assignee");
admAddFieldToScreenTab(s.id, demoTabId, "description");
admAddFieldToScreenTab(s.id, demoTabId, "versions");
admAddFieldToScreenTab(s.id, demoTabId, "customfield_10012");
admAddFieldToScreenTab(s.id, demoTabId, "customfield_10021");
admMoveFieldLastInTab(s.id, demoTabId, "description");
admRemoveFieldFromScreenTab(s.id, demoTabId, "customfield_10021");
admMoveScreenTab(s.id, demoTabId, 0);



runnerLog("All screen schemes:" + admGetAllScreenSchemes());

JScreenScheme scheme;
scheme.name = "DemoScheme";
scheme.description = "A descrription";
scheme.editScreenId = s.id;
scheme.defaultScreenId = 1; //standard screen

scheme = admCreateScreenScheme(scheme);

scheme.description = "A better description";

scheme = admUpdateScreenScheme(scheme);

admDeleteScreenScheme(scheme.id);
admDeleteScreen(s.id);

return true;
```