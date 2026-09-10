# Tags and Expressions

Tags are special blocks that perform operations on sections of the template and Expressions are literal expressions similar to those in javascript.

The most commonly used tags and expressions are covered below, from the perspective of use within **JMWE**. You may also want to check the Nunjucks [Templating documentation](http://mozilla.github.io/nunjucks/templating.html) for other built-in [tags](http://mozilla.github.io/nunjucks/templating.html#tags) and [expressions](http://mozilla.github.io/nunjucks/templating.html#expressions).

## Tags

## set

The `set` tag creates or modifies a variable.

**For example:**

`{% set comments = issue.fields.comment.comments %}` sets the *comments* variable with all the comment objects of the issue.

## setContextVar

The `setContextVar` tag creates or modifies a *context variable*. Context variables are used to pass information between post-functions in a Sequence of post-functions, a Shared Action or a Scheduled Action. Context variables are available through the `context` global variable. For example, if you create a context variable `myVar` in the first post-function of the sequence:

```text
{% setContextVar myVar = "a value" %}
```

This variable will then be available to subsequent post-functions as:

```text
{{ context.myVar }}
```

## if

The `if` tag tests a condition.

**For example:**

```text
{% if issue.fields.issuetype.name == "Task"}
This is a task
{% endif %}
```

returns `This is a task` if and only if the issue type is "Task".

## for

The `for` tag iterates over an array of values or objects.

**For example:**

```text
{% set comments = issue.fields.comment.comments %}
{% for comment in comments %}
{{ comment.body }}
{% endfor %}
```

iterates over the *comments* variable and displays each comment body.

## include

The **include**tag pulls in other templates in place. It's useful when you need to share smaller chunks across several templates. An included template does not participate in the block structure of its including template; it has a totally separate inheritance tree and block namespace. In other words, an `include` is *not* a pre-processor that pulls the included template code into the including template before rendering; instead, it fires off a separate render of the included template, and the results of that render are included.

**Syntax:**

```text
{% include "Test" %}
```

where `Test` is the name of the shared Nunjucks template saved in the Admin page.

## import

The `import` tag loads a template and allows you to access its exported values. Macros and top-level assignments are exported from templates, allowing you to access them in your current template.

**Syntax:**

```text
{% import "Test" as Test1 %}
{{Test1.sum(2,3)}} {# Calling the macro sum #}
```

where `Test` is the name of the shared Nunjucks template saved in the Admin page. `sum` is the name of the macro.

**For example:**

A Mapping macro to set the Priority based on the impact on the issue.

**Shared Nunjucks template:**

Name of the template : `Mappings`

```text
{% macro priorityFromImpact(impact) %} 
    {%- if impact == "Company wide" %}
        Highest
    {% elseif impact == "More than one project" %}
        High
    {% elseif impact == "Single project" or impact == "Individual" %}
        Medium
    {% else %}
    	Low
    {% endif %}
{% endmacro -%}
```

Access the template in a post-function to set the Priority of the issue:

```text
{% import "Mappings" as Mappings %}
{{Mappings.priorityFromImpact(issue.fields.Impact)}}
```

## Whitespace control

The Nunjucks script outputs everything outside of variable and tag blocks verbatim, with all whitespace (spaces, tabs, newlines,...) as formatted in the script. For example, the following script:

```text
This issue is
{% if issue.fields.priority.name == "Blocker" %}
  urgent
{% else %}
  not urgent
{% endif %}
```

will result in the following output:

```text
This issue is
  not urgent
```

If you don't want the extra whitespace between Nunjucks tags, then you can add the minus sign (`-`) to the start or end block to strip leading or trailing whitespace. For example:

```text
This issue is
{%- if issue.fields.priority.name == "Blocker" %}
 urgent
{%- else %}
 not urgent
{%- endif %}
```

will result in the following output:

```text
This issue is not urgent
```

See the [Nunjucks documentation](https://mozilla.github.io/nunjucks/templating.html#whitespace-control) for more details.

**JMWE for Jira Cloud** already automatically removes some spaces and carriage returns surrounding template result values in most post-functions. However, it is highly recommended to test the output of any Nunjucks template before releasing to Production.

## Expressions

## Mathematical expressions

Nunjucks allows you to do simple calculations on numbers.

**For example:**

`{{ issue.fields.Field1 + issue.fields.Field2 }}` outputs the sum of two custom field values, where `Field1` and `Field2` are the custom field names.

`{{ OriginalEstimate*2 }}` doubles the original estimate of the issue.

## Comparisons

Nunjucks allows you to compare two values or objects.

**For example:**

`{{ issue.fields.issuetype.name == "Task" }}` compares the value of the variable to the static value.

## If

Nunjucks allows you to use if as an inline expression.

**For example:**

`{{ "true" if var else "false" }}` outputs the string "true" if the variable *var* is defined, else it outputs "false".