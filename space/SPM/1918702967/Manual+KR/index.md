# Manual KR

**About this page**

This page describes features that are supported **only** in [**BigPicture Advanced**](/cms_trial/space/SPM/3451617346/BigPicture+Standard+vs+Advanced/). These features are not available in BigPicture Standard.

In manual mode, the user updates the Key Result progress.

There are two main components of the manual KR progress:

- KR values (start, current, target)
- Measure as (value unit)

Note the **KR icon** difference between an auto and manual KR.

| Auto KR icon. | Manual KR icon. |
| --- | --- |

## Available KR values and units

You must update manual KR progress manually. For that reason, you need to first define their values and units.

### KR values

There are two KR values related to the KR progress that reflect what you want to achieve with a specific OKR:

- **Start** - The initial state of the KR’s progress. When creating a KR, you define the starting value once, but you can edit it if needed.
- **Current** - The value indicating progress. As your teams work toward completing the KR, you will manually update this value.
- **Target** - The goal you want to achieve with a KR. When creating a KR, you define the target value once, but you can edit it if needed. As your teams work toward completing the KR, the current value should be getting closer to the target value for successful completion.

### KR value units (Measure as)

The value units should match the KR goal you want to achieve. Since there can be many different numeric goals, the OKR module gives you the flexibility to choose one of the many different units:

- **Standard** - Numeric (no unit) and percent (%).
- **Currency** - USD ($), EUR (€), GBP (£), BRL (R$), INR (₹), CHF (CHF), IDR (Rp), ZAR (R).

## Set the KR value and unit

On the [KR creation screen](/cms_trial/space/SPM/2324726248/Create+OKR/), you can set the start and target values and units.

1. On the **KR creation screen**, select **Update manually** under **Progress tracking**.
2. Below **Progress tracking**, define:

- **Start** value (This is the same as the “start” value)
- **Target** value (the goal of the KR)
- **Measure as** unit (for example, “Percent”)

![Screenshot of setting the KR value and unit in the OKR module.](/cms_trial/assets/9f1ad9e6-0801-43eb-a444-7a048e6cbb50.png)

## Change the start and target values and unit

You can change the start and target values of the manual KR at any time on the [*OKR Details*](/cms_trial/space/SPM/1918536390/OKR+details+page/) page.

1. Open the dropdown menu under **More actions** (**…**) in the top-right corner.
2. Select **Edit configuration**.
3. On the **Change start and desired value of the key result** screen, update the start and target (desired) values.
4. If you want the new values and unit to apply to the previous KR updates, check the option below the start value.

![The Change start and desired value of the key result screen.](/cms_trial/assets/ef8f118a-dc15-4ec0-bc0d-0d88c3452966.png)

Cannot see the **Edit configuration** option in the menu? It means your Key Result is in auto-mode. [Convert it](/cms_trial/space/SPM/2223538218/Convert+OKR/) to manual mode first.

## Update manual KR progress

You can [update the KR progress](/cms_trial/space/SPM/1918507253/Update+OKR+progress/) value on the KR update screen. (The **Current** field is grayed out for auto-KRs.)

![KR update modal partial screenshot focusing the Progress fields.](/cms_trial/assets/a1767377-f01e-4814-958e-d3c428293d1f.png)

As the current value increases, the app calculates the progress according to the formula:

`(current - start) / (target - start) = progress x 100%`

The change in progress is reflected in the OKR module’s individual pages:

- [*Overview*](/cms_trial/space/SPM/1918834317/OKR+Overview/) page (**Progress** column)
- [*Hierarchy*](/cms_trial/space/SPM/1918669889/OKR+Hierarchy/) page
- [*Progress Dashboard*](/cms_trial/space/SPM/1918801225/Progress+Dashboard/) page
- [*OKR Details*](/cms_trial/space/SPM/1918536390/OKR+details+page/) page (**Progress** tab)

![okr-details-page-kr-progress.png](/cms_trial/assets/5aca35c1-b9cc-4974-9b9e-9147356615a0.png)

### KR target on track: Example

Say you want to conduct a series of UX interviews to gather feedback from current customers about the app you launched a few months ago. Your KR could be: “Conduct 25 customer interviews to understand product usage and satisfaction.”

Since you have not started any interviews yet, the values for such an OKR would be as follows:

- Start value: 0
- Target value: 25 (you want to conduct 25 interviews in a specific OKR period)
- Current value: 4 (4 interviews conducted so far)

The unit for this KR is purely numeric, since you're aiming for a specific number of interviews. Once a few interviews are conducted, you can update the current value to reflect the progress, for example, 4.

As a result:

`(4 - 0) / (25 - 0) = 0.16 x 100% = 16%`

![An example of the manual KR progress.](/cms_trial/assets/deb63635-9c30-45e2-8a46-37ef2bac7406.png)

### KR target surpassed: Example

What if your teams went that extra mile and conducted 3 more interviews than initially planned (25)? In that case, progress will exceed 100%.

- Start value: 0
- Target value: 25 (you want to conduct 25 interviews in a specific OKR period)
- Current value: 28 (28 interviews conducted in total)

`(28 - 0) / (25 - 0) = 1.12 x 100% = 112%`

![An example of the manual KR progress.](/cms_trial/assets/ff65fa97-2bc7-494d-aafc-d2d5d47c170f.png)

### KR below target: Example

You want to reduce customer churn from 10% to 5%. Unfortunately, due to unforeseen events, churn rose to 13%.

- Start value: 10
- Target value: 5 (you want to conduct 25 interviews in total in a specific OKR period)
- Current value: 13 (churn has increased to 13%)

As a result:

`(13 - 10) / (5 - 10) = -0.6 x 100% = -60%`

![An example of the manual KR progress.](/cms_trial/assets/4b7d7ca0-232c-4238-86b0-7f017f4e5752.png)

You can [link work items](/cms_trial/space/SPM/1918507296/Link+work+items+to+Key+Results/) and boxes to a manual KR. Linked work items an[d boxes](/cms_trial/space/SPM/2229665803/Link+boxes+to+Key+Results/) do not affect manual KR progress, but they are useful to provide visibility and context.