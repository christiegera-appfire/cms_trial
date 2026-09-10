# Adding extensions to transitions

## Adding extensions

![Copy post function to Shared action button](/cms_trial/assets/49140cd6-75fa-430b-ae6d-a8f8e52523f4.png)

There are three ways to create an extension (a [Post function](/cms_trial/space/JMWEC/465242045/Post+functions/), [Condition](/cms_trial/space/JMWEC/465473735/Conditions/), or [Validator](/cms_trial/space/JMWEC/465474068/Validators/)):

1. Add it directly to a transition through the Jira Workflow Editor. Each extension documentation page has specific steps for this method, including configuration information specific to that extension.
2. Use the **Create new** button on the [JMWE Workflow Extensions](/cms_trial/space/JMWEC/466321411/JMWE+workflow+extensions/) administration page. See the [Create new](https://appfire.atlassian.net/wiki/spaces/MWECS/pages/edit-v2/449839404#Create-new) section for more details on this method.
3. Copy an existing post function to a [Shared Action](/cms_trial/space/JMWEC/466288975/Shared+actions/). See below for more details on this method.   
   ⚠️ **Note**: only post functions can be copied using this method.

Once an extension has been added to a transition, you must publish the workflow for the new extensions to take effect!

**Post function outcome may not be visible immediately**

JMWE post functions are processed remotely and communicate back with Jira to update the issue. This helps ensure the stability and performance of your Jira Cloud instance; however, this also means that some updates may occur in the background after the view issue page has reloaded. A workaround is to enable the "Auto-refresh Issue" feature in the JMWE Configuration page which auto-refreshes the View Issue Screen if a change made by a JMWE post function is detected within 10 seconds after the Transition completes.

## Copying post functions to a Shared Action

You can copy an existing post function to a [Shared Action](/cms_trial/space/JMWEC/466288975/Shared+actions/), creating a copy of the post function that can then be applied to any other transition in your Jira instance through the use of the [Shared action post function](/cms_trial/space/JMWEC/466323396/Shared+Action+post-function/). This is a particularly useful when you have created a complex post function on a single transition, and have determined that it can be used in multiple places within your Jira projects. To copy a post function to a Shared Action:

1. In your Jira instance, click **Settings** in the upper right corner of the screen and select **Issues**.
2. In the left-hand panel, click **Workflows**.
3. For the workflow that contains the post function you want to copy, click the **Action** menu ( [actionmenu icon] ) and select **Edit**.
4. Open the transition that contains the post function.
5. To the right of the JMWE post function name, click the **Copy** button (Figure 1, right).
6. The **Add to shared action** dialog will open. Select an existing Shared action from the top pulldown menu, or enter the name of a new Shared action in **Name**. Click **Confirm**.

## Placement of post functions

The position, or order, of a post-function in the list of post-functions for a transition is an important factor for its proper execution. When adding a new post function to a transition, you must move it to the appropriate position, which depends on the type of transition (a **Create** transition or a standard one) and the type of post function you configure. There are a few considerations:

- **On the Create transition**  
  You need to place any JMWE post functions *after* the **Creates the issue originally** built-in post function. *Failure to do so will result in the creation of new issues raising an error (see*<https://ecosystem.atlassian.net/browse/ACJIRA-961> *for details).*
- **On any regular transition**  
  On a regular transition, most post functions can be placed anywhere in the list, except for post functions that transition issues (see below). However, it is advisable to always move them to the bottom of the list anyway.
- **Transition Issue(s), Transition Parent Issue, Transition Linked Issues post functions**  
  Post functions that automatically transition issues should always be placed at the end of the list of post functions. This applies to the following post functions:

  - [Transition issue(s)](/cms_trial/space/JMWEC/465242612/Transition+issue(s)/)
  - [Transition parent issue (Deprecated)](/cms_trial/space/JMWEC/465242394/Transition+parent+issue+(Deprecated)/)
  - [Transition linked issues (Deprecated)](/cms_trial/space/JMWEC/466257658/Transition+linked+issues+(Deprecated)/)

**Random post function execution order**

Due to the asynchronous nature of Connect post functions, it is not possible to guarantee the order in which post functions are executed. Therefore, you should ensure that your workflows do not depend on post functions being executed in a specific order. If a specific order is required, you can handle this using either the [Sequence of Post functions](/cms_trial/space/JMWEC/466322933/Sequence+of+Post-functions/) post function to be sure that a series of post functions run *in a predictable order* during a transition. Alternately, you can use [Delayed execution](/cms_trial/space/JMWEC/466322009/Delayed+execution/) to delay the start of post functions that are dependent on the completion of others, but there is still no guarantee that the post function will execute in a specific order.