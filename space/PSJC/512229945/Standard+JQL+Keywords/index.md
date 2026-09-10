# Standard JQL Keywords

For best results remember to enable auto-synchronization and the corresponding category and index the issues initially, otherwise the results may not be accurate.

## Attachments

#### **attachedBy**

Search issues where a specified user has attached a file to them using the attachedBy keyword.

|  |
| --- |
| ```text attachedBy = "jdoe" AND created > startOfYear() ``` |

*Data type: User*

#### **attachmentEarliestDate**

Search issues based on the earliest date an attachment was added using attachmentEarliestDate keyword.

|  |
| --- |
| ```text attachmentEarliestDate < startOfMonth() //or attachmentEarliestDate = "2020-01-01" ``` |

*Data type: Date*

#### **attachmentLatestDate**

Search issues based on the latest date an attachment was added using attachmentLatestDate keyword.

|  |
| --- |
| ```text attachmentLatestDate > startOfDay() ``` |

*Data type: Date*

#### **countOfAttachments**

Search issues based on the number of attachments it has using the countOfAttachments keyword. This can be used to determine if the issue has any attachments at all.

|  |
| --- |
| ```text project = "Test" AND countOfAttachments > 0 ``` |

*Data type: Number*

#### **typeOfAttachment**

Search for issus that contain a specific type of attachment. This search is based on the file extension of the attachment. For example, to search for a Microsoft Word document use "doc" or "docx".

|  |
| --- |
| ```text project = "TEST" AND typeOfAttachment = "jpg" //or created > startOfWeek() AND typeOfAttachment = "pdf" ``` |

*Data type: Text*

## Comments

#### **commentAuthors**

Search for issues based on users who have commented on the issue using the commentAuthors keyword.

|  |
| --- |
| ```text project = "Test" AND commentAuthors = jsmith //or project = "Test" AND commentAuthors in (jsmith, jdoe, juser) ``` |

*Data type: User*

#### **commentedOnDates**

Search for issues based on the dates that comments were created using the commentedOnDates keyword.

|  |
| --- |
| ```text commentedOnDates = 2020-06-18 //or commentedOnDates > startOfMonth() ``` |

*Data type: Date*

#### **commentVisibleGroups**

Search for issues with comments that have visibility restrictions applied for a specified group using the commentVisibleGroups keyword.

|  |
| --- |
| ```text commentVisibleGroups = "Developers" //or commentVisibleGroups in ("Developers", "Managers") ``` |

*Data type: Text*

#### **commentVisibleRoles**

Search for issues with comments that have visibility restrictions applied for a specified project role using the commentVisibleRoles keyword.

|  |
| --- |
| ```text commentVisibleRoles = "Administrators" //or commentVisibleRoles in ("Administrators", "Project Managers") ``` |

*Data type: Text*

#### **countOfComments**

Search issues based on the number of comments it has. This can be used to determine if the issue has any comments at all using the countOfComments keyword.

|  |
| --- |
| ```text countOfComments > 0 //or countOfComments = 2 ``` |

*Data type: Number*

#### **firstCommentedOnDate**

Search issues based on the earliest date a comment was added using the firstCommentedOnDate keyword.

|  |
| --- |
| ```text firstCommentedOnDate = 2020-06-18 //or firstCommentedOnDate > startOfMonth() ``` |

*Data type: Date*

#### newestCommentAuthor

Search issues based on username of the last person to add a comment to an issue using the newestCommentAuthor keyword.

|  |
| --- |
| ```text newestCommentAuthor = "jsmith" ``` |

*Data type: Text*

#### **lastCommentedOnDate**

Search issues based on the latest date a comment was added using the lastCommentedOnDate keyword.

|  |
| --- |
| ```text lastCommentedOnDate = 2020-06-18 //or lastCommentedOnDate > startOfMonth() ``` |

*Data type: Date*

#### **newestCommentVisibleGroup**

Search for issues with a visibility restrictions applied for a specified group for the newest comment added using the newestCommentVisibleGroup keyword.

|  |
| --- |
| ```text newestCommentVisibleGroup = "Developers" ``` |

*Data type: Text*

#### **newestCommentVisibleRole**

Search for issues with a visibility restrictions applied for a specified project role for the newest comment added using the newestCommentVisibleRole keyword.

|  |
| --- |
| ```text newestCommentVisibleRole = "Project Managers" ``` |

*Data type: Text*

## Issue Links

#### **hasLinkType**

Search issues based on the link type name using the hasLinkType keyword.

|  |
| --- |
| ```text hasIssueLinks = "is blocked by" //or hasIssueLinks in ("is blocked by", "is cloned by") ``` |

#### **hasIssueLinks**

Search issues based on the link type inward description using the hasIssueLinks keyword.

|  |
| --- |
| ```text hasLinkType = Blocks //or hasLinkType in (Blocks, Cloners) ``` |

#### **countOfLinks**

Search issues based on the number of links it has. This can be used to determine if the issue has any links at all using the linksNumber keyword.

|  |
| --- |
| ```text countOfLinks > 0 ``` |

*Data type: Number*

## Subtasks

#### **countOfSubtasks**

Search issues based on the number of subtasks it has. This can be used to determine if the issue has any subtasks at all using the countOfSubtasks keyword.

|  |
| --- |
| ```text countOfSubtasks > 0 ``` |

*Data type: Number*

**Contents**