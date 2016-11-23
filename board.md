# Testplannen
De testplannen indien aanwezig vond ik vaak erg goed en waren voor mij absoluut het meest waardevol om inzicht te krijgen in zowel de applicatie als het daadwerkelijke probleem/request (issue). Ik hoop dat we deze wellicht wat prominenter bij de PBI kunnen toevoegen zonder dat we daar nog een aparte task voor nodig hebben. 

Op dit moment lijkt het erop dat het schrijven van testplannen veel gebeurd door dezelfde personen. Ik hoop dat ik niet de enige ontwikkelaar ben die het enorme nut van de testplannen ervaart en dat testplannen in de toekomst geschreven worden door iedereen binnen het team al dan niet in samenwerking (als dit al niet gebeurt).

Als een aanvullende opmerking, de testplannen vond ik vaak zo goed dat ik verschillende keren nagedacht heb of we deze als aanvulling op de handmatige uitvoering ook niet geautomatiseerd kunnen laten uitvoeren. Ik ben geen groot voorstander van browser based testing als vervanging van unit tests maar het kan zeker een waardevolle aanvulling zijn.

# Onbeheerde issues
Onbeheerde (unassigned) issues zijn goed want deze kunnen (als het goed is) door een ontwikkelaar opgepakt worden. Ontwikkelaars zouden (indien ze niets te doen hebben) altijd de backlog moeten afspreuren naar onbeheerde issues met hoge prioriteit en waar ze in staat zijn deze op te pakken.

Helaas kwam ik veel onbeheerde issues tegen die ik vaak niet op kon pakken door gebrek aan informatie. 

Als je een issue onbeheerd (unassigned) achter laat op het bord, vraag jezelf dan af of er voldoende info aanwezig is zodat een andere ontwikkelaar die potentieel niets van de (mondelinge) voorgeschiedenis en afspraken weet er mee verder kan. 

Als je de issue achterlaat omdat deze geblokkeerd is, zorg er dan voor dat de blokkade en eventuele verantwoordelijke contactpersonen vermeld staan in de comments. Trouwens, als je een issue niet kunt voltooien omdat deze geblokkeerd is dan is er vaak wel iemand anders binnen het team in staat om de controle over te nemen, het lijkt me dan ook beter om in het geval van blokkade de issue aan de desbetreffende persoon toe te wijzen.

Het is erg lastig als de informatie over een bepaalde PBI over zo veel verschillende plekken verspreid is. Linked items zijn leuk maar wellicht kunnen we hier wat streamlinen door slimmer gebruik van TFS processflow inrichting.

# Fysiek bord
Ik ben geen fan van dubbele administratie maar ik heb ervaren dat een fysieke versimpelde versie van een scrumbord echt kan helpen voor meer overzicht. TFS is uitermate geschikt voor traceerbaarheid en de verbinding tussen wijzigingen in de code en de uitendelijke PBI maar door de hoeveelheid aan taken is het lastig om daar het daadwerkelijke overzicht van de status van de PBI's te zien. Daarnaast heeft het iets om een fysieke representatie van de issue te hebben. 

# Scrum master
Ik kreeg daarnaast ook het gevoel dat de rol van scrummaster niet echt duidelijk naar voren komt. Ik vermoed dat dit geen onwil of onkunde is maar puur een effect van het feit dat er niet voldoende tijd over is om hier effectief aandacht aan te schenken. 

Een belangrijke rol van de scrum master is om blokkades op te heffen en beschikbaar te zijn om te helpen indien een teamlid tegen zogenaamde "beren" aan loopt.

In het ideale geval zou de rol van scrum master potentieel full time moeten zijn. Ik zeg full time omdat dit hopelijk niet nodig is zodat de scrum master wellicht ook nog tijd heeft voor andere zaken. De scrum master is de olie in de machine, na gelang van de omstandigheden heb je meer of minder nodig maar als je zonder komt te zitten (omdat de olie ergens anders mee bezig is) dan komt heel de machine tot een halt.

# Team effort
Het is belangrijk dat het team bewust is van het feit dat het team and niet de inviduele ontwikkelaars verantwoordelijk is om te sprint tot een succesvol einde te brengen. Ik heb niet het idee dat dit een directe issue is, ik vond vrijwel overal direct hulp en gehoor al had ik wel af en toe het idee dat ik mensen op het verkeerde moment (of wellicht te vaak) stoorde. Ik realiseer me natuurlijk ook dat deze omstandigheden opgedowngen worden door invloed van buitenaf.

# Klanten
Een scrum team is toch een klant team? Of niet? Echter, gezien de traditionele maar ook veilige arbeidsverhoudingen (voor werknemers met name) in Nederland en relatief gezien ook in Europa (over het algemeen) is het gebruikelijker dat werknemers lange tijd op dezelfde plek werken. Echter, klanten hebben vaak het liefst zo laat mogelijk zo veel mogelijk wensen in een zo kort mogelijke tijd. Hierdoor ontstaan er vaak scherpe pieken en dalen in de hoeveelheid werk die van een bepaalde klant afkomt. Vaak gaan deze gepaard met promoties, campagnes, beurzen, reorganizaties, overnames, etc. 

Door bovengenoemde factoren is het vaak niet erg winstgevend om een full time team te handhaven voor 1 klant. Dus hebben teams te maken met meerdere klanten. Dit hoeft geen probleem te zijn. Echter denk ik dat de manier waarop wij (en veel andere bedrijven) het proberen te handhaven beter kan.

# Beter scrummen?
## Disclaimers
Ik weet niet veel (en heb daar ook niets mee te maken) hoe overeenkomsten op dit moment gesloten worden. Alle bedrijven waar ik gewerkt heb draaiden voor en na mij nog steeds goed zover ik kan bepalen dus ik heb niet de illusie dat ik ook maar enigzins kaas gegeten heb van de beste manier om software contracten af te sluiten. Mijn perspectief hier is voornamelijk gericht vanuit het klant- en ontwikkelaarperspectief. Ik ben voornemens om het perspectief vanuit het softwarehuis (de leverancier) ook nog een keer te belichten zodra ik wat zekerder ben om hierover te oordelen.  

Daarnaast claim ik ook geen officiele scrum expert te zijn. Ik heb de materie behoorlijk uitbundig bestudeerd gedurende mijn gehele loopbaan vanuit professionele interesse en omdat ik er bij inmiddels ook al 10 jaar mee te maken heb als ontwikkelaar met ambities wellicht ook eens de rol van scrum master op zich te nemen. 

Ik heb (nog geen) officieel onderzoek gedaan en sommige van de cijfers die ik noem zijn enigzins gebaseerd op mijn potentieel bedriegelijke geheugen. De precieze cijfers (met name wanneer ik het heb over inzet/benodigde resources) zijn sterk afhankelijk van project tot project en team tot team en de omstandigheden waarin ze dienen te opereren. Echter kan ik het toch niet laten om af en toe een ietwat brede borstel te gebruiken om wat *ballpark* inschattingen te geven.

## Voor de klant
Wat veel mensen niet weten is dat dat scrum juist voor de klant ideaal zou moeten zijn. Het is de (software) leverancier, wij dus, die het risico draagt. 

Laten we zeggen dat iemand 50k heeft voor een X aantal wensen. Wat X precies is maakt niet zoveel uit. En stel dat een maand ontwikkeling ongeveer 10k kost. Wat is de beste optie voor de klant?

1. Betaal ons 50k, over 5 maanden is het (hopelijk) af.
2. Betaal ons elke maand 10k, over maanden is het (hopelijk) af en elke maand tonen wij je de voortgang, heb je een potentieel minimaal maar werkend product en kun je afhaken indien je niet tevreden bent.*

Echter optie twee behoeft wel een hele dikke notitie. Indien de klant voor deze optie kiest word hij of zij mede verantwoordelijk voor het ontwikkelproces. Dit is en blijft een lastige kwestie die op verschillende manieren of een combinatie daarvan opgelost (of omzeilt) word:

1. Het team reist af naar de klant, krijgt daar wat werkplekken en voltooid het project on-site (voor de klant vaak ideaal maar niet geliefd bij leveranciers)
2. Omgekeerd, de klant plaats een (of soms meerdere) personen bij de leverancier waar zij een werkplekken krijgen (ideaal voor leverancier maar niet voor klant)
3. De externe partij, een derde persoon is product owner (deze optie kan goed werken indien de surrogaat beschikt over kennis en mandaat).
4. De combi, iemand met een bestaande rol neemt daarnaast ook de rol van product owner op zich (vaak geen bevordering voor een soepel verloop van het scrum proces).

Uit bovenstaande blijkt al dat het de product owner rol is die toch vaak voor een spanningsveld zorgt binnen een scrum project. Het is echter ook belangrijk om te vermelden dat dit een enorm lastige rol puur omdat de potentiele werkdruk vaak pas tijdens het verloop van een sprint duidelijk wordt. Het is ook niet noodzakelijk dat deze rol 40 uur per week vervuld wordt. 

Veel teams hebben ongeveerd 2/3 dagen (potentiele) fulltime access tot een product owner nodig voor een comfortabel verloop van het scrum proces. 

## Team naar klant of omgekeert (1 & 2)
De eerste opties twee zijn vaak lastig te realiseren voor veel bedrijven. Beide opties werken vaak echter wel erg goed. Als de complexiteit hoog ("lastig in te schatten" dient in alle gevallen als **superhoog** te tellen bij aanvang van een project of *sprint zero*). Als je te maken hebt met hoge complexiteit of een onzekerheid dan is het een goed idee om op zijn minst 2 dagen in de week een afgevaardigde van de kant naar het team of het team naar de klant te sturen.

## De externe partij (3)
De derde optie komt regelmatig voor en werkt over het algemeen ook erg goed. Vaak is het de klant die een externe partij voor de duur van een project inhuurt om als product owner te fungeren.

## De combi (4)

## Product owner
Het grote probleem is dat, net zoals met de scrum master rol, de rol van product owner enorme pieken en dalen kent in werkdruk. Soms heb je hem of haar dagen niet nodig en andere dagen moet je helaas die persoon meerdere malen in het uur lastig vallen. 

## Conclusie
Van bovengenoemde opties is 4 sowieso absoluut de slechtste als je puur kijkt wat voor een spoedig verloop van het ontwikkelproces nuttig is. Optie 1 en 2 zijn beide goed maar er zijn argumenten waarom optie 1 beter is als optie 2. Ten eerste is de product owner een rol die door 1 persoon (met mandaat indien nodig) vervuld zou moeten worden. En daarnaast is het puur objectief gezien logischer als 1 persoon en niet een heel ontwikkelteam extern werkt gedurende een project. 

# ORM
Object-relation-mapping. ORM. Het domein van ORM, de voor en tegens, de overhead, het gemak, de zogenaamde *leaky abstractions*. 

Een *leaky abstraction* ontstaat over het algemeen als een *library* pretendeerd eenvoudige toegang te verlenen tot een onderlliggend complexer systeem. Ergens lekt elke abstractie wel iets. Het bijna niet te vermijden zonder een hele grote hoeveelheid aan *power* (mogelijkheden, the kracht en mogelijkheden om je gedachten en denkwijze om te zetten in code) op te offeren. 

Het belangrijkste punt is echter: ORM bied enorm veel voordelen. Het is ideaal voor de *CRUD* (create-read-update-delete) schermen waar we toch vaak mee te maken krijgen en is zeker een belangrijk hulpmiddel in ons arsenaal. Echter, het mag geen cult worden (ik was ooit deel van die cult, totdat ik een paar keer op mijn bek ging). ORM is goed en bruikbaar in een grote hoeveelheid scenarios maar het is belangrijjk om tevens te beseffen wanneer ORM niet geschikit is.

Laten we er vanuit gaan dat ORM fantastisch is en we gebruiken het overal. Zijn er situaties waar we wellicht kunnen overwegen om *geen* ORM te gebruiken? Off wat voor voordelen halen we er uit en wat zijn de nadelen. Weliicht zijn er meer licht-gewicht alternatieven waarmee we nog steeds comfortabel onze software kunnen ontwikkelen zonder gekoppeld te zijn aan de (helaas) overhead tie ORM frameworks ons geven.

Ik moet toegeven, ik ben een groot voorstander van ORM waar mogelijk. Maar als ORM *the only way* is dan moet ik ook erkennen dan wordt het hard tijd voor wat bijsturing. Laten we er niet verder omheen draaien, did doet mij net zoveel pijjn alls jullie maar het moet benoemd worden anders komen we nooit verder.

De voordellen van ORM:
* Het maakt **potentieel** *CRUD* appilcaties aanzienlijk eenvoudiger om te ontwikkelen. 

Potentieel.

En het heeft potentie. Vergis je niet. Indien in de juiste omstandigheden toegepast dan is ORM een zeer krachtig middel.

Als je applicatie bestaat uit 80% *CRUD* (dat wil dus zeggen een overzicht met regels, potenteel filterbaar en sorteerbaar, misschien paginatie en bijbheroende detailschermpjes gekoppeld met *business logic* (zie rant hieronder) dan is het wellicht geen slecht idee om zoveel mogelijk een ORM te gebruiken. 

Echter, schrijf je een stuk code what in een scheduler komt te draaien en potentieel op zijn minst meer als 1 aanvraag per minuut kan verwachten dan wil je niet dat jouw "werk" (in code) in minuut in beslag neemt. Het zou niet zo'n probleem zijn  als dit 1 minuut in *jouw* code zit want in dat geval hebben we er potenteel nog controle over. Afhankelijkj van je stuk code kun je wellicht op top level wat tijd winnen door zaken uit te voeren terwijl je anders toch maar aan het wachten bent (`async`).

Ik heb wel een kanttekening bij het bovenstaande. Het is een zeer nobel streven om jouw code zo te schrijven zodat deze eenvoudig parralleliseerbaar is. Dat betekend dus zoveel mogelijk vermijjden van *muteerbare staat*.  

Maar als je gaat *profilen* en je komt erachter dat (in een crue voorbeel natuurlijk) die 1 minuut verspeeld wordt door een component in het systeem waar je geen (of niet direct) controle over hebt (zoals een ORM of externe serice, what een database eigenlijk ook is) dan kun je eindeloos je ORM proberen te *tweaken* door hier en daar een kopje om te zetten maar dat gaat een structureel probleem op de lange termijn niet helpen. 

Nogmaals, ik heb op het moment van schrijven nog niet diepe research kunnen doen maar ik ervaar als *newbie* well dat sommige applicaties voor mijn gevoel trager zijn als verwacht in de rol van simpele gebruiker. In de rol van programmeur krijg ik af en toe het idee dat mijjn browser echt moeite heeft met het weergeven van bepaalde schermen. 

Ik kan op dit moment nog niet goed behoordelen of dit probleem bij de database, de ORM of de inefficiente JavaScript zit. Of het feit dat sommige overgangen gedaan worden met behoorlijk heftige popups and loading indicators. Er is iets wat me stoort tijdens het gebruik van de applicatie en het heeft vooral te maken met de aggressive en vaak onduidelijke foutmeldingen die soms wel een grote hoeveelheid aan text bevatten maar weinig informatie.

## PROGRAMMERS
Het zal je wellicht bekend voorkomen, je krijgt een stuk *business logic* and er kunnen van allerlei dingen fout gaan. Het is voor zelfs doorgewinterde ontwikellaars verlijdelijk om de volgende methode te schrijjven (eerst wel effe de interface uitbreiden natuurlijk, of beter: een `IValidatable` interface implmeenteren). Wat mag het ook, leten we `IValidate` doen, dat is een good voorbeeld. Hier is de niet zo heel goeie versie:
```
interface IValidatable {
    IsValid(): bool;
}
```

Het zou mooi zijn om `IsValid` een `property` te maken maar dat gaan we niet doen. De kans is vrij groot dat `IsValid` een behoorlijke hoeveelheid werk moet verzetten. Potenteel zou deze methode zelfs naar een service moeten gaan om zaken te controleren. Als je in `services` denkt dan voel je waarschijnlijk al aankomen waar het probleem zit.

Een `interface` is per definitie een service. Het is een beschrijjving van een service en wij (als ontwikkelaars) hebben de flexibiliteit om tie kiezen welke *service provider* we gebruiken (de implementatie).

Terzijde, dit is waarom je vaak hoort:

> Program to interfaces not classes

Interfaces (op wat voor manier dan ook) geven jou en je collegae en potentieelll iedereen in die toekomet een punt waarmee ze kunnen koppelen en wat ze kunnen *tweakien*. 

Het belangrijkste is dat een interface een abstract contract is, het beschrijft de regels over een verwacht gedrag. Het is een specificatie. Omdat het een specificatie is, is het tevens documentatie. Het schept *verwachtingen* en *verplichtingen* en het is aan zowel degene die de interface implementeerd als aan de gebruiker van het stuk code dat de interface implementeerd om aan deze verwachtingen te voldoen. Het is een van de meest eerlijke constructies (en ook een van de meest bruikbare) die we hebben.

# Muteerbare staat (oftewel, functineel programmeren)
## Assignment
Een zichzelf respecterende functionele programmeertaal staat het volgende niet toe:

```
int x  = 3;
x = 5; // won't even compile!
```

If you are not familair with function programming you might be thinking `wtf` and I will excuse you for your foul lange!

There's no weird stuff going on here. Assignment is final in functional programming [En ik realiseer me net dat ik de helft in Engels aan het schrijven ben en eigenlijk is dat is een stuk makkelijker dus ik ga er mee door].

Think about that. Assignment is final. If I say `C = 3` then `C = 3` always and everytime. And if I dare to change it the compiler (or interpreter) will bark at me.



# De `interface` 
# OOP?
Zelfs 15 jaar nadat er al gebreken bleken in de manier waarop mensen `OOP` (object-georienteerd programmeren/*object oriented programming*) blijken er nog steeds grote misconcepties te zijn over *hoe je object georienteerd pgorammeert*.

Laten we eerlijk zijn - de meeste mensen hebben totaal geen benul waar ze het over hebben in het geval van OOP. Na 15 jaar geprobeerd te hebben om er iets van te maken kan ik alleen maar wijzen naar **Alan Kay** die de uitvinder van OOP is. En helaas, volgens hem doen we het allemaal fout. 

Helaas is Alan Kay ook een ietwat zure man die mooi kan vertellen maar nogal cynisch is. Ik ben iets positiever en hoop mensen terug naar de basis te brengen en OOP daadwerkelijk in een realistch en bruikaar perspectief te plaatsen. Zelfs als zou Alan Kay zeggen dat we noobs zijn laten het cynisme vergeten en de focus leggen daar waar we daadwerkelijk en aangetoond winst kunnen boeken.

## Het grootste probleem met OOP
Niemand snapt precies what OOP is behalve Alan Kay. En zijn visie is zo grandioos on economisch onhaalbaar dat hij er zelf verzuurd van is geraakt.

Zacht gezegt, niet de beste figuur om een idee te promoten.

## Het andere grote probleem met OOP
In de software wereld is het niet al te moeilijk om in te spellen op een concept wat weinig mensen begrijpen. Veel van wat gebeurt is enigzins magisch voor best veel mensen (heel ander verhaal). Je hebt tegenwoording daarom een hoop bedrijven die inspelen op het onbenul en de onzekerheid en bijvoorbeeld zaken als certificatie aanbien en dergelijke. Deze bedrijven spelen in op algmene onwetendeid en de gedachte dat iedereen met een professioneel logo waarschijjnlijk wel te vertrouwen is. 

Helaas, zoals ik al eerder aangaf - niemand weet precies wat OOP is behalve Alan Kay. En hij is zo pissed off omdat we in the 80's niet naar hem geluisterd hebben dat hij het op dit moment niet eens meer wil uitleggen.

Het andere probleem is eigenlijk dat "bedrijven" het concept OOP gekaapt hebben en gemaakt hebben tot iets wat it niet is. Hetzellfde is gebeurt met scrum, tdd, xp, dsdm, etc.

# "Hidden" pixel op corporate 
## BELANGRIJK 
Dit stuk is verplichte kost voor alle ontwikkelaars! Alle andere teamleden worden uitgenodigd om het te lezen en mocht je interesse of meer info hebben dan ben ik natuurlijk beschikbaar. 

Het gaat niet alleen om het verhaal over de pixel en alhoewel dat aanleiding was voor deze sectie gebruik ik de mogelijk tevens om een *key statement* te maken over hoe het zoveel malen beter had gekund. Daarnaast is het inzicht wat ik (hopelijk) probeer over te brengen toepasbaar op bijna elk probleem wat je tegen zult komen (inversion of control is belangrijk niet alleen als techniek mar ook als katalysator voor allerlei andere mogelijke verbeteringen die we kunnen doen). 

Gelukkig merk ik dat de techniek al behoorlijk ingeburgerd is maar desalnietemin is dit een prachtige gelegenheid om in een *realistisch* (?) scenario relatief eenvoudig te demonstreren hoe IoC ook op plaatsen waar je het niet zou verwachten een krachtige techniek blijkt te zijn.

# Ok...
Nu over de bewuste *hidden pixel* (spoiler: het is geen *pixel* en was ook niet *hidden*). Dit kan volgens mij echt niet. Niet deze link, niet het excuus. Helemaal niet in productie en absoluut niet op **elke** pagina op onze corporate site. Dit is een site waar ook onze prospects en klanten naar toe gaan om uit te vinden we we zijn. 

Zelfs al zou die (in mijn ogen lelijke in irritante) pixel niet te zien zijn en was de *hit area* onzichtbaar, dan nog is er het risco dat een potentiele *mis swipe* of *mis click* actie de gebruiker plots op [ishetalweekend.nl](http://ishetalweekend.nl) doet belanden zonder dat hij of zij beseft wat er net gebeurde. Denk je eens in dat je een potentiele klant bent en je krijgt zo een "geintje" voorschoteld.

Ergens kan ik natuurlijk de gein van zoiets wel inzien, het kost niet veel tijd en het heeft mij persoonlijk uiteindelijk ook wel een minuut of twee rondklikken opgeleverd in een poging om uit te vinden wie en waarom. Echter, ik denk dat het niet onredelijk is om dit soort dingen op zijn minst niet verder te laten komen dan de O (en wellilcht in uitzonderlijke gevallen tot ST) in inze OTAP (OSTAP?) straat.

Verder heb ik nog een paar extra opmerkingen betreffende de hack...

Tegenvallend dat het niet echt een pixel was maar een punt (`.`) in een klein lettertype. Het was vele male cooler geweest als ik een enkele gerenderde pixel in een WebGL 3D canvas aangetroffen had maar helaas. Een SVG punt was ook tof geweest.

Het had getuigd van een waar staaltje begrip van software engineering als de maer van de hack deze via de principes van IoC en door middel van DI (dependency injection) ge-implementeerd had. Ik kan me zo voorstelllen dat er een `ISiteCredits` service is:

```
interface ISiteCredits {
    getRenderable(): Renderable;
    getUrl(): Url;
}
```

En als je het echt goed wilt doen dan krijg je al snel zoiets als:

```
interface ISiteCredits {
    getRenderable(): Lazy<Renderable>;
    getUrl(): Lazy<Url>;
}
```

En dat deze in de ontwikkkel configuratie geimplementeerd wordt door een `GimmickSiteCredits` service:

```
class GimmitSiteCredits implements ISiteCredits {
    getRenderable: () => return new StringRenderable(".");
    getUrl: () => return new Url("http://ishetalweekend.nl"); 
}
```

En natuurlijk hebben we ook een implementatie voor productie:

```
class DefaultSiteCredits implements ISiteCredits {
    getRenderable: () => return new StringRenderable("top");
    getUrl: () => return new Url("http://corp.com/");
}
```

Maar helaas, het is geen *micro service*.

Trouwens, in het voorbeeld hierboven, idealiter zouden beide methodes in de interface een `Promise<T>` (of vergelijkbaar *lazy* resultaat) terug moeten geven zoals bijvoorbeelld `Promise<Renderable>` (of `Lazy<Renderable>`) i.p.v. `Renderable`. Echter, daardoor zou bovenstaande voorbeeldcode te veel vervuild raken met onrelevante code.

Er is me verteld dat dit een bij-effect van het feit dat het betreffende 
`site-credits` veld verplicht ingevuld moest worden. Hierop heb ik een paar dingen te zeggen. Ten eerste is [ishetallweekend.nl](http://ishetalweekend.nl) gewoon een slechte keuze voor productie. Als het echt on-overkomelijk is om iets in te vullen gebruik dan gewoon een link terug naar de top van dezefde pagina of nog beter, gewoon `#`. And ten tweede, een beetje software ontwikelaar is in staat om de gebruikte template zodanig aan te passen dat deze an zijn of haar wensen voldoet. En niet dat we terug moeten vallen op een beetje trieste *hacks* zoals het invullen van een punt (`.`) want dat ziet toch bijna niemand tot het invullen van een studentenurl want, wederom, dat ziet toch niemand. Ik zeg: smoesjes.

# Plan
Mocht het bovenstaande negatief overkomen dan kan ik alleen maar zeggen: zo is het absoluut niet bedoeld. Ondanks dat ik helaas ook negatieve punten heb besproken, heb ik tevens getracht om tegelijkertijd opbouwende kritiek te geven alsmede suggesties over hoe het anders zou kunnen. 

Dit hele stuk is ook niet bedoeld als een soort van *roast* maar meer als een observatie van iemand die dezelfde problemen en manieren om daar mee om te gaan al eerder tegen gekomen is. Er is waarschijnlijk geen magische oplossing, geen gouden set van regels die je kunt volgen waardoor alles goed komt. Elk project is uniek. Ander zouden het geen projecten maar *lopende-band-werk* zijn. 

Dus is de vraag, wat kunnen we doen. Hopelijk zijn op zijn minst een aantal van onderstaande punten relevant genoeg om te overwegen voor implementatie.