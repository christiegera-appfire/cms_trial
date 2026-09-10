# Release notes 17 February 2026

**Release date**: February 17, 2026

Our team is thrilled to announce the latest release of the Dashboard Hub family of apps for Jira and Confluence.

---

## Enhancements

## Dark mode

Enhanced dark mode compatibility to support the dark mode option in Confluence panels and the Confluence macro configuration view.

---

## Bug fixes

The following bug fixes are included in this release summary:

- Dashboard Hub bar chart widgets now correctly render bar heights when time values use different units, ensuring that larger logged times (e.g., 1 week) are accurately represented as taller bars than smaller values (e.g., 3 or 7.5 hours).
- Dashboards can now be reliably filtered by issue key and summary fields, ensuring search results are returned correctly for all users.
- Fixed display issues across dark and light modes, including: improved text contrast when hovering over table rows in Custom Reports, correct dark theme styling for the City field and Delete button, and proper rendering of Getting Started in light mode.
- Connector apps now install successfully, with new entries correctly created in forgeInstallations after aligning lifecycle event handling between Forge lambda and remote endpoint implementations.
- License data is now retrieved using the correct Forge mechanism, ensuring reliable data initialization and eliminating errors.

---