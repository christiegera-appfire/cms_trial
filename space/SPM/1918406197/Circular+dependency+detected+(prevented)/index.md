# Circular dependency detected (prevented)

If you can see this message, a circular dependency would exist if the shift action defined by structure builders were performed.

![contentId-1918406197](/cms_trial/assets/b863f316-0df7-4422-842c-8f7fd2b46117.png)

## Why do I see this message?

[Task structure](/cms_trial/space/SPM/1918667217/Manage+task+structure/) rules conflict.

Rules with an opposite effect have been created (in two different Boxes that share at least part of their scope). Those rules are trying to produce contradictory results:

![contentId-1918406197](/cms_trial/assets/8a673767-6fd7-4cbd-9c89-1f0fc06737db.png)

## How to fix the issue?

Changes to the WBS structure haven't been applied because of the conflict. To fix the issue:

- Correct the task structure rules in one of the affected Boxes
- or change the task details to ensure all Box rules can be applied at the same time

**Once the issue has been addressed, clear the warning log and trigger a data re-sync.**

## Case 1 - Inverse vs. normal use of link-based structure builders

Any "link-based" structure builders can lead to this situation because they have the "inverse" option.

![image2022-3-11_8-19-55.png](/cms_trial/assets/c169fa9d-c210-4691-8ba9-b610d1c5cd3a.png)

The app can't fulfill the setup when:

- Tasks are in two separate Boxes (Boxes share at least part of their scope)

  ![contentId-1918406197](/cms_trial/assets/7ae1cc32-f99f-4450-a435-67566f9a4a26.png)
- "link-based" structure builders have been used to create a WBS structure (in one Box, the "inverse" checkbox has been selected; in the other one, it's empty).

  ![contentId-1918406197](/cms_trial/assets/964ca535-f9ef-475d-8bb2-394392b9639f.png)

Those rules have the opposite effect. They would produce contradictory results:

![image2022-3-11_8-15-33.png](/cms_trial/assets/8a673767-6fd7-4cbd-9c89-1f0fc06737db.png)

In the example, the "Relates" link type has been used:

- Normal links:

  ![contentId-1918406197](/cms_trial/assets/e483b4ed-6c88-4d84-964f-992c808cd05d.png)
- Inverted links:

  ![contentId-1918406197](/cms_trial/assets/1bc95ab3-a9d9-4c2f-8c9c-d253b41f1707.png)

## Case 2 - structure builders in the opposite order

Different order of structure builders in two Boxes (with the same scope).

![contentId-1918406197](/cms_trial/assets/091ec62a-a134-4cbd-b745-f1dbd6be446b.png)

The two Boxes share at least part of their scope:

![image2022-3-11_7-39-54.png](/cms_trial/assets/7ae1cc32-f99f-4450-a435-67566f9a4a26.png)

Those rules would try to create an opposite parent-child relationship in those Boxes (both can't be true simultaneously).