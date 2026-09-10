# Manage baseline permissions and version history

![Baseline settings](/cms_trial/assets/dacf713a-3d64-47c9-9795-ec137ebfca98.png)

## Baseline permissions

For more information, check [the Box security roles page](/cms_trial/space/SPM/1918668158/Box+security+roles/).

## Impact of baseline settings

Baseline settings apply to a single box.

Baseline settings cannot be customized per user.

## Version history

![Baseline permissions](/cms_trial/assets/a8924ad3-7713-4594-85e9-f04d872eb58a.png)

**Save to version history** saves the current set of baselines for all the tasks (each start and end date). A version also holds information on whether a task has a baseline. Upon saving a version, you can choose its name and color.

**Delete** - removes the current set of baselines, leaving all the tasks without a baseline.

**Version history** - here, you can check the list of saved versions and choose one of them to be displayed in the Gantt chart, along with the current baseline, for comparison. In the screenshot above, the “Baseline created 05/Mar/24-2” marked with red color is chosen. In the Gantt chart, you can see two versions of baselines: current and red. By choosing the “None” version, only the current baseline is displayed in the chart.

**New baseline** - creates a baseline for each task. Note that this option overwrites the current baselines:

**Version history** - here, you can check the saved baseline versions. The list is sorted by the add date, descending. By using one of the three icons in a version line, you can respectively:

- **Restore saved baseline** - restoring means that this version will be the current one. **Restoring overwrites the current version** - if you want to keep the current baseline, [save it](#) before restoring. Note that the restore process updates the baseline start and end dates for each task. This means that if a baseline is set to a task in the current version and not in the restore version, then the baseline for this task will be erased upon the restore.
- **Edit saved baseline** - you can change the baseline name and color.
- **Delete saved baseline** - removes a version from the list.