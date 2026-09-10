# Jira string type compatibility with Salesforce string textarea

## Summary

You can get Salesforce HTML formatted fields translated to Jira text area fields starting with release versions 2.36.17 of Connector for Salesforce and Jira.

## Environment

- [Supported Jira version](https://confluence.atlassian.com/support/atlassian-support-end-of-life-policy-201851003.html)

## Resolution

### Prerequisites

- Using Connector for Salesforce and [supported Jira version](https://confluence.atlassian.com/support/atlassian-support-end-of-life-policy-201851003.html).
- Using a Salesforce field with **Text Area (Rich)** type  
  For instructions check Salesforce documentation [Create custom Rich Text Fields for your Object](https://help.salesforce.com/s/articleView?id=ind.doc_gen_create_custom_rich_text_fields_in_your_object.htm&type=5).

  ![TextArea rich.png](/cms_trial/assets/cdbeb465-1c07-4ef3-8b95-51ed916e2691.png)
- Using Jira field with **Paragraph** type

  ![custom fields select.png](/cms_trial/assets/af9e33f0-7036-456e-9c30-e2f8d503fba2.png)

### **Steps:**

1. Set the renderer of this particular Jira field to **Wiki Style Renderer**

   1. First select the **Field Configurations** as illustrated below then navigate to **Settings** area. Click **Issues**.

      ![Settings Issues.png](/cms_trial/assets/48ec1036-8424-4cd3-8821-25de8fdadcb8.png)
   2. Set the renderer to **Wiki Style Renderer.**Optionally, refer to Atlassian’s [guide](https://support.atlassian.com/jira-cloud-administration/docs/specify-field-behavior/?__hstc=72543820.4e76311f874131a99198a462418b615c.1678085111437.1678938561256.1678943188858.44&__hssc=72543820.27.1678943188858&__hsfp=3075603085) on setting the renderer for a particular field.

      ![Wiki Style Recerer.png](/cms_trial/assets/ef67f7ac-56a8-453c-9f13-156137dacb9d.png)
2. Configure the field mapping.  
   ⚠️ Salesforce field with **Text Area (Rich)**  type will be labeled differently, as compared to the general **Text Area** type…

   ![2024-11-27_12-22-56.png](/cms_trial/assets/f65f568c-143d-440e-be26-3b695b3917f4.png)

### Known Limitations

List of common differences in the transition output between **Salesforce’s HTML** and **Jira’s Wiki Marku**

- Images are not rendered
- Code blocks are not rendered