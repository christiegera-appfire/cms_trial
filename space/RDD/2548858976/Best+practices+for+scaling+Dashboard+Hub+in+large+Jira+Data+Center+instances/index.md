# Best practices for scaling Dashboard Hub in large Jira Data Center instances

This page offers recommendations and tips for enhancing the performance of dashboards in large data center environments.

## **1. Manage access to Dashboard Hub through user groups**

While Dashboard Hub for Data Center does not currently include a dedicated permission to restrict who can *create dashboards*, you can effectively control usage and system load by limiting access to the application through Jira user groups.

We recommend the following approach:

- Start by granting access to a **specific group** (for example, *dashboard-hub-users* or *reporting-creators*) that includes only administrators, reporting specialists, or advanced users.
- Keep Dashboard Hub restricted for general usersuntil you confirm the system performance behaves as expected.
- Gradually expand access by adding more groups as adoption increases and system metrics remain stable.

This approach helps prevent mass dashboard creation, reduces the number of concurrent data queries, and allows your team to monitor the impact on performance in a controlled manner.

Dashboard Hub for Data Center relies entirely on your existing Jira infrastructure and database. It does not use external services or storage engines, so the primary scalability factors are the number of dashboards created and the volume of data queried.

## **2. Roll out access gradually and monitor usage**

For large Jira Data Center environments, the best approach is to introduce Dashboard Hub in controlled phases. This helps your administrators and reporting teams observe adoption patterns, measure system impact, and adjust access or dashboard design if necessary.

We recommend the following staged rollout plan:

### **Phase 1: Pilot group**

1. Start with a small number of users (for example, Jira administrators and reporting specialists).
2. Validate permissions, data sources, and general dashboard performance.
3. Collect early feedback about usability and dashboard load times.

### **Phase 2: Power users and team leads**

1. Extend access to users who will actively create or maintain dashboards for their teams.
2. Encourage best practices in dashboard design (number of gadgets, slides, refresh rates).
3. Monitor concurrent usage during working hours.

### **Phase 3: Organization-wide adoption**

1. Gradually add new user groups once stability and performance are confirmed.
2. Communicate internally about recommended dashboard usage limits and how to request access.

### **Phase 4: Continuous monitoring**

1. Periodically review which dashboards are used the most.
2. Archive or delete obsolete dashboards to keep the system tidy.
3. Adjust group permissions if some areas of the organization do not require Dashboard Hub.

Monitoring doesn’t require additional tools; you can track usage through Jira’s audit logs, and your system administrators can check app-level activity via standard Data Center monitoring tools.

## **3. Optimize dashboards for performance and usability**

The number of dashboards in the system is not a direct performance concern; the main factor is the amount of data being queried and displayed when dashboards are viewed, especially if many users access them simultaneously.

To ensure a smooth experience across your instance, we recommend the following best practices:

- **Limit dashboard complexity:** Use a maximum of three slides per dashboard, with no more than nine to ten gadgets per slide. This keeps load times predictable and prevents large concurrent data requests.
- **Group related information logically:** Instead of creating very large dashboards, split content into multiple smaller dashboards by use case, for example, *Team Performance*, *Project KPIs*, or *Incident Overview*.
- **Avoid excessive refresh rates:** If a dashboard includes gadgets with live data, for example, Jira issues or metrics from external data sources, use reasonable refresh intervals (default or higher) to reduce repeated API calls.
- **Monitor usage patterns:** If possible, identify the dashboards most often used by large groups of users and review their structure; simplifying them can improve the experience for everyone.

Performance in Dashboard Hub DC scales mainly with the number of concurrent gadget queries. Keeping dashboards concise ensures the system remains responsive even under heavy load.

## **4. Technical considerations for large environments**

Dashboard Hub for Data Center is designed to run entirely within your Jira infrastructure and uses Jira’s APIs to collect and visualize data (or other APIs, depending on the gadget).

Performance mainly depends on concurrent dashboard usage and the complexity of the data queries executed by gadgets. To ensure optimal performance in large environments, administrators can configure specific parameters under **Global Settings** → **Performance Options**, as described in [Manage Performance Options](/cms_trial/space/RDD/811106832/Manage+Performance+Options/).

![Dashboard Hub scaling recommendations for large Jira Data Center instances](/cms_trial/assets/dc9d876d-c295-4423-818f-0606ef40517c.png)

### Performance Options

- **Auto refresh interval**

  - Defines how often gadget data is automatically updated.
  - For large instances, it’s recommended to increase the interval (10–15 minutes) or even disable automatic refresh to reduce background API calls.
  - Users can still refresh dashboards manually when needed.
  - *High-priority gadgets* are updated every minute regardless of this setting.
- **Issue limit per gadget**

  - Controls the **maximum number of Jira issues** returned by JQL queries.
  - Default: 2,500.
  - Reducing this limit can significantly improve chart rendering time for large issue sets.
  - For global or project-level dashboards, keep queries focused and indexed.

- **Maximum parallel requests**

  - Sets the **number of concurrent threads** Dashboard Hub uses to request data from Jira or external sources.
  - Default: 6.
  - Increasing this value can improve load times, but it also increases CPU usage. In very large instances, it’s safer to keep this value low (2–3).

These settings can be adjusted without downtime and allow administrators to fine-tune Dashboard Hub’s behavior to match their infrastructure’s capacity and user concurrency patterns.