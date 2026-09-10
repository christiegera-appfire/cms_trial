# Workload and holiday plans sync

## Workload and holiday plans synchronization

![image-20240122-084827.png](/cms_trial/assets/e14931bc-dba7-4e5b-8567-8f3d75ed5177.png)

The Workload Schemes which were imported from the Tempo plugin can be distinguished by:

- Tempo label,
- Tempo code.

Codes of these external Workload Plans were automatically generated to describe the external (Tempo's) WP's. These codes also have Tempo attached to their name, so you cannot mistake them for our native codes.

You might have also noticed that before the synchronization in BigPicture and in the Tempo plugin there were two workload patterns recorded under the same name: a Workload Plan and a Workload Scheme named „Full-time”, then after we proceeded with the synchronization of a Workload Scheme -  a new „Full-time” Workload Plan was generated. As a result, we have two Workload Plans named: „Full-time” of which one is native, and one is external. This decision was made to avoid unwanted mistakes and make our project safer. This is why we do not merge any objects and do NOT alter any data or information in any of your Workload records (even if they carry the same name).

The same rule applies to our Holiday Plans.

Synchronization performed on the Workload Plan page will ONLY perform full sync of Workload Plans / Schemes, leaving Holiday Plans and Resources untouched for further synchronization on pages dedicated to these records (modules).

### Plans updated using Tempo

One-way sync at request if provided by the app.

Will the plans in Tempo be synchronized to reflect BigPicture? The answer is: "No, they won’t”. And it is not an error - it is indeed a feature. A feature that intends to give a user as much control over a project as possible. For the External Workload/Holiday plans to be synchronized correctly after changes were implemented in Tempo Schemes, you will have to use the "Synchronize with Tempo” button. This sort of behavior may seem far from intuitive, though (as we’ve mentioned) it is intended to give you as much control over the data flow between both plugins as possible.

### Plans updated using BigPicture

What will happen if you modify the synchronized Workload/Holiday Plan in BigPicture? Plans will be overwritten and a "pen" icon will be added to the label.

### Delete plans

What will happen when we delete from Tempo Workload/Holiday Scheme synchronized with BigPicture? It depends if the object you deleted was ‚synchronized’ or "overwritten".

- If the object is marked as 'synchronized', then during the Synchronization with Tempo it will also be deleted from BigPicture.
- If the object is marked as 'overwritten' (which means you’ve implemented some changes from the perspective of BigPicture, which are only visible in BigPicture), then during the next synchronization with Tempo, it WILL NOT be deleted and will become a 'native’ object.

### Synchronization rules

The synchronization rules are summed up in the table below:

| **Type of Action Performed in Tempo** | **What will happen during Synchronization in BigPicture** |
| --- | --- |
| Adding Workload/Holiday Scheme | - Creation of a new - external Workload/HolidayPlan with the data stored in Tempo.   Warning: An external Workload/Holiday Plan will be generated even if a native W/H Plan is already in place in BigPicture (with the same name and/or the same daily workloads). |
| Modifying Workload/Holiday Scheme | - If corresponding Workload/Holiday Plan is synchronized, then all changes will be implemented. - If corresponding Workload/Holiday Plan is overwritten, then all changes will be ignored. |
| Deleting Workload/Holiday Scheme | - If corresponding Workload/Holiday Plan is synchronized, then the Workload/Holiday Plan will be deleted. - If corresponding Workload/Holiday Plan is overwritten, then the status of that W/H Plan will be set to ‚native’. |
| **Type of Action Performed in BigPicture** | **What will happen with the 'external’ Workload Plans (ones which were pulled from Tempo)?** |
| Adding native Workload/Holiday Plan | - Nothing will happen with the external Workload/Holiday Plan. The W/H Plan will just be added as a "native" one. |
| Adding external Workload/Holiday Plan | - Such an operation cannot be performed. In BigPicture only native Workload/holiday Plans can be added and the external ones are generated only through the synchronization with Tempo. |
| Modifying native Workload/Holiday Plan | - Nothing will happen with the external Workload/Holiday Plans. The W/H Plan will just be modified and stay in the native status. |
| Modifying external Workload/Holiday Plan | - If Workload/Holiday Plan is synchronized, then changes will be applied and W/H Plan will change its status to 'overwritten’. - If Workload/Holiday Plan is overwritten, then changes will be applied without a status change.   Warning: It is possible to switch the "overwritten" Plan back to its 'synchronized’ state by clicking the 'Re-synchronize with Tempo’ button in the detailed view of that specific W/H plan. |
| Deleting native Workload/Holiday Plan | - Nothing will happen with the external Workload/Holiday Plans. The W/H Plan will just disappear. |
| Deleting external Workload/Holiday Plan |  |

#### Automatic synchronization

You can set automatic synchronization with Tempo and define items to synchronize.

1. Go to **BigPicture > App configuration > Integrations > Tempo**.
2. Enable the **Automatic Tempo Synchronization** toggle switch.
3. Check items to synchronize automatically.
4. Define synchronization time.
5. Click **Save**.

![image-20240131-115044.png](/cms_trial/assets/f21cddde-8d85-48b4-8e29-33d1eb463d64.png)