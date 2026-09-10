# set-expiration

The **set-expiration** trigger action is used to add or update the due date for a workflow state.

![Comala visual editor setexpiration trigger with due date period options](/cms_trial/assets/dcfdc977-078d-4af2-a73a-ecbce66ca145.png)

The expiration is set for the workflow state specified in the workflow trigger condition. If no condition is set, the expiration is set for the workflow state when the event occurs.

## Set expiration action parameters

| **Action Parameter** | **Value** | **Notes** |
| --- | --- | --- |
| **Due Date** MANDATORY | Duration period or fixed date and time   - **Period**: the duration period set for expiration as one of years, months, days, minutes, or seconds - **ISO\_8061**: duration period set for expiration in a formatted duration string, such as **P1D** - **Fixed Date\*** as a specific date and time in user-preferred date format\* | A value must be added for the **Due Date**.  The **Set Expiration** trigger action overrides any existing expiration for the state. |

When the workflow trigger event occurs, it checks that any required conditions are met. If met, the `"set-expiration"` action sets a new expiration date. The due date can be a period of time or a specific date and time.

## Add a fixed due date

In some Cloud instances, you can only use the code editor to set the due date to a specific date and time.

![Comala code editor setexpiration trigger with fixed date value](/cms_trial/assets/b54b390d-f3fa-4465-bbd2-01709cb9c03c.png)

After adding it, you can switch to the visual editor to modify the fixed date.

![Comala visual editor setexpiration trigger with calendar date picker](/cms_trial/assets/30ea5e0d-4ece-4c52-99f3-033eb4cd58a9.png)

If you change the **Due Date** to a duration in the visual editor, the **Fixed Date** will be removed. You must then add a new **Fixed Date** value using the code editor.

## “set-expiration” JSON code

A **Set Expiration** workflow trigger action added using the [visual editor](/cms_trial/space/CDMC/2193162438/Visual+builder+editor/) is automatically displayed in the workflow [code editor](/cms_trial/space/CDMC/2192837873/JSON+code+editor/) as a `“set-expiration”` trigger action.

![Comala visual editor setexpiration trigger action settings](/cms_trial/assets/fb17d71b-2152-4dea-98bc-bc0f5cdcf4ea.png)

You can also use the code editor to add the workflow trigger and the `“set-expiration”` action.

## "set-expiration" parameters and workflow example code:

### `"set-expiration"`

"`set-expiration`" sets an expiration due date for a state.

- **action (*****set-expiration*****)**

  - **dueDate❗️** Expiration due date

    - period (in ISO 8601 format)
    - fixed date (in the Confluence user-preferred format for the site)

---

### ❗️ Mandatory parameter

**dueDate**

A value must be added for the due date.

---

### Example workflow trigger code

```text
"triggers":
[
	{"event": "on-change-state",
	"conditions":
	[
		{"final":true}
	],
	"actions":
	[
		{"action": "set-expiration",
			"dueDate": "P6M"}
	]}
]
```

The `"dueDate"` in the above example is set using ISO 8601 format. For example, adding **P6M3W5D** adds a due date period that is 6 months, 3 weeks, and 5 days.

An existing state expiration can be removed using the [clear-expiration trigger action.](/cms_trial/space/CDMC/2193950419/clear-expiration/)