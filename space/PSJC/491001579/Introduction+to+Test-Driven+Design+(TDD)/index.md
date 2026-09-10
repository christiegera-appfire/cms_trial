# Introduction to Test-Driven Design (TDD)

What is the most effective approach to developing scripts and code maintenance? Well, with Test-Driven Design, of course!

## Background

With Test-Driven Design (TDD), you can write code in an efficient, easy-to-use approach to script development. TDD is not just a method or tool you grab out of the toolbox, but a way of thinking. Let's get started!

## Make a Short, Detailed List of Engineering Tasks to Be Performed

The goal of TDD is to create a small task each step of the way and create a test for each step.

## Red, Green, Refactor

This is a basic mantra of TDD and you will learn to say this in your sleep! The idea here is to create a small, falsifiable test which returns negative (on purpose). Creating a falsifiable test is an important step to avoid false negatives. If you would like a bit more background into the idea of falsifiability, check out this [wikipedia post](https://en.wikipedia.org/wiki/Falsifiability). In it, you will read all about Karl Popper and why falsifiable tests are so important in science.

To complete the "red bar" test, write a piece of code we know that will return a failure of our test.

Next, create a piece of code that makes the test pass (green bar).

Lastly, refactor your code so that it reads better. This is perhaps the most important part of TDD is that we can create code that is designed to refactor.

## Example

If you have not already done so, please read this introduction to silUnit. For our first test case, create a function sayHello() which simply returns the string "hello".

## Running a Suite of Tests

Running al tests in a directory is easy to set up. Just set the directory you want to test by setting it in the "testDirectory" folder.

|  |
| --- |
| ```text include "Includes/_silUnit.incl";    string testDirectory = silEnv("sil.home")+"/Tests"; suiteResults result = executeSuite(testDirectory); return toJson(result); ``` |

## Step 1 - Create a Basic Test

Our function below is fairly simple. We create a function, itSaysHello(), and place the "/\*\* TEST \*\*/" annotation above so that the silUnit recognizes it as a test.

|  |
| --- |
| ```text include "Includes/_silUnit.incl"; include "hello.sil";     /** TEST **/ function itSaysHello() {     assertEquals(sayHello(), "hello"); } ``` |

## Step 2 - Create a Function Which Causes the Test to Fail

Returning "not hello" would definitely not be saying hello!

|  |
| --- |
| ```text function sayHello() {     return "not hello"; } ``` |

## Success! We have a failing test!

When we run our first test, we get a failing result. This is exactly what we were aiming for!

|  |
| --- |
| ```text Result File: _silUnitResults/Tests.xml  -- Test Files: 1 Tests/sayHello.test.sil ---> Tests: 1 (P: 0 - F: 1)   Done. Program returned: {"name":"Total","total":1,"passes":0,"failures":1,"resultXML":"_silUnitResults/Tests_sayHello.test.silResults.xml"} ``` |

When we look at "Tests.xml", we see the following:

|  |
| --- |
| ```text <testsuites> <testsuite tests='1'>    <testcase classname='Tests/sayHello.test.sil' name='itSaysHello'>       <failure type='assertEquals'>'hello' does not equal the expected result 'not hello'</failure>    </testcase> </testsuite> </testsuites> ``` |

## Step 3 - Rewrite the Code in sayHello() Which Makes the Test Pass

Making this the test pass is easy. Simply return "hello" instead of "not hello":

|  |
| --- |
| ```text function sayHello() {     return "hello"; } ``` |

## Success! We have a passing test!

Now the results of our tests in the SIL Manager console look like the following:

|  |
| --- |
| ```text Result File: _silUnitResults/Tests.xml  -- Test Files: 1 Tests/sayHello.test.sil ---> Tests: 1 (P: 0 - F: 1)   Done. Program returned: {"name":"Total","total":1,"passes":0,"failures":1,"resultXML":"_silUnitResults/Tests_sayHello.test.silResults.xml"} ``` |

Now the "Tests.xml" file looks like this:

|  |
| --- |
| ```text <testsuites> <testsuite tests='1'>    <testcase classname='Tests/sayHello.test.sil' name='itSaysHello'/> </testsuite> </testsuites> ``` |

## Additional Help

Need help implementing unit tests on your script? Talk to me directly to me by clicking on the bot on this page.