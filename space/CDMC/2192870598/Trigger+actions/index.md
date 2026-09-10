# Trigger actions

## Overview

Trigger actions let you automate tasks when a workflow event occurs, such as assigning reviewers, changing state, sending custom email notifications, or updating page restrictions and labels. You can set one or more actions for a named event. When the event occurs, the trigger checks that any required conditions are met before executing the actions.

For example, the following trigger displays an on-screen notification when the state changes to **Rejected**.

![Comala visual editor workflow trigger with state change event and setmessage action](/cms_trial/assets/6195521c-655f-494d-b661-19389126c520.png)

You can add one or more actions to a workflow trigger using the **Add Action** option in the visual editor.

![Comala visual editor trigger action setmessage configuration](/cms_trial/assets/c128c88d-22b5-4e29-a3c8-7c3993e8e8ea.png)

You can customize some workflow actions in the visual editor by setting **Action Parameters**, such as the content of a notification or the users and groups included in a page restriction.

For example, the **set message** action uses these parameters:

- **Type** (required): the message panel style, either *Info, Warning,* or *Error*

- **Body** (required): the message text

- **Title** (optional): a heading for the message

Some workflow trigger actions are part of a gradual rollout of new features and may not be available in all instances yet.

## Trigger actions

- [State actions](/cms_trial/space/CDMC/3637903679/State+actions/)
  - [change-state](/cms_trial/space/CDMC/2193787075/change-state/)
  - [set-expiration](/cms_trial/space/CDMC/2193950357/set-expiration/)
  - [clear-expiration](/cms_trial/space/CDMC/2193950419/clear-expiration/)
- [Notification actions](/cms_trial/space/CDMC/3638493477/Notification+actions/)
  - [set-message](/cms_trial/space/CDMC/2193853008/set-message/)
  - [clean-messages](/cms_trial/space/CDMC/2193852928/clean-messages/)
  - [send-email](/cms_trial/space/CDMC/2193852968/send-email/)
- [Page restrictions actions](/cms_trial/space/CDMC/3637608858/Page+restrictions+actions/)
  - [add-restrictions](/cms_trial/space/CDMC/2193590021/add-restrictions/)
  - [set-restrictions](/cms_trial/space/CDMC/2193458748/set-restrictions/)
  - [remove-restrictions](/cms_trial/space/CDMC/2193688848/remove-restrictions/)
- [Label actions](/cms_trial/space/CDMC/3638493580/Label+actions/)
  - [add-labels](/cms_trial/space/CDMC/2193458799/add-labels/)
  - [clean-labels](/cms_trial/space/CDMC/2193491914/clean-labels/)
  - [remove-labels](/cms_trial/space/CDMC/2193787135/remove-labels/)
- [Page copy actions](/cms_trial/space/CDMC/3638493674/Page+copy+actions/)
  - [copy-page](/cms_trial/space/CDMC/2193950590/copy-page/)
- [Metadata actions](/cms_trial/space/CDMC/3637575910/Metadata+actions/)
  - [set-metadata](/cms_trial/space/CDMC/2193723026/set-metadata/)
  - [increment-metadata](/cms_trial/space/CDMC/2400584152/increment-metadata/)
- [Publishing actions](/cms_trial/space/CDMC/3638395140/Publishing+actions/)
  - [publish-page](/cms_trial/space/CDMC/2193950517/publish-page/)