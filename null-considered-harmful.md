# On why `null` should be considered **harmful**
Why oh why do we as programmers so easily let `null` seep into our systems and deal with it like it's the most normal thing on earth.

> Just do this and this and then check for `null` 

It's totally unnecessary and as we will see also hazardous. When a `null` gets into your system it **will** turn up in the strangest of places. When you least expect it.

> Suprise surpise! The unexpected is the best prize!

# Business summary
If you use [Optional](https://github.com/nlkl/Optional) by **Nils Lück** (what a fabulous name by the way) you could replace all potential `null` values with more sensible `Optional<T>` or `Optional<T,TEx>` values. I do realize however that the `Option` type is also contagious just as `null` and even though I feel it's a better (more explicit) solution (that keeps good stack traces as well in case things go wrong) it should be applied with care and small does. 

Once you are in `Option` land it's not that easy to get out of it.

It's a better solution than `null` but the best solution is not dealing with `null` at all.

# The rage agains `null`
So **just say no** to `null` now because you don't need it. It's an evil value that represents nothing. It holds even less information than a **bit** and you can't get much lower than that. It's ambiguous most of the time for what exactly it means unless you carefully document it. 

And when you carefully have to document your code you probably should consider making your code more clear and less ambiuous instead. Let's not forget: the **code is the blueprint** and we can make beautiful diagrams for all we want but if only we would utilize the tools that are already builtin to our fancy programming languages we wouldn't need to document things on that level. 

Of course we would still need to document thing but those could really cut to the chase instead of dwindlingn on what a particular value of `null` represents in what scenario.

# How to make it explicit
First consider if you really want to deal with `null` in the first place. Ask yourself:

> WTF would I deal with `null` (I almost typed `dull` there) when I'm trying to create value for customers?

Dealing with `null` to me is like dealing with the processor clock cycle. As a business programmer you usually don't worry about those things because you have more important stuff to worry about.

In order to more clearly examine how to deal with `null` instead of dealing with `null` we need to look at when it crops up.

If you really need to handle `null` because of some kind of API you have to deal with then you should consider replacing them with either an `Option` or (maybe better) a `NullValue` implemenation if you're dealing with a lot of behaviour. This is similar to using `Nullable` which at least makes it explicit but doesn't offer much safety and is also not ideomatic when you're already dealing with reference types.

### As an unknown value
Something you have this method and it's in the family of *mapping* methods and you give it a thing and it returns some other thing (it might have side-effects as well and in that case shame on you but I'll talk about that in a future story about **CQRS**).

You might be tempted to return `null` in case the user gives you something that your method doesn't understand. **Don't do it.**

Usually the best option is to just let your method crash according to the rules of the runtime (.NET in our case mostly). This is in spirit of: **crash early** and **crash hard**. 

This doesn't mean you should leak exceptions to your end users though - for production you always should have some kind of general *catch-all* that logs the exception for support and presents the end-user with a generic error screen.

It *does* mean that you should never program defensively or let ambiuous values such as `null` slide along in your code. Unless you have a really good plan of dealing with them and not present the client of your code with the burden of figuring out what the heck that `null` means when it finally pops up in his or her code.

### As an error value
So something went wrong and you return `null`?

If you are an endpoint this might be perfectly acceptable but if you're doing this anywhere else in your code you're spreading evil.

### As a "not found" value
So you ask a respository for a thing with an explicit id and the respoitory returns `null`. Great, now you think: "yay, I can finally dig into that super interesting repository code to see where that `null` originates".

If I would just get the `KeyNotFoundException` or whatever thing goes wrong in some form I instandly would know that my input was shit. But since the *service* (from my persective as a client) is giving me `null` values I don't even trust the service anymore so that means digging into the code (not good).

Of course lots of people will say: "but you can reasonly expect `null` will mean not found" and trust me I do. Sadly I also find `null` meaning a lot of other things:

* Not found
* Some error occurred but we just gave you `null` instead just because
* Unavailable
* True
* False
* FileNotFound

And a whole host of other things that can only be gleaned from context. And granted, those last three are a reference to [What is Truth (TDWTF)](http://thedailywtf.com/articles/What_Is_Truth_0x3f_).

### As an error value
The value `null` is not an error value. As said before - `null` holds even less meaning than a bit and it's ambiguous as well. So don't use it as an error value. Either implement an error value, use `Optional` or just use the C# built in mechanims and give your client the joy of dealing with the actual `Exception` instance instead of some wrapped up or worse `null` object.

Again - at the final boundary between your application and user there should definitely be a catch-all that prevents any sensitive exception information from leaking into user land.

# Summary
* Don't deal with `null` unless you absolutely have to and have a great and more valuable alternative to "just let it blow up".
* Just letting it "blow up" is often the right choice, especially if you're not facing user land.
* Be aware of who is giving what arguments
* If your arguments are from user land then yes, check and double check them.
* If your arguments come from other code then you don't have to check nor doulbe-check them. Code users often just prefer just the `Exception` and will probably have a plan to deal with it. Please don't give them `null` and provide them with a dilemma or a difficult means to get to 
the actual problem.
* The last point is mainly if you're writing code that is not on the "outside" facing user land.

Just say no guys, you can do it. Dont "safe" cast unless you have an explicit way for dealing with that `null` (in an `Equals` override for example). To me *safe casting* is actually very unsafe because it offers a real danger for `null` values getting into your system and popping up in distant other places of the system. If we all **just say no** and let it blow and have catch-all handlers facing user land I think we should be golden.

I might be missing something though.

**Much <3**