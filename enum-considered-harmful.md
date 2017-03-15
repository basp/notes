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

Another insight I want to create is that mutating state is bad. It's very easy to program but very hard to 
maintain. I think we could better spend our time by investing more time in developing and less time in the 
debugger.

Often I see good intentions but either no clue or too much confidence in order how to tackle stuff. Let's say
you have a long method

## An example
As of late I've been toying around with a particular system (at work, I won't name it). But in essense I really 
like playing with it. It has some pecularties. Let me describe the context.

This class is dynamically instantiated and the methods from the contract get called in some predefined order.
That's not too bad except that the documentation about this order is not easily accessible. I recommend checking
it in under (for example) a `doc` directory.

Once we get instantiated we get passed some stuff. That's all cool actuallly, the list of parameters is 
not too bad so we can work with this.

Now however the problems arrive. Because sadly each and every thing we get passed goes off into different 
directions in order to obtain the actual data it needs to fullfil its reqwuest. We have stuff that's going
via weirdly named stuff likk `dsSomethingFrotz` and `dmsOMethingFrotZWithWeridSepelling` and it's at first 
kinda hard to make sense of it all.

The trick however is to kill/break some class in the middle of the system and try to get your information
from it. That basically involes asking the system the question:

> Can you give me enough insight in what went wrong even if I know aht I did to break you?

I you can't even answer that question you should stop workking on a solution and first focus on a deeper
understanding on how to make the system fail in a sensible way.

That's basically the trick. Once you try to do something with the system and you think well that
seems *sensible* but the system doesn't comply. That's when you know you need to work on your usuability.

## Programmer friendly
Also, make sure it's programmer friendly. We want small bricks that don't abstract too much but *do* give
us **guidance** and **insight** in what we should do with them. Either via plain code and logical
thinking, documentation, intellisense or whatever. If you try to write things in such a way that you wont
readily need a debugger to verify it then things will be sweet (and testable probably as well).