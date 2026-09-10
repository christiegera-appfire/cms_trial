# Team-related issues

## When assigning the team to a story, it appears as "unknown team."

A team is created, members added, and assigned to a specific board. However, the team is not showing up on the board. Additionally, when attempting to assign the team to a story, it shows as an "unknown team" even though the team is assigned to the same board.

### Preconditions

- **Auto-inherited upper-level teams** toggle switched off for the Iteration box type.
- Teams created and assigned in the upper-level ART box.

### **Steps to Reproduce**

1. Create a team.
2. Add members to the team.
3. Assign the team to a board.
4. Attempt to assign the team to a story on the same board.

**Expected Behavior:**

- The team should appear on the board.
- When assigning the team to a story, it should show correctly as the assigned team.

**Actual Behavior:**

- The team does not appear on the board.
- When assigning the team to a story, it appears as "unknown team."

### Solution

The issue is caused by the **Auto-inherited upper-level teams** toggle being disabled in the **Iteration** box type. This prevents teams assigned at the ART Box level from being inherited by Iteration Boxes, resulting in tasks being grouped under “Unknown Team.”

Once this setting is enabled, the behavior is corrected and consistent. What matters is whether the Iteration Box can access team data via inheritance or direct assignment.