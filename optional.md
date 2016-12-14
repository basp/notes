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

