# Looping 101
> Is there a difference in speed between a `foreach` and a `for` loop?

It depends on the data structure that you're using. 

If you're not dealing with an `Array` then a basic `for` will probably 
be out anyway. I recommend writing your API around `IEnumerable<T>`
instead of `IList<T>`, `ICollection<T>` and `Array<T>`. Focus on the 
intent of your code first and on performance later. 

That said, there are definitely scenarios when it makes sense to use
`for` instead of `foreach` but in most scenarios I would not advice 
for it in typical business code.

## Example
Say, even if we're dealing an array of lines from a text file, like a 
`string[]` in C# for example. And that we have this function:

    static string[] SkipHeader(string[] lines)
    {

    }

Our task is to skip the first 3 lines because they apparently 
contain gibberish that we don't need. Yes I know, it already feels
hacky but due to time constraints you are forced to implement
this. Now there's all kinds of things horribly wrong with this API
and it could be so much better, but for the sake of writing a note
and not a book let's just say you are to implement this horrible 
hack.

Would you implement it like this?

    // I'm still being kind in this example (could be worse even)
    static string[] SkipHeader(string[] lines)
    {
        var body = new List<string>();
        var i = 0;
        while(i < lines.Length)
        {
            if(i > 2)
            {
                body.Add(lines[i]);
            }

            i += 1;
        }

        return body.ToArray();
    }

Is that *nice* code? And you might think well that you would never 
use a `while` statement here and indeed and in fact, you should never 
unless you're writing a *daemon* behavior. And don't mention `Tree` 
data structures because you should be using the **visitor** pattern and/or
pattern matching and recursion instead (the visitor pattern is basically imperative pattern matching on trees if you think about it).

Anyway, you could also write this:

    static string[] SkipHeader(string[] lines)
    {
        var body = new List<string>();
        for(var i = 2; i < lines.Length; i++)
        {
            body.Add(lines[i]);
        }

        return body.ToArray();
    }

This, to my eyes at least is a bit better. At least it shows the 
intend... Somewhat. It's still not great though.

> I've seen the same crazy stuff with people using reader classes 
> to do the same crazy shit. Usually a `while` loop is more
> approprate in those cases because it interfaces easily with 
> the `EOF` property on a few of the `StreamReader` classes and
> that is probably even more wrong. 
>
> Look, if you're streaming already using a `StreamReader` class 
> then it makes a whole  of sense to keep using `IEnumerable<T>` 
> and stream and transform throughout your whole process... 
> Just saying.

We're gonna probably use a `List<T>` in there anyway. A `List<string>` 
in this case. If you're gonna solve this by copying bytes and involving 
buffers you're probably doing it wrong.

Due to the interface (method signature) we're gonna have to `ToArray()` 
that list anyway. I would probably write something like this:

    static string[] SkipHeader(string[] lines)
    {
        return lines.Skip(3).ToArray();
    }

And if you wanna make the *hack* really neat you can also include a 
constant named something like `Header` or something like
that so it reads pretty nice:

    static string[] SkipHeader(string[] lines)
    {
        const int Header = 3;
        return lines.Skip(Header).ToArray();
    }

> You could include such a constant in the `for` example as 
> well and it wouldn't be *too* bad... I guess. Also the
> name `Header` is not very accurate but considering how tiny
> its scope is and how nicely it reads in the context of where
> its used (and how close that is to where its declared) I'm 
> inclined to like this one.
>
> Note that `Header` wouldn't really work in the `for` case 
> though and we would *have* to resort to something like
> `NumHeaderLines` or something like that. in the `Skip` case
> we at least have the option.

And although such a constant might seem like a simple thing, it's 
the first step to abstract such values out of your core logic. from
now it will be easy to add an extra (optional) parameter for it or
include it in the interface of something bigger.

Is the LINQ version slower? It will probably carry more overhead 
than just straight buffer copying the bytes yourself using `for`
loops yeah. But are you dealing with all the complexity of encoding?
Are you dealing with all the edge cases that the .NET BCL is taking
care of for you?

In the end though, intend should have a higher priority than
performance unless you have carefully profiled the hotspots and
identified solutions that actually improve the efficiency. It's a 
bad idea to use `for` because they *feel* faster. 

My advice is to get a good grasp of the class library (especially the collections) you're working with and make educated decisisions keeping readability and intent at highest priority. And never (prematurely) 
optimize before you profile.

# IEnumerable
> Why is `IEnumerable` and especially `IEnumerable<T>` so imporant? 

Because it's an extremely simple interface that allows for very 
powerfull logic. The `IEnumerable` is quite easy to implement and if
you fully realize the power of LINQ that is built **on top** of it 
you start to understand how powerful this thing really is. 

Bascially, when you use an `IEnumerable` you are leaving the realm 
of simple collections and enter the realm of lazy calculations. And
that is the **main difference** between for example `IList` and 
`IEnumerable`.

When you use an `IList` people who see that assume the value is 
already there or at least easily populated from memory. When you use
an `IEnumerable` you are actually signalling that the result is 
a *stream of values* where not every value may be available instantly.
And this is in fact exactly where the `yield` keyword comes into 
play (but more on that later).

Another thing that I like is the read-only aspect of `IEnumerable` in
that you can never ever add values to it. Of course you *can* easily 
create new `IEnumerable` instances by transforming your source but 
you can never ever add or remove instances from the source (though 
you're free to ignore them of course).

# Compilation
Another thing to consider is how it will be compiled. Some compilers 
might create one set of instructions and/or the VM you're running in
and its capabilities. In the end you should always try to use those
data structures that make sense for your algorithm. And then let those
structures lead you in the decision on *how* to use them well in 
accordance with their various strengths and weaknesses. 