# Create risk register

Hedge lets you create multiple risk registers tailored to the specific needs of your teams, projects, or compliance standards. Whether you choose from predefined templates or design custom ones, each register can be configured to align with your unique workflows and requirements.

See how fast and easy it is to create a risk register in Hedge.

## Define the register's scope

When you create a risk register, you choose which risks it includes:

- **Projects** (required): select one or more projects.
- **Issue Types** (optional): limit the register to specific work item types.
- JQL query (optional): narrow the scope further with a Jira Query Language (JQL) query. Use it to split risks into separate registers by initiative, department, component, team, priority, or any other criteria.

Hedge combines these settings with AND. A risk appears in the register only if it matches all of them:

```text
project in (<selected projects>) AND type in (<selected work item types>) AND (<your JQL query>)
```

You can change the scope later in the register's settings. To learn more, see [Customize the risk register](https://support.appfire.com/space/HED/602865672/Customize+the+risk+register).