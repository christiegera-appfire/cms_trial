# admUpdateProjectVersion

## Description

Updates the version of the project by the id field. The version name of the project is unique and it has an id version that corresponds with it.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | admUpdateProjectVersion(versionStruct) | **Package** | adm |
| **Alias** |  | **Pkg Usage** | updateVersion(versionStruct) |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| versionStruct | JVersion | Yes | Version id and the version name should have values assigned. |

## Return Type

**String / Boolean**

You can safely ignore the return value of this function on server. On cloud it will return true if the version is updated and false otherwise.

## Example

```javascript
JVersion jVersion;
jVersion.id = 10201;
jVersion.name = "Version2";
jVersion.description = "This is the second version.";
jVersion.startDate = "2014-10-27";
jVersion.releaseDate = "2014-10-30";
return admUpdateProjectVersion(jVersion);
```

This function updates only the name, description, startDate and releaseDate fields. The archived and released fields can be updated using [admArchiveProjectVersion](/cms_trial/space/PSJC/746324309/admArchiveProjectVersion/) and [admReleaseProjectVersion](/cms_trial/space/PSJC/744165367/admReleaseProjectVersion/) functions. Name must be unique.

## See also