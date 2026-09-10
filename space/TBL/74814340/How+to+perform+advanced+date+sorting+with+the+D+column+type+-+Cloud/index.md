# How to perform advanced date sorting with the D column type - Cloud

## Overview

The default date handling (using the *Date in the browser date format (D)* column type) provides support for the browser default date format. But, this may not work properly for columns that have a date format that is different than the default format set for individual browsers. More advanced and automatic capabilities are possible, provided your administrator has provided an extension that supports this.

**For Confluence administrators**

Install the relevant date handling library to avail advanced data handling capabilities. Documentation and source for the library can be found at [JavaScript Toolbox](http://www.javascripttoolbox.com/lib/date/index.php). Install the *date.js* file on your Confluence server in ***<confluence-installation-directory>/confluence/includes/js*** directory. Note that the default date library is in English for date formats that include characters. It is possible to easily modify the date library for other languages before installing it on your server.

## Steps

If this support is available on your installation:

- Specify the *D* column type on the *Column types* parameter. This is automatically matched successfully with many popular standard date formats.
- Specify the *D* column type followed by a [valid date format](http://www.javascripttoolbox.com/lib/date/documentation.php) for more unique date formats.

If a date format contains a comma (,), it must be enclosed in double quotes, for example, *MM ","YYYY*.