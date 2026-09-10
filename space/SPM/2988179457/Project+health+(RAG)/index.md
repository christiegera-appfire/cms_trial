# Project health (RAG)

Visit the [Contextual reports](/cms_trial/space/SPM/2481848664/Contextual+reports/) page to learn about availability, permissions, and how to add reports to your view.

See the video about the project health report.

## Project health

The Project health report visualizes project health using the RAG (Red-Amber-Green) system.

![Project health report.](/cms_trial/assets/7662a2ae-c29f-430d-855b-329c8fc626a6.png)

It displays a clean, visual status overview with three colors: Green (on track), Amber (caution/risks), and Red (critical issues/immediate action needed).

The following project health indicators are shown:

- **Progress burndown**
- **Capacity vs. workload**

When a team's workload exceeds the capacity thresholds defined in the *Administration* settings, the indicator’s color will automatically update. For example, if a team with a capacity of 10 story points is assigned 12 story points for the Sprint, the 120% utilization rate triggers an "exceeded capacity" (Red or Amber) status.

- **High severity risks**

### Customize the indicator thresholds

The color-status thresholds for each indicator can be customized by a Jira Admin and [App Admin](/cms_trial/space/SPM/1918535770/App-level+permissions/) in **App settings** > **Administration** > **Reports**.

![context-report-project-health-administration.png](/cms_trial/assets/12cfcd8e-6d5a-46fb-9e8d-81a2d7af00d9.png)

### Change the report view

The Project health report offers two different views you can switch between by clicking the middle button in the top-right corner:

- **Pie chart**: Shows health statuses for the parent box (based on all child boxes). If the box has no children, no data is displayed.

![Project health report. Pie chart view.](/cms_trial/assets/d699b25e-d0c3-4b49-a343-2b360fcb696e.png)

- **Table**: Shows health statuses for the current box.

![Project health report. Table view.](/cms_trial/assets/037b5fe3-0240-430e-9c2c-76dbcfe174e3.png)

### Check the health of the sub-boxes

To see which sub-boxes fall within the selected RAG category, click the corresponding color on the pie chart or the status in the pie chart view.

![Initiatives that are off track.](/cms_trial/assets/50325dc3-cf92-45d4-ab16-26e9849e3980.png)

### Customize the RAG settings

Box Admins and Box Editors can customize the report:

1. Click the **cog** button on the report.
2. Select one option in each category:

![Project health report settings.](/cms_trial/assets/d56fb2a6-77fd-4e5c-b3fc-ac97db19d821.png)

- **Project health selection mode**:

  - Automatic - based on all metrics (app automatically assigns the overall project health status)
  - Manual - user selected (user assigns the project health status manually)
- **Report scope**:

  - Portfolio
  - Own-scope
  - Sub-boxes
- **Progress**:

  - Original estimate
  - Story points

Burndown progress calculations are based on your selected configuration, which currently supports either story points or original estimate as the primary metric. It is not possible to calculate the combined project health of the box when some sub-boxes have effort expressed in story points and others in the original estimate.

- **Capacity vs Workload**

  - Workload
  - Overall capacity

1. Click **Save** to finish.

### Manually assign the project health status

To manually assign the health status to your project:

1. Select the **Project health selection mode** in the report settings.
2. Switch to the table view.
3. Click the top health indicator to open the dropdown
4. Select the status to assign it to the current box:

   1. **Not set** (gray)
   2. **Off track** (red)
   3. **At risk** (amber)
   4. **On track** (green)

![A dropdown for manual selection of the project health status.](/cms_trial/assets/df876e86-0617-44e3-90c8-110c8ca294a9.png)

## How is the project's risk health calculated?

The data used to calculate the health status of risks in your project is pulled from the [Risk Management](/cms_trial/space/SPM/1918798201/Risk+management+module+(new+module)/) module.

The calculation is based on a matrix algorithm that is independent of user-defined colors or labels. Instead, it analyzes the risk's position (coordinates) within the risk register (matrix).

Visit the [Create new risks register](/cms_trial/space/SPM/1918406430/Create+new+risk+register/) page to learn about the sizes and types of risk registers (risk matrices).

The risk calculation process consists of three main steps:

- **Normalization**: The app converts risk values into coordinates (Indices).
- **Severity Index Calculation**: It then determines the numerical "strength" of the risk.
- **Classification**: And finally, it compares the result against thresholds (which depend on the matrix size).

The system "virtually" builds the matrix (under the hood) and tests every possible cell. The algorithm below flags cells that return the HIGH status.

#### Calculation algorithm

START: **Task risk analysis**.

1. **Get matrix dimensions** (N x N).

Example: For a 5x5 matrix, N = 5.

1. **Determine risk coordinates on the matrix** (X, Y).

Values are sorted in ascending order: Lowest = 1, Highest = N.

Example: Risk Likelihood is 5 and Risk Consequence is 4 => X =5 and Y = 4.

1. **Calculate the severity index**.

a) Find MIN and MAX for the XY coordinates:

min = Math.min(X, Y)

max = Math.max(X, Y)

b) Check the Spread:

Is (max - min) > 1?

YES (large spread) => Index = max -2

NO (close together) => Index = min

1. **Determine a HIGH threshold** (based on N).

Is N >= 5? (Large matrix)

YES => HIGH threshold = N -1

NO => HIGH threshold = N

1. **Final verdict**

Is Index >= HIGH threshold?

YES (HIGH) => Included

NO (LOW/MEDIUM) => Ignored

---

### Risk health calculation examples

#### Scenario 1: A large 5x5 risk matrix

For a 5x5 matrix, the HIGH threshold is 4 (5 - 1 = 4).

For a cell (5,5):

min = 5, max = 5 => Difference = 0

Index = min = 5

5>=4 => 🟥 HIGH risk (the highest possible risk; included).

For a cell (4,5) or (5,4):

min = 5, max = 4 => Difference = 1

Index = min = 4

4>= 4 => 🟥 HIGH risk (included).

For a cell (3,5):

min = 3, max = 5 => Difference = 2 (large spread)

Index = max - 2 => 5 - 2 = 3

3 < 4 => 🟧 MEDIUM risk (not counted as HIGH)

Final verdict: For the 5x5 matrix, the "high risk" zone is effectively the 2x2 block in the top-right corner.

---

#### Scenario 2: A medium 3x3 risk matrix

The algorithm is more restrictive in this scenario.

For a 3x3 matrix, the HIGH threshold is 3 (N =3).

For a cell (3,3):

min = 3, max = 3 => Difference = 0

3 >= 3 => 🟥 HIGH risk

For a cell (2,3):

min =2, max = 3 => Difference = 1

Index = min = 3 - 1 = 2

2 < 3 => 🟧 MEDIUM risk

### Questions and answers

**Q**: What if I set my highest risks in the bottom-left corner?

**A**: BigPicture will ignore your "highest risks" in the bottom-left and will count those in the top-right instead. This happens because the mechanism relies on numerical values (`value`), not colors or UI placement.

**Example**:

In this scenario, you used a sort of "inverted Logic” to classify your risks. The 1 = Worst and 5 = Best. If you configure a matrix where **1x1** is "Critical" (Red), and **5x5** is "Safe" (Green), then:

1. **Sorting**: The app sorts the values in ascending order: 1, 2, 3, 4, 5.
2. **Anchoring**: The algorithm always looks for the maximum values (5x5), assuming that higher numbers indicate higher probability and impact.
3. **Result**: The app will flag the safe (green) level as **High Severity** and include those tasks in the report.
4. **Ignore**: Your bottom-left corner (1x1, red) will be mathematically treated as **Low Severity** and ignored.

This is not a bug but an intended behavior.

The Risks module also assumes risk increases with the numerical sequence. It adheres to the philosophy that a higher number = a higher risk.

Soif the bottom-left is just a result of UI sorting (for example, displaying descending order) but the numerical values remain standard (Worst = 5), the calculation will work perfectly. The system ignores the UI and looks only at the numbers.

This ensures that even if you label a cell (5,5) as "Low" (text-wise), the system will mathematically identify (5,5) as a critical position and include those tasks in the Project health report.