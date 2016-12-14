# Optional
[Optional](https://github.com/nlkl/Optional) is an awesome library. I've been
trying to work with it during the last few days and I've grown to love it.

So what is `Optional` then? Well, it's a very robust and functional `option`
implementation for .NET aimed at users who have come to love the `option` type
from other functional languages like for example F# which has it baked in.
That's why it still surprises me to this day that C#, with all its functional
aspirations doesn't have a decent `option` type yet. And no, `Nullable` doesn't
even come close.

## Nullable
Let's take a look at `Nullable<T>` then. What does it do for us? Well, its 
main purpose is make a *value type* **kinda** optional by allowing us to 
**almost** treat it like a reference value.

Say we have this `int i`. It can never be `null`. If it, at some point would end up as `null` then something seriously is wrong with your .NET virtual machine state. 

> This is because it's a value type. Value types always reserve
> the memory they need upfront and are *copied* when they are passed 
> along but more on this in another post.

However it's fine to have an `object o` that is `null`. That's because it is
a *pointer* and not an actual value. It's fine to have a pointer point to 
nothing. And often it's desirable to do so as well. This is the power and
at the same time the strength of pointers (and also that you can do cleaver
arithmetic with them but that's not for this note).

> Sadly, *null pointers* appear more frequently than it should be and 
> leaves programmers scratching their heads and diving into the debugger
> to find out the root cause. And debugger time is unproductive and unfun.

Anyway back to `Nullable<T>`. It *wraps* a value so that it mimics something
else. By making it nullable we often kinda feel like we're making it optional
but that only makes matters worse. And this is where the similarities with a real `Optional` end. 

Instead of having a reasonably *safe* value type that at least forces some thought we can now just wrap it into a `Nullable<T>` and pass it along like nobody cares until it finally ends up in user-land where it (hopefully) results
in a server error for some programmer. In the worst case your user is looking
at the stack trace of a server process that died to something being `null`
somewhere down your processing pipeline.

> If at some point you think: "Wait! I need `Nullable<T>` then stop everything
> that you're doing and think again for at least 10 minutes. Repeat this
> simple process until you found a better way to do things.

## Option
So why is `Option` better? For one, you cannot easily get a value out of it.

For the same reasons that `IEnumerable` is so powerful, due to its simple interface and strict contract, `Option` is powerful as well. If only that it
**forcess** *clients* (callers) to deal with the result that your function 
is passing back.

### Example
Say we have this (useless and contrived) function:

    static string ReadFile(string path)
    {
        return File.ReadAllText(path);    
    }

Now clearly this will `throw` something when we supply an invalid argument
for the `path` parameter. Often, you *want* this and you especially during
development it's often not a bad idea to have errors bubble up straight in
your face. This will help identify errors and mistakes early while they 
still can be fixed easily.

However, you might wanna be a bit more defensive about it. Maybe it's not a 
bit problem if this particular `ReadFile` fails because you have a default
value anyway. 

Let's use `Option` instead then and see how it *restricts* and *empowers*
us at the same time:

    static Option<string> ReadFile(string path)
    {
        try
        {
            var text = File.ReadAllText(path);
            return Some(text);
        }
        catch
        {
            return None();
        }
    }

This is not too bad but we're missing something. Notably, the `Exception`
that was thrown. It's nice to have a `None` result but this is barely
better than *eating* the exception and returning `null` instead.

However, we can do much bette. Sadly, due to how C# type inference works
it does get a bit ugly with types. However, there's good way to work with 
it and make it less horrible. For now it's not too bad:

    static Option<string, Exception> ReadFile(string path)
    {
        try
        {
            var text = File.ReadAllText(path);
            return Some<string, Exception>(text);
        }
        catch
        {
            return None<string, Exception>(ex);
        }
    }
    
And yeah I know, the type annotations are horrible but we'll have to live
with them for now if we wanna be funky.

Let's see what happens when we call this method with an invalid path:

    var res = ReadFile(@"frotz");
    Console.WriteLine(res); // Option ???

How do we get a value out of this thing? Well that's the beauty. You have 
to consider what you wanna do with it. That value is something important.
It might be an `Option` but you'll have to deal with it. 

You could just ignore it but then you can't get to the value. It's a valid option in some cases.

If you wanna get to the file contents or the exception you have a few 
safe ways and a also unsafe ways. I'll deal mostly with the *safe* ways.

# Imperatively
Let's face it, when you actually wanna accomplish stuff you need to venture
into imperative land now and then. And since C# is somewhat imperative due
to its heritage we'll take a first look at `Option` from that side.

Let's say you're writing this imperative algorithm and someone hands you
an `Option<string,Exception>` and you don't really have the luxury of 
functionally returning. Something like this:

    static void Run()
    {
        // Do some stuff...

        // Invoke something that returns an option
        var opt = ReadFile(cfg.Path);

        // Need to use file contents here

        // Do more stuff most likely involving file contents
    }

Now in the middle of some imperative algorithm you get this functional
option value. How to deal with it? Well the easiest way is to use
the `HasValue` property.

    var opt = SomethingThatReturnsOption("frotz");
    if (!opt.HasValue)
    {
        // Handle error case, possibly return early (1)
    }

    // At this point we know for sure that opt has a value (2)

That still leaves us with the question on how to get to the value. The
safe and simplest way to do it is the `ValueOr` method:

    var value = opt.ValueOr("TILT");

This will get us the `string` value that is in the option or if the option 
is `None` then it will get us the `"TILT"` value. When combined with
`HasValue` this is reasonly safe and simple way to get values out of your options in imperative land. 

Note that this should be considered as a bit of a hack as this is not how `Option` values are intended to be used. It is (sadly) though a necessary pattern to know when dealing with the real world.