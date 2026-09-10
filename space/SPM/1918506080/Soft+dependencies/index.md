# Soft dependencies

## About soft dependencies

Soft links are just information about a dependency between the tasks and have no scheduling impact.

By default, Soft links are not visible as this type of link is dedicated to showing dependencies using the Board module. Such links are displayed using a dashed line:

![Tasks in Gentt chart connected with soft dependencies](/cms_trial/assets/bba10bd0-31e7-4d70-b98d-2f9ecd71eb96.png)

## Display soft dependencies

How dependencies are displayed varies based on a module.

### Gantt module

![Soft dependencies in Gantt module](/cms_trial/assets/f9fca32b-33ef-4c80-8fe4-75c087d0f816.png)

### Board module

![Soft dependencies in Board module](/cms_trial/assets/202e826b-ca7a-4e37-9ea1-e6f0430e42de.png)

## Soft dependency in Jira task sources

For all Jira task sources: the soft dependency links are mapped by default to the "is blocked by / blocks" Jira link, which is one of the default links automatically created by Jira.

If that link is removed or cannot be detected, the mapping will be left empty.