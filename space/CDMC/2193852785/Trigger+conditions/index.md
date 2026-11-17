# Trigger conditions

## Overview

One or more `"conditions"` can be set for a trigger event in the workflow. Adding a condition to a workflow trigger is optional.

When you add a condition to a trigger, it becomes a requirement for the trigger to execute its [actions](/cms_trial/space/CDMC/2192870598/Trigger+actions/). When the named workflow event occurs, the trigger checks that any required condition is met before executing one or more actions.

## Conditions

However, when you add a **condition** to the trigger, it becomes a **requirement** for the trigger to execute the specified action(s).

The available conditions are:

- [**state**](/cms_trial/space/CDMC/2193787242/State/)-  sets a single named workflow state; the trigger runs only when the document is in that state.
- [**initial**](/cms_trial/space/CDMC/2193659136/Initial/) -  Boolean condition; the trigger runs only when the document is in the workflow’s **initial** state.
- [**final**](/cms_trial/space/CDMC/2193458873/Final/) - a Boolean condition; the trigger runs only when the document is in the workflow’s **final** state.
- [**first-loop**](https://appfire.atlassian.net/wiki/pages/createpage.action?spaceKey=cdmc&title=First%20Loop&linkCreation=true&fromPageId=2193852785)- a Boolean condition for the `on-change-state` event that controls how often the trigger runs: `true` runs only the first time a document enters the state; `false` runs every time.
- [**has label**](/cms_trial/space/CDMC/3784704394/Has+label/) - checks whether a page has one or more specified labels. You can use it with any trigger event.
- [**Approval Name**](https://appfire.atlassian.net/wiki/pages/createpage.action?spaceKey=cdmc&title=Approval%20name&linkCreation=true&fromPageId=2193852785) - checks whether an approval matches a specified name. Use this condition with approval-related trigger events to restrict when workflow actions run.

Boolean condition values `true` and `false` are entered in the code editor **without** quotation marks; for example, `"final":true`.