# Shared Nunjucks Templates

![JMWE Administration page listing Shared Nunjucks Templates](/cms_trial/assets/92ef0321-0e94-44e4-a07b-c79308383a1e.png)

**JMWE for Jira Cloud** provides support for shared Nunjucks templates. A shared template can be used across many post-functions, and updating a shared template through the administration page will update the template everywhere it is used, increasing maintainability and efficiency.

A shared Nunjucks template can also be used to implement lengthy templates - longer than those normally possible inside post-functions.

![JMWE for Jira Cloud shared Nunjucks templates editor with template management](/cms_trial/assets/834b9810-ceee-46d9-9af7-90b39a8f9222.png)

The sections below explain how to create shared Nunjucks templates and reuse them from JMWE post functions or the [Nunjucks tester](/cms_trial/space/JMWEC/465503776/JMWE+Administration/).

## Creating a shared Nunjucks template

1. Log in to your Jira Cloud instance as an administrator.
2. Click the **Settings** icon ⚙️ in the upper right corner and select **Apps**.
3. Under *JIRA MISC WORKFLOW EXTENSIONS* in the left-hand panel, click **Shared Nunjucks templates**.
4. At the top of the list of shared templates, click **Create new template**.
5. The **Shared Nunjucks Template Editor** (Figure 2, right) will open.
6. Configure and build the template:

   1. **Template name** - Give the template a name.
   2. **Description** - Give the template a description, if desired.
   3. **Nunjucks template** - Enter the Nunjucks template.
7. Optionally, you can test the template against any issue using the **Test Nunjucks template…** button in the upper right corner of the editor.
8. Click **Save**.

## Working with Templates

Within the list of Shared Nunjucks templates (Figure 1, right), there are several tools for sorting, filtering and working with your templates:

- Use the **Filter** button ( ▢ ) to filter by any column.
- Use the **Sort** button ( ▢ ) to sort a column.
- Use the **Action** button ( click **Edit** to the right of the Shared Template name.
- To delete a template, click **Delete** to the right of the Shared Template name.

## Import/Include a Nunjucks template

You can [import](https://innovalog.atlassian.net/wiki/spaces/MWECS/pages/138447486/Tags+and+Expressions#TagsandExpressions-import) or [include](https://innovalog.atlassian.net/wiki/spaces/MWECS/pages/138447486/Tags+and+Expressions#TagsandExpressions-include) a shared Nunjucks template into your post-functions or Script tester using the respective tags available in Nunjucks.

### Limitations of macros

Nunjucks macros have two limitations about which you need to be aware:

1. Macros do not have access to the *global variables* of the calling Nunjucks template (such as `issue`, `currentUser`, etc.) If you need to access these variables from the body of the macro, you need to pass them as *parameters* to the macro.
2. Macros cannot execute asynchronous code. This means that *any filter that calls the Jira API* will fail when used inside a macro, and the failure is *silent* (no error message). This is a major limitation of Nunjucks macros. The workaround is *not to use macros* and instead `include` Shared Templates.
3. Macros cannot be used inside an `{% if %}` block. When a macro needs to be used in an if block, use **ifAsync** instead. For example, instead of:

   ```text
   {% if true %}
   {% import "getReporter" as Reporter %}
   {{ Reporter.getReporter("Test",1) }}
   {% endif %}
   ```

   Use:

   ```text
   {% ifAsync true %}
   {% import "getReporter" as Reporter %}
   {{ Reporter.getReporter("Test",1) }}
   {% endif %}
   ```

## Examples

**Example 1:** To set the Priority of the issue based on its impact.

1. Go to **Shared Nunjucks templates** in the JMWE administration pages.
2. Enter `Mappings` into the **Name** field and click **Add**.
3. Provide the following template in the Nunjucks editor.

   ```javascript
   {% macro priorityFromImpact(impact) %} 
       {%- if impact == "Company wide" %}
           Highest
       {% elseif impact == "More than one project" %}
           High
       {% elseif impact == "Single project" or impact == "Individual" %}
           Medium
       {% else %}
       	Low
       {% endif %}
   {% endmacro -%}
   ```
4. To access the template in a post-function, go to the configuration of the post-function.
5. Write the following template in the editor.

   ```javascript
   {% import "Mappings" as Mappings %}
   {{Mappings.priorityFromImpact(issue.fields.Impact)}}
   ```
6. You can test the written template against any issue using the Nunjucks tester and verify the result.

**Example 2:** To provide a resolution date excluding the weekends and based on the priority of the issue:

1. Go to **Shared Nunjucks templates** in JMWE administration pages.
2. Enter `addDateExcludingWeekends` in the **Name** field and click **Add**.
3. Provide the following template in the Nunjucks editor.

   ```javascript
   {% set priority = issue.fields.priortiy.name %}
   {% if priority == "Highest" %}
   	{% set nod = 2 %}
   {% elseif priority == "High"%}
   	{% set nod = 4 %}
   {% elseif priority == "Medium"%} 
   	{% set nod = 6 %}
   {% elseif priority == "Low"%} 
   	{% set nod = 8 %}
   {% else %}
   	{% set nod = 6 %}
   {% endif %}
   {{ from | date('businessAdd', nod ) | date() }}
   ```
4. To access the template in a post-function, go to the configuration of the post-function.
5. Write the following template in the editor.

   ```javascript
   Hi {{issue.fields.reporter.displayName }},

   This is in response to the ticket : {{issue.key}} that you created with us on {{issue.fields.created | date("DD/MM/YYYY") }}. Your issue will be resolved on or before :{% set from = issue.fields.created %} {% include "addDateExcludingWeekends" %}

   Regards,
   {{ issue | projectInfo | field("lead.displayName")}}
   ```

**Example 3:** To include a shared email body template in an Email Issue post-function:

1. Go to **Shared Nunjucks templates** in JMWE administration pages.
2. Create a new shared template to hold the HTML body of an email and name it `emailHtmlBody`
3. In the HTML Body field of the Email Issue post-function, write the following template:

   ```text
   {% include "emailHtmlBody" %}
   ```