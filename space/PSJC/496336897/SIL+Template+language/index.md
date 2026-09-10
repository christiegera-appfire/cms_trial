# SIL Template language

The SIL Template Language allows you to quickly build large amounts of text, or HTML, using a template that can be populated using dynamic variables.

## Template Language

The template language need appeared in early versions of SIL™. Creating real mail templates was not very easy, and the SIL™ programmer had to resort to all kind of artificial constructs for that. Especially, repetitive constructs were hard to embed in the body of the mail, and they needed to be built in the script before inserting them into the mail, with all necessary escapes, making the process of sending that mail cluttered.

The first step in creating a real template language was done with the (unpublished) app SIL™ on-the-fly Reporter, at version 3.x. However, this initial development was aimed at that app only, and in version 4.x a substantial effort has been employed to put STL at the base of the apps, near SIL™ so it can be used from all the places and all apps.

That being said, STL (SIL Template Language) should not be confounded with C++ STL (Standard Template Library). They are different beasts.

## How It Works

The idea of the STL is simple:

1. Template is provided by the user. The user writes embedded code within it.
2. The code is translated into a fully executable SIL™ script, buffered in memory.
3. The SIL interpreter is called on the given script. The script is executed and the result is gathered in a special area, in memory.
4. The result is retrieved and used wherever is needed.

The technique is resembling the JSP (Java Server Pages) technique.

## Syntax

The syntax used is backward compatible with the previous versions of templates, so you can expand the use of STL immediately over your old templates.

| Token(s) | Explanation | STL Example |
| --- | --- | --- |
| **$!**expression**$** | Translates the expression into SIL exactly as it is | $!for (number i = 0; i<o; i++) $ |
| **$**output**$** | outputs the string expression in the result | $assignee$ |
| **\$** | the $ character ($ needs to be escaped now) | \$ |

An example is represented below:

#### **STL Example**

```text
<html>
<body>
Hello $reporter$ from $custName$, the sender $sender$ announces you that the assignee for issue $key$ is $assignee$ and that work has started
$!
//this is a simple script, not carrying too much meaning, but just used as an example.
for(number i = 0; i < 3; i++) {
    $
    <p>
        Hooray!
    </p>
    $!
}
$
</body>
</html> 
```

## How To Use Them

The scripting usage is simple. You can use STL to create template emails or directly in your programs you may call the [executeTemplate()](/cms_trial/space/PSJC/496336897/SIL+Template+language/) function to parse and execute a template.

These two use cases are represented below:

- [Email templates](/cms_trial/space/PSJC/496336933/Email+templates/)
- [Executing the templates programmatically](/cms_trial/space/PSJC/496336977/Executing+the+templates+programmatically/)

## How Do I Edit Templates ?

You can access your templates from the **SIL Manager** page, by selecting the Kepler Home tree view:

![Power Scripts for Jira Cloud SQL datasource configuration interface](/cms_trial/assets/ba49e214-4d0f-4caa-9ad2-aa3ee095cd6d.png)

As of now, the SIL Manager does not have proper support for checking the STL syntax. We're working on it, but it may take a while

In the backstage, SIL defines 3 internal functions:

- \_stl\_\_init()
- \_stl\_\_done()
- \_stl\_\_print()

The following template is translated to the following one:

#### **template text**

```text
start
$v$
$! 
if(v == 1) { 
$
inside-if
$!
}
$
end
```

#### **translated SIL unit**

```text
_stl__init();
_stl__print("start");
_stl__print(v);
if(v == 1) { 
  _stl__print("inside-if");
}
_stl__print("end");
return _stl__done();
```

The STL generator keeps track of the line numbers so it can report back errors in the template, and not in the translated SIL™ unit.

Execution appends the result of the print statements in a buffer kept as a local execution variable in the SIL context, so once the script has finished, the unnecessary is ready to be collected.

In fact, STL is pluggable and doesn't depend on these exact symbols. The generator can use different separators and different function names. However, the bridge between STL and SIL™ have defined them as stated above.

Don't create very large templates. We do not see the need right now for very large templates. If you need such templates, [let us know](https://apps.appf.re/PSJ/support).