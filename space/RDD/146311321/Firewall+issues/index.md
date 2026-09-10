# Firewall issues

## Overview

Our apps run on AWS servers. To improve the performance and security of our services, we perform different requests with very specific scopes. This means that our apps can make multiple calls to our servers, requesting very specific data.

Ensure that your system administrator adds the following URLs to the allowlist for your firewall:

- [https://dashboardhub-eu.appfire.app](https://dashboardhub-eu.appfire.app/)
- [https://dashboardhub-us.appfire.app](https://dashboardhub-us.appfire.app/)

## The problem

A common problem in cloud instances is that some firewalls identify third-party app servers as *untrustworthy*, preventing users from accessing our app*’s* functionalities.

### How to check if you are affected by a firewall issue

To know if you are affected, the first thing that can happen is that an error page displays when you load our app (a blank page with the error message):

![Dashboard Hub firewall issue error message](/cms_trial/assets/6392d85a-bd9f-4296-b8a3-a7cc441ec230.png)

If you see this page, you might be affected. To confirm that this is the case, try to open the following URLs.

- <https://dashboardhub-eu.appfire.app/images/dashboard.svg>
- <https://dashboardhub-us.appfire.app/images/dashboard.svg>

If you are unable to load it and see the following image instead, then you are affected by this issue.

![Dashboard Hub firewall issue configuration example](/cms_trial/assets/c187a24f-786f-49dc-ab90-4a3c0624d192.png)

To further test if this is the problem, you can try disabling the firewall and launching the app again. Remember to enable the firewall again following the test.

If it still doesn’t load, submit a help request through [our support portal](https://roninpixels.atlassian.net/servicedesk/customer/portal/7).

## Solution

To enable our app to work with your firewall, contact the system/firewall administrator and ask to include these URLs on the allowlist:

- [https://dashboardhub-eu.appfire.app](https://dashboardhub-eu.appfire.app/)
- [https://dashboardhub-us.appfire.app](https://dashboardhub-us.appfire.app/)

## See also

- [Security and compliance](https://appfire.atlassian.net/wiki/pages/createpage.action?spaceKey=DTPS&title=Security%20and%20compliance)
- [Data Residency](/cms_trial/space/RDD/146309741/Data+Residency+(Cloud)/)