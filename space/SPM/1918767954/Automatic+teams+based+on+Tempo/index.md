# Automatic teams based on Tempo

## How does the Team synchronization work?

Team names are used.

The following Team Tempo attributes are synced:

- Team Name
- Team Summary
- Team Members who are Jira users (including Team Members added using Jira groups). A Team Member is synchronized with all its Memberships, including:

  - Joining Date
  - Leaving Date
  - Skill
  - Availability

The following team Tempo attributes are **NOT** synchronized:

- Team Mission Team Lead (a user who is the team leader)
- Team Program (Program in Tempo is a group of Teams; each Team Tempo can belong to a maximum of 1 such group)
- Team Members who are not Jira users (Tempo lets you add such "virtual" Members)
- Permissions Links to Boards and Projects

During Team Synchronization, all Skills with Tempo are synchronized, and missing Resources are created (as NATIVE).