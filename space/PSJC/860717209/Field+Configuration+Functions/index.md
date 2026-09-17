# Field Configuration Functions

Field configurations are used ultimately to set up the hidden or required field flags, based on issue types and projects. Most of these only work for *Company-Managed Projects* (classic projects)

## Functions Summary

- [admAppendFieldConfigDefaultITMapping](/cms_trial/space/PSJC/860881084/admAppendFieldConfigDefaultITMapping/)
- [admAppendFieldConfigITMapping](/cms_trial/space/PSJC/860848297/admAppendFieldConfigITMapping/)
- [admAssignDefaultFieldConfigSchemeToProject](/cms_trial/space/PSJC/860488166/admAssignDefaultFieldConfigSchemeToProject/)
- [admAssignFieldConfigSchemeToProject](/cms_trial/space/PSJC/860455585/admAssignFieldConfigSchemeToProject/)
- [admCreateFieldConfig](/cms_trial/space/PSJC/861667573/admCreateFieldConfig/)
- [admCreateFieldConfigScheme](/cms_trial/space/PSJC/860422613/admCreateFieldConfigScheme/)
- [admDeleteFieldConfig](/cms_trial/space/PSJC/862388249/admDeleteFieldConfig/)
- [admDeleteFieldConfigScheme](/cms_trial/space/PSJC/860422850/admDeleteFieldConfigScheme/)
- [admGetAllFieldConfigItems](/cms_trial/space/PSJC/862224438/admGetAllFieldConfigItems/)
- [admGetAllFieldConfigs](/cms_trial/space/PSJC/860423072/admGetAllFieldConfigs/)
- [admGetAllFieldConfigSchemes](/cms_trial/space/PSJC/514818850/admGetAllFieldConfigSchemes/)
- [admGetFieldConfigById](/cms_trial/space/PSJC/860717838/admGetFieldConfigById/)
- [admGetFieldConfigITMappings](/cms_trial/space/PSJC/860357745/admGetFieldConfigITMappings/)
- [admGetFieldConfigsByName](/cms_trial/space/PSJC/861044800/admGetFieldConfigsByName/)
- [admGetFieldConfigScheme](/cms_trial/space/PSJC/515146283/admGetFieldConfigScheme/)
- [admRemoveFieldConfigDefaultITMapping](/cms_trial/space/PSJC/860324541/admRemoveFieldConfigDefaultITMapping/)
- [admRemoveFieldConfigITMapping](/cms_trial/space/PSJC/860324528/admRemoveFieldConfigITMapping/)
- [admUpdateFieldConfig](/cms_trial/space/PSJC/861733003/admUpdateFieldConfig/)
- [admUpdateFieldConfigItem](/cms_trial/space/PSJC/861733016/admUpdateFieldConfigItem/)
- [admUpdateFieldConfigScheme](/cms_trial/space/PSJC/860324334/admUpdateFieldConfigScheme/)

Structures used:

**JFieldConfigurationScheme**

```text
int id;
string name;
string description;
```

This is the topmost structure, the one you may use to assign to projects

**JFieldConfiguration**

```text
int id;
string name;
string description;
boolean isDefault;
```

This does not represent a certain field. It’s the totality of the configs you associate with issue types.

**JFieldConfigITMapping**

```text
int fieldConfigurationId;
int issueTypeId;
```

If issue type id is zero (0) it actually means the default issue type.

**JFieldConfigurationItem**

```text
string field;
string description;
string renderer;
boolean hidden;
boolean required;
```

Renderer may be changed only for text fields, and accepted values are ‘*text-renderer*' and ‘*wiki-renderer*’. Field is the Jira name of the field, like ‘*summary*’, ‘*fixVersions*’ or '*customfield\_12345*’.