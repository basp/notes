# Projectitis
This is mainly for the .NET folks but similar problems are occuring elsewhere in development land (I'm looking at you Node.js guys).

Listen up people, it's time to stop the madness. I've seen this so much it is getting silly. And I'm not innocent either, I've fallen in the same trap more than once so this is not me pointing fingers but more me just taking a stance on something and hopefully getting some insights from that.

And this post is by no means a reflection on my current or previous employers. It's just a general issue that I see in projects all over the place including my own and I'm just trying to take a stab at it right now because I was triggered by some very good questions and insights at work today. And this is just a realy big pet peeve.

# Why do we have so many projects?
Really guys, why? I mean, it's not just us right now but it's everywhere. It's like a solution has a dozen projects even before something meaningful has been programmed. And it doesn't just happen in so called *enterprise* software but even in halfway decent open source projects.

### The project file is horrible, the solution file even worse
Ok granted, these files are bitches to fix in merges. I can merge most of the code any day but when there's a conflict in the solution or project file I feel a real sense of dread and despair. I have no real solution for this except cursing. Or use different tools. Command line tools with .NET core and Visual Studio Code looks like it might work.

### Because namespaces
Wrong. Namespaces and projects map to eachother orthogonally. In other words, a project may span multiple namespaces as well as a namespace can span multiple projects. These two are not so strictly tied to eachother as for example files and types.

### Dependencies
Sometimes you literally have so much projects that the only way to solve dependency problems is to create a new project in order to prevent circular references. Welcome to *dependency hell*. You had `N` problems and now you have `N+1`. Don't you wish all those projects would be in a single convienient assembly right now? Since that is wat the circular dependency problem implies.

Note that if you're ever in this situation then you probably have no other choice than to accept that the number of projects will continue to grow while the code is refactored into a more wholesome whole (hopefully). 

These operations take a long time and at first things might seem desperate. However, eventually you'll be able to merge newly created projects back together based on their dependencies and hopefully slowly pull stuff back in while the plane keeps flying.

Things *will* get worse before they get better and you can't pull something that is not a whole apart either.

It might be useful to create a custom `Attribute` or maybe a few so you can more easily mark code for moving/removing while the *road is being cleared*.

### Reusability
So you're finding that you're writing such awesome code and think: "man, I bet everyone would love to use this.". Well lemme break the sad truth, most people don't. Most people don't want to use an undocumented, clumsy, bug-ridden API over some other half-decent API that is at least a little bit less bug-ridden or half-baked. 

The above may sound harsh but that's the unfortunate truth. Most people even don't know the BCL well enough to be able to develop assemblies that they can dogfood themselves in another project, let alone release them for others to consume them (I consider myself one of them). I refuse to use it without decent documentation anyway. 

> If I have to dive into the code to see how it works it's not something I would willingly use. Its easier (and more efficient) for to write something up myself than to try understand some poorly designed API.

### About wrapping
And about wrappers (sometimes mistakingly called facades). I think sometimes they might be a bit overused. I know how tempting it is to wrap every single thing so to make it easier to work with but you sometimes have to realize that things are often so for a reason you might not forsee at the moment you're wrapping it. 

You can *try* and make it easier but in the end what happens is that possible consumers are harmed because they are limited, not given enough info when things go wrong, not being able to properly debug or a combination or worse.

And when is the last time you completely changed for example the logging library? Is it really completely necessary to have a facade for this? I assume that once you settle on a good logging library you made up your mind for that project. The same with dependency injection or whatever trivial thing you want to wrap.

Unless you *really intend* to wrap it into something better and can clearly explain the additional functionality over the thing that you're wrapping, don't bother to wrap it. Do stuff with it, offer a library or something with useful functions, extension methods if you want, but please for the love of everything that is cute and fluffy please **don't wrap** it in some more useless API that hides even more information about what is actually going on.

Never *ever ever ever* hide information from your fellow programmers. Nobody will like your library or framework or whatever for it. In fact, think about it, how much would you like it?

### That's how the pros do it
It's not. Look at `mscorlib.dll` for example or `EntityFramework.dll` for that matter. Those are actual deploy units. Stuff that actually belongs together should stay together for *as long as possible* untill you have no other choice for *some reason*. You can use only part of an assembly, no need to cut it up into a dozen little pieces prematurely.

### It's to give guidance to new programmers
Ah ok, yeah. That works out great. It's much easier to figure out where everything goes when I literally have over a hundred places to choose from. Including a lot of places which are (or should not be used) anymore. Yeah I totally see how that helps me out if I don't know the application. If it has to be this way then somebody *in the know* should really take some time to document that shit properly (and in one place) before we waste any more time on that stuff. 

Also, if you do insist on having everybody put their thingy in the proper pigeonhole then why not just use directories instead? You *don't* really need separate projects for that.

### For deployment
This is the only valid reason, maybe. If can point to a reason why having another project/assembly is valid then it will be because it eases deployment *somehow*. However, that somehow better have a good explanation.

### It's a good way to start over
It's not. It looks like nobody has a clue except just start a new project and hope it goes better this time. And that we can integrate it into the main code base somehow (hardly ever happens fully). So you end up with two solutions/ways of doing things to the same problem. And then a while later somebody thinks, just start over with a new project and surely it will go better. And now we have three. Cool.

These things should've been carried out in a seperate branch of the code in the first place. Or properly integrated. It's a topic for a whole different note.

### It's an application
Valid reason, an application has to be a seperate assembly. You can try to merge but that is just pretending to be one while you're actually not. When you need a new application, whether it a console, service, forms, web or whatever application you most likely need a new project. There's a few things to consider though: 
* Should in that case the new application be really part of the solution that already exists or perhaps it should be in its own solution completely?
* Maybe you have a lot of stuff that looks like it make sense in a `Core` or something assembly/project but often you don't even get to use (dogfood) it yourself so how do you expect others to re-use it properly? Maybe it makes more sense to keep it close to the application and polish and document that until maybe someone actually *needs* to re-use functionality.