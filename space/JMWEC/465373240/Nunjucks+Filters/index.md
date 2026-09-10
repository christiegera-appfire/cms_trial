# Nunjucks Filters

Nunjucks filters are functions that can be applied to variables in a Nunjucks script; they can be used to format values, return values, and filter or find values within variables. Filters are called with a pipe operator (|) and can take arguments.

This page details some of the Nunjucks filters included with **Jira Miscellaneous Workflow Extension (JMWE)**. These custom filters are specific to JMWE and extend the native Nunjucks filters; anywhere you can use Nunjucks in JMWE supports all native Nunjucks filters. More information on native filters can be found [**here**](http://mozilla.github.io/nunjucks/templating.html#builtin-filters).

## currency

The **currency**filter formats a number as a monetary amount. It takes the optional, *symbol*parameter, whose default value is `$.`

**For example:**

`{{ 100 | currency }}` returns `$100`

`{{ 3000 | currency("€") }}` returns `€3000`

## dump

The `dump` filter dumps an object as a JSON string into the template.

**For example:**

`{{ issue.fields.reporter | dump(2) }}` dumps the Reporter user object in "pretty" JSON format, using 2 spaces as indentation.

`{{ issue.fields.fixVersions | dump }}` dumps the array of Fix Version/s of the issue in un-prettyfied JSON format.

## filter

Filters an array, searching for either a value (e.g., string) or an object based on the value of a field. It supports using regular expressions to filter.

**For example:**

`{{ issue.fields.fixVersions | filter({name: “3.0”}) }}` returns the object representing version 3.0

## find(criteria)

Finds the first element of an array matching the condition, searching for either a value (e.g. string) or an object based on the value of a field. This supports using regular expressions to find.

**For example:**

`{{ issue.fields.labels | find(“test”) }}` returns `test` if the issue’s labels field contains the test label. Otherwise it returns an empty string.

## find(path, value)

Finds the first element of an array of objects for which the value at the specified field path matches the `value` parameter. This supports using regular expressions to find.

**For example:**

`{{ issue.fields.comment.comments | find(“author.active”, true) | field(“body”) }}` returns the body text of the first comment made by an **active** user.

## first

The `first` filter gets the first value/object in the array.

**For example:**

`{{ issue.fields.fixVersions | first }}` returns the first Fix Version/s object of the issue.

`{{ issue.fields.labels | first }}` returns the first label of the issue.

## join

The `join` filter returns a string which is a concatenation of strings.

**For example:**

`{{ issue.fields.fixVersions | join("," , "name") }}`joins the *names* of the Fix Version/s, separated by commas. For example: `1,1.0,2.0`

## last

The `last` filter gets the last value/object in the array.

**For example:**

`{{ issue.fields.components | last }}` returns the last component object of the issue.

`{{ issue.fields.labels | last }}` returns the last label of the issue.

## percent

The **percent**filter formats a number as a percentage. It takes the optional, *decimals*parameter, whose default value is `0`.