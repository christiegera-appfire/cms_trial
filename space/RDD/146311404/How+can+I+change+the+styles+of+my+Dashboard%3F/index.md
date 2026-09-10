# How can I change the styles of my Dashboard?

You can use CSS to change elements such as font style, size, or even more complex style changes. You can modify CSS in Jira and Confluence Data Center.

Jira: [How to hide elements in Jira using CSS or JavaScript](https://confluence.atlassian.com/jirakb/how-to-hide-elements-in-jira-using-css-or-javascript-958774526.html)

Confluence: [Styling Confluence with CSS | Confluence Data Center and Server](https://confluence.atlassian.com/doc/styling-confluence-with-css-166528400.html)

Customizing in cloud instances requires Themes from the Atlassian Marketplace.

## A browser plugin to customize my dashboards

A browser plugin can suit the needs of avid users who prefer customized options to refine every detail.

### Stylebot for Chrome

[Stylebot is a plugin for Chrome](https://chrome.google.com/webstore/detail/stylebot/oiaejidbmkiecgbjeifoejpgmdaleoha?hl=en) that lets you configure web elements: font, color, margins, visibility, custom CSS, and more.

![Dashboard Hub dashboard style settings page](/cms_trial/assets/3816c7f1-76c1-4e03-982d-b8e3860388ca.png)

In *Basic* mode, you can modify different elements without using CSS, but if you want to create advanced styles, select the *Code* option.

If you don’t know how to start, you can copy and paste the following examples and create your own style:

![Dashboard Hub dashboard style customization fields](/cms_trial/assets/983c19c0-d90b-4f27-8746-7c4cdf9e4874.png)

#### Example to edit the font of the first slide

```css
@import url(https://fonts.googleapis.com/css2?family=Fira+Code:ital,wght@0,100;0,300;0,400;0,500;0,700;0,900;1,100;1,300;1,400;1,500;1,700;1,900&display=swap);
body{
  font-style: cursive !important;
}
div.wallboard-slide.slide-number-0.active {
  font-family: Fira Code;
}
```

#### Example to edit the font for all slides

```text
@import url(https://fonts.googleapis.com/css2?family=Fira+Code:ital,wght@0,100;0,300;0,400;0,500;0,700;0,900;1,100;1,300;1,400;1,500;1,700;1,900&display=swap);

div.wallboard-slide.active {
  font-family: Fira Code;
}
```