# Post-functions seem to be running in no apparent order

## Problem

I have configured several JMWE post-functions on a single transition, in a specific order, but the post-functions seem to be running in a different order when I trigger the transition.

This can be a problem in certain cases. For example, if one post-function copies the "Affects Version/s" field from the parent issue of the subtask being transitioned, and then a second post-function copies the "Affects Version/s" field of that subtask to the "Fix Version/s" field, it will not work if the execution order of the two post-functions is reversed.

## Solution

Due to the way non-native post functions (those provided by add-ons) are implemented in JIRA Cloud, it is not possible to guarantee the order in which post functions will be executed. Therefore, if your workflow incorporates post-functions provided by the JMWE add-on, you should ensure that your workflows do not depend on post-functions being executed in a specific order.

## Workaround

To enforce a predictable execution order of a set of post-functions, you should put them inside a [Sequence of post-functions](/cms_trial/space/JMWEC/466322933/Sequence+of+Post-functions/) post-function or a [Shared Action](/cms_trial/space/JMWEC/466288975/Shared+actions/).

Alternatively, you can use the [Delayed execution](/cms_trial/space/JMWEC/466322009/Delayed+execution/) option provided in the post-function configuration to delay the execution of the post-function by a selected number of seconds, thereby creating a more predictable execution order. But this approach is much less reliable than using a [Sequence of post-functions](/cms_trial/space/JMWEC/466322933/Sequence+of+Post-functions/) post-function.

## Related articles

|  |  |
| --- | --- |
| Related issues |  |