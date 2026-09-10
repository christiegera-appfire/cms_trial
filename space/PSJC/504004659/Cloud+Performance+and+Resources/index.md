# Cloud Performance and Resources

Each customer is unique and our solutions are tailored to meet both memory and CPU requirements.

Valid reasons to request additional resources include:

1. Scripts are efficient but you notice frequent reboots, meaning that standard processing requires additional memory.
2. Additional memory is required to load a large amount of data, including CSV files or issue lists, that must be bulk processed.

Feel free to request additional resources each time you need it. We recommend you to both request it via the Self-Help page and opening a ticket on our support portal.

We usually check for new requests weekly.

Request more resources in **Self Help** > **Engine Resize**.

![Power Scripts for Jira Cloud engine resize configuration panel](/cms_trial/assets/b344a617-4152-4a6f-a27b-207cc8c69579.png)

The Cloud is a shared environment where memory and CPU resource allocation follows an equitable schedule. Inefficiencies in one environment impact others, including performance and maintenance costs, and both may affect service costs.

Note that Appfire may deny your request if scripts are not optimized. Oftentimes, scripts run multiple Jira searches, loading countless issues but processing just a few, making a negative impact on performance.

## Sizing

The following table lists installation sizes:

| **Sizing** | **Notes** |
| --- | --- |
| Default | A good starting point when there are minimal integrations.  Maximum - 200 users. |
| Medium | Midsize.  100-500 users with 10+ integrations. |
| Large | 250-500 users with 25+ integrations. |
| Xlarge | 250-1000 users. |
| XXlarge | 1000 users with 50+ integrations. |
| XXXlarge | Significant installations. |
| Huge | Very large installations. |
| Xhuge | The largest installations. |

Installation sizes overlap because every customer has unique use cases. For example, a well-scripted instance with ten users could be classified as *xlarge* if it requires significant processing power. Similarly, a 1000 user installation may only use a few simple integrations, and the *medium* instance is sufficient.

## Background Operations

### Shutting down an Engine

To maintain low costs, your SIL Engine is put to sleep in the following cases:

1. It is unused.
2. Your license becomes inactive.
3. You uninstall PS Cloud.
4. You submit a request in the support forum to put it to sleep.

Notes about installations that are put to sleep:

- No data is lost.
- Scripts and integrations are maintained.
- They can be reinstated at any time.

**An unused engine is defined as one that does not have scripts and does not service requests.** Evaluation installations are only considered unused if they are inactive one month after the install. Note that workflow validators and conditions defined via PowerScripts are executing on the Jira side therefore they are not used in determining if the engine is used.

Note that, when problem licenses are identified, they are not immediately shut down.

### Updates

When updates are performed, a restart may be necessary. In these instances, an announcement displays in the status handler or the following URL:

<https://us1.powerscripts.anova.appfire.app/status>

![Power Scripts for Jira Cloud monitoring dashboard with performance metrics](/cms_trial/assets/346fe0ff-3bb9-4889-b770-f5687caedb9d.png)