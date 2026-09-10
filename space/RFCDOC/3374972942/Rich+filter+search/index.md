# Rich filter search

Watch this short video for an introduction to the search feature:

This document explains how the Rich filter search functionality works in Rich Filters for Jira Dashboards (Cloud). You can search for rich filters in:

- The search box on the *Rich filters* page.
- The *Rich filter* search when configuring gadgets.

## How search works

Rich filter search is based on filter names.

### Search is case-insensitive

Uppercase and lowercase letters are treated the same. For example, the following searches return the same results:

- `My Filter`
- `my filter`
- `MY FILTER`

### Multiple words are matched with “any”

When you enter multiple words, filters matching any of those words are returned. For example:

- `abc xyz` matches filters containing *abc* or *xyz*.

### Use `+` to require particular terms

Add `+` before a word to find filters containing that word. For example:

- `+abc +xyz` matches filters containing both *abc* and *xyz*. This is the best way to narrow down results when you have many filters.

- `+abc def xyz` matches filters containing *abc* and either def or *xyz*.

### Use quotes for exact phrases

Put text in double quotes to search for an exact phrase. For example:

- `"my important filter"` matches filters that contain those words in that exact order.

Exact phrase searches do not work reliably when the phrase contains special characters such as `-`, `/`, or `()`. These searches can fail even when the filter exists.

In this case, instead of searching for the exact phrase, search without quotes and with the `+` operator. Keep in mind that unquoted searches may return additional matching filters.

| Filter name | Recommended search |
| --- | --- |
| abc - def | `+abc +def` |
| my (filter) | `+my +filter` |
| test/filter | `+test +filter` |

## Search tips

- Start with simple keywords.
- Use `+` to narrow down results.
- Avoid special characters when searching.
- Use consistent filter naming conventions to make filters easier for everyone to find.

### What if I still can't find my filter?

Try:

- Using `+` before important search terms.

- Removing special characters from your search.

If the filter still doesn't appear, contact support.