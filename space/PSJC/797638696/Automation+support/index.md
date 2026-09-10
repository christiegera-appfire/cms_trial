# Automation support

This page describes which Power Scripts automation triggers and features are supported with Jira Product Discovery projects and which are not.

## Why some triggers don’t work

Jira Product Discovery uses simplified workflows instead of the highly configurable workflows found in standard Jira projects. This means automation triggers that depend on workflow customization aren't available. However, event-based automation can handle most of the same use cases.

## Compatible automation

These automation features work fully with Product Discovery because they operate outside individual projects and aren't affected by the simplified workflow structure:

- [SIL Listeners (event-based actions)](/cms_trial/space/PSJC/490997990/SIL+Listeners/)
- [SIL Runner dashboard gadget](/cms_trial/space/PSJC/490998486/SIL+Runner+Gadget/)
- [SIL Scheduler](/cms_trial/space/PSJC/490998807/SIL+Scheduler/)
- [Webhooks](/cms_trial/space/PSJC/490996447/Webhook+configuration/)

## Incompatible automation

Jira Product Discovery doesn't support workflow-based automation because it uses simplified workflows. Event-based automation with SIL Listeners provides an alternative for many use cases.

The following automations are not available with Product Discovery:

- [SIL Panel](/cms_trial/space/PSJC/490998470/SIL+Panel/)
- The following [Workflow automation](/cms_trial/space/PSJC/490999005/Workflow+Automation/) triggers:

  - [Conditions](/cms_trial/space/PSJC/584581177/Writing+Conditions+and+Validators/)
  - [Validators](/cms_trial/space/PSJC/584581177/Writing+Conditions+and+Validators/)
  - [Post Functions](/cms_trial/space/PSJC/490999217/Writing+Actions+(Post-Functions)/)