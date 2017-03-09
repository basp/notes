# running nanibot
During most of the development, I was just running **nani** locallly whenever I was at one of my computers. This meant that whenever I wanted to shutdown or reboot the bot would start with a clean state. I could usually not be bothered to save her ETS tables nor did I really want to anyway because it's just much easier to work with.

However, now that I spend some effort on making her properly robust (mostly by moving all the potential hazardous functionality out of the core bot process and into event handlers) I wanted to have her running for longer periods of time, like indefinitely if possible. I don't wanna run one of my own computers for *24/7* but then it dawned on me that I could just run it on my Digital Ocean cloud instance instead. I already have that thing and it's mostly idling anyway so surely it can handle an Erlang VM and with a small bot process as well?

# ssh access
The first hurdle is usually getting proper `ssh` access to your instance. Mine is running Ubuntu and I've done this before. First thing involves getting a decent setup and since I'm on windows and I'm picky about my consoles that means getting a real `ssh` executable working in **cmdr** my host of choice.

The easiest way for me was to just make use of the **Cygwin** installer which I already have anyway and getting the right package. Then I can just bootup a bash shell in cmdr and use `ssh` to connect to my host:

    > ssh root@your.host

The most difficult thing here is probably remembering or figuring out what password to use. Hopefully your host has a good management console which allows you to (re)set it.

# installing erlang
I just used `apt-get` the Ubuntu package manager and went to install Erlang, the step should have been relatively painless and I did get an Erlang but unfortunately as things turned out, it was not the right Erlang.

My bot was written for Erlang 19 and one of the new things in 19 is the `gen_statem` behaviour. And because I needed a state machine and because from the documentation it seemed like this behaviour was a superset of the old `gen_fsm` behaviour (which I would've used otherwise) I decided to use `gen_statem` instead. 

However when I updated my box I got Erlang 18 which doesn't include the `gen_statem` behaviour. 

# updating the box
So I went to update the box (instance actually) and I'm sure I did it in the wrong way but I just treated it like how I would update any actual Ubuntu box and that seems to have worked pretty decently.

In the end I did have to fiddle around a bit with package sources in order to convice `apt-get` to get the Erlang 19 package. Also I had to just install `erlang-base` in the end. Trying to install `erlang` just led to too much conflicts and revolving all of them wasn't something I was prepared to do.

In the end I did get the right Erlang and I was able to finally run my bot, but then I stumbled into the next problem.

# running a node
The next problem was that I had to getup an Erlang node and also make sure that would keep running with my bot inside it even though I wasn't actually connected to it anymore.

Now this problem was more due to my lack of understanding and experience with how to do fancy stuff with multiple Erlang nodes so I had to dig into that for a bit.

Turns out my problems where mainly due to not understanding (the importance of) names properly. Once I figured that out it wasn't too hard. Just in case I forget, here's what I did.

First, we startup a *detached* Erlang node with a *short name*. Since I only want to connect to this node locally (after `ssh`ing to it), using a short name is fine for me. 

    > erl -sname bot@hostname -detached

This will spin up an Erlang VM node that is detached from the current shell that you're working in. We can see it with the `ps` command if we want.

The next thing we wanna do is startup **another** Erlang shell and connect to the detached node. We can do this using the *remote shell* argument. As always, when connecting things in erlang we need a name also. Again, we'll use a *short name* for this:

    > erl -sname dev@hostname -remsh bot@hostname

And this will (hopefully) connect us to the Erlang node that is going to run the bot. You can verify this by checking out the prompt (it should reflect the name of the detached process).

Now we can startup the bot and do any other housekeeping we want. There's one very important thing to keep in mind though.

# logging off
Once you are done working in a remote shell you should probably never ever use the `q()` command unless you want to actually kill that node. If I was working on the `bot` node and I would issue `q()` it would actually kill that node (and all of the bot processes with it) which defeats the purpose of starting up a detached node in the first place.

Instead, once you are done just use the *user switch* command `^G` and then use `q` if you are done. This ensures that the detached (remote) shell keeps running while your working shell (`dev` in my case) will exit and put you back on the operating system prompt.