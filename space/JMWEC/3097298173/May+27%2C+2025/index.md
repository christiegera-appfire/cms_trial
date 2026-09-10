# May 27, 2025

## Feature Release - JMWE for Jira Cloud 1.2.44

**Release date**: May 27, 2025

This release of **JMWE for Jira Cloud** includes updates to the callRest and callJira APIs, adding support for FormData. Additionally, some bugs have been resolved.

---

## Enhancements

## APIs

### FormData support in callRest and callJira APIs

The callJira and callRest Nunjucks filters have been updated to both support form data! callJira has been expanded to support additional API endpoints, and callRest has been updated with a new parameter - headers - that adds support for processing form data. See [callJira](/cms_trial/space/JMWEC/465243039/callJira/) and [callRest](/cms_trial/space/JMWEC/465242995/callRest/) for more information.

## Bug fixes

The following bugs are fixed in this release:

- **Errors when using the ‘Ignore deactivated user(s)’ option** - In some configurations, post functions are encountering the same error when the ‘Ignore deactivated user(s)’ option is either checked or unchecked. This has been resolved.
- **‘Time spent’ fields not validating correctly** - The [Field required](/cms_trial/space/JMWEC/465242701/Field+Required+Validator/) validator is not working when configured to require a “Time spent” field. This has been resolved.
- **UI fix for Assign issue(s) post function configuration screen** - The help text below some configuration options is displaying incorrectly and is not legible. This has been resolved.

---

**Questions and feedback**

- Explore exciting features, pricing updates, reviews, and more on the Marketplace.
- Stuck with something? Raise a ticket with our support team.
- Do you love using our app? Let us know what you think here.

**Credits**

A heartfelt thank you to our valued customers! Your incredible support and feedback inspire us to improve our apps and products continually. You are the driving force behind why we create software. We appreciate your trust in JMWE!