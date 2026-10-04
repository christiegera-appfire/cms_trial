# Decorator for Data Type Select

A new Data Type Select decorator - STYLED\_TEXT - can recognize an HTML-based code and visualize it accordingly.  
The user can now change the color of lozenges of selections to make information clear, similar to how Objectives can be color-coded on a Roadmap.

The available <span style=“…”>…</span> tags are:

```text
['background']: /^(#([0-9a-f]\{3})\{1,2})|([a-z]+)$/i
['border']: /^[0-9]+[a-z]+ [a-z]+ (#([0-9a-f]\{3})\{1,2})|([a-z]+)$/i
['color']: /^(#([0-9a-f]\{3})\{1,2})|([a-z]+)$/i
['font-weight']: /^[a-z]+$/
['padding']: /^([0-9]+[a-z]+\s)*[0-9]+[a-z]+$/
['display']: /^[a-z\-]+$/
['text-align']: /^[a-z]+$/
['min-width']: /^[0-9]+[a-z]+$/
['-moz-border-radius']: /^[0-9]+[a-z]+$/
['-webkit-border-radius']: /^[0-9]+[a-z]+$/
```

*Examples:*

```text
<span style="background: #ddfade; border: 2px solid #93c49f; color: black; font-weight: bold; padding: 4px 12px; -moz-border-radius:3px; -webkit-border-radius: 3px; display: inline-block; text-align:center; min-width:60px;">Green</span>

<span style="background: #ffd; border: 2px solid #f7df92; color: black; font-weight: bold; padding: 4px 12px; -moz-border-radius:3px; -webkit-border-radius: 3px; display: inline-block; text-align:center; min-width:60px;">Yellow</span>

<span style="background: #ffe7e7; border: 2px solid #df9898; color: black; font-weight: bold; padding: 4px 12px; -moz-border-radius:3px; -webkit-border-radius: 3px; display: inline-block; text-align:center; min-width:60px;">Red</span>
```

Using the Styled Text decorator:

1. Create a Custom Field of the 'Select list (single choice)' type
2. Add the HTML code as an option in your single select for the options to be displayed, then set the field in the scope to be "Styled text" as shown in the screenshot below:

![contentId-1918765422](/cms_trial/assets/74669d9a-41d7-49a5-985c-75392a872225.png)

For Text/Lozenge decorators, the field will display the code; once Styled Text is selected, it will display the chosen style.

Just as you would normally add options to your single-select list, you can add different entries using HTML code, so they display different colors.

Example of setup:

![contentId-1918765422](/cms_trial/assets/c714f124-6976-48e5-9c73-c3b7f45e48bb.png)

Thus, with three options (each containing a different HTML code), three different colors are displayed in BigPicture:

![contentId-1918765422](/cms_trial/assets/c4a04057-94c4-47af-8955-5e06a0224a0b.png)

For safety reasons, the new decorator ignores the remaining part of the code.