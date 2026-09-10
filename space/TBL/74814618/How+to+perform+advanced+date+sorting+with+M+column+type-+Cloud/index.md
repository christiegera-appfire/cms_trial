# How to perform advanced date sorting with M column type- Cloud

## Overview

The recommended date format type to use for sorting dates is the *M* column type. The support for *M* type date sorting is built-in including multiple language support and does not require any additional server installation.

### How to know if the M column type is available in my Confluence instance

In the macro browser, search for the *Table Plus* macro and find the *Column types* parameter. If *M* is listed in the help text, then it is available for use. See [Column types](/cms_trial/space/TBL/74814225/Column+types+-+Cloud/) for more information.

### Acknowledgement

Advanced date sorting support with the *M* column type is provided using Javascript with the help of the [Moment.js](http://momentjs.com/) library (open source, MIT license). A summary of the relevant parts of the Moment.js documentation is repeated here.

## Automatic support

On specifying just the *M* column type, default date parsing recognizes a number of common date formats including those recognized by the browser specific Javascript implementation. However, there can be browser specific inconsistencies. The following **ISO-8601** formats are recognized consistently across browsers:

![Advanced Tables ISO 8601 column type formats for advanced date sorting](/cms_trial/assets/c78fbc0f-82dc-4dfb-9d25-20f2312e633e.jpg)

## User-specified formats

On specifying a format string following the *M* column type, a specific date format can be handled. Construct the date format string from the set of format tokens.

### Non-alphanumeric characters

Non-alphanumeric characters are ignored, so, for this example, both of the following are treated the same with the MM-DD-YYYY format:

- 12-25-1995
- 12/25/1995

Similarly, formats can be specified with or with non-alphanumeric separators. However, using separators helps with readability.

## Format tokens

See the [Moment.js documentation](http://momentjs.com/docs/) for further information.

| Token | Description |
| --- | --- |
| M, MM | Month Number (1 - 12) |
| MMM, MMMM | Month Name (In current language) |
| D, DD | Day of month |
| DDD, DDDD | Day of year |
| d, dd, ddd, dddd | Day of week  The input for these tokens is ignored, as there are 4-5 weeks in a month, and it would be impossible to get the day of the month based off the day of the week. |
| YY | 2 digit year (if greater than 68, returns 1900's; else, 2000's) |
| YYYY | 4 digit year |
| a, A | AM/PM |
| H, HH | 24 hour time |
| h, hh | 12 hour time (use in conjunction with a or A) |
| m, mm | Minutes |
| s, ss | Seconds |
| S | Deciseconds (1/10th of a second) |
| SS | Centiseconds (1/100th of a second) |
| SSS | Milliseconds (1/1000th of a second) |
| Z, ZZ | Timezone offset as `+07:00` or `+0700` |
| X | Unix timestamp |

## Language support (i18n)

When the date format contains any other language words, the appropriate language must be indicated. English (US) is the default if nothing is specified. The language is specified by following the *M* with (language indicator) prior to the format string.

### Examples

- **M(de)YYYY-MMM-DD**for a German date: *2013-Mrz-10*
- **M(fr)** for a French date: *Janv 10, 2013*

### Supported languages

Click the link, in the following list of languages supported by the Moment.js library, to get the details of the specific localization:

| Language indicator |
| --- |
| [ar-ma](https://github.com/moment/moment/blob/develop/locale/ar-ma.js) |
| [ar](https://github.com/moment/moment/blob/develop/locale/ar.js) |
| [bg](https://github.com/moment/moment/blob/develop/locale/bg.js) |
| [br](https://github.com/moment/moment/blob/develop/locale/br.js) |
| [ca](https://github.com/moment/moment/blob/develop/locale/ca.js) |
| [cs](https://github.com/moment/moment/blob/develop/locale/cs.js) |
| [cv](https://github.com/moment/moment/blob/develop/locale/cv.js) |
| [da](https://github.com/moment/moment/blob/develop/locale/da.js) |
| [de](https://github.com/moment/moment/blob/develop/locale/de.js) |
| [el](https://github.com/moment/moment/blob/develop/locale/el.js) |
| [en-ca](https://github.com/moment/moment/blob/develop/locale/en-ca.js) |
| [en-gb](https://github.com/moment/moment/blob/develop/locale/en-gb.js) |
| [eo](https://github.com/moment/moment/blob/develop/locale/eo.js) |
| [es](https://github.com/moment/moment/blob/develop/locale/es.js) |
| [et](https://github.com/moment/moment/blob/develop/locale/et.js) |
| [eu](https://github.com/moment/moment/blob/develop/locale/eu.js) |
| [fa](https://github.com/moment/moment/blob/develop/locale/fa.js) |
| [fi](https://github.com/moment/moment/blob/develop/locale/fi.js) |
| [fr-ca](https://github.com/moment/moment/blob/develop/locale/fr-ca.js) |
| [fr](https://github.com/moment/moment/blob/develop/locale/fr.js) |
| [gl](https://github.com/moment/moment/blob/develop/locale/gl.js) |
| [he](https://github.com/moment/moment/blob/develop/locale/he.js) |
| [hi](https://github.com/moment/moment/blob/develop/locale/hi.js) |
| [hu](https://github.com/moment/moment/blob/develop/locale/hu.js) |
| [id](https://github.com/moment/moment/blob/develop/locale/id.js) |
| [is](https://github.com/moment/moment/blob/develop/locale/is.js) |
| [it](https://github.com/moment/moment/blob/develop/locale/it.js) |
| [ja](https://github.com/moment/moment/blob/develop/locale/ja.js) |
| [ka](https://github.com/moment/moment/blob/develop/locale/ka.js) |
| [ko](https://github.com/moment/moment/blob/develop/locale/ko.js) |
| [lv](https://github.com/moment/moment/blob/develop/locale/lv.js) |
| [ms-my](https://github.com/moment/moment/blob/develop/locale/ms-my.js) |
| [nb](https://github.com/moment/moment/blob/develop/locale/nb.js) |
| [ne](https://github.com/moment/moment/blob/develop/locale/ne.js) |
| [nl](https://github.com/moment/moment/blob/develop/locale/nl.js) |
| [nn](https://github.com/moment/moment/blob/develop/locale/nn.js) |
| [pl](https://github.com/moment/moment/blob/develop/locale/pl.js) |
| [pt-br](https://github.com/moment/moment/blob/develop/locale/pt-br.js) |
| [pt](https://github.com/moment/moment/blob/develop/locale/pt.js) |
| [ro](https://github.com/moment/moment/blob/develop/locale/ro.js) |
| [ru](https://github.com/moment/moment/blob/develop/locale/ru.js) |
| [sk](https://github.com/moment/moment/blob/develop/locale/sk.js) |
| [sl](https://github.com/moment/moment/blob/develop/locale/sl.js) |
| [sq](https://github.com/moment/moment/blob/develop/locale/sq.js) |
| [sv](https://github.com/moment/moment/blob/develop/locale/sv.js) |
| [th](https://github.com/moment/moment/blob/develop/locale/th.js) |
| [tr](https://github.com/moment/moment/blob/develop/locale/tr.js) |
| [tzm-la](https://github.com/moment/moment/blob/develop/locale/tzm-la.js) |
| [tzm](https://github.com/moment/moment/blob/develop/locale/tzm.js) |
| [uk](https://github.com/moment/moment/blob/develop/locale/uk.js) |
| [zh-cn](https://github.com/moment/moment/blob/develop/locale/zh-cn.js) |
| [zh-tw](https://github.com/moment/moment/blob/develop/locale/zh-tw.js) |