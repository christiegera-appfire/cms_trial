# Dependencies report

## About the Dependencies report

The **Dependencies** report gives you a quick overview of existing dependencies in your projects.

![Window for adding a new report](/cms_trial/assets/4758dd50-8dfd-4f45-8d8d-5170a3b33cd7.png)

The Dependencies report is in the form of a matrix and presents the names of projects or iterations that:

- are assigned to a given program or project
- have at least one incoming or outgoing dependency (note - both dependency tasks must be open).

![Dependencies square](/cms_trial/assets/256e389b-0694-42cb-88c3-8dbf732e853d.png)

The intersection of the matrix's rows and columns shows the number of dependencies between projects and their iterations from lower levels (PI Iterations, Sprints, etc.).

With more dependencies, the color changes from green to yellow to red.

If there are no dependencies between projects/iterations, the report will present "No data."

**Contrary to the Cross-team dependencies report:**

- This report does not display parent-child dependencies.
- The report also displays dependencies inside a project or iteration (in the fields on the matrix diagonal).

When you click the report field,

![Dependencies square highlighted green](/cms_trial/assets/9c503cc4-5fc9-439c-adef-b24237a96cd3.png)

you will see detailed information about each dependency (divided into projects or iterations between which they occur).

![Dependencies window](/cms_trial/assets/85baec7e-8fba-4129-9138-eb182db2f29e.png)

The report presents soft dependencies (marked as S) or strong dependencies (marked as SE, EE, ES, SS).

The digits between iterations indicate the number of dependencies.

![Soft dependency](/cms_trial/assets/d7bf5154-eb0e-4c89-ab34-a6271ab3aec2.png)

Status is abbreviated:

![In progress status](/cms_trial/assets/c3a8ea04-2bbc-493a-9621-bcc8acaa5e8c.png)

## Report configuration

#### **Name**

You can rename your report using the report configuration.

![Dependencies report configuration](/cms_trial/assets/49beb78e-a00b-474b-a0b8-1d5f7a41d58f.png)

#### Hide/show the same Box dependencies

The cross-team dependencies report can show dependencies on the diagonal (only Soft/Hard links; it does not show Child-Parent relationships within the same team).

This functionality is turned off by default. It can be turned on / off in the report configuration panel (the "Hide dependencies for the same team" checkbox is selected by default).

![Hide dependencies for the same project or iteration](/cms_trial/assets/0f24507e-9829-4b75-ae9e-5fe85b14ba6e.png)

Diagonal cells on the matrix won't contain any information (the information is hidden).

![Dependencies window, empty cells](/cms_trial/assets/3c6eea8d-50ea-4ec5-8a2a-42be4f8c0a4e.png)

Otherwise, those cells contain information on dependencies within a single Box.

![dependencies-single-box.png](/cms_trial/assets/f753059d-a680-484e-8653-2498e50f48d8.png)

**Multi-level Box structure**

![Box tree](/cms_trial/assets/48b23e89-55cf-4490-b79c-01379679baf6.png)

When you create a report in the main program Box, the matrix is based on Program Increments (direct lower level). Under Program Increments, Iterations are nested.

When you don't hide the dependencies:

![Dependencies report configuration window](/cms_trial/assets/11ca4822-b69b-4046-b0dc-c103f6dfd4a6.png)

You can see all dependencies within a Program Increment, including the Iterations it contains.

![Dependencies, iterations](/cms_trial/assets/644eb091-e591-4b85-9643-71bd65a5fe8e.png)

## Export

[BigTemplate](https://appfire.atlassian.net/wiki/spaces/BTc) addon is required.

You can export information of a given cell into .xlsx.

![Dependencies squares](/cms_trial/assets/46ee46af-b74c-451d-92ff-7a8dfdc7bdc7.png)

The file is a flat list (items are not grouped per Box). The following information on both the source and target tasks of a dependency:

- Box name
- task key
- task status
- summary
- dependency type

![Dependencies in MS Excel](/cms_trial/assets/f0bbcbf1-a3d8-41aa-ab51-49030de96207.png)