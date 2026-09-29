# MCP

MCP integration is currently available for **beta testing** with select partner organizations. You can reach out to check availability for testing via [support portal](https://appfire.atlassian.net/servicedesk/customer/portal/11).

The **Model Context Protocol (MCP)** integration in 7pace Timetracker enables AI coding assistants (such as Cursor and Claude Desktop) to interact directly with 7pace Timetracker. Using MCP, your AI assistant can analyze your coding activity, Git commits, active branches, and prompt history to propose and automatically record accurate time logs.

## Access

Before individual users can connect their AI clients, MCP must be enabled at the organization level by a 7pace Administrator:

1. Open **7pace Settings**.
2. Select the **Integrations** tab.
3. Locate the **MCP Integration** section.
4. Click **Enable MCP** and acknowledge the administrative agreements and permission requirements.

![enable-mcp.png](/cms_trial/assets/db5d3406-ef3e-4093-91e8-53f41b92fe8f.png)

The following acknowledges and administrative agreements are required to enable the MCP option:

- **Terms and conditions**: “I acknowledge that our use of the services is governed by Appfire's terms and conditions.

  [View Appfire’s terms and conditions﻿](https://apps.appf.re/7pace/jira/doc/ssa)“
- **Data and privacy**: 'I acknowledge that we have received and read the privacy policy.

  [View Appfire’s privacy policy﻿](https://apps.appf.re/7pace/jira/doc/privacy-policy)“
- **Enable MCP for your organization**: 'I acknowledge that members of our organization will be able to connect AI agents to 7pace through MCP using personal API tokens. AI agents may create worklogs on a user's behalf, subject to individual consent, and may make mistakes.

  [View MCP documentation﻿](https://apps.appf.re/7pace/jira/doc/mcp)[﻿](https://apps.appf.re/7pace/jira/doc/mcp)  
  [View EULA﻿](https://apps.appf.re/7pace/jira/doc/eula)“

## Connecting AI clients

In **7pace Settings** navigate to personal Settings, next **MCP / API Tokens.**

![mcp-tokens.png](/cms_trial/assets/2c7ab778-1217-476c-9645-b68ebca6b1ff.png)

### Step 1: Generate an API token

Click **Create Token** to generate a new personal token for MCP access. Choose a name and validity date. Tokens can be valid for up to one year. You can choose a shorter validity date.

Select **Create**.

![create-token-1.png](/cms_trial/assets/eb8b7abe-fff3-4a85-bf07-c775d6e6b0c2.png)

Now you can copy the token.

Copy and save the token. You **CANNOT** recover the token after this step is finished.

![create-token-2.png](/cms_trial/assets/9873580c-15bd-4b30-b96f-beb72b16d078.png)

### Step 2: Configure your client

You can connect your client using either of the following methods using the MCP server URL `https://timehubjra.7pace.com/mcp`:

- **Quick Setup (Recommended for Cursor):** Click **Copy cursor configuration**. This copies a pre-formatted configuration block directly to your clipboard. Paste it into your Cursor MCP settings.
- **Manual Setup:** Copy the generated API Token manually, then paste the token into your AI agent's MCP configuration settings.

Save the configuration in your client. The connection takes effect immediately without needing to restart the app.

#### Configuration Examples

#### Cursor **(**`.cursor/mcp.json`**):**

```json
{
  "mcpServers": {
    "7pace": {
      "url": "https://timehubjra.7pace.com/mcp",
      "headers": {
        "Authorization": "Bearer <YOUR_TOKEN>"
      }
    }
  }
}
```

#### Claude Desktop **(**`claude_desktop_config.json`**):**

```json
{
  "mcpServers": {
    "7pace": {
      "command": "npx",
      "args": [
        "-y",
        "mcp-remote@0.1.38",
        "https://timehubjra.7pace.com/mcp",
        "--header",
        "Authorization: Bearer <YOUR_TOKEN>"
      ]
    }
  }
}
```

## Example usage: Logging Time using MCP

### Interacting with the AI Agent

Prompt your AI assistant using natural language commands, such as:

- *"Log time for the work I did today."*
- *"Log time to DEMO-6."*

### How the MCP Agent Works

1. **Context Gathering:** The agent invokes MCP server commands (such as `list_worklogs`) to retrieve existing worklogs, prompt activity count, Git branch names, and commit history.
2. **Target Resolution:** If a Jira issue key is not explicitly provided, the agent attempts to infer the target issue key from your active Git branch or commit messages.
3. **Break and Gap Detection:** Calculates duration while accounting for coding gaps, non-interactive periods, and breaks.

## Safety Guardrails and Validation Policies

To prevent unauthorized or erroneous time entries, 7pace MCP incorporates several strict guardrails:

- **Multi-Step Proposal Confirmation:** The agent generates a *proposed worklog* detailing duration, target issue key, commit/prompt summary, and proposed comments. The user **must explicitly confirm** the proposal before any worklog is recorded in 7pace.
- **Duplicate and Conflict Detection:** Automatically flags and blocks overlapping worklog entries or duplicate logs for the same activity.
- **Capacity and Period Locking:** Strictly enforces workspace daily hour limits and period lock restrictions.
- **Custom Rules and Required Fields:** Enforces project rules, required custom fields (for example, billing items), and issue status restrictions.
- **Throttling and Data Privacy:** Protects sensitive data and limits request rates.