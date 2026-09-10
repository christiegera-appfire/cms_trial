# Best practices for Rich Filters in Jira Cloud

There are several key differences between Rich Filters Data Center and Rich Filters for Jira Cloud, as listed on the [Feature Parity](/cms_trial/space/RFCDOC/783942143/Feature+parity+%E2%80%93+Cloud+vs+Data+Center+comparison/) page. Here, you can find a list of best practices that can help you work around these differences and get the most out of Rich Filters in the Cloud environment.

## Related pages:

[How to Migrate to Cloud](https://appfire.atlassian.net/wiki/spaces/RFP/pages/803406935)

[Feature parity](/cms_trial/space/RFCDOC/783942143/Feature+parity+%E2%80%93+Cloud+vs+Data+Center+comparison/)

## Best practices

The following list outlines practical tips for building Rich Filters and dashboards in Jira Cloud, including JQL recommendations, dashboard design, and date-specific guidance. Following these practices helps ensure dashboards stay fast, accurate, and within platform limits.

### 1. Base filter design

**Keep filters fast and focused**

- Avoid overly broad queries:

  ```text
  project = ABC
  ```
- Prefer narrow, relevant queries:

  ```text
  project = ABC AND statusCategory != Done AND updated >= -90d
  ```
- Exclude inactive or old work items to stay below the 50,000 work item limit.

**Break large filters into smaller, purpose-built filters**

- Instead of a single large filter:

  ```text
  project = ABC
  ```
- Create multiple targeted filters:

  ```text
  project = ABC AND issuetype = Bug
  project = ABC AND issuetype = Story
  project = ABC AND issuetype = Task
  ```
- Combine them in dashboards using Rich Filters views or smart counters.

---

### 2. Use smart filters

**Simplify dashboard interactivity**

- Use smart filters instead of long JQL statements.
- Example: “Priority Grouping” smart filter values:

  - High: `priority in (Highest, High)`
  - Medium: `priority = Medium`
  - Low: `priority in (Low, Lowest)`

This keeps base filters clean while giving users flexible filtering.

---

### 3. Relative dates and time filters

**Use relative dates instead of fixed dates**

- Avoid static dates:

  ```text
  updated >= "2024-01-01"
  ```
- Prefer dynamic ranges:

  ```text
  updated >= -30d
  created >= -90d
  ```

**Pair relative dates with status filtering**

```text
project = XYZ AND statusCategory != Done AND updated >= -60d
```

**Use Jira date functions for reporting periods**

- Examples:

  ```text
  updated >= startOfWeek()
  updated <= endOfWeek()
  created >= startOfMonth(-1)
  ```

**Leverage rolling windows for KPIs**

- Common rolling windows: 7, 14, 30, 90, 180 days

```text
resolved >= -7d
created >= -90d
updated >= -14d AND priority = High
```

**Use Rich Filters time filters instead of hardcoding dates**

- Allow users to switch time ranges without editing JQL: Last 7 days, Last 30 days, This Quarter, YTD.

---

### 4. Performance and maintenance

**Monitor dashboard performance**

- Track work item counts for each base filter
- Identify slow-loading filters
- Check filter usage (“Last Used” in Cloud) for cleanup

**Use static filters for expensive queries**

- Expensive JQL (for example, text searches or multi-project queries) should use static filters to store results rather than recomputing every load.

**Naming conventions for maintainability**

- Examples:

  ```text
  RF - ABC - Bugs - Base Filter
  RF - ABC - Smart: Priority Grouping
  RF - ABC - View: Leadership
  ```

**Use views to separate audiences**

- Executive view, Engineering view, Support KPIs
- Reduces clutter and avoids unnecessary filter duplication.

---

### 5. Avoid performance traps

- Avoid text searches on date fields:

  ```text
  text ~ "2023"  → slow, expensive
  ```
- Always use date functions like `startOfMonth()`, `-30d`, or `resolved >= -7d`
- Clean up unused filters before migration to Cloud
- Use Rich Filters Cloud features like automatic archive and bulk operations to maintain a healthy dashboard environment

If you need further assistance, please don’t hesitate to submit a support ticket through our [Customer Support Portal.](https://appfire.atlassian.net/servicedesk/customer/portal/11)