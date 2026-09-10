# How to set object permissions in profiles for a Salesforce user?

To make sure a Salesforce user has access to all Salesforce objects, no matter which type of user license they are using, you have to set proper object permissions for their profile. In Salesforce, you can set a user to have the *Modify All* permission for all Salesforce objects by assigning the user a profile with the *Modify All* data permission enabled. One user can have multiple profiles.

**Before you start**

Make sure you have:

- Administrator rights in Salesforce - only administrators can set up the profile permissions.

## Steps

1. In Salesforce, in the upper right corner, click the **Settings** icon (▢) and select **Setup**.
2. In the **Quick Find** box, type `Profiles`.
3. Click **Profiles**.

   ![Profiles.png](/cms_trial/assets/8717e876-b0ce-477d-9822-cf766e4833e0.png)

   Select the profile assigned to the Salesforce user.
4. Click **Edit** for the profile.
5. In the *Standard Object Permissions* check the box for **Modify All** if you want users with this profile to have full access to all records of the selected object type, regardless of the sharing settings for the object.

   ![Modify All.png](/cms_trial/assets/e48f1d1d-d742-45d6-9d99-e1fc3cd555a6.png)

   The Modify All permission lets you:

   - Read, edit, and delete all records for the object
   - Transfer and share all records for the object
   - Administer records in an approval process
6. Click **Save**.

## References

- [Profiles in Salesforce](https://help.salesforce.com/s/articleView?id=platform.admin_userprofiles.htm&type=5)
- [Standard Profiles](https://help.salesforce.com/s/articleView?id=platform.standard_profiles.htm&type=5)
- [Edit Object Permissions in Profiles](https://help.salesforce.com/s/articleView?id=platform.perm_sets_object_perms_edit.htm&type=5)