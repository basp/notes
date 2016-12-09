# Constructor type inference
Or rather the lack thereof.

In C# when you have a generic type such as `Foo<T>` with a constructor such as 
`Foo(T value)` then the compiler will not infer the type of `T`. I don't want to 
dive into the technical details too much but in case you're interested, check 
out [this answer on SO](http://stackoverflow.com/questions/3570167/why-cant-the-c-sharp-constructor-infer-type) 
by C# language guru Eric Lippert.

This note is more about a neat little trick that you can use to *fix* this. First, 
let's take a look at the meat of the *problem*. Assume we have a few types with
reasonably long names such as `GenerateXmlRequest` and `GenerateXmlResponse`. Now
suppose we want to create a `Tuple<T1,T2>` with those types, the type will look 
like `Tuple<GenerateXmlRequest,GenerateXmlResponse>`. 

Now this is already getting a bit word wordy but there's simply no way around it. 
When we want to create an instance using the constructor it looks like this:

    var request = new GenerateXmlRequest(...);
    var response = new GenerateXmlResponse(...);
    var tuple = new Tuple<GenerateXmlRequest,GenerateXmlResponse>(request, response);

This is a bit unfortunate because it almost looks like it should be possible to infer
types of `T1` and `T2` but sadly, calling the constructor like this doesn't work:

    // NOTE: This doesn't work
    var request = new GenerateXmlRequest(...);
    var response = new GenerateXmlResponse(...);
    var tuple = new Tuple(request, response);

However, there's a cute work-around for this using a *factory method*. Let's say we
we have this `class` (note that `Tuple` is already in the BCL, this is just an example
and can be useful for almost any class with type parameters):

    class Tuple<T1,T2>
    {
        public Tuple(T1 item1, T2 item2) { ... } 

        ...
    }

We'll can define a non-generic class as well 

    class Tuple
    {
        public static Tuple<T1,T2> Create<T1,T2>(T1 item1, T2 item2)
        {
            return new Tuple<T1,T2>(item1, item2);
        } 
    }

And with this we can now instantiate `Tuple<T1,T2>` much more tightly because the type 
inference *does* kick in on methods:

    var request = new GenerateXmlRequest(...);
    var response = new GenerateXmlResponse(...);
    var tuple = Tuple.Create(request, response);

When working with generic types and long type names this might help making your code 
much more readable.