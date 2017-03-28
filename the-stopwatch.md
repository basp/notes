# Yet another `Stopwatch`
But this one is very simple. I needed one tonight and I was messing around with all kinds of crazy stuff like timers and who knows what. And then it suddenly dawned on me: it doesn't have to be that difficult. Let me present you with the most simple of **stopwatch** classes:

    public class Stopwatch
    {
        private DateTime started;

        private Stopwatch()
        {
        }

        public static Stopwatch(bool startImmediately = false)
        {
            var swatch = new Stopwatch();
            if(startImmediately)
            {
                swatch.Start();
            }

            return swatch;
        }

        public void Start()
        {
            this.started = DateTime.NowUtc;
        }
        
        public TimeSpan Lap()
        {
            var now = DateTime.UtcNow;
            var dur = this.started - now;
            this.started = now;
            return dur;
        }
    }

A default `Stopwatch` doesn't start until you tell it to start timing:

    var sw = Stopwatch.Create();
    Thread.Sleep(1000);
    var dur = sw.Lap(); // Should be 0 duration (didn't start timing)

You can tell it to start timing by calling the `Start` method:

    var sw = Stopwatch.Create();
    sw.Start();
    Thread.Sleep(1000);
    var dur = sw.Lap() // Should be very close to one second

Often you want to start timing right away, just pass the `startImmediately` flag and you're good to go:

    var sw = Stopwatch.Create(startImmediately: true);
    Thread.Sleep(1000);
    var dur = sw.Lap(); // Should be very close to one second

Here's an example on how to use `Lap` for one operation:

    var sw = Stopwatch.Create(startImmediately: true);
    DoSomething();
    var duration = sw.Lap();

If you want to `Lap` multiple operations in a row that's easy too:

    var sw = Stopwatch.Create(startImmediately: true);
    DoSomething();
    var dur1 = sw.Lap();
    doSomeOtherThing();
    var dur2 = sw.Lap();

If you want to start over just call `Start` again:

    var sw = Stopwatch.Create(startImmediately: true);
    DoSomething();
    var dur1 = sw.Lap();
    
    // Maybe log results and do some other stuff
    // that doesn't require timing.
    sw.Start();

    DoSomeOtherThing();
    var dur2 = sw.Lap();

