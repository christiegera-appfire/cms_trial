# IP allowlist considerations for CMJ Cloud on Premium Jira Cloud

If your **Premium Jira Cloud** instance has the IP allowlist feature enabled, you may encounter issues when installing or using the Configuration Manager for Jira (CMJ) Cloud. This is because IP allowlist restrictions prevent connections from any source not specified as allowed, including CMJ Cloud’s servers.

### Symptoms

- CMJ Cloud installation fails.
- CMJ Cloud can’t be seen in the Atlassian Marketplace.
- CMJ Cloud actions fail to run.
- Connection errors related to network or authorization.

---

### Resolution

To resolve this, add CMJ Cloud’s IP addresses to your Jira Cloud allow list. You can follow Atlassian’s official guide here - [Specify IP addresses for product access](https://support.atlassian.com/security-and-access-policies/docs/specify-ip-addresses-for-product-access/#Add-an-allowlist).

#### Step-by-step guide:

1. In the **Atlassian Admin** panel, go to *Security → IP allowlisting*.
2. Click **Add IP range**.
3. Enter each CMJ Cloud IP address from the table below.
4. Save changes and retry using or installing CMJ Cloud.

---

### Required IP addresses

| **Region / Purpose** | **IP address** |
| --- | --- |
| CMJ Cloud App Server #1 | `52.205.121.251` |
| CMJ Cloud App Server #2 | `23.23.215.132` |