# Filter Administration Functions

This section contains functions that enable users to handle filters, including creating, updating and sharing them. Also the filter event function

## Functions Summary

- [admChangeFilterOwner](/cms_trial/space/PSJC/720902557/admChangeFilterOwner/)
- [admCreateFilter](/cms_trial/space/PSJC/720902428/admCreateFilter/)
- [admDeleteFilter](/cms_trial/space/PSJC/720604973/admDeleteFilter/)
- [admFavourFilter](/cms_trial/space/PSJC/722075940/admFavourFilter/)
- [admGetAllFilters](/cms_trial/space/PSJC/722108903/admGetAllFilters/)
- [admGetAllOwnedFilters](/cms_trial/space/PSJC/722174348/admGetAllOwnedFilters/)
- [admGetFavouriteFilters](/cms_trial/space/PSJC/722076017/admGetFavouriteFilters/)
- [admGetFilterById](/cms_trial/space/PSJC/720473851/admGetFilterById/)
- [admGetFilterOwner](/cms_trial/space/PSJC/722174167/admGetFilterOwner/)
- [admGetFiltersByName](/cms_trial/space/PSJC/720473817/admGetFiltersByName/)
- [admGetFiltersForProject](/cms_trial/space/PSJC/720605278/admGetFiltersForProject/)
- [admShareFilter](/cms_trial/space/PSJC/722174268/admShareFilter/)
- [admUnfavourFilter](/cms_trial/space/PSJC/722141511/admUnfavourFilter/)
- [admUnshareFilter](/cms_trial/space/PSJC/720637428/admUnshareFilter/)
- [admUpdateFilter](/cms_trial/space/PSJC/722141349/admUpdateFilter/)

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

See below example on usage

### JFilter

```text
int id; //id of the filter
string jql; // the jql
string name; //must be unique in your Jira
string description; // just a description, optional
string owner; // account id of the owner
JSharePermission [] editPermissions; //edit
JSharePermission [] sharePermissions; //share
```

### Example usage

```java
//create a filter
JFilter f = admCreateFilter("pcfilter", "project = TEST and issueType = Bug", currentUser(), "This is programatically created");
//get it's owner
string owner = admGetFilterOwner(f.id);

//update the filter
f.description = "Modified description";
f.name="pcfiltertwo";
admUpdateFilter(f);

//update various bits 
admChangeFilterOwner(f.id, someOtherUser);
admFavourFilter(f.id, currentUser());

//Get filters in different ways
f = admGetFilterById(f.id);
JFilter [] allFilters = admGetAllFilters();
JFilter [] namedFilters = admGetFiltersByName("pcfiltertwo");
JFilter [] owned = admGetAllOwnedFilters(currentUser());
  


//Share a filter:
JSharePermission perm;
perm.type="project";
perm.object="TEST";

admShareFilter(f.id, 1, perm);

perm.type="group";
perm.object="site-admins";
admShareFilter(f.id, 1, perm);
```