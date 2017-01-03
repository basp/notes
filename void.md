# void
I tend to dislike `void` methods. It's not that they are bad but they are just overused and nobody seems to think twice before making something void. It seems to be the **norm rather than the exception** and I hate that with a passion.

Void makes things hard to test, it offers **no** information at all when you read the method signature. It often implies *lazy* programming and even more often heavy imperative code (in situations where it doesn't have to be that way). It's a cludge and doesn't have any real meaning anymore in most legacy applications.

# why void is bad
Void is nothing. So basically when you declare your method `void` that is because it's **all side-effects** that it does. Now think about that. Wasn't there something about *side-effects* that we should all know by know? Mmm...

Oh yeah! They are **evil** in a really really really bad kind of way. They are the spawn of the devil and your goal, as a programmer, is to steer clear of side-effects whenever possible.

That doesn't mean you can't use side-effects, without them we would get nothing done but please for the love of all that is programming, don't use them *all over the place*. Keep your methods/functions pure and sweet and it will be a lot easier to reason about your code.

# commands and queries
In the Pascal family of languages there's a clear distinction between callable blocks of code that return nothing (void) and callable blocks of code that return something (anything except void). These are respectively called `procedure` and `function`. For most of my career I didn't like the distinction but I've come to appreciate it because you see the same concept all over and over and even still in modern software. Sometimes though, the difference is similar but complementary.

For example, in SQL Server you cannot perform data modification from within a `function` but you can happily do so from a stored `procedure`. This implies that functions are meant to calculate stuff and procedures are meant to mutate stuff.

> As a sidenode, if you wanna be really annoying you can insist that only `SELECT` statements are to be called *queries* while all the other commands are just that, *commands*.

And that leads us into a (not so modern) idea that is known as [CQRS](http://martinfowler.com/bliki/CQRS.html) which is the idea that there are in essence two interesting operations you can do within the context of a computer program: 

* You can either read and calculate (the `Q` for query)
* You can either write a result to some store (memory, disk, etc., the `C` for command)

**CQRS** implies that these two should be kept seperate as there's often different models for updating data v.s. just reading data and calculating with it. The Martin Fowler article which I linked to above is really anal about CQRS and I don't like to think of it as some kind of dogma. It's just an observation on how systems tend to work in general and of course, there are exceptions.

# closing
Personally, I find the distinction between *commands* (`procedure`) and *queries* (`function`) in code pretty useful because it often leads to systems that are easy to test and reason about. It's also why I tend to dislike `void` because it means that method/function is hard to test. It's not that bad when the body is relatively compact and makes use of a lot of pure'ish functions but when you're dealing with all void helpers as well things are not fun anymore.

Also `void` implies side-effects all over the place and side-effects suck. Use instances (objects) to carry (minimal) state and service references around and don't be scared if you end up with a lot of **private** static functions in your classes to perform all kinds of steps in whatever algorithm you're writing.