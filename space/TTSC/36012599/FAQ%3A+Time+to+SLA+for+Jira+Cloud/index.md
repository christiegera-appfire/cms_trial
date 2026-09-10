# FAQ: Time to SLA for Jira Cloud

We know there’s a lot to learn and read about the Time to SLA platform. That’s why we wanted to answer some of the most frequently asked questions on one page. If you think we’re missing any critical tips, let us know by [getting in touch](https://appfire.atlassian.net/servicedesk/customer/portals).

### **Where is the EULA?**

Answer:

Please refer to [the EULA provided by Appfire](https://appfire.com/eula/).

### **Can I get a demo for my team? Do you offer a free trial? If yes, can I extend my free trial?**

Answer:

Of course! You can [request a free demo](https://appfire.atlassian.net/servicedesk/customer/portals) through our support portal, and you can use TTS Cloud free of charge for 30 days. [Check out our Atlassian Marketplace listing](https://marketplace.atlassian.com/apps/1211843/time-to-sla?tab=pricing&hosting=cloud&utm_source=appfire.com&utm_medium=solutions&utm_campaign=Time-to-SLA) to get started. For Cloud apps, you cannot extend your free evaluation period. All cloud apps are immediately subscribed to by a user, and we provide a free evaluation period. This is a minimum of 30 days and ends on the second billing cycle after you first subscribe to the app.

### **I have 100 Jira users, but only 30 of them will use Time to SLA. Can I pay for only 30 users?**

Answer:

The Jira user count should match the TTS user count. The pricing is always calculated based on the number of Jira users.

### **How does Cloud app pricing work?**

Answer:

Cloud apps are sold as a monthly or annual subscription. You are eligible for support and automatic version updates as long as your subscription is active. When your subscription renews each month, you are automatically billed for apps based on the number of users in your instance. To figure out the exact cost, [click here](https://marketplace.atlassian.com/apps/1211843/time-to-sla?tab=pricing&hosting=cloud&utm_source=appfire.com&utm_medium=solutions&utm_campaign=Time-to-SLA) and enter the number of users you have.

If app pricing changes after your initial purchase, there's a 60-day grandfathering period during which you can renew based on the old pricing.

Apps are billed based on the number of users in your Atlassian product. Jira Cloud apps are priced based on the maximum number of users of the Jira products on your instance. For example, if you have Jira Software (50 users) and Jira Service Management (10 agents) in the same instance, you pay the 50-user price for apps.

Note: While this app has features specific to Jira Service Management and Jira Software, the app is technically available across the whole Jira instance. Therefore, the above guidelines for licensing across the maximum number of users still apply.

### **Can I get a refund?**

Answer:

Yes, within 30 days. You can get in touch with our Support team to file a request.

### **I'm migrating to Cloud from Data Center. Do you support dual licensing?**

Answer:

Yes, we do support dual licensing as outlined [here](https://www.atlassian.com/migration/assess/calculate-pricing/dual-licensing). If you have any issues with applying for the dual license with Atlassian, please feel free to reach out to us.

### **Is Time to SLA Cloud Fortified?**

Answer:

It is! Check out the Cloud Fortified criteria Time to SLA meets below:

![Time to SLA FAQ page showing Jira SLA panel example](/cms_trial/assets/215fd2ef-f5bc-4ec2-b9f5-76bee03611c1.png)

### **What is your privacy policy?**

Answer:

Atlassian's privacy policy is not applicable to the use of Time to SLA. Please refer to the [privacy policy provided by Appfire](https://trust.appfire.com/).

### **Are you SOC2 compliant?**

Answer:

Time to SLA is SOC2 compliant.

### **What data does Time to SLA collect from my Jira instance? Where is the information stored?**

Answer:

The “INFORMATION WE COLLECT AND RECEIVE” section of [Appfire’s privacy policy](https://trust.appfire.com/) covers what Time to SLA collects. Like all apps, we maintain data on our own servers, separate from the Atlassian Cloud. We only retain work item/user/group ID values. Access to this customer data is protected through JWT token verification, and database access is limited to system administrators. Additionally, the data is stored in an encrypted format. We utilize AWS servers for this purpose, with the data being stored in Ireland.

### Do you offer compensation?

Answer:

As per our [company policy](https://appfire.com/eula/), we do not offer compensation. This policy is in place to ensure fairness and consistency for all of our customers.

### I’m getting a “Something’s gone wrong: Our team has been notified. If the problem persists, please contact Atlassian Support.” error. How can I fix this?

Answer:

Here are some things you can try to fix this problem:

- Uninstall the addon and then reinstall it. It is important to note that unsubscribing only affects billing, and none of your data will be deleted. Wait a few moments for TTS to restart.
- Clear the browser cache or load TTS in incognito mode.
- Try using a different browser in incognito mode.
- Try loading the TTS on a completely different computer and network. You can use a personal hotspot.
- Ensure that the project role `atlassian-addons-project-access` has all project permissions and that the group `atlassian-addons-admin` has all global permissions. Global permissions should include:

   Browse users and groups  
   Share dashboards and filters

- In addition, if possible, have at least one of the three groups (`administrators`, `jira-administrators`, and `site-admins`) for all global permissions.

### I'm encountering a '307 Temporary Redirect' issue while using Time to SLA Cloud with my VPN. How can I resolve this problem?

Answer:

When a user encounters a "307 Temporary Redirect" response, it usually indicates that the server is sending this status code as an instruction to fetch a different URL with the same method that was used in the original request. This can occur for various reasons, but when it’s related to the use of a VPN, manually configuring the VPN or DNS settings to accommodate **Appfire app URLs** can often resolve the problem, especially if the issue is related to DNS resolution or specific traffic routing when the VPN is active.

**Solution:**

**Context:** Sometimes, the VPN might use its own DNS servers, which could lead to resolution issues, especially when Appfire app URLs are not properly resolved by the VPN’s DNS.

**Recommendation:** Time to SLA Cloud utilizes Amazon Route 53 for its DNS services. If you are using private VPN servers set up by your system or network team, the DNS resolver associated with that VPN may not be configured to properly resolve domains hosted on Amazon Route 53. Please reach out to your network team regarding this issue and inform them that they need to adjust the DNS resolver settings for ‘[snapbytesapps.com](http://snapbytesapps.com/)’.

**Consideration:** Keep in mind that changing DNS settings can affect how all domains are resolved, not just Appfire app URLs. Ensure that any changes don’t adversely affect other applications or services you might be using.

### How long do users have to retrieve their data after uninstalling the app, and what happens if they reinstall the app after 6 months?

Answer:

If users uninstall the app, they can retrieve their existing data within 6 months. However, if they reinstall the app after 6 months, they will not be able to access their previous data.

### What happens to my SLA data if I uninstall Time to SLA?

Answer:

If Time to SLA is uninstalled, the data remains protected for 90 days. Reinstalling the application within this time frame allows users to regain access to their current calendars, SLAs, and other associated data.

### How can I uninstall Time to SLA for Jira Cloud?

Answer:

Log in to Jira and open **Manage your apps** from the **Apps** menu. Click **Stop Trial** and the **Unsubscribe from app** pop-up will appear. Click **Unsubscribe**, and then you’ll be able to click **Uninstall**. This will remove Time to SLA from your Jira Cloud. The SLA configurations will be preserved even if you uninstall or disable the Time to SLA plugin. However, as a good measure, we recommend that you [export your SLAs and calendars](https://appfire.atlassian.net/wiki/spaces/TTSC/pages/36110695) beforehand to avoid losing any data.

### Does Time to SLA support custom domains or site renames?

Answer:

Yes. Time to SLA is fully compatible with Atlassian’s **Cloud Site Rename** feature. Renaming your site can help you strengthen your brand identity by using a domain that reflects your organization and simplify navigation by making it easier for teams to identify the right site.

You can safely rename your Atlassian Cloud site (for example, from `companyname.atlassian.net` to `yourbrand.atlassian.net`) without affecting Time to SLA functionality.

Your SLAs, configurations, and data will remain intact, and the app will continue to work seamlessly after the change.

For more details on how Cloud Site Rename works, see [Atlassian’s official documentation](https://support.atlassian.com/organization-administration/docs/can-i-change-the-url-used-to-access-a-product/).

### I’m getting the “Some apps are not registered to receive migration notifications” error during the JCMA migration process. Why?

Answer:

This happens when Time to SLA for Jira Data Center is running on a version earlier than 11.5.0. From version 11.5.0, Time to SLA uses Forge-based migration support. Versions below this do not register with the Jira Cloud Migration Assistant (JCMA), so the app cannot receive migration notifications and does not appear as migratable.

![Time to SLA FAQ page showing related SLA status message](/cms_trial/assets/570f7be6-61e4-45ed-b9cc-aa54a4b910f6.png)

**How to fix this**

1. Upgrade Time to SLA to version 11.5.0 or later.
2. Restart the Jira Cloud Migration Assistant.

### I am trying to migrate my Time to SLA instance from DC to Cloud, but I can’t upgrade the app because my Jira version is no longer supported. What can I do?

Answer:

Time to SLA cannot release new versions for Jira versions that Atlassian has marked as End of Support (EOS).

Cloud migration support in Time to SLA is Forge-based, and Forge capabilities are only available on Jira versions that are still supported by Atlassian. As a result, the Time to SLA version required for migration (v11.5.0 or later) is not compatible with Jira versions that have reached end of support.

This limitation is based on Atlassian’s support policy, not on the migration process itself.

You can review Atlassian’s supported Jira versions [here](https://confluence.atlassian.com/support/atlassian-support-end-of-life-policy-201851003.html).