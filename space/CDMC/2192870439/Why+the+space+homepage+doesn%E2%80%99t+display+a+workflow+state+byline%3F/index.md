# Why the space homepage doesn’t display a workflow state byline?

You want to apply a **Comala Document Management** workflow to a space, including its homepage. However, the **workflow state byline** does not appear on the homepage after the workflow is applied. Additionally, you cannot apply a **single-page workflow** to the homepage.

## **Problem**

Comala Document Management **does not support** a workflow app for a space’s homepage. As a result, the homepage **will not display** a workflow state byline.

This limitation is due to restrictions within the **Atlassian Confluence Cloud** platform.

This **Atlassian Cloud limitation** also affects **Comala Publishing**. It prevents the source space homepage from being published to the target space, which means the homepage will not display a **publishing lozenge**.

## **Workaround**

To manage content effectively, we recommend:

- Designing the **homepage** using only **page macros** such as the **Page Tree Macro** or **Children Macro** to display space content.
- A **Comala Document Management** workflow can be applied to manage content on child pages.

This approach ensures proper workflow management while working within Confluence Cloud limitations.