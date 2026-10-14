# How to use regular expressions - Cloud

## Overview

A number of apps provide advanced features that require the use of [regular expressions](http://en.wikipedia.org/wiki/Regular_expression) for pattern matching. Generally, just a simple understanding of regular expressions and a few examples are enough to get by for most use cases. This page has **a few simple examples** to get started. Use the references for more advanced information. We recommend testing your regular expressions in one of the well-known regex testing sites such as [RegexPlanet](http://www.regexplanet.com/advanced/java/index.html) or [Regex101](https://regex101.com/).

### Regex for workflow conditions

For Jira workflow functions using regex expressions to condition whether the post function should continue processing, a **blank** pattern means that condition processing is not done and processing should continue.

### Key tips

- Dot or period (.) is a special regex character. If you really want to match on it, you need to escape it with a backslash: **\.**
- Don't be confused with generic pattern matching used for file systems for instance. On a file system, \*.png means all files ending with **.png**. That is an illegal regex expression. For regex you need: **.\*\.png**. Or to simplify: **.\*png** which will find all files ending in **png** (not necessarily ending in an extension of png).
- Regex is **case sensitive** by default. In most cases, use the case insensitive flag: **(?i)**. See one of the examples below.
- **Dotall** mode when you need to match across line breaks.

  - In dotall mode, the expression . matches any character, including a line terminator. By default this expression does not match line terminators. Dotall mode can also be enabled via the embedded flag expression **(?s)**. (The s is a mnemonic for "single-line" mode, which is what this is called in Perl.)

## Simple examples

| **Value** | **Regex** | **Matches** | **Demonstrates** |
| --- | --- | --- | --- |
| ABC | A.C | ✅ | . matches any single character |
| ABC | A.\* | ✅ | - indicates 0 or more characters |
| ABC | .\*C | ✅ |  |
| A.B | A\.B | ✅ | Escape special regex characters with backslash if necessary |
| ABC | AB\* | ❌ | Regex is NOT generic matching 🙂 |
| ABC | A.+ | ✅ | + indicates 1 or more |
| ABC | ABC.+ | ❌ |  |
| ABC | ABC.\* | ✅ |  |
| ABCD | ABC.\* | ✅ |  |
| ABC | [ABCD]\* | ✅ | [ ] indicates a class of characters |
| ABC | [ABZ] | ❌ |  |
| ABC8 | [A-Z0-9] | ✅ | - indicates a range of characters |
| ABC | [AB^C] | ❌ | ^ in a class means NOT the following character |
| ABC | DEF|ABC | ✅ | | indicates OR |
| image.png | .\*png|.\*jpg | ✅ |  |
| image.jpg | .\*png|.\*jpg | ✅ |  |
| image.JPG | .\*png|.\*jpg | ❌ | defaults to case sensitive matching |
| image.JPG | (?i).\*png|.\*jpg | ✅ | (?i) indicates case insensitive matching |
| ABAB | (AB)+ | ✅ | () indicates a grouping |
| ABCD | (AB)+ | ❌ |  |
| 112233 | \d+ | ✅ | \d for digits |
| A B | A\s\*B | ✅ | \s for whitespace |
| ABC | \S\* | ✅ | \S for non whitespace |
|  | \S+ | ❌ | Value must have at least 1 non whitespace character |
| A | \S+ | ✅ |  |
| XYZ,ABC,UVW | .\*\bABC\b.\* | ✅ | Word boundaries. Finding words in a comma or blank separated list [using word boundaries](http://www.regular-expressions.info/wordboundaries.html) |
| XYZ,ABCD,UVW | .\*\bABC\b.\* | ❌ |  |
| ABC | (?m)(^ABC$)|(^ABC,)|(,ABC,)|(,ABC$) | ✅ | Looking for text matches in a comma separated list by covering all cases: only, start, middle, and end. This uses the multi-line flag: (?m) |
| XYZ,ABC,UVW | (?m)(^ABC$)|(^ABC,)|(,ABC,)|(,ABC$) | ✅ |  |
| XYZ,ABC DEF,UVW | (?m)(^ABC$)|(^ABC,)|(,ABC,)|(,ABC$) | ❌ |  |

## Advanced examples

| **Value** | **Regex** | **Matches** | **Find** | **Demonstrates** |
| --- | --- | --- | --- | --- |
| example.txt | `^((?!\.png).)*$` | ❌ | ✅ | Find string **not** containing a word. In this example, files that do not have a **.png** extension |
| example.png | `^((?!\.png).)*$` | ❌ | ❌ | Find string **not** containing a word. In this example, files that do not have a **.png** extension |
| example.jpeg | `(?=^((?!\.png).)*$)(?=^((?!\.jpeg).)*$)` | ❌ | ❌ | Find string **not** containing a word. In this example, files that do not have a **.png** or **.jpeg** extension |
| collateral wholesale retail | `.*(?=.*\bretail\b.*)(?=.*\bcollateral\b.*).*` | ✅ |  | Match exact words anywhere in string. In this case a blank separated list of labels and we require both collateral and retail to be included before we want the match to be successful |
| wholesale retail | `.*(?=.*\bretail\b.*)(?=.*\bcollateral\b.*).*` | ❌ |  | Both are required for a match |
| merger acquisition | `.*\b(?:merger|acquisition)\b.*` | ✅ |  | Match string containing either word |

## References

- [RegexOne](http://regexone.com/) - interactive tutorials to learn how to construct regular expressions
- [Regexlib.com](http://regexlib.com/) - searchable collection of user-contributed regular expressions
- [RegexPlanet test site](http://www.regexplanet.com/advanced/java/index.html) - test your expressions quickly
- [Regex101 test site](https://regex101.com/) - understand a regex expression and test it
- [Wikipedia regular expressions](http://en.wikipedia.org/wiki/Regular_expression)
- [Regular expression reference](http://www.regular-expressions.info/reference.html)
- [Quick reference](http://docs.oracle.com/javase/6/docs/api/java/util/regex/Pattern.html#sum) - best once you have the concepts
- [Using word boundaries](http://www.regular-expressions.info/wordboundaries.html)
- [Regular expression to match string not containing a word?](http://stackoverflow.com/questions/406230/regular-expression-to-match-string-not-containing-a-word)