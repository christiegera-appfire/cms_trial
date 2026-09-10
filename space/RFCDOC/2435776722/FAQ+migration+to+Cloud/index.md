# FAQ migration to Cloud

### **1. How can I improve my dashboard loading speed?**

The most effective way to optimize performance is to focus your dashboards on the most important information. We recommend:

- Review your current dashboards and remove gadgets you rarely use
- Split large dashboards into smaller, focused ones
- Upgrade to the latest browser versions
- Use recent workstations (above i5 processors)

### **2. Why does my dashboard take time to load initially?**

Dashboards with multiple gadgets and high data volumes (that is, high number of issues, fields and JQL queries) require time to set up during initial load. The good news is that, once loaded, data refreshes happen much faster! The data is refreshed every time you filter in the controller, and you can also trigger it with the optimized refresh button in the controller.

### **3. How long should I expect my dashboard to load?**

Initial load times vary significantly based on your specific configuration, including the number and complexity of gadgets and your data volume. Typically, the load takes between a few seconds and a few tens of seconds. For a better sense of expected performance in your environment, feel free to reach out to our support team.

### **5. Will performance improve over time?**

Yes! We continually optimize performance and are exploring ways to further enhance the loading experience. Keep in mind that dashboard loading performance is heavily dependent on the performance and limitations of Jira's APIs.

### **6. Does my Internet connection affect dashboard speed?**

Unless it’s very slow or unstable, your Internet connection typically has minimal impact on dashboard loading, as most processing happens in your browser and in Atlassian’s Cloud. Computer performance is usually the primary factor, though individual configurations can vary.

### **7. Who can I contact for help optimizing my dashboards?**

Our support team is here to help! Every environment is unique, and performance can be affected by many factors specific to your setup. Contact us so we can investigate your specific case and provide personalized recommendations that apply to your situation.

### 8. How to find rich filters with SQL in your DC instance

1. **SQL to find the rich filters that haven’t been used since the 2.2 upgrade**

   This query displays all rich filters sorted by the last time they were used, starting with the oldest. Filters with a NULL last used date appear first. A NULL value means the rich filter hasn’t been used since the app was updated to version 2.2.
2. A rich filter is considered *used* when it’s edited or when a gadget that uses it is loaded.

   The query was validated with MySQL. You might need to make small adjustments if you are using a different database.

   Paste the query below into an SQL console:

Click here to see the SQL

```text
SELECT * FROM AO_24D977_QRFRFE0
ORDER BY 
  CASE WHEN LAST_USED_DATE IS NULL THEN 0 ELSE 1 END,
  LAST_USED_DATE ASC;
```

### **9. Script to find Rich Filters with more than 50,000 work items**

1. Log in to Jira DC as an administrator.   
   This part is important because the script might return incomplete results if you are not logged in with administrator rights.
2. Go to the **Manage Rich Filters** page and open your browser’s development tools.
3. Paste the script below into the JavaScript console and press Enter.   
   The script runs automatically. When it finishes, it prints a result:

   For example:  
   **Found X rich filters with more than 50.000** work items**:** followed by a list of rich filter names, ids, base filters, and the number of work items they have.

**Execution time depends a lot on how complex the base filter JQLs are for each rich filter.**

The script stops after it identifies 200 rich filters with more than 50,000 work items. If you need to, you can change the **MAX\_DISPLAYED\_RICH\_FILTERS** value at the top of the script. For a first run, it is better to keep the default value.

Click here to visualize the script.

```text
const ISSUE_COUNT_THRESHOLD = 50000;
const MAX_DISPLAYED_RICH_FILTERS = 200;

async function fetchAllResults(batchSize = 50) {
  const aboveThreshold = [];
  let startAt = 0;
  let total = null;
  let visitedJiraFilters = {};

  try {
    while (true) {
      const url = `${contextPath}/rest/qoti-rich-filters/latest/rich-filters/search?showTotal=true&access=edit&advancedSearch=true&startAt=${startAt}`;
      const response = await fetch(url);

      if (!response.ok) {
        throw new Error(`Error fetching data: ${response.statusText}`);
      }

      const data = await response.json();
      const results = data.results || [];
      total = data.total || total;

      for (const richFilter of results
        .filter(result => result.jiraFilter?.value?.jql?.input != null && result.jiraFilter?.value?.jql?.error == null)) {

        const jiraFilterId = richFilter.jiraFilter.value.id;

        if (visitedJiraFilters[jiraFilterId] == null) {
          const res = await fetch(`${contextPath}/rest/qoti-rich-filters/latest/support/issue-count`, {
            method: "POST",
            headers: {
              accept: "application/json",
              "content-type": "application/json"
            },
            body: JSON.stringify({
              richFilterId: richFilter.id,
              workingQuery: ""
            })
          });

          const { issueCount } = await res.json();
          visitedJiraFilters[jiraFilterId] = issueCount;
        }

        const issueCount = visitedJiraFilters[jiraFilterId];

        if (issueCount >= ISSUE_COUNT_THRESHOLD) {
          aboveThreshold.push({
            name: richFilter.name,
            id: richFilter.id,
            issueCount,
            jiraFilterId
          });
        }

        if (aboveThreshold.length >= MAX_DISPLAYED_RICH_FILTERS) {
          console.log(`Stopped after ${MAX_DISPLAYED_RICH_FILTERS} rich filters.`);
          return aboveThreshold;
        }
      }

      if (startAt + batchSize >= total) {
        break;
      } else if ((startAt + batchSize) % 100 === 0) {
        console.log(`Verified ${startAt + batchSize} rich filters.`);
      }

      startAt += batchSize;
    }

    return aboveThreshold;

  } catch (e) {
    console.error(`Unexpected error occurred while executing the script, returning partial results.`, e);
    return aboveThreshold;
  }
}

fetchAllResults().then(results => {
  console.log(`Found ${results.length} rich filters with more than ${ISSUE_COUNT_THRESHOLD} issues.: `, results);
});
```

**Is the 50,000 work item limit a hard limit? What happens if we exceed it?**  
Yes, this is a hard limit. If a rich filter returns more than 50,000 work items, the dashboards will show an error. Since most gadgets display aggregated results, using a soft limit would result in incomplete or misleading values.

**How can we verify whether any of our current rich filters exceed the limit?**  
You can verify this by opening the base Jira filter behind each rich filter in the Work item Navigator and checking the work item count. You can also use the script mentioned [**above**](https://appfire.atlassian.net/wiki/spaces/RFCDOC/pages/edit-v2/2548040102#2.-Script-to-find-Rich-Filters-with-more-than-50%2C000-work-items) in the DC instance to find any rich filters that exceed this limit.

### 10. The 7500 total rich filter limit

**What happens when we reach the 7500 filter threshold?**

On Cloud, rich filters support soft delete, meaning you can move filters to the trash before permanent deletion. The rich filters present in the trash do not count toward the limit. During migration, all filters are moved over, even if the total exceeds 7,500.

Once the limit is reached, you won’t be able to create new rich filters until enough existing ones are moved to the trash to free up space. If you notice any filters that didn’t migrate, please reach out to us so we can take a closer look at your configuration.

**Is there a way to identify inactive or unused filters on DC so we can safely remove them?**

Starting with version 2.2.0 of the Data Center app, every rich filter has a “last used date” stored in the database. This timestamp updates whenever a filter is edited or loaded in a dashboard. Although this field isn’t displayed in the DC UI, it can be queried directly from the database.

**See the SQL listed** [**above**](https://appfire.atlassian.net/wiki/spaces/RFCDOC/pages/edit-v2/2548040102#1.-Find-rich-filters-with-SQL)**.**

A clean-up of unused rich filters before migrating to Cloud is strongly recommended.  
The “last used date” is migrated to Cloud, where it becomes visible in the UI and powers the automatic archiving feature. See more, [Archived rich filters](/cms_trial/space/RFCDOC/783941683/Manage+Rich+Filters/).

**The documentation says we can request a limit increase. How does that process work, and is there a maximum?**

You can request a limit increase by opening a [support ticket](https://appfire.atlassian.net/servicedesk/customer/portal/11) with us. We routinely test the Cloud app with several thousand rich filters. Our recommended approach is to clean up unused filters before migration, then request a reasonable increase (we’ll help determine the appropriate number), and use cloud-side tools such as auto-archiving and bulk actions to maintain a healthy environment.

---

**Need help?** Contact our support team—we're happy to work with you on optimizing your dashboard experience!