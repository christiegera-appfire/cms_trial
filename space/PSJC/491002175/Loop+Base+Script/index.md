# Loop Base Script

In origami, there are many types of base folds that give you a good starting point for more complex creations. In order to make an origami crane, you would first start out with the folds that make a basic bird base. At the recent Atlassian Summit in Barcelona, we gave visitors to the Power Scripts booth an opportunity a chance to challenge our experts with something we called the 5-minute challenge. We asked users to come to us with a problem they were having trouble solving and the experts would solve the problem using Power Scripts in five minutes or less. Almost by accident, it was discovered that the majority of the solutions actually started out from the very same script base. We realized that this base was an important building block for many different types of scripts, much like a base fold in origami can be used to make many different types of animals. We are calling this script the loop base.

|  |
| --- |
| ```text string [] issues = selectIssues("project = TEMP"); for(string i in issues) { 	runnerLog(i); } ``` |

## Common Use Cases for the Loop Base

- Checking status of sub-tasks or a value of a custom field within the subtask
- Getting the status of linked issues or a value of a custom field within the linked issue
- Creating custom JQL functions
- Escalation services
- Checking attachment names
- Working with database search results
- Working with results from REST API
- Searching for other issues in Jira
- Creating a scheduled service
- And many more

## Sections

The loop base is made of 3 sections, the List section, the Loop section, and the Action section. In its most basic form, the script is only 4 lines of code.

|  |
| --- |
| ```text //List section string [] issues = selectIssues("project = TEMP");   //Loop section for(string i in issues) { 	 	//Action section 	runnerLog(i);  }//end Loop section ``` |

## List Section

The List section is the part of the code where a list of objects is gathered. This list could be any other issues in Jira, a list of sub-tasks, links, rows in a database, etc. In almost every case this section only needs to be one line of code.

### Examples of how to retrieve different types of information in the List section:

|  |
| --- |
| ```text string [] issues = selectIssues("project = TEMP"); ``` |

|  |
| --- |
| ```text string [] subtasks = subtasks(key); ``` |

|  |
| --- |
| ```text string [] links = linkedIssues(key); ``` |

|  |
| --- |
| ```text string [] attchmnts = attachments; ``` |

|  |
| --- |
| ```text string [] data = sql("External_DB", "SELECT * FROM TABLE"); ``` |

## Loop Section

The Loop Section is the part of the code where we go through the list of objects one by one. The syntax for this loop is almost always the same. This section is essentially one line of code with a closing bracket at the end.

### Here is an example of a Loop section:

|  |
| --- |
| ```text for(string i in issues) { ... ``` |

## Action Section

This section is where actions are performed on the objects gathered in the list section. This could be writing a message to the screen, closing a subtask, or writing data to a database. This section could have as little as one line of code or many more lines depending on the action being performed.

### Here are some example actions:

|  |
| --- |
| ```text autotransition("Close", s); ``` |

|  |
| --- |
| ```text %i%.customDate = %i%.dueDate; ``` |

|  |
| --- |
| ```text %i%.priority = "High"; ``` |

|  |
| --- |
| ```text sendEmail("projectmanager", "teamleader1", "Transition executed", currentUser() + " has executed a transition"); ``` |

## Complete Examples:

|  |
| --- |
| ```text string [] issues = selectIssues("statusCategory != Done AND duedate < startOfDay()"); for(string i in issues) { 	%i%.priority = "High"; } ``` |

|  |
| --- |
| ```text string [] subtasks = subtasks(key); for(string s in subtasks) { 	autotransition("Close", s); } ``` |

|  |
| --- |
| ```text string [] issues = selectIssues("project = TEMP"); for(string i in issues) { 	%i%.newCustomField = %i%.oldCustomField; } ``` |

|  |
| --- |
| ```text string [] subtasks = subtasks(key); for(string s in subtasks) { 	%s%.assignee = assignee; } ``` |