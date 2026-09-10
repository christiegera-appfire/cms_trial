# Required skills field

The **Required Skills** value can be synchronized with a Jira field.

Default field - Labels (labels)

![contentId-1918767792](/cms_trial/assets/e273ecb1-2024-4b55-a98c-451681425ec2.png)

## General vs. custom configuration

Field mapping can be configured per Jira project.

Custom synchronization settings are on the right. Settings are created per a Jira project (not per Box).

## Not synchronized

Skills data is stored only in the app.

## Synchronization with a "labels" field

All fields of type "label" are supported.

![contentId-1918767792](/cms_trial/assets/86b394aa-99e6-46b0-9941-c977c5c7b93f.png)

Synchronization with the "labels" field makes it possible to:

- execute bulk changes → you can handle multiple issues at the same time and assign/remove skills
- Search for tasks → skill information can be used in Jira searches
- automate skill assignment → you can use 3rd party add-ons such as Script Runner and Adaptavist

### Bi-directional sync

You can update the skill details in the way that you find most convenient:

- When you add/remove a **skill,** a matching value is added as a label.
- When you add/remove a **label,** a matching skill is added.

Naming convention

**skill#skillname** → skill labels always start with "**skill#,"**making it easy to find and add an appropriate label. Spaces between words are replaced by "\_" underscore signs.

![contentId-1918767792](/cms_trial/assets/a0efbce6-fe64-4735-bf77-8ee11d0b9add.png)

### Requirements

You can't create a new required skill using a "labels" field.

The app can only recognize skills that already exist in Administration > Skills.

If a user adds a skill label when no corresponding skill exists in the app, the label behaves like a standard Jira label. Retroactively adding the skill to the app won't trigger the processing of tasks that already have labels.