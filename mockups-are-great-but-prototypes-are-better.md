# Disclaimer
Wordt niet halverwege kwaad omdat ik af en toe misschien een beetje bot ben. Ik hou van iedereen binnen onze organisatie en dit is alleen maar bedoeld als voer voor een kritische maar noodzakelijke discussie die we uiteindelijk ook organisatiebreed zullen moeten voeren.

Jullie zijn echter als eerste aan de beurt! :P

## De klant is geen softwareontwikkelaar
Er ontstaat langzaam een beetje een hele vreemde perceptie hoe software (en met name nieuwe *greenfield* projecten) ontwikkeld worden. En dan bedoel ik met name bij het ontwikkelteam (ook ik heb me schuldig gemaakt aan onderstaand gedrag) (onze PO'er wat dat betreft volgens mij wel op de juiste lijn).

In het kader van **UI** en **gedrag**:

> De klant moet maar vertellen hoe het gebouwd moet worden dan maken wij het wel.

Nee zo werkt het dus niet. Tenminste, niet helemaal. Als jij fotos laat maken dan vertel je de fotograaf toch ook niet hoe dat hij of zij de fotos moet maken? Als je naar een pretpark gaat vertel je de entertainers toch ook niet hoe ze zich moeten gedragen? Als je een wagen koopt dan vertel je de fabrikant toch ook niet hoe dat hij of zij de wagen en/of de opties bij elkaar moet knutselen? Dat vergt *expertise*, expertise waarvoorde klant **ons** inhuurt. 

Wij kunnen zeker de klant *opties* bieden. Maar welke opties dat zijn is **volkomen** aan ons, waartoe we als team toe in staat zijn en hoeveel de organisatie van de klant houdt. Maar we kunnen niet van de klant verlangen dat deze ons gaat vertellen welke opties er zijn. Als dit anders is dan betekend dit dat we simpelweg het **probleem** niet goed begrijpen en alleen maar in oplossingen aan het denken zijn. Wij zouden deze oplossingen moeten aanbieden, niet de klant. Als we alleen maar het probleem goed zouden begrijpen.

## Documentatie:

> Als wij het niet documenteren dan begrijpen we er over twee weken niets meer van.

Dit valt mij behoorlijk **erg** slecht maar ik snap wel waarom dit komt. Dat is niet alleen de schuld van het team. Als ik persoonlijk naar onze twee "voorbeeld" projecten kijk, en dan bedoel ik M%_A en A%_R dan wordt ik daar niet blij van. Nogmaals, dat reken ik jullie niet alleen aan. Het is eerlijk gezegd absoluut bizar om te zien hoe met name die projecten uitgegroeid zijn tot ongeveerd 85% infrastructureel geneuzel en ongeveer 13% functionaliteit. Die resterende 2% is *MIA* (missing in action). Het zijn architecturele *monstrums* wat mij betreft en niet echt een referentie om de toekomst mee in te gaan.

Als wij op die manier software gaan schrijven waarbij deze architectuur ook nog eens doorsijpelt in de manier waarop we tests schrijven dan bouwen we dus **geen** *cathedralen* maar in plaats daarvan **pyramides**. En als we dusdanig software gaan bouwen dan hebben we die pyramides over een paar jaar hard nodig. Voor onszelf.

En ook:

> Ja maar het moet wel met **Sphinx**, **PlantUML** (**UML** really??), een **build pipeline** voor onze docs etc.

Sorry maar **WTF**? Waarom is documentatie gelijk zo *hard ass*? Waarom hebben we een dozijn tools nodig en een buildpipeline en weet ik wat gewoon om ergens wat nuttige informatie achter te laten voor een collega? Sheez!

Ik wordt hier echt een beetje pissig van want documentatie is supersimpel. We hebben al die shit niet nodig. Gewoon een `.md` bestandje met wat nuttige en praktische info is meer als genoeg. We hoeven geen Python en geen Sphinx en geen build pipeline en geen PlantUML en geen RST en whatever. Gewoon een `.md` bestandje, open met VSCode (die we allemaal inmiddels hebben) en gebruik markdown preview en voila. Daar is je documentatie, lokaal, te bewerken, in versiebeheer en mooi geformateerd. Wat wil je nog meer? 

Binnenkort hebben we nog *meta-documentatie* nodig. Documentatie over hoe dat je documentatie moet maken. En voor je weet schrijven we binnenkort ook unit tests voor onze documentatie.

Ik heb niet echt het idee dat dat *agile* is of dat de klanten dat van ons verlangen. Kan aan mij liggen.

## Diagrammen die na twee weken *out-of-date* zijn:

> Dat moeten we doen anders kunnen we geen goede software maken.

Hola-di-yo dat is dus absoluut niet zo. De enige software die diagrammen, schemas en plaatjes nodig heeft buiten de code is software die *obfuscated* (of *obtuse*) is. Wat niemand lijkt te begrijpen is dat de code juist ons ontwerp is. Daarom hamer ik ook altijd op leesbaarheid, duidelijkeheid en vooral ook **begrijpelijkheid** van de code. Het is onze blauwdruk voor de software die we uiteindelijk produceren. Hoe meer *state* je in je hoofd moet bijhouden om een stuk code te doorgronden hoe meer problemen dat uiteindelijk geeft.

> Hoe meer **functioneel** je programmeert, des te minder fouten je uiteindelijk maakt. Je kunt hier natuurlijk in doorslaan, zoals ik zelf nog wel eens wil doen, maar uiteindelijk kun je altijd nog **imperatief** gaan als het echt moet. 

Waarom maken we blauwdrukken voor blauwdrukken en niet blauwdrukken voor blauwdrukken voor blauwdrukken? 

Ik geloof dat diagrammen, ontwerpen (anders dan in code) programmeurs valse zekerheid geven en ze zelfs het verkeerde pad op leiden omdat ze naar diagrammen werken en elke notie van de daadwerkelijke blauwdruk (code) uit het beeld verliezen. 

Elk software project wat een beetje strak in elkaar zit is te doorgronden door gewoon de blauwdruk (de **code** dus) te inspecteren. En dat zijn niet alleen triviale projecten. 

Ik ben hier trouwens enorm stellig in omdat ik alle variaties al een keer geprobeerd heb en ja, het is dus echt zo dat de code uiteindelijk de enige echte blauwdruk is en dat zogenaamde documentatie in de professionele sfeer eeder vaak een *red-herring* is dan een stukje informatie waar je echt wat aan hebt. 

Nou is een stukje praktische documentatie niet verkeerd maar wat wij doen, uitleggen *hoe iets in elkaar zit* is extreem nutteloos. Niemand wil dat lezen want iedereen weet dat die informatie toch nooit klopt met de daadwerkelijke code. 

Wat we nodig hebben is: 
* informatie over hoe we zaken op kunnen starten, hoe we in kunnen loggen en hoe we de basis functionaliteit uit kunnen proberen
* hoe we de tests moeten draaien
* wat voor bestanden waar moeten staan en wat voor directories waar aangemaakt moeten worden
* praktische zaken waarmee en ontwikkelaar aan de slag kan om zo snel mogelijk dat *breakpoint* te raken

Het laatste wat ik wil weten hoe het in elkaar zit. Zodra ik het lokaal kan draaien kom ik daar snel achter. Echter als ik alleen maar informatie heb over hoe het in elkaar zit maar ik kan het hele systeem niet eens opstarten of inloggen dan is dat enorm frustrerend. Al die verloren uren in mooie PlantUML diagrammetjes en dan kan een medeontwikkelaar nog steeds niet aan de gang. Sad face.

En ga nou niet helemaal zwart-wit hier: ik zeg niet dat diagrammen, modellen, schemas etc. erg zijn. Helemaal niet maar ze moeten nietg de leidraad zijn voor wat gemaakt gaat worden. Dat zou de klant moeten bepalen en niet onze UML diagrammen. Als uiteindelijk blijkt dat je ergens een nuttig plaatje hebt staan van een situtatie die vaak ter discussie komt dan is het helemaal niet erg om die informatie te formaliseren in de vorm van documentatie.

Maar als we ons eigen werk zo nauwkeurig moeten gaan documenteren omdat we er anders niets meer van snappen dan stel ik voor om deze sprint ergens een half uurtje te overleggen wat we nou echt van deze abstracties vinden want persoonlijk wordt ik hier niet gelukkig van (als programmeur) en volgens mij de klanten ook niet.

## Tests die superveel overhead hebben
> Ik ben soms gewoon een dag bezig alleen om een unit test te schrijven terwijl de implementatie een uurtje werk was.

Ok we weten allemaal dat unit tests cool zijn maar wij gebruiken ze *totaal* verkeerd. We schrijven de code, doen keurig alle *lagen* en hebben dan **de infrastructuur**  klaar. Vervolgens zijn we vaak een paar uur verder en kunnen we eindelijk voor de klant aan de bak. Oh *CRUD* what are we doing. Nadat je ongeveer honderdvijftig projecten hebt aangepast ga je een unit test schrijven. *Moq*'ed ongeveer een dozijn services en dan roep je een methode aan op je *sut* om te kijken of alles werkt.

Heb je logica getest? Heb je verwachtingen getest? Heb je waarde voor de klant getest? "De zogenaamde *business rules*? Wat heb je getest? Infrastructuur? Heeft het waarde? Is het waarschijnlijk dat het stukje code kapot gaat in de toekomst? Is het complex dusdanig dat het te documenteren is met een heldere testcase?

Sorry maar al die infrastructuur omtrend test cases dat is echt doorschieten. Een testcase zou documentatie moeten zijn maar nu voordat ik de testcase can begrijpen ben ik bijna genoodzaakt om een analyse briefje op het bord te plakken van een uur... Dat is echt niet goed.

Dat gezegd hebbende - ik hou heel erg veel van jullie allemaal en ons team en hoop dat we binnenkort gewoon zeggen van "wij regelen dit want we hebben grote ballen" i.p.v. "ze moeten maar zeggen hoe dat we het moeten doen". 

<3 en tot morgen!

Bas

PS. Nou zul je wellicht denken:
> Bas dat was wel echt een hoop gezeik, ben je echt zo ontevreden? 

Nee dat absoluut niet, het is een superteam en ik heb het enorm naar mijn zin en ben ook enorm trots op hoe jullie het voor elkaar gekregen hebben om een dusdanige gedaanteverwisseling te ondergaan. 

Ik vind echter dat we zover gekomen zijn dat de tijd aangebroken is om deze problemen aan te kaarten aangezien het onze *agility* behoorlijk limiteerd en daarnaast ook nog een hoop overhead en frictie veroorzaakt. Wat we anders moeten doen weet ik morgen vast nog wel als ik deze post herlees. En daarnaast geloof ik dat jullie het juiste willen doen maar ik denk tegelijkertijd dat het juiste misschien niet helemaal is wat jullie denken en ik zou de discussie graag openbreken.

PS2. Weinig oplossingen
Die heb ik maar komen later. Verdient een eigen verhaal.

PS3. https://www.thoughtworks.com/insights/blog/microservices-evolutionary-architecture