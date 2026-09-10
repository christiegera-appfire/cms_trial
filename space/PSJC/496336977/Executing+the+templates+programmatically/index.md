# Executing the templates programmatically

To execute a template, call the [executeTemplate()](/cms_trial/space/PSJC/435028509/executeTemplate/) function over any pre-defined file.

So, this sounds easy, right? Because it really is.

Please take a moment to examine the documentation of the function. The [executeTemplate](/cms_trial/space/PSJC/435028509/executeTemplate/)() function takes one mandatory parameter, the path to the template file, either absolute or relative in that case the file must reside in the Kepler Home directory on the server. The second parameter, optional, is the charset, in case you wrote the file with a different charset encoding. Let's discuss several examples.

## A Simple Example

#### **<KEPLER\_HOME>/templates/some.tpl**

```text
 $! if(isNotNull(baseVar)) { $
Well done, $baseVar$ !
$! } else { $
Nobody to congratulate ?!? Whoaaaa !!!
$! } $
```

The example above shows the **baseVar** variable is not defined in the template. However, it is referred in both the if code block and as an output variable. So where does it come from?

The answer is in the calling script:

```text
string baseVar = "Monster";

return executeTemplate("templates/some.tpl"); 
```

The **baseVar** variable is defined prior of the template execution call, and it is injected as a global variable (i.e. the uppermost context) in the resulting SIL™ script of the interpreted template. This means that you can exploit it like any normal variable and output it, and this is what we do there ($baseVar$).

The template tool ensures that all variables defined in contexts (read: blocks) are passed onto the template. Let's complicate a bit the example, and add the following to the script:

```text
string baseVar = "Monster";
number baseNo = 10; //+another variable gets defined
string ret;
for(number i = 0; i < 3; i++) { //+ iterate 3 times
  ret += executeTemplate("templates/some.tpl") + " "; //+ concatenate result
}
return ret, baseNo; //return also the baseNo
```

Let's modify the template to make use of those variables:

```text
$! if(isNotNull(baseVar)) { $
Well done, $baseVar$ $i$ ($baseNo$) !
$! } else { $
Nobody to congratulate ?!? Whoaaaa !!!
$! } $
$! baseNo++; $
```

The little surprise is that:

1. Everything runs smoothly, with no error 🙂.
2. Both i and baseNo variables are defined at runtime in the template, along with **baseVar.**
3. baseNo gets incremented, as expected. This is the only method of returning from templates, although this practice should be discouraged, because of the side-effects it may have.

The output of the above script is:

```text
Well done, Monster0 (10) ! Well done, Monster1 (11) ! Well done, Monster2 (12) !, 13
```

### Advice

Always document your templates, stating what variables it expects. STL does not offer code comments, but you can always add a code block with comments, like in the example below:

```text
$!
// This template does A and B
// It receives the following params:
// x, type string, representing X
// y, type number, representing Y
// z, output param, type string
$
..... rest of the template here ....
```

### Advice

 Always state the side effects! Try as much as possible not to modify the variables, even if the mechanism allows you to do that!

## Templates In The Issue Context

Templates in the issue context have the wonderful property of letting you access the issue variables like any other variable. This makes the template easily adaptable in your SIL™ scripts. Of course, they retain the above behaviour.

Let's examine this template:

```text
$!
// A simple issue template. Runs only in an issue context. 
// param: baseVar a string. If not null sets a customfield to a magic value.
$
$! if(isNotNull(baseVar)) { $
Well done, $baseVar$, the reporter of the issue $key$ is $reporter$
$!customfield_10000 = 2;$
$! } $
```

Let's create a workflow action (post function) on some transition in a workflow:

```text
string baseVar = "Monster";
description += "\n" + executeTemplate("templates/descript.tpl");
```

What you need to remember is that the custom fields and issue fields may be accessed in the template as you do in the script. Of course, this only applies if you are in an issue context, otherwise you will get an error in the logs and nothing is returned from that template execution call.

As you can easily imagine, the result of the transition execution of the issue will look like:

![Power Scripts for Jira Cloud template execution interface](/cms_trial/assets/a5464c6d-1c28-4f96-a395-4576455957a6.png)