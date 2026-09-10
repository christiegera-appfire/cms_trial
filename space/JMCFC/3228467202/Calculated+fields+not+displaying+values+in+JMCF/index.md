# Calculated fields not displaying values in JMCF

In JMCF for Jira Cloud, calculated fields require a specific syntax to reliably retrieve data at execution time. While the script editor's **Test** function is sometimes more forgiving, the actual runtime engine requires you to use the `api.issue.getField()` format.

If you use raw field references (like `customfield_12345`) without the API wrapper, the script might look correct while testing, but fail to return data when it’s actually running on an issue.

### The solution: Use the correct script format

To ensure your script retrieves field values correctly, you must use the standard [JMCF API format](https://support.appfire.com/space/JMCFC/1325137936/getField).

#### Example 1: Basic math (Ratio)

If you are trying to divide one custom field by another, your script should look like this:

```text
JavaScript
```

```text
const field1 = await api.issue.getField(issue, "customfield_10147");
const field2 = await api.issue.getField(issue, "customfield_10102");

return field1 / field2;
```

#### Example 2: Date difference

If you want to calculate the number of days between two dates, you still need to use the `getField` syntax to ensure the date objects are handled correctly by the runtime engine:

```text
JavaScript
```

```text
const startDate = await api.issue.getField(issue, "customfield_10200");
const endDate = await api.issue.getField(issue, "customfield_10201");

if (startDate && endDate) {
    const diffInMs = new Date(endDate) - new Date(startDate);
    return diffInMs / (1000 * 60 * 60 * 24); // Returns difference in days
}

return null;
```

### Key things to remember

- **Field IDs:** Always use the `customfield_XXXXX` format for the most reliable results.
- **Data types:** Be mindful that some fields return strings while others return numbers or date objects. Using the `api` call ensures the data is fetched properly before you perform any logic.
- **Editor validation:** We’re currently working on an improvement to make the script editor smarter. Soon, it will flag these formatting errors during the testing phase, so you don't have to wait until you save to see if it works.

---

**Need more help?** If your script still isn't returning the expected value after updating the syntax, reach out to our [support team](https://support.appfire.com/portal/11).