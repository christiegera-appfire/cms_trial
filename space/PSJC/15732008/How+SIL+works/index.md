# How SIL works

Simple Issue Language (SIL) functions as a standalone scripting language that can operate independently of Jira, yet its capabilities are significantly enhanced when operating within the Jira environment.

## SIL architecture

The SIL architecture consists of multiple layers.

![Power Scripts for Jira Cloud SIL architecture diagram](/cms_trial/assets/c4b1b05e-070e-437f-b519-ec76618d5c91.png)

| **See also:**   - [Background and design philosophy of SIL](/cms_trial/space/PSJC/15731838/Background+and+design+philosophy+of+SIL/) |
| --- |

When a SIL script executes, it follows a top-down flow through these architectural layers:

- The *SIL Standard Interpreter* serves as the base layer of the architecture, functioning as the core language processing engine. It provides core scripting functionality that operates independently of Jira and maintains a registry for all functions. This design allows the interpreter to be applied to platforms beyond Jira, such as Confluence.
- The *Jira SIL Interpreter* acts as an extension layer that enhances the capabilities of the standard interpreter. It adds Jira-specific functions to the registry and enables interactions with various Jira components. This layer also provides predefined standard variables, such as the `key` variable that represents the issue key.
- The *Issue Context* forms an optional top layer in the architecture. It provides direct access to field values from the current issue and automatically maps issue fields to accessible variables. This layer significantly simplifies scripts by eliminating the need for explicit field access code, enabling users to reference issue fields directly as variables in their scripts.

---

## Script processing explained

| **When…** | **Then…** |
| --- | --- |
| A script is processed | Depending on the context in which the script is processed, it starts by requesting functionality from the appropriate layer in the downward flow:   - Issue-specific operations pass from the *Issue Context* layer to the *Jira SIL Interpreter*. - Jira operations utilize the core language capabilities of the *SIL Standard Interpreter*.   For additional details, see [The processing contexts](/cms_trial/space/PSJC/15732008/How+SIL+works/) section below. |
| The script references a variable | Variable resolution is handled in the following way:   1. First, it checks the current code block (the immediate scope where the variable is referenced). 2. If not found there, it checks parent code blocks in sequence (moving up the stack of nested blocks). 3. Only after exhausting all code blocks in the script does it then check the issue context (if available).   For additional details, see the [Variable resolution process](/cms_trial/space/PSJC/15732008/How+SIL+works/) section below. |
| Functions are called | The interpreter locates the function in the registry.   - For Jira-specific functions, the J*ira SIL Interpreter* handles processing. - For core language functions, processing is passed to the *SIL Standard Interpreter*. |
| A SIL script modifies issue data | The system tracks changes rather than applying them immediately. Then, it creates temporary (in-memory) clones of the affected issues and records all changes in these temporary copies. |
| Script processing completes | The post-processing phase determines the final outcome. For standard operations, changes are saved to the Jira database. For read-only operations or those with errors, changes are discarded.  For additional details, see the [Post-processing explained](/cms_trial/space/PSJC/15732008/How+SIL+works/) section below. |

---

## The processing contexts

Just like any other programming language, a standalone SIL program contains variables, functions, conditional statements, and loops. When operating within a Jira context, your script gains access to Jira-related functions such as `createIssue` or `linkIssue`. Put simply, the script has Jira context.

Adding an issue context within the Jira context enables access to field values stored in the issue. This includes standard fields like summary, description, and assignee, as well as any custom fields. These fields are predefined and immediately available without requiring explicit variable declarations.

All scripts used by Jira apps operate within Jira context but may not have access to issue context. Scripts without issue context cannot directly use variables such as summary, assignee, or custom fields.

## Variable resolution process

When the interpreter encounters a variable, it follows the resolution process described above, which is similar to other programming languages. Each block of code creates its own variable context, with nested blocks pushing these contexts onto a stack.

During variable lookup, the interpreter begins in the current code block and moves down the stack of contexts. If the variable isn't found in any code block, the interpreter attempts to match it against the fields on the issue (effectively at the bottom of the stack).

These code examples illustrate how SIL works similarly inside and outside Jira and issue contexts. The Jira and issue contexts provide extended functionality that can be used seamlessly within your program.

| **Outside Jira** | **Jira and issue context** |
| --- | --- |
| ```text start block // context_0 - this is your program 	declare variable a; 	start block // push context_1 		declare variable b; 		start block // push context_2 			declare variable c; 			use variable b; // from context_1 		end block // pop context_2 		// no more variable c here 	end block // pop context_2 	// no more variable b here end block 		 ``` | ```text start block // JIRA context // defines JIRA-related functions like createIssue(...) 	start block // issue context - transparent to the user 	// this context contains the issue field definitions 	// you can imagine this contains instructions like 	// string summary = "the summary of the issue"; 		start block 			// context_0 - this is your program 			declare variable a; 			start block // push context_1 				declare variable b; 				start block // push context_2 					declare variable c; 					use variable b; // from context_1 				end block // pop context_2 				// no more variable c here 			end block // pop context_2 			// no more variable b here 		end block // this is the end of the program 	// behind-the-scene post-processing 	end block // pop the issue context end block // pop the JIRA context ``` |

## Post-processing explained

When running inside a Jira context, the system implements a post-processing phase during which the SIL interpreter creates temporary in-memory clones of all modified issues and their respective changes. This approach enables control over several important aspects of program execution:

1. It determines how to handle read-only operations. If a program is designated as read-only, such as a workflow condition or validator, the changes recorded by the interpreter will not be saved to the database or index. For standard operations, the post-processing ensures all recorded changes are properly persisted to the Jira database.
2. It provides reliable error handling. If a program encounters an exception, the system prevents data corruption by discarding all pending changes rather than storing partial modifications that occurred before the error. This approach reports the error while leaving the issue data in its original state, ensuring data integrity even when problems occur.

**Important exception**: Some functions (such as `createIssue`) create immediate changes that cannot be automatically reverted. These functions will persist their changes to the Jira database regardless of whether the script was designated as readonly or encountered errors.