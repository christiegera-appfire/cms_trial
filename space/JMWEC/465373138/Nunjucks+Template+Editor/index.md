# Nunjucks Template Editor

![JMWE for Jira Cloud Nunjucks template editor with basic editing interface](/cms_trial/assets/eb28b8bb-ca51-4788-8e86-f2d86e82f005.png)

JMWE for Jira Cloud provides a Nunjucks template editor in various post-function configuration screens. The Nunjucks editor includes an inline help system detailing standard fields, blocks, tags, and global variables. Additionally, the Nunjucks editor in JMWE Cloud is available for all input fields that support Nunjucks annotations. This editor includes a number of features for creating Nunjucks templates, including:

- Automatic code indenting
- Syntax checking
- Keyword colors
- Comments and variables
- Find and Replace
- Keyboard shortcuts

The following functions are available across the top of the editor window:

- **Find** - Search the current template code. Includes searching by regular expression. Hit **Enter** to perform the search.
- **Find Next** - Locate the next occurrence of the search.
- **Replace** - Find and replace text within the current template code. Enter a search term and hit **Enter**, then enter the replacement term. Hit **Enter** again to perform the search and confirm each replacement.
- **Lookup user…** - Search for a user ID to insert into the template code.
- **Lookup group…** - Search for a group ID to insert into the template code.
- **Test Nunjucks template…** - Run a test of the Nunjucks template. Results will be displayed below the editor.

## **Inline Help**

The editor also includes a Help section below the template field. The Help tabs include basic instructions for creating Nunjucks templates and shortcuts for inserting common template elements and fields. The Help section has the following tabs:

**Expected Value** - *Not available in the Nunjucks Template Tester*. This tab lists the possible expected values for the selected field. See [Expected value for each field type](/cms_trial/space/JMWEC/466256753/Expected+value+for+each+field+type/) for more information.

**Nunjucks Basics -** This tab has a brief introduction to Nunjucks.

**Block and Tags** - This tab lists a few important Nunjucks blocks and tags that are common to templates. Hover over any button to get more information, click on it to insert it into the editor. For more information, see [Tags and Expressions](/cms_trial/space/JMWEC/466322168/Tags+and+Expressions/).

**Global Variables**- This tab lists the Global variables that are available for Nunjucks templates. Hover over any button to get the information, click on it to insert it into the editor. For more information, see [Variables in Nunjucks Templates](/cms_trial/space/JMWEC/465373277/Variables+in+Nunjucks+Templates/).

**Issue Fields** - This tab lists the fields of the current issue, the linked issue, or the parent issue (depending on the current context). See Issue Fields for more information.

**Filters**- This tab lists the built-in and custom Nunjucks filters that can be applied to the variables in your Nunjucks templates. Hover over any button to get more information and click on it to insert it into the editor. See [Nunjucks Filters](/cms_trial/space/JMWEC/465373240/Nunjucks+Filters/) and [Custom Filters](/cms_trial/space/JMWEC/465373638/Custom+filters/) for more information.

**More help**- This menu includes links to additional help pages.

## Nunjucks Template Tester

JMWE includes a tool for testing Nunjucks templates; with this tool a template can be built and tested before adding it to a post-function configuration. The tool is available through the **JMWE Misc Workflow Extension** section of Jira Administration. For more information, see [Nunjucks Template Tester](/cms_trial/space/JMWEC/465373737/Nunjucks+Template+Tester/) .

## Example - Building a Nunjucks Template

**Scenario**: An issue is left unassigned.

**Desired Outcome**: The issue should be assigned to the Project Lead.

Steps to resolve:

1. Open the **Create** transition immediately after the start of the workflow.
2. Click **Post Functions**, then click **Add post function**.
3. Select the **Set issue fields** post-function and click **Add**.
4. Set the issue on which the post-function should operate.
5. Select the `Assignee` field.
6. In the **Value** editor, enter `{{` (the editor will autocomplete the closing braces).
7. Click on the **Globals** tab of the Help section.
8. Click on the **issue** variable button.
9. Click on the **Filters** tab of the Help section.
10. Click the **projectInfo** button under the **Other Jira Info**.
11. Click the **field(fieldName)** button under **Objects**.
12. Input `lead.name` in between the double quotes.
13. Under the **Conditional Execution** section, check **Run this post-function only if a condition is verified**.
14. In the new editor, enter `{{` (the editor will autocomplete the closing braces).
15. Click on the **Issue Fields** tab of the Help section.
16. For **Select a field**, select `Assignee`.
17. Under the **Testing the field's value** section click the `issue.fields.assignee==null` button.
18. Click **Add** to add the post-function to the transition.