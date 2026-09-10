# Release notes Apr 2, 2025

**Release date**: April 2, 2025

Our team is thrilled to announce the latest release of BigPicture Enterprise Cloud.

---

## New features

This release marks a major evolution for BigPicture Enterprise on Cloud, transforming this powerful PPM extension into a strategic platform that bridges the gap between long-term goals and day-to-day execution. At the enterprise level, aligning strategy with execution becomes increasingly difficult as coordination across teams, departments, and portfolios grows more complex. BigPicture Enterprise addresses these issues with a comprehensive strategic portfolio planning layer, introducing new modules for prioritization, objectives (OKR) tracking, financial oversight, and risk management. With deep Jira integration, faster time-to-value, and support for SAFe®, LeSS, Scrum, hybrid, and custom frameworks, it enables organizations to drive alignment and execution with greater clarity and control.

**Note:** BigPicture Enterprise requires an active instance of BigPicture, licensed separately.

## **Priorities module**

In the new Priorities module, you can prioritize tasks with customizable scoring frameworks (RICE, WSJF, ICE)

![F - Priorities main view (unsorted).png](/cms_trial/assets/9ebd028d-5b67-4ff8-9cb1-0a64f748caaf.png)

Visualize and track priority scores across the modules.

![Foxly - Gantt - edit the score.png](/cms_trial/assets/637dbe50-a515-4d7b-b681-9a88fc2f210c.png)

Use the score to help you plan your work.

![O - Board module.png](/cms_trial/assets/8ab29ef0-bf08-499f-8322-deab210ca2b9.png)

To calculate the priority score, you can use one of the available templates.

![F - Priorities Configuration - List of available priority templates open (no strategic alignment).png](/cms_trial/assets/1a6782fa-e871-4784-aee9-cd1746179722.png)

You can also create new templates and tailor the **Score formula** to align more closely with your specific requirements.

![contentId-1918404311](/cms_trial/assets/844a7022-5eca-4a70-b8a9-b2a9cb04c5a2.png)

[Unmapped macro: button-handy — no content to fall back on]

## OKRs module

The new **OKR module** empowers you to convert strategy into quantifiable key results and connect them to your work. With automated tracking, it provides real-time visibility from teams to leadership.

![OKR - NEW Overview general.png](/cms_trial/assets/3865bf3a-49c6-40a7-9791-13b4414bf329.png)

You can base the task structure on the **Objectives** and **Key Results** to keep things organized.

![Objectives - Gantt task tree.png](/cms_trial/assets/a4b8e702-239d-4c06-8ff2-a335715dd8a0.png)

Key result **progress** can be updated **manually** or calculated **automatically** based on the progress of linked issues.

![OKR - Create KR - progress manual.png](/cms_trial/assets/58938b38-ab2f-4f49-8285-750f03626560.png)

You can view the objectives and key results linked to your tasks across various modules.

![Objectives - Gantt columns.png](/cms_trial/assets/f9b63e9c-c6df-493f-a4ad-1c3c42b435a0.png)

And easily check on their progress.

![OKR - Gantt - KR details v2.png](/cms_trial/assets/080ff087-bdc3-43ff-b52f-e4e460995917.png)

Visit the Key Result details page to gain a comprehensive understanding of progress and historical data.

![OKR - Details page - progress v2.png](/cms_trial/assets/2b55b7e0-7f92-4592-a695-4194900b7edc.png)

The Hierarchy view enhances your understanding of the connections among Objectives, Sub-objectives, and Key Results.

![OKR - NEW hierarchy v3.png](/cms_trial/assets/8976d028-f7ed-4432-bf68-6143e904ed91.png)

The OKR dashboard provides valuable insights into the progress of your objectives and key results.

![OKR - Dashboard.png](/cms_trial/assets/4a84f90e-8b2d-4ca8-b28e-084c89f1d2bb.png)

[Unmapped macro: button-handy — no content to fall back on]

## Financials module

In the Financials module, you can track actual vs. planned costs, configure rates and effort modes, and analyze trends—all without external spreadsheets.

You can conduct a detailed analysis of your data at the initiative box level.

![Financials v2 - initiative view.png](/cms_trial/assets/5b1c1fae-daef-4d90-9611-89de175f7389.png)

Explore the portfolio level to assess the performance of your initiatives.

![Financials v2 - graph with selection.png](/cms_trial/assets/f53756ba-b2bd-42bb-8d41-936ac5097a67.png)

Edit the **calculation settings** to ensure accurate estimation.

- The effort can be provided in

  - story points
  - with hourly time tracking.
- The rate can be

  - set up as a flat rate for an entire initiative box
  - configured per team

![Financials v2 - calculation settings.png](/cms_trial/assets/4316a3bb-8c1b-4e5d-8863-05a7bdfea950.png)

Easily switch between different periods.

![F - TIme period selection.png](/cms_trial/assets/a1330bfb-32c0-46c8-aa55-07ee5b3e859d.png)

Set up a budget for each period.

![F - Budget vP.png](/cms_trial/assets/6f08f77c-92f5-4f4f-b14d-020abf9540b6.png)

The cost baseline feature lets you capture snapshots to effectively compare planned costs against actual spending or current cost forecasts. This helps you maintain control over financial performance, ensuring projects stay aligned with initial objectives and funding.

![image-20250402-095736.png](/cms_trial/assets/8179acf0-8678-4f67-9a52-b71f5ef39a36.png)

Access to the financial information is restricted. **New BigPicture roles** have been added to give you more control:

- **App Financial Admin** - they can configure the calculation settings
- **App Financial Viewer** - readonly access

![F - Roles.png](/cms_trial/assets/d0cef68b-13ed-4799-adf7-4ea672e87491.png)

[Unmapped macro: button-handy — no content to fall back on]

## Risks Management module

The new **Risk Management** module helps you Identify and mitigate risks at every level. Custom registers and scoring models turn risk into a proactive strategy.

In the new module, risks are calculated for Jira tasks. You can calculate risk scores for any selected issue types, such as tasks, stories, and epics. If needed, you can also create a separate issue type specifically for your risks. You have full control over what will be shown in the Risk Management module.

![Risk General settings.png](/cms_trial/assets/62b289b2-7fdc-4687-9385-09989e48c58e.png)

You can create multiple **risk registers** within a single box. If you want, the same tasks can be included in multiple risk registers across the organization. This flexibility means that you can evaluate the same task from different perspectives. For example, one team might analyze a Legal risk, while another team focuses on the Financial risk associated with the same task.

![R - Risk Registers overview.png](/cms_trial/assets/6aa083ae-1cd0-4cd9-b474-18100a6a3e55.png)

Open a risk register to view and manage the score. The new Risk Management module lets you assign multiple scores to the same risks. For example, this feature lets you effectively compare the **inherent risk score** with the **residual risk score**.

![contentId-1918404311](/cms_trial/assets/9e006417-fa55-48c1-9130-f5dd36f16495.png)

The **actual progress** column is essential for monitoring the advancement of tasks aimed at mitigating risks.

![R - Actions progress column.png](/cms_trial/assets/3f4efb4e-dbd5-404c-bfc0-df1cd5a15c8d.png)

To automatically monitor the actual progress, connect tasks using the **is mitigated by** link. If you want to use a different link type, you can change the settings.

![R - mitigate the risk.png](/cms_trial/assets/8af382a9-225e-44e4-b4ef-d1858f155cf6.png)

Review the reports to gain a clearer insight into your risk situation.

![R - Reports v2.png](/cms_trial/assets/e836981b-ac95-4139-ae45-190736b4b98f.png)

The **risk calculation** is flexible and can be customized. You can change the **risk score formula**, **metrics,** and **matrix** to better suit your needs.

![R - Customization p1.png](/cms_trial/assets/73c81df3-f772-41b5-bb77-d91d69905836.png)![R - Customization p2.png](/cms_trial/assets/55cb32bc-603d-4fd6-85ed-1c2457d0fca4.png)

[Unmapped macro: button-handy — no content to fall back on]

---

**Questions and feedback**

- Explore exciting features, pricing updates, reviews, and more on the Marketplace. [unmapped inline: placeholder]
- Stuck with something? Raise a ticket with our [support team](https://appfire.atlassian.net/servicedesk/customer/portal/11).
- Do you love using our app? Let us know what you think [here](https://marketplace.atlassian.com/apps/1215158/bigpicture-enterprise?tab=overview&hosting=cloud).

**Credits**

A heartfelt thank you to our valued customers! Your incredible support and feedback inspire us to continually improve our apps and products. You are the driving force behind why we create software. We appreciate your trust in BigPicture Enterprise Cloud!