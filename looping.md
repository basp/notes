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

Another thing to consider is how it will be compiled. Some compilers 
might create one set of instructions and/or the VM you're running in
and its capabilities. In the end you should always try to use those
data structures that make sense for your algorithm. And then let those
structures lead you in the decision on *how* to use them well in 
accordance with their various strengths and weaknesses. 