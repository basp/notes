[original](https://web.archive.org/web/20061015072808/http://freegw.xs4all.nl/~basp/wordpress/index.php/2006/04/13/88/)

# Stuff about Monad
Last few weeks I've been toying with Msh a.k.a. Monad, the new Microsoft Command Shell. I remember reading somewhere that you could use Windows Forms but that it was impossible to bind handlers to events. Luckely, this is not true. It does require calling an exotic method (for a C# programmer at least) with an ugly name but once you get over this it's not hard at all.

A Button instance has a Click event. In C# one could bind a handler to this event by doing something like:

    button.Click += delegate(object sender, EventArgs e)
    {
        MessageBox.Show("Clicked");
    }

In Monad we cannot use the familiar += syntax but this does not mean that we cannot bind event handlers. But how then can we accomplish something similar? Let's inspect a Button instance using the get-member cmdlet:

    $button = new-object System.Windows.Forms.Button
    $button | get-member | more

If you execute the above script you can see the strangely named add_Click and remove_Click methods scroll by. These methods are equivalent to += and -= operators as used for events in C#. Binding an event handler to a Button instance in Monad can thus be easily accomplished by doing something like this:

    $button.add_Click({ write-host 'OnClick' })

As you've probably guessed, the get_ and set_ methods are the properties getters and setters but in Monad we can use the actual property itself:

    $button.Text = 'I am a button me'
