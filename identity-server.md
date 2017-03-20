# Figuring out IdentityServer3 as a nub
So tonight I got sick of my API being so unprofessionally unsecure so I decided
to play around with Identity Server 3 for a bit. By no means a hard task - it
was pretty much smooth sailing - I did stumble into a few snags here and there.
I'll try to document them here so other people may hopefully benefit from my
stumbling around.

# Where's the template?
As most of the examples and documentation is based on an OWIN server this gave
me a bit of a had scratcher at first. The core templates in Visual Studio tend
to give you an OWIN based application but the classic .NET Framework template
is based on the traditional IIS infrastructure and uses the somewhat old school
`global.asax` way of initializing applications.

There's not really an OWIN template. At least not one that ships with Visual
Studio Community edition. Luckily the empty ASP.NET application template suits
just fine. First we'll create an empty blank solution (under **Other project types**) 
and we'll name it **IdSrvTutorial** for demo educational purposes.

Next we'll *add** a new project to that solution that is gonna be our identity
server endpoint. We'll use an **ASP.NET Web Application (.NET Framewor)** template
and name it **IdSrv**. In the next dialog we want the **empty** template. 

This should give us a very barebones ASP.NET application. We'll setup the server
in the next section.

To complete our project we'll need to install two packages:

    install-package Microsoft.OWIN.Host.SystemWeb

And:

    install-pacakge IdentityServer3

Once we have those we can start to build our identity server endpoint.

# Setting up the server
TODO

# Notes
Below is some random notes 

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