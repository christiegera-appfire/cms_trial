# Using 7pace Timetracker for Jira with Dashboard Hub Pro

![TryItButton (2).png](/cms_trial/assets/6bd642a7-9b6f-4b3c-86d3-72a34d329076.png)

## **Introduction**

This guide walks you through how to use **7pace Timetracker for Jira** as a data source within **Dashboard Hub Pro**, enabling you to build insightful, flexible, and visually rich reports. You'll learn how to connect the 7pace API, retrieve time tracking data, and create powerful visualizations like pie charts, tables, and more using[Dashboard Hub's Custom Reports engine](https://appfire.atlassian.net/wiki/spaces/RDD/pages/1529219266).

**7pace Timetracker** provides a reliable, developer-focused time tracking tool that integrates directly into Jira, with data available via a REST API. This data can be transformed and visualized in Dashboard Hub using JSON5 and[JSONata](https://jsonata.org/) for querying.

**Relevant Docs:**

- [7pace Timetracker for Jira - API Reference](https://appfire.atlassian.net/wiki/pages/createpage.action?spaceKey=7tfj&title=Connect%20external%20systems%20by%20APIs&linkCreation=true&fromPageId=2115797698)
- [Dashboard Hub Pro - Custom Reports Overview](https://appfire.atlassian.net/wiki/spaces/RDD/pages/1529219266)

---

## **Step 1: Connecting the 7pace Timetracker API to Dashboard Hub**

Before you can use 7pace data in reports, you need to configure it as a **REST datasource** in Dashboard Hub.

### **Instructions:**

1. In **Dashboard Hub Pro**, navigate to the **Custom Reports** module.
2. Open the **Datasources** section and click **Add new datasource**.
3. Choose **REST API** as the datasource type.
4. Configure the fields:

   - **Name**: `7pace`
   - **Base URI**: `https://api.7pace.com/jira/v1/worklogs`
   - **Authentication**: Use your 7pace API token if required, or integrate with Jira's authentication depending on your organization setup.
5. Click **Test Connection** to verify that the API is reachable.
6. Save the datasource.

You can now use this datasource in any report by referencing its URI:

text

CopyEdit

`datasource://7pace/worklogs`

---

## **Step 2: Understanding 7pace Data Structure**

When you call the 7pace Timetracker API for Jira (`/worklogs` endpoint), it returns data under a top-level key called `result`. Each entry represents a worklog and contains fields such as:

json

CopyEdit

`{`

`"result": [`

`{`

`"id": 456789,`

`"authorId": "abc123",`

`"authorName": "John Doe",`

`"duration": 5400, // in seconds`

`"date": "2025-06-12T09:00:00Z",`

`...`

`}`

`]`

`}`

### **Important fields:**

- **authorId**: Unique identifier for the Jira user who logged time.
- **authorName**: Display name of the user.
- **duration**: Time logged in **seconds** (important: divide by `3600` to convert to **hours**).
- **date**: Timestamp of the worklog entry.

For full schema details, consult the[7pace API for Jira documentation](https://appfire.atlassian.net/wiki/pages/createpage.action?spaceKey=7tfj&title=Connect%20external%20systems%20by%20APIs&linkCreation=true&fromPageId=2115797698).

---

## **Step 3: Displaying 7pace Data in Dashboard Hub**

Now that your data source is ready, let’s create a simple Custom Report that displays raw 7pace data.

### **Sample Report Block:**

json5

CopyEdit

`{`

`"id": "worklogs",`

`"type": "rest",`

`"uri": "datasource://7pace/worklogs",`

`"path": "$.result",`

`"children": {`

`"type": "json"`

`}`

`}`

### **Explanation:**

- The `rest` node fetches data from the 7pace worklogs endpoint.
- The `path` points to `$.result` to isolate the array of worklogs.
- The `json` node simply displays the data for inspection.

This is a good starting point to ensure the datasource is working correctly.

---

## **Step 4: Visualizing Worklogs in a Pie Chart**

Let’s build a **pie chart** that shows total hours logged by each user. To do this, we’ll:

- Group worklogs by `authorId`
- Sum the durations
- Convert seconds to hours
- Feed this transformed data into a Recharts-compatible pie chart

### **JSONata Transformation:**

json5

CopyEdit

`"path": "(\`

`$grouped := $.result.authorId{ \`

`name: $distinct($.authorName)[0], \`

`value: $sum($.duration) \`

`}; \`

`$map($keys($grouped), function($id) { \`

`{ name: $grouped[$id].name, value: $round($grouped[$id].value / 3600, 2) } \`

`}) \`

`)"`

### **Visualization Node:**

json5

CopyEdit

`{`

`"type": "chart",`

`"options": {`

`"chart": {`

`"type": "pie",`

`"height": 300`

`},`

`"data": {`

`"series": [`

`{`

`"name": "Hours Tracked",`

`"data": "$"`

`}`

`]`

`},`

`"pie": {`

`"label": {`

`"show": true,`

`"formatter": "{{name}}: {{value}}h"`

`}`

`},`

`"legend": {`

`"layout": "vertical",`

`"align": "right",`

`"verticalAlign": "middle"`

`}`

`}`

`}`

### **Explanation:**

- JSONata groups worklogs by user and computes total time tracked.
- The chart displays this as a pie chart using Recharts-compatible syntax.
- `value` is shown in **hours**, formatted to two decimal places.

---

## **Step 5: Enriching Worklog Data with Jira User Info (Optional)**

Sometimes, `authorId` alone isn’t enough. You may want to show full names, avatars, or emails from Jira’s `/user/bulk` endpoint.

### **How to enrich:**

1. Create an additional REST node calling:

text

CopyEdit

`/rest/api/3/user/bulk?accountId={{$join($distinct($.result.authorId), ',')}}`

1. Store the result in context (`users`).
2. Use `$lookup($root.users, $.authorId)` to enrich each row or chart label.

### **Example enrichment use:**

json5

CopyEdit

`{`

`"name": "$lookup($root.users, $.authorId).displayName",`

`"value": "$sum($.duration)"`

`}`

You can also add avatars in tables using a child node with `type: 'image'` pointing to `avatarUrls.48x48`.

More on this approach here: Dashboard Hub – Advanced Enrichment Techniques

---

## **Step 6: Troubleshooting and Tips**

- **Duration always in seconds** – always divide by `3600` to convert to hours.
- **Grouping by field**: use `$.result.authorId{ ... }`
- **Chart won't render?** Check:

  - No missing `value` or `name`
  - Height of chart is defined (e.g. `300`)
  - JSONata syntax is valid
- **Preview your JSON** with the `json` node before applying transformations