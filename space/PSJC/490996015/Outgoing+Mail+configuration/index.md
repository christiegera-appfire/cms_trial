# Outgoing Mail configuration

This guide explains how to configure the outgoing mail functionality for Power Scripts for Jira Cloud. These settings control the global mail configuration used by the `sendMail()` function, letting you customize how the system sends emails to recipients. Understanding these configuration options is essential for system administrators and developers who need to implement email notifications, alerts, or other automated communications through Power Scripts.

## How to access the Outgoing Mail configuration

To access the Outgoing Mail configuration:

1. Click **Settings** > **Marketplace Apps**.
2. Go to **Power Scripts** > **Configurations** > **Integrations** > **Outgoing Mail**.

![Power Scripts for Jira Cloud gadget parameter configuration](/cms_trial/assets/5baee7c3-560a-4eff-b2a0-4831ca2272ab.png)

---

## Key configuration settings

The Outgoing Mail configuration consists of three primary elements: email templates, mail language settings, and mail sender type.

| **Configuration setting** | **Type** | **Description** |
| --- | --- | --- |
| **Mail Templates Directory** | field | Specifies where email templates are stored and how they're organized. The default *Mail Templates Directory is* `/jirasoftware-home/kepler/templates`.  Both the [sendEmail](/cms_trial/space/PSJC/433654656/sendEmail/) and [executeTemplate](/cms_trial/space/PSJC/435028509/executeTemplate/) functions use this path. |
| **Mail language on** | drop-down menu | Controls which language is used for emails. Options include:   - **Sender**: Emails use the language of the person sending the email. - **Receiver**: The system creates separate emails in each recipient's language. |
| **Send mail via** | drop-down menu | Determines how emails are delivered from the system. Options include:   - **Null sender, log only**: Logs the email content without actually sending it (useful for debugging). - **Direct sender, custom**: Sends emails directly to mail servers with custom SMTP configuration options including protocol, mail host, port, authentication credentials, and from address. When you choose this option, your script will pause execution until it receives confirmation that the mail server has accepted the email.   Email that is successfully sent does not automatically translate into the recipient receiving the email. It can be rejected for multiple reasons. SMTP does not guarantee delivery.  If you are unsure what to enter in the **Direct sender, custom** configuration form, ask your network administrator to provide details of your company mail setup. |

---

## About email templates

Email templates in Power Scripts for Jira Cloud support multiple languages, enabling you to send emails in the appropriate language based on either the sender's or receiver's language preference.

- Email templates are text files with a `.tpl` extension.
- They are stored in the **Mail Templates Directory** you specify and must follow a specific naming convention for proper language detection.
- Templates can contain HTML, plain text, or a combination of both, along with Simple Template Language (STL) code.
- You can create and edit templates using one of the following:

  - Any text editor of your choice.
  - The built-in template editor in SIL Manager, accessible from the `kepler` home tree view as shown in the screenshot below:

    ![SIL Manager templates folder.](/cms_trial/assets/e572224d-ce66-44a3-854f-3f1a6be72815.png)
- For optimal language resolution, we recommend organizing your email templates in the following structure within your specified templates directory:

| **For…** | **Use…** | **Example** |
| --- | --- | --- |
| Language and country-specific templates | `/[language_code]_[country_code]/templatename.tpl` | `/fr_FR/mytemplate.tpl` for French (France) |
| For language-only templates | `/[language_code]/templatename.tpl` | `/fr/mytemplate.tpl` for French (any region) |
| For default templates | `/templatename.tpl` | `/mytemplate.tpl` (used when no language-specific template is found) |

This structure aligns with the language resolution algorithm described below and ensures your templates are selected based on language preferences.

### How language resolution works

The system uses a hierarchical approach to locate the appropriate template for a given language. Let's walk through an example with the template file `mytemplate.tpl` for a French (France) user. The table below outlines the key steps of the language resolution process:

|  |  |
| --- | --- |
| First search | The system looks for `fr_FR/mytemplate.tpl` in your templates directory   - Uses the two-letter language code plus the two-letter country code format. - This allows for regional language variations (like French/France vs. French/Canada). |
| Second search | If not found, the system looks for `fr/mytemplate.tpl`   - Uses only the language code, ignoring regional variations. - Provides general language support when region-specific templates aren't available. |
| Fallback search | If still not found, the system looks for `mytemplate.tpl` in the mail templates directory.   - Uses the default template when no localized version exists. |
| Error case | If none of these files exist, the system returns an error. |

### How to create template content with SIL Template Language (STL)

Within your email templates, you can include dynamic content using STL.

For basic field references, use the  `$field$` notation to insert any standard or custom field value from the issue that triggered the email. For example:

```text
Hello $assignee$,

A new issue ($key$) has been assigned to you by $reporter$.
```

More advanced uses of STL include embedding SIL scripts within the email templates, enabling sophisticated dynamic content, such as:

- Conditional sections (showing content only under certain conditions)
- Loops (generating repeated content, such as table rows)
- Complex calculations or text formatting

For detailed information on using STL in your templates, please refer to the [SIL Template Language](/cms_trial/space/PSJC/496336897/SIL+Template+language/) and [Email templates](/cms_trial/space/PSJC/496336933/Email+templates/) pages.

---

## About Mail language settings

The **Mail language on** setting in your Outgoing Mail configuration affects how templates are selected and emails are sent:

| **When set to…** | **Then…** | **Use for…** |
| --- | --- | --- |
| **Sender** | - The system uses the sender's language preference to select a single template - One email is sent to all recipients using this template | Simpler, efficient processing. |
| **Receiver** | - The system groups recipients (from TO, CC, and BCC fields) by their language preferences. - For each language group:    - The appropriate template is selected based on that language.   - A separate email is sent to that group. For example, if you have English, French, and Spanish recipients, up to three separate emails might be sent. | More personalized experience for recipients.  Using this option can result in multiple emails being sent for a single action, higher resource usage (memory and processing). It can also impact performance, especially when using email queues. |

---

## More configuration guides