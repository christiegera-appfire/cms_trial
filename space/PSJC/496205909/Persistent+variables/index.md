# Persistent variables

## What is a Persistent Variable?

A persistent variable is a variable that is used in a SIL script whose value continues to persist after the script is run. The values of these variables are stored and can be accessed by other scripts run in the future.

## What are they used for?

Often, during the development of an integration or a special customization, people get stuck because of the lack of context. Questions appear: which user clicked the button for the next status? Did the manager approve this item? What was the result of the calculation in the previous step? The traditional way of dealing with such questions was to create additional custom fields to keep that data, usually hidden from users (so excluded from the screens schemes), effectively adding bloat to Jira and ultimately worsening indexing - and general - performance. Enter persistent variables, a way to store this information without introducing a new custom field to bloat the system.

That's one scenario, however there are many more like storing usernames and passwords or storing file paths that are used across multiple scripts. There are many possibilities and basically persistent variables are there for you to store whatever you need.

## Issue context…what?

So basically here are two types of persistent variables, those that are in an issue context and those that are not.

- **In an Issue Context** - The value of these variables are tied to that issue specifically, just like a custom field would be.
- **Out of an Issue Context** - The value of these variables is constant from issue to issue. These variables are global.

**See More**

- [Helper functions](/cms_trial/space/PSJC/496205929/Helper+functions/)
- [Persistent variables in Issue context](/cms_trial/space/PSJC/496205945/Persistent+variables+in+Issue+context/)
- [Persistent variables outside the Issue context](/cms_trial/space/PSJC/496205969/Persistent+variables+outside+the+Issue+context/)
- [Managing persistent variables](/cms_trial/space/PSJC/496205995/Managing+persistent+variables/)