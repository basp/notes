# Enum considered harmful
Time and time again I have `enum` appear as a cludge. An old remnant and always
a cludgy *bottleneck* in the system. Even I find myself using it in tight situatinos
and I always wonder how to avoid it. In this memo we'll take a look at why the `enum` 
is considered harmful, what we can do to avoid it and when it serves our purpose
well.

# The basic problem
Ut often looks like this:

* There's a data table with (preseeded) values
* There's some definition in the code that maps the database record to some particular set of behavior
* Code inspects the `enum` and does a switch (why not) and follows some path off into *never never land*
in order to eventually `throw` a `NullReferenceException` (or even worse, the dreaded `AggregateException`)
or hopefully a result.
* There's usually other pieces of codes with similar `if` or `switch` statements in order to do other 
creative kinds of branching and see how far we can get involving as much different kinds of layers as we can.

One of my primary goals is to **decrease** the time spent in the debugger. I don't even want to think about 
all lthe hours we waste debugging stuff that takes ages to setup in the first place. It's not only draining 
on the commpany resources, it's also demotivating.