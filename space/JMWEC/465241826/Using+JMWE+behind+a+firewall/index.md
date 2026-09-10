# Using JMWE behind a firewall

## JMWE Domain for allowlists

**JMWE for Jira Cloud** utilizes numerous APIs hosted on Heroku (and therefore on Amazon Web Services), which may be called by the user’s browser. When accessing JMWE from behind a firewall, it may be necessary to allowlist the JMWE server’s domain name:

## jmwe.appfire.app

## IP Addresses for API Calls

JMWE provides a Nunjucks filter - [callRest](/cms_trial/space/JMWEC/465242995/callRest/) - that enables calling external APIs to return data to a Nunjucks template. To enable accessing these external APIs from behind a firewall, the **callRest** filter runs through an Appfire proxy that has a set of static IP addresses.

You can download a JSON file containing the list of services and their IP addresses using the link below.

Download the JMWE IP address file here:

![contentId-465241826](/cms_trial/assets/c900cc62-739f-4f2e-9890-4838dc755678.json)