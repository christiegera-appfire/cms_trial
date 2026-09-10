# Upload a snapshot

### When to upload a snapshot

You can upload snapshots to Configuration Manager for Jira (CMJ) Cloud when they’ve been created in another Jira Data Center instance. This lets you move configurations across environments and reuse them in your current Jira Cloud site.

Uploaded snapshots behave like locally created ones: you can view their summary, delete them, or deploy them to another Cloud site. However, you cannot create new versions for them, since their scope is adjusted from a Jira Data Center instance. Additionally, the uploaded snapshots cannot contain any issues or issue data.

---

### Upload a snapshot

1. In your Jira Cloud site, go to **Apps > Configuration Manager > Snapshots**.
2. Select **Upload**.

   ![Upload-snapshot.png](/cms_trial/assets/1180f289-de60-4189-abf0-c1277705ad7d.png)
3. Browse and select the exported snapshot file from your system.
4. The file will begin uploading.
5. The snapshot will enter a PROcessing state, which could take up to several minutes.

   ![Screenshot 2025-11-07 at 11.54.44.png](/cms_trial/assets/115df684-a456-4b2f-90e7-c3619c0dd33f.png)
6. After the snapshot is completely processed, the status will switch to Done and all of its metadata will be available in the snapshot summary screen.

The snapshot will be added to your **Snapshots list**. Additionally, snapshots from the same Jira Data Center instance will be automatically grouped in the same scope.

---