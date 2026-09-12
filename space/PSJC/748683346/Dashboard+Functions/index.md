# Dashboard Functions

This page lists all the available functions used to manipulate dashboards and gadgets.

- [admAddGadgetToDashboard](/cms_trial/space/PSJC/747801902/admAddGadgetToDashboard/)
- [admCopyDashboard](/cms_trial/space/PSJC/748162099/admCopyDashboard/)
- [admCreateDashboard](/cms_trial/space/PSJC/747965192/admCreateDashboard/)
- [admDeleteDashboard](/cms_trial/space/PSJC/747965336/admDeleteDashboard/)
- [admGetAllDashboards](/cms_trial/space/PSJC/748552437/admGetAllDashboards/)
- [admGetAvailableGadgets](/cms_trial/space/PSJC/748618518/admGetAvailableGadgets/)
- [admGetDashboardById](/cms_trial/space/PSJC/748683420/admGetDashboardById/)
- [admGetDashboardGadgetById](/cms_trial/space/PSJC/748718574/admGetDashboardGadgetById/)
- [admGetDashboardGadgets](/cms_trial/space/PSJC/748063606/admGetDashboardGadgets/)
- [admGetDashboardsByName](/cms_trial/space/PSJC/748683364/admGetDashboardsByName/)
- [admGetDashboardsByOwner](/cms_trial/space/PSJC/748618158/admGetDashboardsByOwner/)
- [admGetDashboardsForUser](/cms_trial/space/PSJC/748618168/admGetDashboardsForUser/)
- [admGetFavouriteDashboards](/cms_trial/space/PSJC/747801635/admGetFavouriteDashboards/)
- [admRemoveGadgetFromDashboard](/cms_trial/space/PSJC/748718777/admRemoveGadgetFromDashboard/)
- [admUpdateDashboard](/cms_trial/space/PSJC/748718317/admUpdateDashboard/)
- [admUpdateGadgetInDashboard](/cms_trial/space/PSJC/748162444/admUpdateGadgetInDashboard/)

Structures used in cloud:

### JSharePermission

```text
int id; // the id of the permission
string type; // the type of the permission
string object; //the corresponding object id, see notes
```

Type must be one of the following:

- `"user"` - object must be the `accountId`
- `"group"` - object must be `groupid`
- `"project"` - object must be `projectKey`
- `"projectRole"` - object must have this form `projectKey|roleId`
- `"global"` - object value is discarded
- `"loggedin"` - object value is discarded

### JDashboard

```c
string id; //id
string name; // name
string description; //description
string viewUrl; // the direct url to view this dashboard 
boolean system; //true if it's a system dashboard
string owner; //the owner. For system dashboards it's the admin
int refreshInterval; // auto-refresh in millis
int popularity; // popularity. how many times favourited by users
int rank; //rank
JSharePermission [] editPermissions; // edit perms
JSharePermission [] sharePermissions; //share perms
```

### JGadget

```c
int id; //id of the gadget instance
string moduleKey; //uri or module key must be non-null
string title; //mandatory.
string uri; //uri or module key must be non-null
string color; //standard colors only: "blue", "red", "yellow", "green", "cyan", "purple", "gray", "white"
int row; //row, index starts at 0
int column; //column. index starts at 0
```

### Examples

#### Manipulating dashboards & their permissions

```c++
JDashboard [] dashes = admGetDashboardsByName("Default");
JDashboard dash = admGetDashboardById(10000);

JDashboard created;
created.name="Empty dash no 1";
created.description="This is a description";
created.owner = currentUser();

//This is how you share the dashboards:
// JSharePermission perm;
// perm.type="project";
// perm.object="TEST";
//created.sharePermissions += perm;

JSharePermission permLI;
permLI.type="loggedin";
created.sharePermissions += permLI;

created = admCreateDashboard(created);
runnerLog("Just created:" + created);

JDashboard copy = admCopyDashboard(created.id, currentUser());
copy.description ="this is a new description";
copy = admUpdateDashboard(copy);

runnerLog("Copy of it:" + copy);

admDeleteDashboard(created.id);
admDeleteDashboard(copy.id);
```

#### Modifying a dashboard

```c++
JDashboard dash = admGetDashboardsForUser(currentUser())[0];

JGadget [] gadgets = admGetAvailableGadgets();
JGadget gadget;
for(JGadget g in gadgets) {
    if(g.title == "Activity Stream") {
        gadget = g;
        break;
    }
}

gadget = admAddGadgetToDashboard(dash.id, gadget);
gadget.color = "red";
gadget.admUpdateGadgetInDashboard(dash.id, gadget);

return admGetDashboardGadgets(dash.id);
```