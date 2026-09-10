# Potential scope misconfiguration

![contentId-1918505821](/cms_trial/assets/75d1712c-035a-499e-b31b-974702797ccf.png)

Depending on your Jira settings, your issues may have multiple fields filled out. Each of those fields can be used for sync with a sub-box. Potentially, an issue can have various fields filled out. This can become a problem if multiple fields are used for sync—there can be two conflicting rules. Remember, an issue cannot be simultaneously assigned to two sub-boxes.

For example:

The first sub-box (PI1) is synchronized with the 'Change risk' field (value = Low).

The second sub-box (PI2) is synchronized with the 'Risk probability' field (value = Medium).

![contentId-1918505821](/cms_trial/assets/ebb0e491-a372-4d0e-80f1-5aa5c6b0dd39.png)

In Jira, there is no problem. However, if an issue meets both of those conditions (has both fields filled out as shown above), the app would have to try to put it in both boxes simultaneously, which can't be done.