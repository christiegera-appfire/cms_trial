# Add days to a date excluding specific days.

The [businessAdd](/cms_trial/space/JMWEC/466323491/date+filter/) filter adds a specific number of days to a date, skipping non-business days, where non-business days mean Saturday and Sunday. This article provides the code snippet to add a given number of days to date while skipping the specified weekdays.

## Instructions

1. Navigate to the intended workflow to make the necessary changes in the edit mode.
2. Select the required transition.
3. Select the *Post functions* tab and click `Add post function`.
4. Select the [Set issue fields (JMWE app)](/cms_trial/space/JMWEC/465504849/Set+issue+fields/) post-function and click `Add`.
5. Select the target issue and target field in **Target Issue(s)** and **Add Field(s)** respectively, and add the following template as **Value** for the added field:

   ```java
   {% set startDate = issue.fields.customfield_10057 %}
   {% set nod = issue.fields.customfield_10055 %}
   {%set endDate = startDate %}
   {% for n in range(0, nod) %}
   {%set endDate = endDate | date('add' , 1 , 'days') | date %}
   {% set day = endDate | date('e') %}
   {% if day == 5 %}
   {%set endDate = endDate | date('add' , 2 , 'days') | date %}
   {% elif day == 6 %}
   {%set endDate = endDate | date('add' , 1 , 'days') | date %}
   {% endif %}
   {% endfor %}
   {{endDate}}
   ```

Replace :

- `10057` with the `id` of the date field to which the number of days should be added.
- `10055` with the `id` of the field, which contains the value of the number of days to be added.

In the above template, we are considering Friday (line #7) and Saturday (line #9) as non-working days. Modify them as per your use case (refer to [this page](/cms_trial/space/JMWEC/466323491/date+filter/))

![JMWE for Jira Cloud date calculation settings for excluding specific days from date operations](/cms_trial/assets/611e2436-296d-4ef2-af0f-791687b5be3d.png)

Publish the workflow to see the changes reflected on the target issue.

### References

- [How to insert information using Nunjucks annotations](/cms_trial/space/JMWEC/465503811/Using+Nunjucks+Templates/)
- [Accessing JIRA Standard fields](/cms_trial/space/JMWEC/466225701/Standard+JIRA+Fields/)
- [date filter](/cms_trial/space/JMWEC/466323491/date+filter/)
- [Tags and Expressions](/cms_trial/space/JMWEC/466322168/Tags+and+Expressions/)

## \uD83D\uDCCB Related articles