# Trigger conditions

## Overview

One or more `"conditions"` can be set for a trigger event in the workflow. Adding a condition to a workflow trigger is optional.

When you add a condition to a trigger, it becomes a requirement for the trigger to execute its [actions](/cms_trial/space/CDMC/2192870598/Trigger+actions/). When the named workflow event occurs, the trigger checks that any required condition is met before executing one or more actions.

## Conditions

However, when you add a **condition** to the trigger, it becomes a **requirement** for the trigger to execute the specified action(s).

The available conditions are

- [**state**](/cms_trial/space/CDMC/2193787242/state/)-  sets a single named workflow state; the trigger runs only when the document is in that state.
- [**initial**](/cms_trial/space/CDMC/2193659136/initial/) -  Boolean condition; the trigger runs only when the document is in the workflow’s **initial** state.
- [**final**](/cms_trial/space/CDMC/2193458873/final/) - a Boolean condition; the trigger runs only when the document is in the workflow’s **final** state.
- [**first-loop**](/cms_trial/space/CDMC/2592702860/first-loop/)- a Boolean condition for the `on-change-state` event that controls how often the trigger runs: `true` runs only the first time a document enters the state; `false` runs every time.

Boolean condition values `true` and `false` are entered in the code editor **without** quotation marks; for example, `"final":true`.