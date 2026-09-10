# Data Residency (Cloud)

## Overview

With Atlassian Cloud products ([Standard, Premium and Enterprise subscriptions](https://www.atlassian.com/software/data-residency)) data residency is available when you create the instance. You can specify where your content and data are hosted.

The importance of data residency is paramount to meet organizational and regulatory data compliance requirements. This is even more important in regulated industries like government, banking, insurance, telecommunications, transportation, life sciences, healthcare, energy, agriculture, construction, defense or postal services.

## How to enable data residency in Dashboard Hub

The storage is done automatically based on your current location: Global, Australia, Europe or USA (read Atlassian’s [Understand data residency](https://support.atlassian.com/security-and-access-policies/docs/understand-data-residency/) for more information).

**If you already installed Dashboard Hub, you have to uninstall and install again** (for installations done before 23rd June 2022, when this mechanism was released for the first time). No data is going to be lost.

## How to view where your data is hosted

Regions cannot be chosen, since these are based on your current location. To view where your product data is hosted, you need to have organization admin permissions:

1. Go to [admin.atlassian.com](http://admin.atlassian.com/). Select your organization if you have more than one.
2. Select **Data management** > **Data residency**.

![Dashboard Hub Atlassian data residency locations](/cms_trial/assets/9a2769b2-d64b-4887-a9c8-cca05c250fc3.png)

Based on your current location, Dashboard Hub services and data are in the following regions:

| **Location** | **AWS regions** | **Dashboard Hub regions** |
| --- | --- | --- |
| **Global** | - Asia Pacific (Singapore and Sydney) - Europe (Frankfurt and Ireland) - US (US East and US West) | - Services in Europe (Frankfurt) - Data in Europe (Frankfurt) |
| **Australia** | - Asia Pacific (Sydney) | - Services in Europe (Frankfurt) - Data in Europe (Frankfurt) |
| **Europe** | - Europe (Frankfurt and Ireland) | - Services in Europe (Frankfurt) - Data in Europe (Frankfurt) |
| **USA** | - US (US East and US West) | - Services in US (N. Virginia) - Data in US East (Ohio) |

![Dashboard Hub Data Residency (Cloud) data residency configuration](/cms_trial/assets/767865a9-9445-44fc-929f-f8b9651facbc.png)

Do you need a new region? [Contact us](https://roninpixels.atlassian.net/servicedesk/customer/portal/7)

If you want to learn more about what we store, see our [Security](/cms_trial/space/RDD/146310544/Security/) page.