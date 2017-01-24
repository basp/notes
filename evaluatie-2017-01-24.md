# Evaluatie 24-01-2017
De hele sprintwisseldag had een ietwat ad-hoc character. Dit was vooral te danken onze onervaren scrum master, het feit dat deze compleet de mist in is gegaan met het boeken van de juiste ruimtes. Het was ook zeker niet handig en op een gegeven moment ook frustrerend om op zolder het tweede deel van dag te moeten houden. Het was ook niet zo tof om gisteren te horen dat de ruimte die al lang van te voren gereserveerd was ineens niet meer beschikbaar was. Echter, met betrekking tot het faciliteren van de *scrum events* ontbrak er nogal wat. 

# Demo
De demo ging helemaal niet onaardig. Er was ongenoegen/feedback omtrend de aanpassingen die voor CZAV doorgevoerd waren. Ik denk dat alle feedback terecht was. Als team zouden we een betere indruk achter laten als we niet direct in een verdedigende houding schieten.

Het is niet altijd makkelijk om enthousiasme op te brengen voor features of fixes die frustrerend waren om te implementeren, waar je niet veel binding mee hebt of die op het eerste gezicht triviaal lijken. Ik denk dat we wellicht met een klein beetje meer *joy de vivre* en betrokkenheid ook de meeste triviale features op een inspirerende manier kunnen presenteren. Een krachtig instrument hierbij is om de waarde voor de klant te benadrukken. Zeker als je keuzes gemaakt hebben die niet of vaag in de specificatie stonden.

Wat mij wel enigzins verbaaste is de verbazing van niet alleen de (surrogaat) klant maar ook van mensen binnen het team. Ik was zelfs ook enigzins verbaast over hoe de functionaliteit geimplementeerd was en meer nog over het feit dat de klant zo verbaast was. 

* Waarom betrekken we klanten tijdens de sprint bij zulk soort beslissingen omtrend UX?
* Het is vaak handig om zo snel mogelijk in een sprint de UX uit de weg te helpen. Het is vaak enorm handig als je de focus legt op UX en vanuit daaruit de feature verder uitdiept. Als je te maken hebt met een bestaande backend dan betekend dit dat je waarschijnlijk te maken zult krijgen met een significante portie mapping logic omtrend je *view model*. Soms ontkom je er niet aan om de backend door de *UI abstractie* heen te laten sijpelen maar deze gevallen dienen zeldzaam te zijn. In principe zou je gewoon de UI moeten kunnen maken zonder je direct over de backend services druk te maken.
* De meeste klanten weten over het algemeen pas wat ze willen als ze zien wat ze niet willen. Als je hiermee rekening houd in de manier waarop je tewerk gaat dan voorkomt dat frustratie (en, waar iedereen blij van wordt, ook verbrande uren).
* Simpel gezegd: als een API ontwikkeld wordt met het oog op meerdere applicaties, en als elke applicatie ontwikkeld wordt met het oog op meerdere backends dan voorkom je een hoop problemen.
* Bovenstaande lijkt misschien een voornamelijk front-end probleem maar dat is niet waar: er is hier geen onderscheid tussen front- en backend ontwikkeling. 

Vanuit de backend heb je net zo goed weer te maken met soms waanzinnige backends en derde partijen die op het laatste moment een mailtje sturen naar iemand die afwezig is en vervolgens een wijziging doorvoeren (of toch niet, of misschien stiekem wel of voor een deel) waardoor een niet onsignificante portie gebruikers van onze applicaties niet meer in kan loggen. 

En als je een API ontwikkelt dan geld net zo goed dat het helpt als je vanuit de klant/gebruiker denkt en in een vroeg stadium met hem of haar bespreekt wat er wel en niet binnen de mogelijkheden valt. Vaak zal dit wellicht een ontwikkelaar uit een ander team zijn maar het kan ook goed iemand van binnen het team zijn. 

En in sommige gevallen moet je zelf tevens de rol van gebruiker en bouwer van een API zijn. De truuk om tot een heldere, (her)bruikbare en documenteerbare API te komen is om deze twee rollen ook daadwerkelijk aan te nemen. En om vanuit beide perspectieven na te denken. Dit is in feite dezelfde gedachtengang die je volgt wordt als je *test first* (of meer popular, *test driven*) bent.

# Retro
Achteraf gezien was het beter geweest om de retro meer gestructureerd op te zetten. De feedback dat discussie op een gegeven moment ietwat in cirkels ging was volkomen terecht. Echter, er kwamen wel degelijk zaken naar boven waar we als team een bijdrage in verbetering kunnen leveren dus dat is goed. Daarnaast moeten we ook zeker doorzetten met de ambitie om serieuzer met deze punten om te gaan. Het idee om ze concreet te maken is iets wat we meteen op kunnen pakken. 

# Wrap-up
De *wrap-up* leek redelijk goed bekend en was relatief vlotjes afghandeld. Afgezien van het geklungel van de *scrum master* (wat tijdens de rest van de middag aanhield). De term was voor mij nieuw maar het concept was wel bekend. Helaas komt het vaak wel neer op het gewoon overslingeren van werkzaamheden die om wat voor reden dan ook niet voltooid zijn.

Nu waren er een paar weken van *kanban* aan vooraf gegaan wat wellicht ook invloed had op de manier waarop we vandaag onze sprint in moesten gaan. Na een echte sprint is het denk ik wel zinnig om tijdens een *wrap-up* kritisch te zijn over zaken die aan het eind van de sprint nog onafgerond op het bord rond dwarrelen:

* Waarom?
* Wat kunnen *wij* als team doen om dit te voorkomen of om problemen eerder te signaleren of escaleren?
* Wat zou de organisatie voor ons kunnen doen om dit in te toekomst te voorkomen?

Als we bovenstaande vragen goed kunnen beantwoorden hebben we niet alleen een constructief verhaal over onszelf maar ook ten opzichte van de rest van de organisatie. Het belangrijkste is dat we niet alleen de verantwoordelijkheid bij de rest van het bedrijf leggen maar zelf ten eerste het voortouw nemen in verbetering. 

# Random
> De manier waarop onze refinements/planning sessies verlopen hebben niet te maken met het wel of niet realiseren van een *glazen huis* om in te ontwikkelen.

Ten eerste is de *glazen huis* metafoor een hele aardige en zeker ook iets om naar te streven en aan te werken. Laten we wel realistisch zijn, om daar te komen zullen we moeten geven en nemen en we zullen er niet komen in een enkele stap. Het zullen een hele hoop kleine stapjes zijn en ja sommige (hopelijk weinig) zullen soms noodgedwongen en soms onverhoopt ook de verkeerde kant op gaan. C'est la vie.

Ten tweede denk ik dat de manier waarop scrum events verlopen en met name ook de refinements en planning sessies wel degelijk invloed hebben op de bouw van het gekoesterde huis. De kwaliteit van deze sessies heeft een directe invloed op de kwaliteit van de sprint en het scrum process in zijn geheel.

> Mijn API (service) die ik moet gebruiken is niet precies makkelijk te gebruiken, nogal dubieus van kwaliteit of beide.

En soms heb je een API maar voornamelijk te pruimen zoals deze je toekomt. In dat geval investeer je in voorbeeldcode en documentatie omtrend bekend gedrag maar vooral ook omtrend vreemd gedrag. In dit geval, tijdens de tijd die je voor analyze krijgt investeer je in tests en dergelijke die veriferen dat de aannames die je doet ook overeen komen met de verwachtingen die geschapen of ondervonden zijn. Let wel op om deze tests geen vast onderdeel van je gebruikelijke unit-tests te maken want daarvoor zijn ze veel te traag. Hier zou het werk redelijk gelijkmatig verdeeld moeten zijn over tests, documentatie en implementatie. Echter, de *hoeveelheid* werk is in een vroeg stadium vaak lastig in de schatten.

> Er is teveel random shit en hierdoor is het lastig om een accurate ureninschatting te geven.

Shit happens. En waar mensen samenwerken en organisaties dynamisch zijn en soms ook weer afhankelijk zijn van derden dan gebeurt er regelmatig iets wat niet voorzien is. Het is makkelijk om deze zaken te zien als *frictie* en *frustratie* op weg naar glazende software en sprints zonder problemen.

