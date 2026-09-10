# Support and troubleshooting for migration

## Migration problem

If you have a problem and the migration is unsuccessful, you should check the details and assessments in the Confluence Cloud Migration Assistant and rerun the migration.

![contentId-2193130141](/cms_trial/assets/20e59220-268f-4af9-830d-f636bf4740d6.png)

If you can't resolve a migration problem using the Confluence Cloud Migration Assistant, [Appfire support](http://appf.re/support) can review the data on your Comala Document Management app usage in your hosted instance.

To help our team help you, use the [support console](https://appfire.atlassian.net/wiki/spaces/CDML/pages/619072030) in the Comala Document Management Server or Data Center app to download a **Support package** file and attach it to the [support ticket](http://appf.re/support).

## Create a support package for a support request

For help in analyzing the use of your server instance in Comala Document Management, you can use the server app [support console](https://appfire.atlassian.net/wiki/spaces/CDML/pages/650250352) to capture helpful information on your current usage of the Comala Document Management app.

- Create an Appfire Comala support package for each space using the [document management support console](https://appfire.atlassian.net/wiki/spaces/CDML/pages/650250352) option in Space Tools.

![contentId-2193130141](/cms_trial/assets/65e778cd-36b6-48cf-8470-c2922f265433.png)

Add the **Usage data** and the **Support package** to a related [support](https://appfire.atlassian.net/wiki/spaces/CDML/pages/649266094) request.

## Moving your page workflows

Page workflows are not migrated to the cloud. If required, you can consolidate these as space workflows in two ways:

- **Manually** - [Consolidating the page workflow in each space](/cms_trial/space/CDMC/2192902721/Moving+your+workflows+to+the+cloud/)
- **Scripted** - Bulk consolidation using the following script:

**Consolidate page workflows script**

**Script**: ▢   
**How to run it:**`python3 consolidate_page_workflows.py page-workflows.csv`  
**Description**: This script reads the CSV file containing page workflows from the **Workflows Usage Report** and consolidates them into space-level workflows using the Confluence REST API. When run, the script:

1. Prompts you to choose the grouping logic:

   - `1`: Group by Space Key + Workflow Name
   - `2`: Group by Space Key + Workflow Name + Workflow Markup
2. Automatically generates a unique label for each group:  
   `WorkflowName` (cleaned) + incremental number (e.g., `SimpleApproval1`)
3. Sends a `curl` request per group to the Confluence REST API to perform the consolidation.

In both cases, page workflows are consolidated as a label space workflow.

See: [Moving your workflows to the cloud](/cms_trial/space/CDMC/2192902721/Moving+your+workflows+to+the+cloud/)

## Complex Confluence instance

Some things can [increase the complexity of your migration](https://www.atlassian.com/migration/plan/cloud-guide#understand-migration-complexity), and you might need some help planning. For example, if the migration involves

- a large amount of data or users
- multiple products and apps

The [Atlassian Migration Guide](https://www.atlassian.com/migration/plan/cloud-guide#atlassian-team) includes a range of resources and guides.

You can contact our [Appfire support](http://appf.re/support) team or an [Atlassian Solution Partner](https://www.atlassian.com/migration/help/find-migration-partner) to help you find the best fit for migrating large instances or those with many users and user groups.