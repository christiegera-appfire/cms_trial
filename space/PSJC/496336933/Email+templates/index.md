# Email templates

Email templates represent one of the first features of this app. Its initial implementation only allowed for simple variables to be injected into the templates. They are now based SIL™ Template Language and therefore their usage got a lot easier than before.

To be short the email templates mechanism is preferred and recommended way of sending emails from SIL™ scripts. The [send Email()](/cms_trial/space/PSJC/433654656/sendEmail/) function packs powerful tools.

Email templates obey the same rules as those presented in the general [STL page above](/cms_trial/space/PSJC/496336897/SIL+Template+language/) and in the [previous chapter](/cms_trial/space/PSJC/496336977/Executing+the+templates+programmatically/) with some notable differences, introduced just to make your life easier.

Just to re-assure you, the email templates preserve the same behavior as stated before:

1. Variable resolution within the template remains the same; variables in the last context are injected in the upper context of the template execution
2. Context behavior is the same: if you are in the issue context, you are allowed to use any issue variable you want, such as key, assignee, reporter, dueDate, etc. Otherwise you will need to refer issue fields by using issue\_key.field notation (e.g. IMJ-321.key).

Make sure you read [sendEmail](/cms_trial/space/PSJC/433654656/sendEmail/)() function documentation to see how it is called, and notice that it has many overloads.

## Mail Templates Base Directory

Unlike usual templates, presented before, email templates got their own base directory, and you can [configure that directory here](/cms_trial/space/PSJC/490996015/Outgoing+Mail+configuration/). This is both for historical reasons and because we recognized the importance of organizing mail templates in our integration projects. Under this directory, you may organize language folders, that will be used to internationalize your email messages. This feature is controlled in the above configuration screen (**Mail language** on: **Receiver**). The default is set on **Sender** that simply uses the declared language of the sender user, whoever s/he may be.

It is important to remember that **mail templates are resolved in line to this special directory**. Let's see how this works with a little example.

Suppose you are asking for template named **template.tpl**and the language may be English, French or Romanian. To internationalize that mail message, you need to create a folder structure having sub-directories named either with **languageCode\_countryCode** or simply **languageCode**, where **languageCode** and **countryCode** are 2-letters ISO standards:

![Power Scripts for Jira Cloud email template editor interface](/cms_trial/assets/0c5b2684-3ac9-4108-9b2e-2640bc213eeb.png)

The resolution of the template 'template.tpl' for an English speaker coming from Great Britain will be picked up from **MAIL\_TEMPLATES\_BASE**/en\_GB/template.tpl, where MAIL\_TEMPLATES\_BASE is, in our case, KEPLER\_HOME/templates directory.

Exactly the same way the resolution for an US English speaker will be **MAIL\_TEMPLATES\_BASE**/en\_US/template.tpl. However, for a Canadian English speaker, the template used is **MAIL\_TEMPLATES\_BASE**/en/template.tpl (selected in the image above).

If we look at the French support, you will see that above we use the same template for all the French speakers, no matter what country they come from. And if we look at the Romanian support, we'll see that, because the internationalization directory ('ro') is missing, it will default to the **MAIL\_TEMPLATES\_BASE**/template.tpl.

### Advice

If you need to send the same mail in multiple languages, do not mix templates used with the [executeTemplate](/cms_trial/space/PSJC/435028509/executeTemplate/)() function with the [sendEmail](/cms_trial/space/PSJC/433654656/sendEmail/)() function. Keep them separate. Of course this is valid only if templates are different, if you use the same for both emails and something else, put them in the same place.

## Additional Injected Variables

In addition to the variables from the context, sendEmail function defines a few more variables,  injected into the topmost context, as strings in your template:

1. **recipient** - the recipient (s) - if there are more than 1 recipient, recipients are joined together with a comma between them
2. **sender** - the sender - but only if the sender is defined.

## Usage Examples

## Do you have cookies?

To exemplify the usage, let's write a workflow action (post function):

```text
string cookie = "We have cookies!";

sendEmail({"spam.receiver@kepler-rominfo.com"}, "Xmas", "basic_template.tpl");
```

And put a template into our base mail template directory, named **basic\_template.tpl**:

#### **basic\_template.tpl**

```text
Hello $recipient$,

This is a test template sent from $assignee$'s issue $key$. The summary  for this issue is: $summary$.

$assignee$ says that $cookie$
```

Variables from our script are exposed into the template (cookie seems unused, but it is not!). This template must run in an issue context, since it refers the pre-defined variables from the issue.

## Bruce Wayne

Let's try to categorize our customers on either Batman's side, the evil side or neutral side. If we create a customfield *customerId*, that is a numeric code provided by the user, the following postfunction will complete a variable (*custName*) with the company name. In production systems, I suppose, you may want to get that customer name from a database (see the [sql](/cms_trial/space/PSJC/434864654/sql/)() function). For this example, a bit of logic will allow us to distinguish between the Batman's owned corporation and ... eh, a phantom, evil, one:

```text
string custName = "";

if(customerId == 1) {
  custName = "Evil Corporation";
} else if(customerId == 2) {
    custName = "Wayne Enterprises";
}

sendEmail("mysender@kepler-rominfo.com", "torecipient1@kepler-rominfo.com", "ccrecipient@kepler.ro", "Your issue:" + key, "template.tpl");
```

Now, customerId is either the name of the customfield or an alias to it (recommended).

Let's write our template, this time a html email:

#### **template.tpl**

```text
<html>
<body>
Hello $reporter$ from $custName$, the sender $sender$ announces you that the assignee for issue $key$ is $assignee$ and that work has started
$!
//this is a simple script, not carrying too much meaning, but just used as an example.
for(number i = 0; i < 3; i++) {
    $
    <p>
        Hip!
    </p>
    $!
}
$
<p>
    Hooray!
</p>
</body>
</html>
```

Now, Hip! Hip! Hip! Hooray! will be put in your email (4 paragraphs). Use standard CSS to nicely format your html email messages.