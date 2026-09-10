# June 4, 2021 - Initial Release

## Initial Release in Private Beta Mode

This initial release contains the core functionality of the Cloud version of *Rich Filters for Jira Dashboards*. Future releases will add new features, with priority given to features already available in the latest Server & Data Center version.

Below is a high-level description of the functional coverage:

- Rich filter [configuration](/cms_trial/space/RFCDOC/783941673/Configure+Rich+Filters/), with support for:

  - [static filters](/cms_trial/space/RFCDOC/783941703/Configure+static+filters/)
  - [dynamic filters](/cms_trial/space/RFCDOC/783941707/Configure+dynamic+filters/) on issue fields that can take predefined values (e.g., status, priority, labels, user pickers, check-boxes, select lists, etc.)
  - [smart filters](/cms_trial/space/RFCDOC/783941713/Configure+smart+filters/) with labels and colors
  - [views](/cms_trial/space/RFCDOC/783941729/Configure+views/) based on Jira fields and smart filters
  - [rights and permissions](/cms_trial/space/RFCDOC/783941839/Rights+and+Permissions/)
- Interactive dashboards, with support for:

  - [controller](/cms_trial/space/RFCDOC/783941745/The+Rich+Filter+Controller+Gadget/) gadgets with custom quick filters layout and additional JQL query
  - [results](/cms_trial/space/RFCDOC/783941759/The+Rich+Filter+Results+Gadget/) gadgets with multiple views displayed as tabs
  - [simple counter](/cms_trial/space/RFCDOC/783941825/The+Rich+Filter+Simple+Counter+Gadget/) gadgets supporting Issue Count and aggregated numeric and time-tracking fields
  - [one-dimensional statistics](/cms_trial/space/RFCDOC/783941781/The+Rich+Filter+Statistics+Gadget/) gadgets supporting simultaneously multiple result columns based on Issue Count or numeric and time-tracking fields aggregated by issue fields
  - [two-dimensional statistics](/cms_trial/space/RFCDOC/783941803/The+Rich+Filter+Two+Dimensional+Statistics+Gadget/) gadgets with results based on Issue Count or numeric and time-tracking fields aggregated by two issue fields