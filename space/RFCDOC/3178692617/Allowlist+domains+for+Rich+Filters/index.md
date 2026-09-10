# Allowlist domains for Rich Filters

Rich Filters for Jira Dashboards app uses specific domains to serve content. If your organization has restrictive firewall or proxy settings, ask your network administrator to allowlist the domains below so the app works correctly. If gadgets or configuration pages fail to load after installation, a firewall block is the most common cause.

## Required domains to allowlist

|  |
| --- |
| `*.atlassian-dev.net` - including all subdomain levels  `rfc.qoticloud.com` |

When allowlisting `*.atlassian-dev.net`, be sure the rule covers the root domain and multiple subdomain levels, not just immediate subdomains.

## Atlassian official domain list

In addition to the domains above, Atlassian publishes a complete list of IP addresses and domains required for all cloud products. Your network administrator should also see [Atlassian's IP addresses and domains](https://support.atlassian.com/organization-administration/docs/ip-addresses-and-domains-for-atlassian-cloud-products/) for details and follow all Atlassian recommendations.

### **Troubleshooting**

If Rich Filters gadgets or configuration pages don’t load or stop working, the most common cause is a firewall blocking the required domains listed above. Verify all required domains are allowlisted, then contact your network administrator and share this page if the issue persists. You can also reach out to our [support](https://support.appfire.com/page/support) for further assistance.