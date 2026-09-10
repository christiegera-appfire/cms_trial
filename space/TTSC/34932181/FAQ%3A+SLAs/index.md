# FAQ: SLAs

Below are some answers to questions we're commonly asked about creating SLAs. For help with something we haven't addressed, [please contact us](https://appfire.atlassian.net/servicedesk/customer/portals).

#### **I defined my SLA configurations, but I can’t see the SLA panel on my work items. What could be the reason?**

Answer:

There can be a number of reasons. Let’s go over them all, with the help of a handy checklist:

- First, go to the Time to SLA work item actions dropdown menu on the work item. Use the “Where is my SLA?” function to figure out what’s wrong.
- Does the work item satisfy the SLA start condition? Check your workflow.
- If you are using **Dynamic Duration** or **Negotiation** Date features as the SLA goal, check whether this field is on the work item and whether you’ve added it to the **necessary screens**.
- Check whether you have the necessary Time to SLA permissions. Go to **Apps** > **Time to SLA** > **Permissions** menu, and confirm your permissions for the SLA Panel.
- Check the SLA Panel position through the **Time to SLA** > **Settings** > **SLA panel** menu. At least one of them (**left panel** or **right panel**) should be enabled.

Still can’t see the SLA Panel? No worries. [Our support team can help](https://appfire.atlassian.net/servicedesk/customer/portals).

#### **I can’t see the SLA Panel on my existing work items. What should I do?**

Answer:

To see the SLA panel on your existing work items, you need to recalculate the SLA data. Navigate to SLA for the existing work item menu, enter a JQL condition for the recalculation, and click **Generate**.

#### **My SLA shows incorrect data / isn’t behaving the way I want it to. What could be the reason?**

Answer:

Let's imagine, for illustration, that your SLA didn't end when it ought to have. In that scenario, try these:

- Go to SLA History, and check the related actions.
- Check the SLA configurations.
- Check if the related condition is met by the work item.
- Check Audit Logs to see whether someone changed the SLA’s configurations. If there’ve been any changes, use recalculation to fix your SLA.

You can adapt these to your specific situation. If the error persists, contact our Support Team.

#### **Why isn’t my SLA starting?**

Answer:

Make sure the start condition is correctly defined and the work item has triggered the start condition.

#### **I’ve set notifiers, but I’m not receiving any notifications. Why?**

Answer:

If you’re sending emails, you should check if the email is in the Spam folder. Or it could be because the recipients or groups you’ve chosen might have been deleted.

You should also make sure that the parameters you put in the subject or body are correct. If you're using our functions, you can [check the related documentation](/cms_trial/space/TTSC/35881100/Action+parameters/). If you’re sending emails, you should check if the email is in the Spam folder. Or it could be because the recipients or groups you’ve chosen might have been deleted.

You should also make sure that the parameters you put in the subject or body are correct. If you're using our functions, you can [check the related documentation](/cms_trial/space/TTSC/35881100/Action+parameters/).

#### **I’m getting too many update notifications, which makes it difficult for me to keep track of important information in my SLA history. How can I fix this?**

Answer:

We recommend you set a higher target date refresh interval number to solve that problem. [Here’s how](/cms_trial/space/TTSC/35684678/SLA+custom+field/).

#### Why do I get a “429 Too Many Requests” error with automation rules?

Answer:

This error happens when too many automation rules or scripts run at the same time, creating excessive API calls. To fix this, you can do the following:

- Run rules that don’t affect SLA calculations as the Automation user and add this user as *ignored* in Time to SLA. Updates from ignored users won’t trigger SLA recalculations, reducing API calls. To learn how, refer to [this documentation](/cms_trial/space/TTSC/37290034/Administration/).
- Run rules that do affect SLA calculations as a Jira administrator (or another user with access), so they are processed correctly.

By separating automation users from SLA-impacting users, you’ll reduce unnecessary API calls and avoid hitting Atlassian’s rate limits.

#### Why do I get a `400 Bad Request – "You don't have access to this URL"` error when calling the REST API?

Answer:

This error is usually related to the authentication token used in the request.

Check the following:

- The token may be expired.  
  Generate a new token and update your request.
- The token may not have the required access  
  Make sure the token is valid and has access to the API you’re calling. The error is related to the token itself, not the permissions of the user who generated it.

After updating or regenerating the token, retry the request.

#### Why isn’t my Jira automation rule triggered by an SLA notification?

Answer:

If you’re using SLA notifications to trigger a Jira automation rule, but the rule isn’t running and no action appears in the automation audit log, this may be related to IP allowlisting.

When IP allowlisting is enabled in your Atlassian organization, Jira may block requests from Time to SLA unless the Time to SLA IP addresses are included in your allowlist. As a result, the automation rule won’t be triggered.

**What to check**

- Verify whether IP allowlisting is enabled for your Jira Cloud instance.
- Review your allowlist configuration and [Atlassian’s IP allowlisting requirements](https://support.atlassian.com/security-and-access-policies/docs/specify-ip-addresses-for-product-access/#:~:text=View%20your%20IP,all%20active%20policies.).

**How to resolve it**

To resolve this issue, add the Time to SLA IP addresses to your IP allowlist. Contact our support team through the [support portal](https://appfire.atlassian.net/servicedesk/customer/portals), and we will share the IP addresses with you.