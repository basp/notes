# Figuring out IdentityServer3 as a nub
So tonight I got sick of my API being so unprofessionally unsecure so I decided to play around with Identity Server 3 for a bit. By no means a hard task - it was pretty much smooth sailing - I did stumble into a few snags here and there. I'll try to document them here so other people may hopefully benefit from my stumbling around.

As background info, related to an upcoming project I was trying to familiarize myself with **OAuth** concepts and **Indentity Server 3** specifically. This is by no means a guide on how to get such a server into production but it should give people some insights into how to get one up and running. My reference was [Building and Securing a RESTful API for Multiple Clients in ASP.NET] by **Kevin Dockx** and one that was recommended to me. If you're unfamiliar with all any or all of OAuth, authentication, authorization, claims you probably should watch it as you are bound to deal with this at some point or another.

[Building and Securing a RESTful API for Multiple Clients in ASP.NET](https://app.pluralsight.com/library/courses/building-securing-restful-api-aspdotnet/table-of-contents)

And even though it is from an ASP.NET perspective, a lot of the material is generally useful to any developer. And especially those that are working in an environment that has affinity with the Microsoft stack.

# The goal
The goal was pretty humble, at least I *thought* it would be a humble. I had
two primary objectives:

* Setup a local Identity Server 3 endpoint.
* Obtain an access token using a CLI (a command line client).

As I was following along with this pretty decent PluralSight course things went smoothly. But then I hit some terrain that wasn't covered in the tutorial and I'll try to cover that here.

Turns out that for a command line client you probably want an authentication flow that is known as a **resource owner password credentials grant** and that was the single flow that wasn't covered in this otherwise great course by Kevin Dockx. So I decided to venture further onto this *barely-trodden path* to see if I could reach the end without any guidance from my - at this point - trustworthy mentor Kevin. 

Turns out it's not that hard to reach the end and the path is not that bad once get familiair with a few hurdles that I try to document in this note.

# Where's the template?
Most of the examples and documentation are/is based on OWIN. This gave me a bit of a head scratcher at first. The **.NET Core** web templates that ship with Visual Studio 2017 Community tend to give you an OWIN based application. But the more traditional **ASP.NET Web Application** template I wanna use is based on IIS infrastructure and uses the somewhat old school `global.asax` way of initializing applications.

The bad news is, there's not really an OWIN template for that sort of application in Visual Studio 2017 Community. The good news is: we don't need one, the empty ASP.NET application template suits just fine. First we'll create an empty blank solution (under **Other project types**) and we'll name it **IdSrvTutorial** for demo educational purposes.

Next we'll *add** a new project to that solution that is gonna be our identity server endpoint. We'll use an **ASP.NET Web Application (.NET Framework)** template and name it **IdSrv**. In the next dialog we select the **empty** template. We don't need any of the ASP.NET MVC, Web API or other stuff so we can leave those checboxes unchecked.

This should give us a very barebones ASP.NET application. 

> As a sidenote, you got to love the clean slate without the pregenerated and opinionated cruft that you usually get from the poorly designed templates. Those templates that you get with Visual Studio have never ever led someone down the *pit of success*. They have only led people down the pit of *frustrating*, *deeply* frustrating **doom**. Use them for convenience but realize they offer no insight into what is considered good software development practice.

To complete our project we'll need to install two packages:

    install-package Microsoft.OWIN.Host.SystemWeb

And:

    install-pacakge IdentityServer3

Once we have those we can start to build our identity server endpoint. We'll configure it in the next section.

# Configuring the endpoint
TODO

# Notes
Below is some random notes on random stuff that I encountered tonight while I was journeying during the fabulous lands of ASP.NET, OWIN, Identity Server 3 and Windows permissions and certificates (ugh).

* There's no starter template for OWIN in Visual Studio 2017 Community. But an empty ASP.NET template will do. Setting up the `Program.cs` and `Startup.cs` 
classes is pretty easy and for an **Identity Server** endpoint you don't need much except the `Microsoft.OWIN.Host.SystemWeb` and `IdentityServer3` NuGet packages.
* When you stumble into opaque `500` errors originating from inside the identity  endpoint (the IdentityServer component) make sure to configure a logger (the **Serilog.Sinks.Trace** sink works nice enough for simple debugging purposes).
to see what *exactly* the error is. 
* Store client secrets server side user `new Secret("somesecret".Sha256())` (or `.Sha512()`) 
and not in plain text (helps with `invalid_client` error response).
* Load example certificates and assign them to `SigningCertificate` property to prevent internal server errors (when you trace you'll see that it gets null values when it tries to read a certificate). This was weird because to me the API, documentation and examples suggested you could do without the cert. I guess I just misinterpreted and it's true: you don't have to *install* them but you still have to assign one to the `SigningCertificate` property at runtime if you want success and not failure.
* In order to have Visual Studio load the certificates (from the bin folder for example) you need to run it with **Administrator** privileges or otherwise you'll get access errors during runtime.
* Set `AllowAccessToAllScopes` if you just want to allow a particular (trusted) client to 
dick around with the API/system (like a development tool for example).

Finally, the client needs to request at least some scope. If you request no scope at all you get an `invalid_scope` error response. On the server side this scope can be as simple as:

    new Scope
    {
        Enabled = true,
        Name = "quux",
    }

Hopefully this helps getting more fun out of getting your endpoint up and running and eventually into production. I thought it was fun to play around with the server, hopefully some of my roadblocks can at least alleviate some of the frustrating moments of being completely clueless that I enountered. Enjoy!