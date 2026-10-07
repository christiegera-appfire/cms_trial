# Release notes 7th October 2026

**Release date**: October 7, 2026

This page outlines the updates included in the latest release of Comala Document Management Cloud.

**App version:** 52.2.0

**Release version:** 5.0.34

---

## Enhancements

### Global and Space Settings

- **Settings** tabs now use consistent naming and ordering across *Global Settings* and *Space Settings*.

### Space Workflows

- You can now view **workflow history** from *Space Workflows,* matching the experience in *Global Workflows*.

### Document Activity

- Document Activity now records a **Created content** entry when you create a page or blog post.
- Document Activity CSV exports now use a consistent file name that identifies the content and the export date and time.

### Workflow builder

- Conditions now include an operator selector. Choose `equals` or `not-equals`, and enter one or more values to compare. With multiple values, `equals` matches any value, while `not-equals` matches none. Existing workflows continue to work without changes and are updated to the new format only when you edit them.

### Parameters and metadata

- Workflows can now reference Comala Document Management parameters and metadata by name using value references such as `@Parameter['Name']@` and `@Metadata['Name']@`. References resolve to the current value when the workflow runs, so you can reuse parameters and metadata in conditions, triggers, and actions. For example, you can use references to preassign reviewers or populate email content.
- For parameters, Comala Document Management uses the first available value from the page, workflow, or parameter default, in that order. For metadata, it uses the first available value from the page or space.

## Bug fixes

The following bugs are fixed in this release:

- The return link in the workflow builder now goes to the *Global Workflows* tab instead of the *Global Document Report* tab.
- Page diagnosis no longer returns an error when retrieving legacy workflow state content.

---

**Questions and feedback**

- Explore exciting features, pricing updates, reviews, and more on the [Marketplace](https://marketplace.atlassian.com/apps/142/comala-document-management?hosting=cloud&tab=overview).
- Stuck with something? Raise a ticket through our [support portal](https://appf.re/support).
- Do you love using our app? Let us know what you think [here](https://marketplace.atlassian.com/apps/142/comala-document-management?hosting=cloud&tab=reviews).

**Credits**

Thank you to our valued customers! Your incredible support and feedback inspire us to improve continuously. We appreciate your trust in Appfire's Comala Document Management Cloud!