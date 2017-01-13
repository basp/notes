# `const` everything
This is mostly about JavaScript and explicit about the modern forms that allow for the `const` keyword. This also includes *transpilers* such as **Babel**, **TypeScript** and friends.

If you come from more *old-school* languages you might see `const` as just something you should use for a boring `string` or `number` that you're gonna use often. Don't be fooled though. This little *kewword* is similar but also totally different. And I argue that you *should* make everything a `const` unless you have absolutely no other choice.

# what does `const` mean? (1/2)
Before we can dive into what `const` actually means we have to dive into what a *variable* means.

# what is a variable
A variable is a *pointer into memory* and/or a *shortcut* to something that is **abstracted** away from the programmer by some kind of machine. It might be an operating system or a virtual machine but somehow you can magically refer to it by name. That's a variable.

Most people are used to being able to do this in JavaScript:

    let x = 123;
    x = "foo";
    console.log(x); // writes "foo" to the console

This is pretty sad programming. By using `const` all over the place we can banish this practice:

    const x = 123;
    x = "foo" // ILLEGAL!
    x = 123   // ILLEGAL! 

We should not assign variables unless maybe we are in a loop and then I can probably forgive you if you treat them wisely.

> Use `const` when you can and `let` when you absolutely can't.