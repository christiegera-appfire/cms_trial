# Use case: Create a portfolio of portfolios

|  |  |
| --- | --- |
| **Goal** | **Create a portfolio of portfolios**  You want to nest a set of portfolios under another portfolio. You also want to create new portfolios under their respective parent portfolios. |
| **Scenario** | As a Portfolio Manager, you manage several portfolios in your organization. For smarter, scalable, and more strategic management, you want to group those portfolios into portfolio hierarchies (composite portfolios). |
| **Key benefits** | - Grouping allows managers to analyze performance across multiple portfolios - Enables composite performance reporting - Managers can monitor overall risk and allocation trends across related portfolios - Helps in organizing large initiatives by, for example:    - Client group   - Investment strategy   - Geography   - Portfolio manager   - Risk category |

## Preconditions

- box admin sub-box creator You are a Portfolio [Box Admin or Sub-box Creator](/cms_trial/space/SPM/1918797447/Box-level+permissions/) (to add new portfolio boxes).
- box admin You are a Home Box Admin (to nest other portfolio boxes under your portfolio box)
- Jira admin App admin Your Jira or App Admin has adjusted **Parent type** settings on the Portfolio **box type configuration** page (if not, see the detailed instructions for your Admin below)

Add a Portfolio as a parent type to the Portfolio box type

1. Click the **App settings** (**wrench icon**)and select the **Box types** from the dropdown (under the **Administration**).
2. On the **Box types** page, open **Portfolio**.
3. On the **General** > **Basics** page, you can see the **Parent types** settings. By default, the only parent type box to a Portfolio box can be the **Main** type (Home/root box). Click the empty space and add **Portfolio** from the list.

![Change parent type to a portfolio box type on the box type configuration page.](/cms_trial/assets/1c3f997c-c615-4387-ad12-35f8cf959ff8.png)

1. Click **Save** to finish the process.

See the video below to review the complete process.

![How to add a portfolio to another portfolio box.](/cms_trial/assets/3811fdc6-a23d-4dbf-9357-7e441d4210e4.mp4)

## Create a portfolio of portfolios step-by-step

Once the Jira or App Admin adds Portfolio as the **Parent type** to the Portfolio box type, all the current and future portfolio boxes created in your organization can hold other portfolio boxes. In other words, portfolio boxes can be parents to portfolio boxes.

For that reason, you can go about creating a composite portfolio in two ways:

- Create new portfolio boxes under the existing portfolio box.
- Move the existing portfolio boxes under the existing portfolio box.

### Scenario 1: Create a new portfolio under another portfolio

1. In the Overview module on the Home box level, open an existing portfolio box (the one you want to turn into a composite portfolio).
2. Click the **+Add new** button and [create a new portfolio box](/cms_trial/space/SPM/1918634872/Create+portfolio+box/).

Your new portfolio box was successfully created under another portfolio box. You can now populate it with the existing project boxes, create new project boxes for future projects, or another portfolio box.

### Scenario 2: Nest existing portfolios under another portfolio

1. In the Overview module on the Home box level, drag the portfolio box and drop it under the target portfolio box.

The portfolio box you moved is now part of the composite portfolio, including all of its children.

![The process of moving (drag and dropping) one portfolio under another on the home box level in the overview module.](/cms_trial/assets/9f084fda-3377-4a04-83f2-895d03e1bc16.mp4)

## Expected outcomes

You can create new portfolios and nest the existing ones to build as robust a portfolio hierarchy as you see fit.

![The Legal portfolio box is nested under the Project Portfolio box.](/cms_trial/assets/4f15bbd5-488e-447d-9de1-0e104715098f.png)

## Additional resources

- [Create portfolio box](/cms_trial/space/SPM/1918634872/Create+portfolio+box/)
- [Box types](/cms_trial/space/SPM/1918830000/Box+types/)