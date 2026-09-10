# Manual KR

**About this page**

This page describes features that are supported **only** in [**BigPicture Advanced**](/cms_trial/space/SPM/3451617346/BigPicture+Standard+vs+Advanced/). These features are not available in BigPicture Standard.

In the manual mode, the user updates the progress of the Key Result.

There are two main components of the manual KR progress:

- KR values (start, current, target)
- Measure as (value unit)

Note the “KR” icon for the manual KR:

![Manual KR.](/cms_trial/assets/104b542e-6dbd-4159-95ad-c63d01d4f2f5.png)

## Available KR values and units

The progress of the manual KRs must be updated manually. For that reason, you need to first define their values and unit.

### KR values

There are two KR values related to the KR progress that reflect what you want to achieve with a specific OKR:

- **Start** - The initial state of the KR’s progress. When creating a KR, you define the starting value once, but you can edit it if needed.
- **Current** - The value indicating progress. As your teams work toward completing the KR, you will manually update this value.
- **Target** - The goal you want to achieve with a KR. When creating a KR, you define the target value once, but you can edit it if needed. As your teams work toward completing the KR, the current value should be getting closer to the target value for successful completion.

### KR value units (Measure as)

The value units should match the KR goal you want to achieve. Since there can be many different numeric goals, the OKR module gives you the flexibility to choose one of the many different units:

- **Standard** - Numeric (no unit) and percent (%).
- **Currency** - USD ($), EUR (€), GBP (£), BRL (R$), INR (₹), CHF (CHf), IDR (Rp), ZAR (R).

## Set the KR value and unit

On the [KR creation screen](https://appfire.atlassian.net/wiki/spaces/SPM/pages/1918538655), you can set the start and target values and units.

1. On the **KR creation screen**, select **Update manually** under **Progress tracking**.
2. Below the Progress tracking, define the:

- **Start** value (This is the same as the “start” value)
- **Target** value (the goal of the KR)
- **Measure as** unit (for example, “Percent”)

![Screenshot of setting the KR value and unit in the OKR module.](/cms_trial/assets/69ccf11e-d6eb-43c3-bf2c-bee12e606eb0.png)

## Change the start and target values and unit

The start and target values can be changed anytime on the [OKR details page](/cms_trial/space/SPM/1918536390/OKR+details+page/).

1. In the **Progress** section, click the **pen icon**.
2. On the **Change start and desired value of the key result** screen, update the start value and the target (desired) value.
3. If you want the new values and a unit to be applicable to the previous KR updates, check the option below the start value.

![The Change start and desired value of the key result screen.](/cms_trial/assets/ec42436d-77b2-4ffd-a1df-72f8f52052df.png)

## Update manual KR progress

You can update the current KR progress value on the [KR update screen](/cms_trial/space/SPM/1918637972/Update+OKR/). (The field is grayed out for the auto-KRs.)

![KR update modal partial screenshot focusing the Progress fields.](/cms_trial/assets/b51ef496-c0df-4c4a-8222-73d6178ec01a.png)

As the current value increases, so does the app calculate the progress according to the formula:

`(current - start) / (target - start) = progress x 100%`

### KR target on track: Example

Say you want to conduct a series of UX interviews to gather feedback from current customers about the app you launched a few months ago. Your KR could be: “Conduct 25 customer interviews to understand product usage and satisfaction.”

Since you have not started any interviews yet, the values for such KR would be as follows:

- Start value: 0
- Target value: 25 (you want to conduct 25 interviews in a specific OKR period)
- Current value: 4 (4 interviews conducted so far)

The unit for such KR would be just numeric because you are after a specific number of interviews. Once a few interviews are conducted, you can update the current value to reflect the progress, for example, 4.

As a result:

`(4 - 0) / (25 - 0) = 0.16 x 100% = 16%`

![An example of the manual KR progress.](/cms_trial/assets/ff9c19d3-0848-4477-9e81-7da58f437937.png)

### KR target surpassed: Example

What if your teams went that extra mile and conducted 3 more interviews than initially planned (25)? In such a case, the progress will exceed 100%.

- Start value: 0
- Target value: 25 (you want to conduct 25 interviews in a specific OKR period)
- Current value: 28 (28 interviews conducted in total)

`(28 - 0) / (25 - 0) = 1.12 x 100% = 112%`

![An example of the manual KR progress.](/cms_trial/assets/779c3f00-4084-4bc2-b67f-45f44f3318ca.png)

### KR below target: Example

You want to reduce customer churn from 10% to 5%. Unfortunately, due to unforeseen events, churn rose to 13%.

- Start value: 10
- Target value: 5 (you want to conduct 25 interviews in total in a specific OKR period)
- Current value: 13 (churn has increased to 13%)

As a result:

`(13 - 10) / (5 - 10) = -0.6 x 100% = -60%`

![An example of the manual KR progress.](/cms_trial/assets/41e0d25c-de50-437f-b459-4c035833007e.png)

Note that it is possible to [link work items](/cms_trial/space/SPM/1918507296/Link+work+items+to+Key+Results/) and boxes to a manual KR. While the linked work items and [linked boxes](/cms_trial/space/SPM/2229665803/Link+boxes+to+Key+Results/) do not affect manual KR progress, they are useful for visibility and context.