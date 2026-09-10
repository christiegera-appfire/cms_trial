# Search issues by version

## With Jira advanced search

You can use Jira’s advanced search to find issues by fixVersion:

`fixVersion=v2.2`

or to search more than one version:

`fixVersion in (v2.2, v2.4)`

You can also find issues matching a range of versions. For example, if there are versions v1.0, v2.0, v2.1, v2.2, v3.0 and you want to see all v2 versions:

`fixVersion>=v2.0 and fixversion <=v2.2`

The order of versions is controlled by how they are arranged in your project’s versions configuration, not by the version number. To change the order, go to your **Project Settings** > **Versions** and reorder the versions by drag-and-drop.

## Wildcard searching and regular expressions

Searching using the version order can be limiting because you must use an existing version to set the range. You may also want to find issues with versions that contain a particular text in the version name. You can perform both of these advanced version searches with **JQL Search Extensions for Jira** [Text functions](https://appfire.atlassian.net/wiki/x/74IDJ).

**To search by wildcard:**

1. Go to **Apps** > **Extended Search** to open the [*Extended Search*](/cms_trial/space/JQLSEARCH/604209464/Extended+Search/) page.
2. Enter `issue in wildcardMatch("fixVersion", "v2.0*")` to find all issues with versions starting with “v2.0”. You can put a wildcard anywhere in a search text.
3. Click **Search**.

**To search with regular expressions:**

For even more control, you can leverage regular expressions. The following query only matches versions between v.2.0 and v2.5 that are beta versions:

`issue in regex("fixVersion", "v2.[0-5]-beta")`

The documentation for [wildcardMatch](/cms_trial/space/JQLSEARCH/604209903/Text+matches/) and [regex](/cms_trial/space/JQLSEARCH/604209903/Text+matches/) provides more examples of how to use the functions in Extended Search.

## Interactive walkthrough

Follow the interactive demo to see how to use the functions in Extended Search.

*Interactive demo of the JQL queries described on this page.*