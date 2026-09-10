# Authorization and Token Questions

## Question - Provided Token is not working with current account

I am being asked to authorize 7pace Timetracker, but when I try, I get the error: "Provided token is not working with current account". How do I fix this?

![FAQ_Auth_Provided_Token.png](/cms_trial/assets/fbfcdc34-10c6-4143-a3d5-6f4e4defa934.png)

### Answer - Make sure the correct A settings are selected

If you use Azure Active Directory in your company, the wrong directory can cause an issue that results in you seeing the "Provided token is not working with the current account" error message. Please make sure that the correct AD settings have been selected.

To do so, please follow the steps below:  
  
1. Go to the "My Profile" section from any DevOps page (top right corner) using the account that is affected by the issue (<https://aex.dev.azure.com/me>).  
2. Check what AD options you have selected and choose the proper directory / your company-specific domain:

![FAQ_Auth_Provided_Token_AD_Options.png](/cms_trial/assets/eff548e1-0899-4635-a64e-55e8aa685a1f.png)

3. Try to authorize again.

If you don't use Active Directory, please try logging out and logging back in (checking to ensure that your Microsoft account is selected) and then try authorizing again.

4. If the above steps don't work, please open the "My Profile" section again and select "Microsoft account".

5. Click "Authorizations" at the bottom left of the page.

6. "Revoke" anything related to your 7pace or Timetracker authorization.

![FAQ_Auth_Provided_Token_My_Profile.png](/cms_trial/assets/398f7cb5-bedf-4ea2-8947-7840751fc1af.png)

 7. Now switch to your Active Directory account and "Revoke" authorizations for the Active Directory account as well.

If you don't have a dropdown that allows options to switch between AD and Microsoft account, then just revoke authorizations for the account that is chosen.

8. Navigate to 7pace Timetracker's "Monthly" page and refresh the page.

9. Click "Authorize".

Authorization should resume from the beginning and will display the extension permissions request. Authorization should successfully complete by clicking "Accept".

![FAQ_Auth_Provided_Token_Auth_Success.png](/cms_trial/assets/f157b7ec-0c2d-4345-a8a3-57b9ae428a36.png)

## Question - Why am I asked to authorize on every page?

I'm the administrator of my account, but Timetracker keeps asking for authorization when I navigate to each page. When I click "Authorize", it says authorization was successful. However, when I refresh the page or try to pair the Windows Client, I get asked to authorize again or the following error displays on the Client: " System.InvalidOperationException: ExecuteAction failed An error occurred. Open web interface, refresh the page, and click "Authorize". [TT:0x00000001]".

Can you help me resolve this issue?

### Answer - Check third party application access via OAuth

Please check your settings here [https://dev.azure.com/{account}/\_settings/policy](https://dev.azure.com/ukpr/_settings/policy) and ensure that "Third-party application access via OAuth" is enabled/"on":

![FAQ_Auth_Provided_Token_Third_Party_App_Access.png](/cms_trial/assets/68d588d6-a4c5-4a61-942b-5a2229c5af97.png)

## Question - OAuth vs. PAT authorization (Cloud only)

What is the difference between authorizing using OAuth or using Personal Access Token (PAT)? (cloud only)

### Answer - Description of each authorization option

[OAuth](https://appfire.atlassian.net/wiki/spaces/7TFA/pages/1253540465) may be a more seamless, short-term method in that the token refreshes itself automatically and frequently. The only potential drawback may occur if something goes wrong during the refresh tokens process, which will render your token unusable and will require you to issue it again. With the [Personal Access Token](/cms_trial/space/7TFA/1253540459/Use+a+Personal+Access+Token+to+authorize+7pace+Timetracker+for+ADO+Cloud/) method of authorization, you have to manually reissue the token, but it remains valid for a period of up to one (1) year.

For more information, see the authorization section [here](/cms_trial/space/7TFA/1253540271/Get+started+with+7pace+Timetracker+for+Azure+DevOps/).

## Question - I used Entra ID to authorize 7pace and receive consent requests for each user

With Entra ID authorization, admin consent requests are required by default for each user.

### Answer - Grant tenant-wide admin consent for 7pace Timetracker

To avoid having admin consent requests for each 7pace Timetracker user, [grant tenant-wide admin consent](https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/grant-admin-consent?pivots=portal) for 7pace Timetracker.