# Sync risk metrics with Jira fields

Sync a risk metric in Hedge with a Jira field so that both stay up to date automatically. When you turn on synchronization, changing the value in either Hedge or Jira updates the other, and Hedge recalculates risk values accordingly.

## Prerequisites

- Since risk data is written to Jira fields, ensure the fields you want to sync with Hedge are added to the Field Scheme associated with your Jira space.
- The Jira field must be a single select field with at least one value. If the field doesn't meet these requirements, Hedge shows an error message, and you can't turn on synchronization.

## Sync a metric with a Jira field

1. In your risk register, click **Settings** > **Risk framework**.
2. In the **Metrics** section, toggle **Map metric to Jira custom field**. Enable the toggle for Probability and Consequence.
3. Select the Jira field you want to map the metrics to.

![Risk metrics in the risk register. The top of the metrics features Map metric to Jira custom field dropdowns for Likelihood and Consequences axes.](/cms_trial/assets/ea4a0d4a-52d5-444b-bca5-6457d80b0f5a.png)

Activating synchronization overwrites the metric's current values with the values from the mapped Jira field.

## How syncing works

- Changing the field in Jira updates the metric's value in Hedge and recalculates risk values.
- Changing the metric in Hedge updates the field's value in Jira.

## Limitations

- If a risk register has multiple contexts, the risk matrix currently displays only the default context for synced metrics.