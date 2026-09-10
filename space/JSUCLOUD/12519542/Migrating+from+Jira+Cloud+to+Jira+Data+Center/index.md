# Migrating from Jira Cloud to Jira Data Center

This page describes the required steps when migrating from a Jira Cloud instance to a Jira Data Center instance when you are using some of the default/JSU Workflow Condition/Validator/Post Functions in your workflows.

Migration from Jira Cloud to Jira Server is not directly possible. You have to be careful as there are many validators and conditions which are built into Jira Cloud, but not in Jira Server. For that, you will need JSU. JSU Cloud's additional post functions make it more powerful with its Related Issues, Perform as Add-on User, and many other post functions that you can use to automate your workflows without any coding.

Looking for documentation on a **Data Center to Cloud** migration? See our [Migrating from Jira Data Center to Jira Cloud](/cms_trial/space/JSUCLOUD/12519557/Migrating+from+Jira+Data+Center+to+Jira+Cloud/) page.

## Background

Years ago, the founders of JSU donated several of JSU's modules to Atlassian. Atlassian integrated most of these workflow conditions/validators/post functions (based on JSU Server 1.4) into their native Jira Cloud environment.  Since then, JSU Server/Data Center has added more functionality to make it more powerful. When JSU for Jira Cloud was released, it also added advanced forms of the post functions that were in JSU Server. If you migrate from Jira Cloud to Jira Server/Data Center, the default JSU workflow conditions/validators/post functions do not exist in the default Jira Server/Data Center version but they can simply be replaced with the JSU app.

## How to fix the workflows

You can do one of the following to fix your migrated workflows:

- Reconfigure the affected workflow modules with the ones from JSU, then remove the broken ones.  
  *This is the safest way to do it, but it can be tedious.*
- Export XML workflows, modify, and import again.
- Modify the workflows directly in the database - if you have the required knowledge.   
  *It's efficient but with more risk.*

## Workflow condition/post functions(JSU)

| Workflow Name | JSU Cloud Module-Key | JSU Server/Data Center Module-Key |
| --- | --- | --- |
| **Conditions** |  |  |
| User Is In Any Users (JSU) | com.atlassian.plugins.atlassian-connect-plugin:com.googlecode.  jira-suite-utilities\_\_userisinanyusers-condition | com.googlecode.jsu.workflow.condition.userisinanyusers-condition |
| **Post Functions** |  |  |
| Clear Field Value (JSU) | com.atlassian.plugins.atlassian-connect-plugincom.googlecode.jira-suite-utilities\_\_clearFieldValue-function | com.googlecode.jira-suite-utilitiesclearFieldValue-function |
| Copy Value From Other Field (JSU) | com.atlassian.plugins.atlassian-connect-plugincom.googlecode.jira-suite-utilities\_\_copyValueFromOtherField-function | com.googlecode.jira-suite-utilitiescopyValueFromOtherField-function |
| Copy or Move Attachments (JSU) | com.atlassian.plugins.atlassian-connect-plugincom.googlecode.jira-suite-utilities\_\_copymoveattachments-function | com.googlecode.jira-suite-utilitiescopymoveattachments-function |
| Create a Linked Issue (JSU) | com.atlassian.plugins.atlassian-connect-plugincom.googlecode.jira-suite-utilities\_\_createlinkedissue-function | com.googlecode.jira-suite-utilitiescreatelinkedissue-function |
| Follow Up Transition (JSU) | com.atlassian.plugins.atlassian-connect-plugincom.googlecode.jira-suite-utilities\_\_followuptransition-function | com.googlecode.jira-suite-utilitiesfollowuptransition-function |
| Linked Transition (JSU) | com.atlassian.plugins.atlassian-connect-plugincom.googlecode.jira-suite-utilities\_\_linkedtransition-function | com.googlecode.jira-suite-utilitieslinkedtransition-function |
| Update any Issue Field (JSU) | com.atlassian.plugins.atlassian-connect-plugincom.googlecode.jira-suite-utilities\_\_updateanyissuefield-function | com.googlecode.jira-suite-utilitiesupdateIssueCustomField-function |

## Mapping between JSU Cloud and JSU Server/Data Center

The following table contains all the attributes that need to be mapped between the JSU Cloud and JSU Server workflow functionality.

### Post function mapping: Clear Field Value (JSU)

| Arg Name: JSU Cloud | Arg Name: JSU Server/Data Center |
| --- | --- |
| Example  ```text  <function type="class">  <arg name="class.name">com.atlassian.plugin.connect.jira.workflow.RemoteWorkflowPostFunctionProvider</arg>  <arg name="full.module.key">com.atlassian.plugins.atlassian-connect-plugincom.googlecode.jira-suite-utilities__clearFieldValue-function</arg>  <arg name="remoteWorkflowPostFunctionConfiguration"> {"preconditions":[], "preconditionAwareFunctionMode-textValue":"TRUE", "field":"assignee", "jsuCloudWorkflowParamsVersion-textValue":"2.8.0", "scopeType":"SAME", "source-scopeTarget":"ISSUE_IN_TRANSITION", "destination-scopeTarget":"ISSUE_IN_TRANSITION", "runAsUser-user":"qm:c14a3779-f1ba-496f-a5ef-dbb4ab1928f4:e5e9400a-0c77-440a-aa18-fbb585fbd6e8"}</arg> <arg name="remoteWorkflowPostFunctionUUID">9dfcbdb2-7738-429c-9af4-e0a4b9490f9a</arg> </function> ``` | Example  ```text  <function type="class">     <arg name="scopeSource-linkEnd"></arg>     <arg name="maxAllowed-integerValue"></arg>     <arg name="runAsUser-user">admin</arg>     <arg name="field">assignee</arg>     <arg name="scopeType">SAME</arg>     <arg name="destination-scopeTarget">ISSUE_IN_TRANSITION</arg>     <arg name="full.module.key">com.googlecode.jira-suite-utilitiesclearFieldValue-function</arg>     <arg name="scopeDestination-linkEnd"></arg>     <arg name="preconditionAwareFunctionMode-textValue">ALWAYS</arg>     <arg name="jsuWorkflowParamsVersion-textValue">2.23.3-SNAPSHOT</arg>     <arg name="source-scopeTarget">ISSUE_IN_TRANSITION</arg>     <arg name="scopeDestination-jql"></arg>     <arg name="class.name">com.googlecode.jsu.workflow.function.ClearFieldValuePostFunction</arg>     <arg name="scopeSource-jql"></arg>  </function> ``` |

### Post function mapping: Copy Value From Other Field (JSU)

| Arg Name: JSU Cloud | Arg Name: JSU Server/Data Center |
| --- | --- |
| Example  ```text  <function type="class">  <arg name="class.name">com.atlassian.plugin.connect.jira.workflow.RemoteWorkflowPostFunctionProvider</arg>  <arg name="full.module.key">com.atlassian.plugins.atlassian-connect- plugincom.googlecode.jira-suite-utilities__copyValueFromOtherField-function</arg>  <arg name="remoteWorkflowPostFunctionConfiguration"> {"preconditions": [], "preconditionAwareFunctionMode-textValue":"TRUE", "field.copyFieldSource1":"assignee", "field.copyFieldDestination1":"customfield_10003", "field.copyFieldMode1":"OVERWRITE", "field.copyFieldSeparator1":"", "field.createTargetValue1":false, "jsuCloudWorkflowParamsVersion-textValue":"2.8.0", "scopeType":"SAME", "source-scopeTarget":"ISSUE_IN_TRANSITION", "destination-scopeTarget":"ISSUE_IN_TRANSITION", "runAsUser-user":""} </arg> <arg name="remoteWorkflowPostFunctionUUID">0e286a2f-b587-4432-8806-be35175e92a1</arg> </function> ``` | Example  ```text  <function type="class">     <arg name="field.copyFieldSource2"></arg>     <arg name="field.copyFieldSource1">assignee</arg>     <arg name="scopeSource-linkEnd"></arg>     <arg name="maxAllowed-integerValue"></arg>     <arg name="field.createTargetValue1"></arg>     <arg name="runAsUser-user"></arg>     <arg name="field.copyFieldMode1">OVERWRITE</arg>     <arg name="field.copyFieldDestination1">customfield_11100</arg>     <arg name="field.copyFieldSeparator1"></arg>     <arg name="scopeType">SAME</arg>     <arg name="destination-scopeTarget">ISSUE_IN_TRANSITION</arg>     <arg name="full.module.key">com.googlecode.jira-suite-utilitiescopyValueFromOtherField-function</arg>     <arg name="scopeDestination-linkEnd"></arg>     <arg name="jsuWorkflowParamsVersion-textValue">2.23.3-SNAPSHOT</arg>     <arg name="preconditionAwareFunctionMode-textValue">ALWAYS</arg>     <arg name="source-scopeTarget">ISSUE_IN_TRANSITION</arg>     <arg name="scopeDestination-jql"></arg>     <arg name="class.name">com.googlecode.jsu.workflow.function.CopyValueFromOtherFieldPostFunction</arg>     <arg name="scopeSource-jql"></arg>   </function> ``` |

### Post function mapping: Create a Linked Issue (JSU)

| Arg Name: JSU Cloud | Arg Name: JSU Server/Data Center |
| --- | --- |
| Example  ```text  <function type="class">  <arg  name="class.name">com.atlassian.plugin.connect.jira.workflow.RemoteWorkflowPostFunctionProvider</arg>  <arg  name="full.module.key">com.atlassian.plugins.atlassian-connect- plugincom.googlecode.jira-suite-utilities__createlinkedissue-function</arg>  <arg name="remoteWorkflowPostFunctionConfiguration"> {"preconditions":[], "preconditionAwareFunctionMode-textValue":"TRUE", "currentProjectType":"SAME", "currentProjectId":"-2", "currentIssueTypeId":"10006", "runAsUser-user":"", "jsuCloudWorkflowParamsVersion-textValue":"2.8.0", "subFunctions":[], "scopeType":"NONE", "source-scopeTarget":"ISSUE_IN_TRANSITION", "destination-scopeTarget":"ISSUE_IN_TRANSITION", "field.attachmentEnablingCustomFieldId":"ALWAYS", "field.existingAttachmentEnablingCustomFieldId":"ALWAYS", "transitionAttachmentsOperation":"copy"} </arg> <arg name="remoteWorkflowPostFunctionUUID">a27f8e4f-f1a0-4e01-9199-057d34df07ee</arg> </function> ``` | Example  ```text <function type="class">    <arg name="field.existingAttachmentEnablingCustomFieldId"></arg>    <arg name="scopeSource-linkEnd"></arg>    <arg name="targetIssueTypeDefinedByCfSelection"></arg>    <arg name="issueTypeId">1</arg>    <arg name="scopeType">NONE</arg>    <arg name="jsuWorkflowParamsVersion-textValue">2.23.3-SNAPSHOT</arg>    <arg name="source-scopeTarget">ISSUE_IN_TRANSITION</arg>    <arg name="field.attachmentEnablingCustomFieldId"></arg>    <arg name="targetIssueType">SELECTED_ISSUE_TYPE</arg>    <arg name="scopeSource-jql"></arg>    <arg name="createIssueAsUser-user"></arg>    <arg name="field.copyTransitionComment">false</arg>    <arg name="targetProjectType">SAME</arg>    <arg name="maxAllowed-integerValue"></arg>    <arg name="transitionAttachmentsOperation">copy</arg>    <arg name="field.issueAssignTo">ASSIGN_TO_ASSIGNEE</arg>    <arg name="targetProjectSelectedCustomField"></arg>    <arg name="destination-scopeTarget">ISSUE_IN_TRANSITION</arg>    <arg name="full.module.key">com.googlecode.jira-suite-utilitiescreatelinkedissue-function</arg>    <arg name="scopeDestination-linkEnd"></arg>    <arg name="field.enablingCustomFieldId"></arg>    <arg name="preconditionAwareFunctionMode-textValue">ALWAYS</arg>    <arg name="scopeDestination-jql"></arg>    <arg name="subFunctions">[]</arg>    <arg name="class.name">ch.beecom.jira.jsu.workflow.function.createlinkedissue.CreateLinkedIssueFunction</arg>    <arg name="projectId">10500</arg> </function> ``` |

### Post function mapping: Linked Transition (JSU)

| Arg Name: JSU Cloud | Arg Name: JSU Server/Data Center |
| --- | --- |
| Example  ```text <function type="class"> <arg name="class.name">com.atlassian.plugin.connect.jira.workflow.RemoteWorkflowPostFunctionProvider</arg> <arg name="full.module.key">com.atlassian.plugins.atlassian-connect-plugincom.googlecode.jira-suite-utilities__linkedtransition-function</arg> <arg name="remoteWorkflowPostFunctionConfiguration"> {"preconditions":[], "preconditionAwareFunctionMode-textValue":"TRUE", "runAsUser-user":"", "status":"", "statusName":"", "workflowName-textValue":"classic default workflow", "integerValue":"2", "textValue":"-1", "jsuCloudWorkflowParamsVersion-textValue":"2.8.0", "scopeType":"ISSUE_LINKING", "source-scopeTarget":"ISSUE_IN_TRANSITION", "destination-scopeTarget":"LINK_END", "scopeSource-linkEnd":"", "scopeDestination-linkEnd":""} </arg> <arg name="remoteWorkflowPostFunctionUUID">45bd3003-b5e2-42b8-ada2-032d3b2b8f83</arg> </function> ``` | Example  ```text  <function type="class">     <arg name="field.copyFieldSource1"></arg>     <arg name="textValue">-1</arg>     <arg name="scopeSource-linkEnd"></arg>     <arg name="maxAllowed-integerValue"></arg>     <arg name="workflowName-textValue">AP: Task Management Workflow</arg>     <arg name="performTransitionAsUser-user"></arg>     <arg name="scopeType">ISSUE_LINKING</arg>     <arg name="destination-scopeTarget">LINK_END</arg>     <arg name="full.module.key">com.googlecode.jira-suite-utilitieslinkedtransition-function</arg>     <arg name="scopeDestination-linkEnd">ANY:ANY</arg>     <arg name="jsuWorkflowParamsVersion-textValue">2.23.3-SNAPSHOT</arg>     <arg name="preconditionAwareFunctionMode-textValue">ALWAYS</arg>     <arg name="source-scopeTarget">ISSUE_IN_TRANSITION</arg>     <arg name="integerValue">21</arg>     <arg name="scopeDestination-jql"></arg>     <arg name="class.name">ch.beecom.jira.jsu.workflow.function.linkedtransition.LinkedTransitionFunction</arg>     <arg name="scopeSource-jql"></arg>     <arg name="status"></arg>  </function> ``` |

### Post function mapping: Update any Issue Field (JSU)

| Arg Name: JSU Cloud | Arg Name: JSU Server/Data Center |
| --- | --- |
| Example  ```text  <function type="class">  <arg name="class.name">com.atlassian.plugin.connect.jira.workflow.RemoteWorkflowPostFunctionProvider</arg>  <arg name="full.module.key">com.atlassian.plugins.atlassian-connect-plugincom.googlecode.jira-suite-utilities__updateanyissuefield-function</arg>  <arg name="remoteWorkflowPostFunctionConfiguration"> {"preconditions":[], "preconditionAwareFunctionMode-textValue":"TRUE", "runAsUser-user":"", "field.name":"summary", "field.value":"test summary", "append.value":false, "jsuCloudWorkflowParamsVersion-textValue":"2.8.0", "scopeType":"SAME", "source-scopeTarget":"ISSUE_IN_TRANSITION", "destination-scopeTarget":"ISSUE_IN_TRANSITION"} </arg> <arg name="remoteWorkflowPostFunctionUUID">e6518c27-cd5e-40b4-a190-14b1c32c1e8e</arg> </function> ``` | Example  ```text  <function type="class">     <arg name="scopeSource-linkEnd"></arg>     <arg name="append.value"></arg>     <arg name="maxAllowed-integerValue"></arg>     <arg name="runAsUser-user"></arg>     <arg name="field.value">test summary</arg>     <arg name="field.name">summary</arg>     <arg name="scopeType">SAME</arg>     <arg name="destination-scopeTarget">ISSUE_IN_TRANSITION</arg>     <arg name="full.module.key">com.googlecode.jira-suite-utilitiesupdateIssueCustomField-function</arg>     <arg name="scopeDestination-linkEnd"></arg>     <arg name="preconditionAwareFunctionMode-textValue">ALWAYS</arg>     <arg name="jsuWorkflowParamsVersion-textValue">2.23.3-SNAPSHOT</arg>     <arg name="source-scopeTarget">ISSUE_IN_TRANSITION</arg>     <arg name="scopeDestination-jql"></arg>     <arg name="class.name">com.googlecode.jsu.workflow.function.UpdateIssueCustomFieldPostFunction</arg>     <arg name="scopeSource-jql"></arg> </function> ``` |

### Workflow preconditions(JSU)

Preconditions in JSU Cloud are built-in as a part of the post function. You can add as many preconditions as you want inside a post function. In JSU Server/Data Center, preconditions are implemented as a separate post function that acts as preconditions. All the preconditions from JSU Cloud are available in the JSU Server/Data Center as well but require a different configuration.

|  |
| --- |
| **Preconditions in JSU Server/Data Center and Cloud** |
| Date Compare (JSU) |
| Date Expression Compare (JSU) |
| Date Window (JSU) |
| Fields Required (JSU) |
| JQL (JSU) |
| Linked Status (JSU) |
| Regular Expression Check (JSU) |
| User Is In Any Groups (JSU) |
| User Is In Any Roles (JSU) |
| User Is In Custom Field (JSU) |
| Value Field (JSU) |

### Precondition mapping: Value Field (JSU)

| Arg Name: JSU Cloud | Arg Name: JSU Server/Data Center |
| --- | --- |
| Example  ```text <arg name="remoteWorkflowPostFunctionConfiguration"> {"preconditions": [{"type":"valueField-precondition-function", "enabled":true, "config":{ "preconditionMode-textValue":"AND", "preconditionNegateResult-booleanValue":false, "conditionList":1, "fieldValue":"2.0", "fieldsList":"fixVersions"}}], "preconditionAwareFunctionMode-textValue":"TRUE", "runAsUser-user":"", "field.name":"summary", "field.value":"test summary", "append.value":false, "jsuCloudWorkflowParamsVersion-textValue":"2.8.0", "scopeType":"SAME", "source-scopeTarget":"ISSUE_IN_TRANSITION", "destination-scopeTarget":"ISSUE_IN_TRANSITION"} </arg> ``` | Example  ```text   <function type="class">      <arg name="conditionList">1</arg>      <arg name="full.module.key">com.googlecode.jira-suite-utilitiesvalueField-precondition-function</arg>      <arg name="jsuWorkflowParamsVersion-textValue">2.23.3-SNAPSHOT</arg>      <arg name="comparisonType">1</arg>      <arg name="precondition">true</arg>      <arg name="class.name">ch.beecom.jira.jsu.workflow.function.valuefield.ValueFieldPreconditionFunction</arg>      <arg name="preconditionNegateResult-booleanValue"></arg>      <arg name="fieldValue">2.0</arg>      <arg name="preconditionMode-textValue">DISCARD</arg>      <arg name="fieldsList">fixVersions</arg>    </function> ``` |

All other preconditions follow a similar pattern as above.

As preconditions in JSU Cloud are built-in, you have to reconfigure all the preconditions manually in JSU Server/Data Center.

## Workflow condition/validator/post functions(Jira)

The following list of workflow conditions/validators/post functions built into the Jira Cloud environment can be replaced with JSU extensions. See below, all the attribute mappings between Jira Cloud and Jira Server/Data Center.

| Workflow Name | Jira Cloud Class-Name | JSU Class-Name (Jira Server/Data Center) |
| --- | --- | --- |
| **Conditions** |  |  |
| User Is In Any Group | com.atlassian.jira.workflow.condition.UserInAnyGroupCondition | com.googlecode.jsu.workflow.condition.UserIsInAnyGroupsCondition |
| User Is In Any Project Role | com.atlassian.jira.workflow.condition.InAnyProjectRoleCondition | com.googlecode.jsu.workflow.condition.UserIsInAnyRolesCondition |
| User Is In Custom Field | com.atlassian.jira.workflow.condition.UserIsInCustomFieldCondition | com.googlecode.jsu.workflow.condition.UserIsInCustomFieldCondition |
| Value Field | com.atlassian.jira.workflow.condition.ValueFieldCondition | com.googlecode.jsu.workflow.condition.ValueFieldCondition |
| **Validators** |  |  |
| Date Compare Validator | com.atlassian.jira.workflow.validator.DateFieldValidator | com.googlecode.jsu.workflow.validator.DateCompareValidator & com.googlecode.jsu.workflow.validator.DateExpressionCompareValidator |
| Date Window Validator | com.atlassian.jira.workflow.validator.WindowsDateValidator | com.googlecode.jsu.workflow.validator.WindowsDateValidator |
| Field Required Validator | com.atlassian.jira.workflow.validator.FieldRequiredValidator | com.googlecode.jsu.workflow.validator.FieldsRequiredValidator |
| Regular Expression Check | com.atlassian.jira.workflow.validator.RegexpFieldValidator | com.googlecode.jsu.workflow.validator.RegexpFieldValidator |
| **Post Functions** |  |  |
| Clear Field Value | com.atlassian.jira.workflow.function.issue.ClearFieldValuePostFunction | com.googlecode.jsu.workflow.function.ClearFieldValuePostFunction |
| Copy Value From Other Field | com.atlassian.jira.workflow.function.issue.CopyValueFromOtherFieldPostFunction | com.googlecode.jsu.workflow.function.CopyValueFromOtherFieldPostFunction |
| Update Issue Custom Field | com.atlassian.jira.workflow.function.issue.UpdateIssueCustomFieldPostFunction | com.googlecode.jsu.workflow.function.UpdateIssueCustomFieldPostFunction |

## Mapping between Jira Cloud modules and JSU Server/Data Center

The following describes all the attributes which need to be mapped between the Jira Cloud and Jira Server/Data Center workflow functionality.

### Condition mapping: User Is In Any Group

| Arg Name: Jira Cloud | Arg Name: Jira Server/Data Center |
| --- | --- |
| group | hidGroupsList (each group is separated by @@ and requires a @@ at the end) |
| Example  ```text <condition type="class">   <arg name="class.name">com.atlassian.jira.workflow.condition.UserInAnyGroupCondition</arg>   <arg name="group">administrators@@</arg> </condition> ``` | Example  ```text <condition type="class">   <arg name="class.name">com.googlecode.jsu.workflow.condition.UserIsInAnyGroupsCondition</arg>   <arg name="hidGroupsList">jira-developers@@</arg> </condition> ``` |

### Condition mapping: User Is In Any Project Role

| Arg Name: Jira Cloud | Arg Name: Jira Server/Data Center |
| --- | --- |
| projectRoleIds | hidRolesList (each group is separated by @@ and requires a @@ at the end and groups are required to be mapped between id to group name) |
| Example  ```text <condition type="class">   <arg name="class.name">com.atlassian.jira.workflow.condition.InAnyProjectRoleCondition</arg>   <arg name="projectRoleIds">10101@@</arg> </condition> ``` | Example  ```text <condition type="class">   <arg name="class.name">com.googlecode.jsu.workflow.condition.UserIsInAnyRolesCondition</arg>   <arg name="hidRolesList">Developers@@</arg> </condition> ``` |

### Condition mapping: User Is In Custom Field

All argument names are the same between Jira Cloud and Jira Server/Data Center.

| Arg Name: Jira Cloud | Arg Name: Jira Server/Data Center |
| --- | --- |
| Example  ```text <condition type="class">   <arg name="class.name">com.atlassian.jira.workflow.condition.UserIsInCustomFieldCondition</arg>   <arg name="fieldsList">customfield_10018</arg>   <arg name="allowUserInField">true</arg> </condition> ``` | Example  ```text <condition type="class">   <arg name="class.name">com.googlecode.jsu.workflow.condition.UserIsInCustomFieldCondition</arg>   <arg name="fieldsList">customfield_10609</arg>   <arg name="allowUserInField">true</arg> </condition> ``` |

### Condition mapping: Value Field

All argument names are the same between Jira Cloud and Jira Server/Data Center.

| Arg Name: Jira Cloud | Arg Name: Jira Server/Data Center |
| --- | --- |
| Example  ```text <condition type="class">   <arg name="class.name">com.atlassian.jira.workflow.condition.ValueFieldCondition</arg>   <arg name="comparisonType">1</arg>   <arg name="conditionList">3</arg>   <arg name="fieldsList">assignee</arg>   <arg name="fieldValue">John</arg> </condition> ``` | Example  ```text <condition type="class">   <arg name="class.name">com.googlecode.jsu.workflow.condition.ValueFieldCondition</arg>   <arg name="comparisonType">1</arg>   <arg name="conditionList">3</arg>   <arg name="fieldsList">assignee</arg>   <arg name="fieldValue">John</arg> </condition> ``` |

### Validator mapping: Date Compare validator

The Jira Cloud 'Date Compare Validator' combines two JSU Date Compare Validators:

- Date Compare Validator (compareTypeField = true)
- Date Expression Compare Validator (compareTypeField = false)

Which of the two validators to use is defined by the Jira Cloud argument name 'compareTypeField'

**Date Compare validator**

All argument names are the same between Jira Cloud and Jira Server/Data Center.

| Arg Name: Jira Cloud | Arg Name: Jira Server/Data Center |
| --- | --- |
| Example  ```text <validator name="" type="class">   <arg name="class.name">com.atlassian.jira.workflow.validator.DateFieldValidator</arg>   <arg name="compareTypeField">true</arg>   <arg name="conditionSelected">3</arg>   <arg name="includeTimeSelected">true</arg>   <arg name="date1Selected">customfield_10017</arg>   <arg name="date2Selected">customfield_10022</arg> </validator> ``` | Example  ```text <validator name="" type="class">   <arg name="class.name">com.googlecode.jsu.workflow.validator.DateCompareValidator</arg>   <arg name="conditionSelected">1</arg>   <arg name="includeTimeSelected">2</arg>   <arg name="date1Selected">created</arg>   <arg name="date2Selected">created</arg> </validator> ``` |

**Date Expression Compare validator**

| Arg Name: Jira Cloud | Arg Name: Jira Server/Data Center |
| --- | --- |
| compareTypeField  (must be false to map to the 'Date Expression Compare Validator') | not required for Jira Server/Data Center. |
| conditionSelected | conditionSelected |
| includeTimeSelected | includeTimeSelected |
| date1Selected | date1Selected |
| expression | expressionSelected |
| Example  ```text <validator name="" type="class">   <arg name="class.name">com.atlassian.jira.workflow.validator.DateFieldValidator</arg>   <arg name="compareTypeField">false</arg>   <arg name="conditionSelected">1</arg>   <arg name="includeTimeSelected">false</arg>   <arg name="date1Selected">customfield_10017</arg>   <arg name="expression">\d</arg> </validator> ``` | Example  ```text <validator name="" type="class">   <arg name="class.name">com.googlecode.jsu.workflow.validator.DateExpressionCompareValidator</arg>   <arg name="conditionSelected">1</arg>   <arg name="includeTimeSelected">2</arg>   <arg name="dateFieldSelected">created</arg>   <arg name="expressionSelected">\d</arg> </validator> ``` |

### Validator mapping: Date Window validator

All argument names are the same between Jira Cloud and Jira Server/Data Center.

| Arg Name: Jira Cloud | Arg Name: Jira Server/Data Center |
| --- | --- |
| Example  ```text <validator name="" type="class">   <arg name="class.name">com.atlassian.jira.workflow.validator.WindowsDateValidator</arg>   <arg name="date1Selected">customfield_10017</arg>   <arg name="date2Selected">customfield_10017</arg>   <arg name="windowsDays">5</arg> </validator> ``` | Example  ```text <validator name="" type="class">   <arg name="class.name">com.googlecode.jsu.workflow.validator.WindowsDateValidator</arg>   <arg name="date1Selected">customfield_10017</arg>   <arg name="date2Selected">customfield_10017</arg>   <arg name="windowsDays">5</arg> </validator> ``` |

### Validator mapping: Field Required validator

| Arg Name: Jira Cloud | Arg Name: Jira Server/Data Center |
| --- | --- |
| hidFieldsList | hidFieldsList |
| contextHandling | contextHandling |
| errorMessage | customErrorMessage-textValue |
| Example  ```text <validator name="" type="class">   <arg name="class.name">com.atlassian.jira.workflow.validator.FieldRequiredValidator</arg>   <arg name="hidFieldsList">assignee@@</arg>   <arg name="contextHandling">ignore</arg>   <arg name="errorMessage">Custom Error Message<arg> </validator> ``` | Example  ```text <validator name="" type="class">   <arg name="class.name">com.googlecode.jsu.workflow.validator.FieldsRequiredValidator</arg>   <arg name="hidFieldsList">assignee@@</arg>   <arg name="contextHandling">ignore</arg>   <arg name="customErrorMessage-textValue">Custom Error Message</arg> </validator> ``` |

### Validator mapping: Regular Expression Check

All argument names are the same between Jira Cloud and Jira Server/Data Center.

| Arg Name: Jira Cloud | Arg Name: Jira Server/Data Center |
| --- | --- |
| Example  ```text <validator name="" type="class">   <arg name="class.name">com.atlassian.jira.workflow.validator.RegexpFieldValidator</arg>   <arg name="fieldSelected">description</arg>   <arg name="expressionSelected">\d</arg> </validator> ``` | Example  ```text <validator name="" type="class">   <arg name="class.name">com.googlecode.jsu.workflow.validator.RegexpFieldValidator</arg>   <arg name="fieldSelected">versions</arg>   <arg name="expressionSelected">\d</arg> </validator> ``` |

### Post function mapping: Clear Field Value

All argument names are the same between Jira Cloud and Jira Server/Data Center.

| Arg Name: Jira Cloud | Arg Name: Jira Server/Data Center |
| --- | --- |
| Example  ```text <function type="class">   <arg name="class.name">com.atlassian.jira.workflow.function.issue.ClearFieldValuePostFunction</arg>   <arg name="full.module.key">com.atlassian.jira.plugin.system.workflowclearFieldValue-function</arg>   <arg name="field">assignee</arg> </function> ``` | Example  ```text <function type="class">   <arg name="class.name">com.googlecode.jsu.workflow.function.ClearFieldValuePostFunction</arg>   <arg name="full.module.key">com.googlecode.jira-suite-utilitiesclearFieldValue-function</arg>   <arg name="field">comment</arg> </function> ``` |

### Post function mapping: Copy Value From Other Field

| Arg Name: Jira Cloud | Arg Name: Jira Server/Data Center |
| --- | --- |
| Example  ```text <function type="class">   <arg name="class.name">com.atlassian.jira.workflow.function.issue.CopyValueFromOtherFieldPostFunction</arg>   <arg name="sourceField">assignee</arg>   <arg name="destinationField">assignee</arg>   <arg name="copyType">same</arg> </function> ``` | Example  ```text <function type="class">   <arg name="sourceField">assignee</arg>   <arg name="class.name">com.googlecode.jsu.workflow.function.CopyValueFromOtherFieldPostFunction</arg>   <arg name="destinationField">customfield_10101</arg> </function> ``` |

### Post function mapping: Update Issue Custom Field

All argument names are the same between Jira Cloud and Jira Server/Data Center.

| Arg Name: Jira Cloud | Arg Name: Jira Server/Data Center |
| --- | --- |
| Example  ```text <function type="class">   <arg name="class.name">com.atlassian.jira.workflow.function.issue.UpdateIssueCustomFieldPostFunction</arg>   <arg name="field.name">customfield_10000</arg>   <arg name="field.value">%%CURRENT_USER%%</arg>   <arg name="append.value">true</arg> </function> ``` | Example  ```text <function type="class">   <arg name="class.name">com.googlecode.jsu.workflow.function.UpdateIssueCustomFieldPostFunction</arg>   <arg name="field.name">versions</arg>   <arg name="field.value">%%CURRENT_USER%%</arg>   <arg name="append.value">true</arg> </function> ``` |