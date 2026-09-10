# User transformations

## Apply transformations to users

You can apply transformations to users the same way you do to the rest of the configuration in the deployment. Basically, you can overwrite user details with the **Bulk transformations** button at the top right of the *Analyze* page in the deployment wizard. You can learn more about [customizing configuration mapping](/cms_trial/space/CMJC/759824434/Download+and+customize+the+configuration+mapping/) and the [mechanisms](/cms_trial/space/CMJC/759988316/Guidelines+to+customize+the+configuration+mapping/) to do it.

**What is mapping or configuration mapping?**

*Mapping* or *configuration mapping* is an extensive map formed during the analysis process. It holds information on how the configuration elements in the deployment scope will be moved to the cloud.

The elements will either be created as new ones or modified if there’s a match between the source and destination counterparts.

[Learn more about the transformations available in CMJ Cloud.](/cms_trial/space/CMJC/759595150/Transformations/)

### User transformation use cases

You can use the **Bulk transformations** option to:

- Correct user problems  
  The *Customize mapping* feature allows you to correct user problems, such as missing and invalid email addresses, when mapping users during a server-to-cloud deployment. You can also *remap server* and *cloud users* this way.
- Merge user accounts  
  You can also use the transformations to map multiple source users to a single Jira Cloud account. To achieve it, you need to change the email addresses of multiple Jira Server/Data Center user accounts to be the same. This way, the CMJ Cloud will map all of them to a single Jira Cloud account.
- Map to a chosen destination user  
  You can also apply a transformation to map a source user to a destination user of your choice. To do so, you just need to provide the destination user’s ID.

## How to apply transformations to users

To address the use cases above, you just need to upload a file with the desired user transformations. For example, if an email address is missing, you’ll be able to prepare and apply a file with a corrected email for a particular user.

### Download and upload a file with user transformations

**To apply transformations to users:**

1. Start a [deployment](https://appfire.atlassian.net/wiki/spaces/CMJC/pages/193921424).
2. On the *Analyze*page, click the **Bulk transformations**button on the top right.
3. To resolve problems with unknown users or to change the default user information, click the **Download map**button at the top right. You will get a JSON file with the default mapping of all configuration elements in the deployment, including users.

   ![DownloadMapButton.png](/cms_trial/assets/f547d8af-9657-4276-8ea0-7f5602131d7a.png)
4. Modify the JSON file to correct missing or invalid email addresses. Also, to map several server users to a single Jira Cloud account, change their email addresses to match the email address of that Jira Cloud user. [Check the guidelines about customizing mapping](/cms_trial/space/CMJC/759988316/Guidelines+to+customize+the+configuration+mapping/).
5. Click **Bulk transformations**, upload the JSON file with the changes, and click **Confirm**.  
   The video below shows how to upload and apply transformations from a JSON file.

   ![UploadingJSON.mp4](/cms_trial/assets/eeae956d-9696-4ba5-9d9b-5410e38c8577.mp4)
6. After you finish updating the user mapping, click **Deploy** to continue the deployment.

After you click **Confirm** on the *Bulk transformations* window, the CMJ Cloud performs a new analysis of the deployed configuration and applies the transformations from the file.

## Guidelines for creating JSON user transformations

In the deployment wizard, you can download a file that contains all the information about the users and how they’ll be deployed to the cloud. Then, you can either make changes to that file to include your desired user transformations, or you can construct your own file and apply either of the files to the configuration.

The applied file must always be in JSON format. Also, there are some requirements on how to list the intended transformations in it. Check the [guide](/cms_trial/space/CMJC/759988316/Guidelines+to+customize+the+configuration+mapping/) we’ve prepared to quickly get you started on building your transformations.

With the **Bulk transformations** option in the deployment wizard, you can apply two types of transformations to users being deployed:

- Change email address
- Map to a destination user by ID

By changing the email address, you can create new users, merge multiple users into a single account, and remap source and destination users.

The important thing to note is that we refer to source users by their names. This means that you always need to provide the source user’s name in the JSON file in order to apply a transformation to it.

Let’s look at the examples below to make it clearer.

### Required JSON records to transform users

You can construct your own JSON file with user transformations and apply it to the configuration you’re deploying. The examples below show you the records you need to have in the file to change a user’s email address or to map it to a destination user.

#### Required JSON records to change the user’s email address

The example below shows the specific records required to change a user’s email address.

```json
{
    "users": [
        {
            "source": {
                "id": "5ed730807d0c0f0ab20920b8",
            },
            "transformation": {
                "email": "validEmail@demo.com"
            }
        }
    ]
}
```

#### Required JSON records to map a source user to a destination user by ID

The example below shows the specific records required to map a source user to a destination user by ID.

```json
{
    "users": [
        {
            "source": {
                "id": "5ed730807d0c0f0ab20920b8",
            },
            "transformation": {
                "id": "5da444878f33800c416f30ed"
            }
        }
    ]
}
```

### Edit a user in a downloaded JSON file

You can apply the same transformations from above by [downloading and editing the current mapping](/cms_trial/space/CMJC/759824434/Download+and+customize+the+configuration+mapping/) file. This [guide](/cms_trial/space/CMJC/759988316/Guidelines+to+customize+the+configuration+mapping/) provides more details about editing or constructing a mapping file. The examples below show how the user records will look in the downloaded file and the additional `transformation` record you need to add.

#### Transformation to change the user’s email address

When you download a mapping file, the `source` and `destination` records for the user will look like the example below. You only need to add a `transformation` record with the new email address without changing the default `source` and `destination` user records. After applying the edited file, the user being deployed will have a new email address.

```json
{
    "users": [
        {
            "source": {
                "id": "5ed730807d0c0f0ab20920b8",
                "name": "usernameInvalidEmail",
                "email": "invalidEmail@demo"
            },
            "destination": {
                "newObject": true
            },
            "transformation": {
                "email": "validEmail@demo.com"
            }
        }
    ]
}
```

#### Transformation to map a source user to a destination user by ID

When you download a mapping file, the `source` and `destination` records for the user will look like the example below. You only need to add a `transformation` record with the destination user’s ID without changing the default `source` and `destination` user records. After applying the edited file, the source user will be mapped to that destination user.

```json
{
    "users": [
        {
            "source": {
                "id": "5ed730807d0c0f0ab20920b8",
                "name": "sourceUser",
                "email": "sourceUser@demo.com"
            },
            "destination": {
                "newObject": true
            },
            "transformation": {
                "id": "5da444878f33800c416f30ed"
            }
        }
    ]
}
```