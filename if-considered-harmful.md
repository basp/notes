# `if` statements considered harmful
### disclaimer
Excuses voor allen genen die niet zoveel om .NET of C# geven. 
Hopelijk is het ook algemeen enigzins nuttig.

### statements
Een statement is vergelijkbaar met iets wat `void` (niets) als resultaat heeft. Het veroorzaakt hoogstwaarschijnlijk een **mutatie** van de omgeving waarin het programma draait op een dusdanige manier dat een eindgebruiker er (uiteindelijk) ook waarde aan kan ontrekken (in wat voor vorm dan ook).

Dit is bijvoorbeeld een `Console.WriteLine` (of `console.log`) statement maar ook het weergeven van een webpagina, het sturen van een mailtje, het wegschrijven van een bestand of wat dan ook waardoor je omgeving veranderd. Dit hoeft niet alleen de omgeving te zijn waarin het programma opereert, het kan ook de staat van het programma zelf zijn. Denk aan een stopwatch die *gestart* of *gestopt* kan zijn. 

Het kan zijn dat deze functies niet `void` (of `unit` of `()`, etc.) zijn maar dat ze ook een zogenaamde *return* waarde hebben. In de praktijk zullen deze waardes voornamelijk genegeerd worden.

### expressies
Een expressie heeft een waarde. Het is functioneel een veel natuurlijkere vorm als een statement (bij een statement houd het op, er komt niets uit waarop je verder kunt borduren). Echter, bij een expressie heb je altijd een waarde waarmee je verder kan. Daarnaast is een expressie de meest oprechte vorm van een `if` in je code. Als je niet als een dolle gaat hacken komt er hoe dan ook een redelijke waarde uit zonder dat je in een zijtak van de code hoeft te gaan neuzelen (waar vaak weer een heel nieuw avontuur voor je ligt).

Dus in plaats van:

    FooBarThing thing;
    if(other == something)
    {
        thing = new FooBarThingStuff();
        // Do lot's of stuff to setup `thing`
    }
    else
    {
        thing = new FooBarOtherThingStuff();
        // Some other mutilation to setup `thing`...    
    }

    // Probably even more stuff done to poor `thing`...


Waarom niet:

    var thing = IsSomething(other)
        ? ThisWay() 
        : ThatWay();

    ...

    static bool IsSomething(object other) { ... }

    static FooBarThing ThisWay() { ... }

    static FooBarThing ThatWay() { ... }

Veel minder mogelijkheden om fouten te maken en je maakt tegelijkertijd duidelijk aan andere mensen die de code zien dat je daar niet moet gaan zitten *hacken* omdat het kan. Het kan namelijk niet zo heel makkelijk zonder goed na te denken over wat je nou echt wilt bereiken. Terwijl als daar al een `if` **statement** staat dan is het supermakkelijk voor iemand die de codebase niet kent om daar in die *scope* gewoon even verder te gaan met van allerlei geneuzel wat daar uiteindelijk helemaal niet eens thuis hoort. Potentieel met nog meer `if` statements ("hey we zijn nu toch bezig!") en andere zaken die de complexiteit van de code alleen maar verhogen.

> Expressies zijn geweldig want ze zijn (hopelijk) puur. Maar we kunnen zeggen dat een programma nutteloos is zonder statements of nauwkeuriger: faciliteiten die ons in staat stellen de omgeving te beinvloeden. Dat is ook waarom zelfs de meest pure functionele programmeertalen (talen waarin eigenlijk alleen expressies zouden mogen bestaan) behoorlijk omslachtig te werk gaan om statements weer naar expressies te transformeren (ik kijk naar jou **Haskell**). Dit kan behoorlijk in de weg zitten als je gewoon effe wat console output wil hebben.

### conclusies
Voordat dit een boek wordt snel wat tips als je denkt" "da's allemaal leuk en aardig maar wat kan ik concreet doen?":

* **Vermijdt** `if` statements als de pest; 99/100 keer kun je ook wegkomen met een welgeplaatste expressie of impliciete branching door middel van andere constructies.
* **Schrijf** *loops* zoveel mogelijk in termen van LINQ expressies.
* **Abstraheer** *predicaten* naar `static bool` methodes met een mooie naam die lekker bekt (leest?) tussen de haakjes van je `if`, `Where` of net waar je een predicaat (expressie met als resultaat een `bool`) nodig hebt.
* **Limiteer** ten alle tijde de scope waarin je opereert; probeer zo snel mogelijk naar de **linker** kantlijn te vluchten, hoe verder je afdwaald hoe gevaarlijker het wordt. 

En ook:
* Dat betekend dat je vaak beter eerder *uit een scope moet springen* dan een lang stuk logica in een scope verder van de linker kantlijn te implementeren.
* Denk na over polymorphisme; hoe kun je een bepaald gewenst gedrag zo vertegenwoordigen dat het resultaat homogeen is (voortkomen, *interface*) maar de manier waarop je tot dit resultaat komt verschilt (implementatie).
* Interfaces zijn *awesome*! Ze bieden je niet alleen een manier om na te denken puur in vormen van gedrag (heel handig als je vanuit consument van een API perspectief denk) maar ook als een veligheidsnet en vorm van documentatie. Als een methode een interface terug geeft in plaats van een concreet type is het vaak veel makkelijker te overzien wat je er echt mee kunt doen.
* Probeer duplicatie in **pure** functies uit te drukken en niet in klasse-hierarchieen of overerving. Op school hebben we geleerd dat we moeten overerven om duplicatie te vermijden als we echt *OOP* willen zijn maar de ervaring leert dat overerving in de meeste gevallen niet leidt tot het gewenste resultaat (hierover meer in een andere memo).
* **Object-georienteerd programmeren** maakt het heel makkelijk om je data-structuur te vereenvoudigen. Dat is ook waarom we in termen van gedrag willen denken als we pretenderen object-georienteerd bezig te zijn; als we een nieuw gedrag toe willen voegen (en we hebben ook nog eens te maken met hierarchieen) dan is dat vaak enorm lastig.
* **Klassen** hebben niets te maken met object-georienteerd programmeren (het is een middel om duplicatie van code tegen te gaan, het zijn *object-factories*). De eerste echte object-georienteerde programmeertalen hadden niet eens een notie van *klassen*.
* **Functioneel programmeren** maakt het heel erg makkelijk om nieuwe bewerkingingen toe te voegen aan een bestaande data-structuur. Echter, als we de data structuur willen wijzigen dan betekend dat vaak dat we al ons bestaand gedrag ook aan moeten passen.
* Merk op dat in dit opzicht functioneel programmeren het spiegelbeeld is van zogenaamd object-georienteerd programmeren.

### reacties
Ik hoor ze graag! Uiteindelijk is dit toch voornamelijk voer voor discussie!