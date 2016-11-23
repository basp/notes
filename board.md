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
## Disclaimer
Ik weet niet veel (en heb daar ook niets mee te maken) hoe overeenkomsten op dit moment gesloten worden. Alle bedrijven waar ik gewerkt heb draaiden voor en na mij nog steeds goed zover ik kan bepalen dus ik heb niet de illusie dat ik ook maar enigzins kaas gegeten heb van de beste manier om software contracten af te sluiten. Mijn perspectief hier is voornamelijk gericht vanuit het klant- en ontwikkelaarperspectief. Ik ben voornemens om het perspectief vanuit het softwarehuis (de leverancier) ook nog een keer te belichten zodra ik wat zekerder ben om hierover te oordelen.  

## Voor de klant
Wat veel mensen niet weten is dat dat scrum juist voor de klant ideaal zou moeten zijn. Het is de (software) leverancier, wij dus, die het risico draagt. 

Laten we zeggen dat iemand 50k heeft voor een X aantal wensen. Wat X precies is maakt niet zoveel uit. En stel dat een maand ontwikkeling ongeveer 10k kost. Wat is de beste optie voor de klant?

1. Betaal ons 50k, over 5 maanden is het (hopelijk) af.
2. Betaal ons elke maand 10k, over maanden is het (hopelijk) af en elke maand tonen wij je de voortgang, heb je een potentieel minimaal maar werkend product en kun je afhaken indien je niet tevreden bent.*

Echter optie twee behoeft wel een hele dikke notitie. Indien de klant voor deze optie kiest word hij of zij mede verantwoordelijk voor het ontwikkelproces. Dit is en blijft een lastige kwestie die op verschillende manieren of een combinatie daarvan opgelost word:

1. Het team reist af naar de klant, krijgt daar wat werkplekken en voltooid het project on-site (voor de klant vaak ideaal maar niet geliefd bij leveranciers)
2. Omgekeerd, de klant plaats een (of soms meerdere) personen bij de leverancier waar zij een werkplekken krijgen (ideaal voor leverancier maar niet voor klant)
3. De surrogaat, een derde persoon is product owner (vaak gezien maar hinderlijk voor het proces)

De eerste twee zijn vaak zo moeilijk te realiseren dat de derde optie veelal de norm is. Het is op het eerste gezicht niet eens een onlogische optie en kan heel goed werken indien de complexiteit van een project zeer laag is of veelal aankomt op herhaling.

Het probleem is dat, net zoals met de scrum master rol, de rol van product owner enorme pieken en dalen kent in werkdruk. Soms heb je hem of haar dagen niet nodig en andere dagen moet je helaas die persoon meerdere malen in het uur lastig vallen. 

Van bovengenoemde opties is 3 sowieso absoluut de slechtste als je puur kijkt wat voor een spoedig verloop van het ontwikkelproces nuttig is. Optie 1 en 2 zijn beide ok maar er zijn argumenten waarom optie 1 beter is als optie 2. Ten eerste is de product owner een rol die door 1 persoon (met mandaat indien nodig) vervuld zou moeten worden. En daarnaast is het puur objectief gezien logischer als 1 persoon en niet een heel ontwikkelteam extern werkt gedurende een project. 

Het zou leveranciers wellicht baten om een deel van kosten die de klant hiervoor moet dragen (wellicht 50%/50%) uit goodwill voor het slagen van het scrum project op zich te nemen.

# Hidden pixel op corporate 
Dit kan volgens mij echt niet. Niet deze link, niet het excuus. Helemaal niet in productie en absoluut niet op **elke** pagina op onze corporate site. Dit is een site waar ook onze prospects en klanten naar toe gaan om uit te vinden we we zijn. 

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
Mocht het bovenstaande negatief overkomen dan kan ik alleen maar zeggen: zo is het absoluut niet bedoeld. Ondanks dat ik helaas ook negatieve punten heb besproken heb ik tevens getracht om tegelijkertijd opbouwende kritiek te geven alsmede suggesties over hoe het anders zou kunnen. 

Dit hele stuk is ook niet bedoeld als een soort van *roast* maar meer als een observatie van iemand die dezelfde problemen en manieren om daar mee om te gaan al eerder tegen gekomen is. Er is waarschijnlijk geen magische oplossing, geen gouden set van regels die je kunt volgen waardoor alles goed komt. Elk project is uniek. Ander zouden het geen projecten maar *lopende-band-werk* zijn. 

Dus is de vraag, wat kunnen we doen. Hopelijk zijn op zijn minst een aantal van onderstaande punten relevant genoeg om te overwegen voor implementatie.

