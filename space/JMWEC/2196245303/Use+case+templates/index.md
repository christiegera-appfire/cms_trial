# Use case templates

The **Use case templates** page of the JMWE Administration pages lists more than 30 prebuilt configurations covering many of the most common use cases for JMWE. These provide quick installation of Event-based actions, Scheduled actions, and other workflow automations.

**Note**: some Use Case templates may require customization for your specific instance.

## Filter and search

The top of the **Use Case templates** page includes tools for finding a template to suit your needs, including:

- **Type filter** - Use the pulldown menu to select the type of automation you’re seeking, such as Event-based actions, Scheduled actions, and post functions.
- **Search** - Search by template name and description.

## Apply a template

To use a template in your JMWE automations, click **Apply use case**. JMWE will open to the configuration screen appropriate to the template selected. For example, the Automation Rule Builder will open for Event-based actions and Scheduled actions, or a window will open prompting you to select a Project, Workflow, and Transition when using a post function template.

A few points to keep in mind when implementing Use case templates:

- Many templates require specific configurations for your instance; for example, you may need to select a Project or workflow to which the template should be applied.
- It is **highly recommended** that you review all configurations for the template before saving it to your instance.
- Thorough testing should be done, preferably in a test instance, before implementing templates in a Production environment.

![JMWE for Jira Cloud use case templates administration with template selection](/cms_trial/assets/fa70cbc1-2c61-422b-b92d-0348556ee8ba.png)