# Analyze freely. Deploy precisely.

## Overview

Configuration changes rarely happen in isolation. New workflows are created, automation rules evolve, permission schemes are updated, and before long, it becomes difficult to answer a simple question:

**What has changed, and what should I deploy?**

Over time, Jira environments naturally drift apart. Multiple administrators make changes, projects evolve, and it becomes increasingly difficult to know which differences are intentional, which are still being tested, and which are ready for production.

Without dedicated comparison tools, administrators are often left to manually investigate configuration differences before deciding what to deploy. CMJ Cloud helps simplify that process.

First, [compare snapshot versions](/cms_trial/space/CMJC/3417473252/Compare+snapshots/) to understand how your Jira configuration has evolved. Then, [create a custom snapshot](/cms_trial/space/CMJC/2506522887/Create+and+manage+snapshots/) containing only the projects and configuration elements you want to deploy.

By separating analysis from deployment, you gain greater visibility into your Jira configurations while maintaining precise control over what reaches your destination environment.

---

## Example scenario

Imagine you're preparing a production release.

Over the past month, several administrators have been working in your development environment. You know that changes have been made to a few workflows and permission schemes, and that a new notification scheme has been introduced. However, you're not sure exactly which configuration objects were modified, how extensive the changes are, or whether everything is ready for production.

Rather than deploying the latest snapshot and hoping it contains only the changes you want, you first need to understand exactly what has changed.

Once you've identified the changes that are ready, you want to package only those configuration elements into your deployment, leaving everything else behind.

This is where the snapshot comparison and granular scope selection features work together.

---

## Understand what changed

Begin by comparing two versions of the same snapshot.

Comparing snapshot versions gives you a clear view of how your Jira configuration has evolved before you make any deployment decisions. Instead of reviewing every project manually, you can immediately see which configuration elements have changed.

The comparison categorizes configuration elements using the following filters:

- **Unique to the source snapshot** – Configuration elements that exist only in the source version.
- **Unique to the destination snapshot** – Configuration elements that exist only in the destination version.
- **Different** – Configuration elements that have changed.
- **Identical** – Configuration elements that are the same in both snapshots.

![image (7).png](/cms_trial/assets/f9cb57d6-fd7c-4db2-b093-cd9f5dc7666e.png)

From there, you can inspect individual configuration elements to understand exactly what changed before deciding whether those changes belong in your next deployment.

Snapshot comparison is useful beyond just deployment planning. Teams also use it to validate testing, investigate unexpected configuration changes, audit environments, and monitor configuration drift over time.

Returning to our production release example, the comparison reveals that three workflows have been changed, a new notification scheme has been added, and two permission schemes have been modified. With that information, you can confidently decide which updates are ready to be included in the next release.

---

## Choose only the changes you need

Once you've identified the changes you want to promote, create a new snapshot using the new granular scope selection to deploy precisely.

Instead of exporting your entire system, you can decide exactly what goes into your snapshot. Whether you're creating a full system snapshot or a targeted snapshot, you stay in control of what goes into your deployment. Choose:

- **Specific elements** to build a targeted custom snapshot by selecting only the projects and configuration elements you need.
- **Everything supported** to create a system snapshot containing all currently supported projects and configuration elements.

![Screenshot 2026-07-01 at 14.33.44.png](/cms_trial/assets/51c98e9b-c5ef-48ff-a192-c875a9e3cf3f.png)

CMJ automatically analyzes your selection and includes any required dependencies, so you don't need to manually identify or recreate related configuration objects. The resulting snapshot contains everything needed for the selected configuration elements to function correctly after deployment.

In most cases, custom snapshots are easier to review, validate, and troubleshoot than system snapshots while reducing the likelihood of introducing unrelated configuration changes into production.

In our example, only the updated workflows are ready for production. By selecting just those workflows, CMJ automatically includes their dependent configuration elements, creating a complete deployment package without bringing along unrelated changes from the development environment.

---

## Deploy precisely

By the time you're ready to deploy, the difficult decisions have already been made.

You've reviewed the changes, selected only the configuration elements that belong in the release, and packaged them into a custom snapshot. Instead of deploying every change made since the last deployment, you're moving forward with only the configurations you've intentionally chosen.

The result is a deployment process that's easier to review, easier to validate, and less likely to introduce unintended configuration changes into your destination environment.

---

## Bringing it all together

The [Snapshot Comparison](/cms_trial/space/CMJC/3417473252/Compare+snapshots/) and [Granular Scope Selection](/cms_trial/space/CMJC/2506522887/Create+and+manage+snapshots/) features are designed to work together as parts of the same workflow rather than as independent capabilities.

Snapshot comparison helps you understand how your Jira configuration has changed over time, while granular scope selection lets you act on that insight by creating custom deployment packages containing only the configuration elements you've approved.

Together, these features help teams take a more controlled approach to Jira configuration management. Rather than relying on assumptions or deploying every accumulated change, administrators can understand what has changed, make informed decisions, and deploy only the configuration elements that are ready.