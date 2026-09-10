# Concepts

## What is a Rich Filter

All the gadgets added by the Rich Filters for the Jira Dashboards app are based on a data source called a rich filter. A rich filter is based on a Jira native filter, extending the Jira native filter to include additional definitions for extra filtering, issue highlighting, multiple views for the results, and other settings that can be used by the *Rich Filter Gadgets*.

## What is a Rich Filter Gadget

The gadgets provided by the *Rich Filters for the Jira Dashboards* app are called r*ich filter gadgets*. All rich filter gadgets are based on rich filters and have one particular property – ***two or more rich filter gadgets are*** ***linked together*** ***in a dashboard if they share the same rich filter***. For example, a *Rich Filter Controller* gadget can change the data displayed by a *Rich Filter Results* gadget if both the *Rich Filter Controller* and the *Rich Filter Results* are based on the same rich filter.

The available gadget types are listed below, grouped by category:

**1. Controlling the dashboard content**

- **Rich Filter Controller Gadget**  
  The *Rich Filter Controller*gadget is particular as it controls all the other rich filter gadgets in the dashboard. It displays buttons and selectors that allow users to filter the issues, thus changing the data displayed by the other rich filter gadgets within the same dashboard in real time.

---

**2. Displaying issue data**

- **Rich Filter Results Gadget**  
  The *Rich Filter Results*gadget displays single or multiple lists of issues (queues), and it can apply single or multiple customizable views when displaying them. It allows for highlighting issues by using customizable tags and color-coding. Users can also preview and update issues directly from the dashboard.

- **Rich Filter** **Issue Activity Stream** **Gadget**  
  The *Rich Filter Issue Activity Stream Gadget* displays the recent activity on the issues returned by the rich filter.

---

**3. Displaying statistics**

- **Rich Filter Statistics Gadget**  
  The *Rich Filter Statistics* gadget displays a collection of issues grouped by specified criteria. It can aggregate multiple values simultaneously (*Issue Count*, *Story Points*, *Time Tracking*, etc.).

- **Rich Filter Two-Dimensional Statistics Gadget**  
  The *Rich Filter Two-Dimensional Statistics*gadget displays a collection of issues grouped by specified criteria in two dimensions. It can aggregate values (*Issue Count*, *Story Points*, *Time Tracking*, etc.).

---

**4. Displaying charts**

- **Rich Filter Flexi Charts Gadget**  
  The *Rich Filter Flexi Charts* gadget displays charts based on issue data. This highly customizable gadget provides multiple options for the chart type and how the data is aggregated and displayed.

- **Rich Filter Created vs. Resolved Chart Gadget**  
  The *Rich Filter Created vs. Resolved Chart* gadget displays values based on the issues created versus those resolved over time. The gadget can compute and display results based on values (Issue Count, Story Points, Time Tracking, etc.).

- **Rich Filter Time Series Chart Gadget**  
  *The Rich Filter Time Series Chart* gadget displays multi-line charts based on date and date-time fields, allowing users to compare and identify trends and correlations between series. The gadget can compute and display results based on values (Issue Count, Story Points, Time Tracking, etc.).

---

**5. Displaying counts and gauges**

- **Rich Filter Simple Counters Gadget**  
  The *Rich Filter Simple Counters* gadget simply aggregates and displays values based on the issues returned by the rich filter (*Issue Count*, sums of *Story Points*, *Time Tracking*, etc.).

- **Rich Filter Smart Counters Gadget**  
  The *Rich Filter Smart Counters* gadget displays values based on the issues returned by the rich filter, grouped by specified criteria. The gadget can compute results based on values (Issue Count, Story Points, Time Tracking, etc.).

- **Rich Filter Simple Gauges Gadget**  
  The *Rich Filter Simple Gauges* gadget displays custom proportions derived from issue data, aggregating single or multiple values simultaneously (Issue Count, Story Points, Time Tracking, etc.).

- **Rich Filter Smart Gauges Gadget**  
  The Rich Filter, Smart Gauges gadget, displays custom proportions derived from issue data grouped by specified criteria. The gadget can compute results based on values (Issue Count, Story Points, Time Tracking, etc.)

---

**6. Displaying rich text**

- **Rich Filter Text Panel Gadget**  
  The *Rich Filter Text Panel* gadget displays configurable rich text. It can inform and guide users and give context to the dashboards.