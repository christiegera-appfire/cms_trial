# Copy field value (the value before the transition) to another field

This article provides the code snippet to copy field value (the value before the transition) to another field using [Set issue fields](/cms_trial/space/JMWEC/465504849/Set+issue+fields/) post-function.

This is a workaround until <https://appfire.atlassian.net/browse/MWEC-1133> is released.

## \uD83D\uDCD8 Instructions

1. Navigate to the intended workflow to make the necessary changes in the edit mode.
2. Select the required transition.
3. Select the *Post functions* tab and click `Add post function`.
4. Add the [Set issue fields](/cms_trial/space/JMWEC/465504849/Set+issue+fields/) post-function.
5. Select the issues for which the field should be set under “Target Issue(s)”.
6. Select the desired field and add the below Nunjucks template:

   ```java
   {{ context.changelog.fields["customfield_10062"].from_string }}
   ```

   Replace `10062` with the id of the source field.
7. Select the checkbox “Run this post-function only if a condition is verified” under “Conditional Execution” and add the below Condition:

   ```java
   {{ context.changelog.fields["customfield_10062"] }}
   ```

   Replace `10062` with the id of the source field. The above condition checks that the field value is changed during the transition.

![JMWE for Jira Cloud field value copying configuration showing pretransition value options](/cms_trial/assets/86900e2f-3b65-4083-8058-df33218d51b2.png)

Note: The post-function must be placed after the “Update change history for an issue and store the issue in the database” built-in post-function.

![JMWE for Jira Cloud workflow setup for copying field values before transitions](/cms_trial/assets/4188b013-58b7-4eab-8b8a-3640feac0264.png)