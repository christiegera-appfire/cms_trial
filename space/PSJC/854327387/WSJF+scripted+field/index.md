# WSJF scripted field

## Problem

You would like to display the outcome of the [Weight Shortest Job First](https://scaledagileframework.com/wsjf/) equation in a Jira field.

## Example WSJF Calculation

Weighted Shortest Job First (WSJF) is a prioritization model used to sequence work for maximum economic benefit. In SAFe, WSJF is estimated as the relative cost of delay divided by the relative job duration.

![Power Scripts Weighted Shortest Job First (WSJF) prioritization model](/cms_trial/assets/eaf68ee9-e11d-4bc1-b0f2-6c81f8544cb1.png)

The actual calculation and prioritization are more straightforward than the explanation that brings us to this point. Compare jobs (three features, in this example) for each CoD component and job size using a simple table or spreadsheet (Figure 5). As with estimating stories, larger values reflect higher uncertainty.

![Power Scripts WSFJ job comparison for each CoD component and job size using a simple table or spreadsheet](/cms_trial/assets/802a91dc-8f72-448c-a5bc-3430ea89f3c0.png)

## Solution

This script assumes that there are custom fields for User Business Value, Time Criticality, Risk Reduction, and Job Size and that those fields also has [SIL aliases](/cms_trial/space/PSJC/793280566/Custom+fields+support+SIL+script/) created for them.

```text
if(isNotNull(userBusinessValue) && isNotNull(timeCriticality) && isNotNull(riskReduction) && isNotNull(jobSize)) {
    number costOfDelay = userBusinessValue + timeCriticality + riskReduction;
    return round(costOfDelay/jobSize, 2);
}
```

Because all the fields used in the calculation are all contained in the issue, and not on a parent, child, or linked issue, **no additional triggers** settings are needed for the [scripted fields configuration](/cms_trial/space/PSJC/856361791/Scripted+Fields+Configuration/).