# the mother of all systems
Imagine a system. That translates `A` to `B`. You put in an `A` and a `B` pops out. Let's call this machine `X`.

This machine `X` is produced by another machine with input `U`. It's a convenient machine and it looks prety sleek as well. This machine which produces `X` *machines* is called `Y`. Or the `Y` machine in contrast to the `X` machine. If we supply this machine with a value of `B` we get `C`.

Now there's this other machine called `Z`. As you might have guessed, this machine produces `Y`s if we feed it with a `V`. If we feed the actual machine instance we would get `D` in this case.

# let's backup
Uhm?

* We need to translate `A` to `B`. So we need a `X` machine.
* To create an `X` machine we need a `Y` machine.
* To create a `Y` machine we need a `Z` machine.
* etc.

There's a few things happening here. First, there's a system of producing systems at play: `X`, `Y` and `Z`. The so called *factories* if we want to relate to programming pattern terms. Those factories require a `U`, `V` and `W` argument respectively.

> To actually do something you need to instantiate a crapload of objects. This might not be a good thing.

# back to the mother
