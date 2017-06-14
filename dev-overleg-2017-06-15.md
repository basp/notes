# Intro
Als je zo eens over die *bullet-points* leest hieronder dan komt dit wellicht over als een soort van *rage-against-the-machine* ding maar dat is niet de bedoeling. Ik wil benadrukken dat onderstaande lijst geen waarheden zijn maar vooral gestoelt op persoonlijke opinie en ervaring. 

Ik wil daarom ook elke lezer vragen vooral kritisch te zijn en altijd te blijven nadenken en benadrukken dat ik niet kritisch zou zijn als het me eigenlijk allemaal niet zoveel zou kunnen schelen. Ik geloof echt dat we met zijn allen een hele toffe crew hebben en mijn (soms een beetje gezoute) opmerkingen maak ik voornamelijk uit liefde en passie voor de zaak.

Mijn hoop is eigenlijk alleen maar dit: mensen aanzetten tot denken en meningen. Al is mijn schrijven alleen maar impuls voor iemand om te zeggen: "daar ben ik het dus niet mee eens" dan komen we al een heel eind verder. 

Dus beschouw het als een (wellicht) ietwat provocerend stuk om iedreen duidelijkheid te geven in hoeverre de spreekwoordelijke *golflengtes* verschillen. En ik neem de aftrap door wat stellingen op te schrijven waar ik zelf achter kan staan (maar waar ik tegelijkterteid ook wel de minpunten van durf te benoemen).

# LINQ-pad demo
*Available soon (morgen dus)*

# If-statements en ander geneuzel
Hieronder een complete brainstorm van ideeen omtrend een van de onderwerpen in aanstaande dev overleg. Er zat een soort van prioriteit in maar sinds ik mijn gedachten op een gegeven moment maar enigzins los heb laten gaan is, met name in het laatste deel van de lijst, de prioriteit niet heel erg consistent. 

Ook de scope gaat van programmeren tot aan dev-ops dus die is ook nogal inconsistent maar het belangrijkste wat ik over wil brengen is hoe belangrijk programmeren op een laag niveau kan zijn voor de mate waarin uiteindelijk nog op een redelijke manier over software geredeneerd kan worden.

* **Pure** functies zijn goed, functies die geen staat nodig hebben of die de staat expliciet als argument ontvangen.
* Een if-statement manipuleert bijna altijd staat.
* Een if-statement dat geen staat manipuleert nodigt uit om staat te manipuleren.
* Een if-expressie is als een pure functie en wekt ook de suggestie aan lezers van de code dat op die plek een manipulatie van staat wellicht niet gewenst is.
* Explicite scopes zijn goed (alle vormen om leesbaarheid en misverstanden weg te halen zijn over het algemeen goed goed).
* Behalve expliciete typedeclaraties over het algemeen.
* Manieren om leesbaarheid te vergroten zijn altijd beter.
* Als je data veranderlijk is programmeer je relatief object-georienteerdj.
* Als je data statisch of *well-known* is dan programmeer je functioneel.
* Als je object-georienteerd programmeert is het makkelijk om extra attributen aan je data toe te kennen.
* Als je object-georienteerd programmeert is het vaak lastig om nieuwe functionaliteit omtrendt je model te implementeren.
* Als je functioneel programmeert is het makkelijk om functionaliteit p,trendt je data-model toe te kennen.
* Als je functioneel programmeert is het vaak lastig om extra eigenschappen aan je model toe te voegen.
* Statische functies zijn niet slecht zolang ze **puur** zijn.
* Vermijdt het bijhouden van staat indien mogelijk want dit maakt concurrency (gelijktijdigheid) erg lastig.
* Staat maakt redeneren over software systemen over het algemeen vrij lastig.
* Als je de debugger vaak nodig hebt dan ben je veel te veel met staat aan het neuzelen.
* Of je bent zelf alternatieve exceptions aan het gooien terwijl je ze daar op dat niveau niet eens af had moeten vangen.
* Overevering en classes en prototyping (zoals in java) zijn geen onderdeel van de essentie object-georienteerd programmeren - het zijn tools om duplicatie te vermijden.
* Interfaces zijn de enige echte vorm van ware ontkoppeling.
* Polymorphisme (in de OOP zin) is overschat.
* Compositie (aggregaten) zijn onderschat.
* Microservices zijn goed voor bepaalde grote systeemdomeinen maar niet zozeer op applicatieniveau.
* DDD denken is ets wat zeker zeer nuttig is - met name op applicatie niveau (dat bounded contexts uiteindelijk als micro-services geimplementeerd worden kan ik me goed voorstellen).
* Een mooi eiland in een zee van drab is nog altijd beter dan alleen maar een zee van drab.
* Code is het enige ontwerp en uiteindelijk ook de enige vorm van documentatie die waar is.
* Als je software niet goed te documenteren is dan klopt of het beoogde/geimplementeerde gedrag niet (op conceptueel niveau) of je implementatie is niet accuraat (doet te veel of te weinig) of een derde partij waarvan je afhankelijk bent heeft een soortgelijk probleem waar je omheen moet werken.
* Comments in code (behalve wellicht API comments, waar ik over het algemeen geen voorstander van ben) beschrijven altijd **waarom** en nooit **hoe** (of er moet echt iets heel geks gebeuren in code (en dan nog: *foei*! **Waarom** schrijf je code waarbij je comments nodig hebt om uit te leggen wat er gebeurt?)
* Geef zaken een naam en maak gebruik van faciliteiten die de taal/omgeving je biedt. Als je een comment plaats zoals `// Id ophalen via een ander nummer` waarom maak je het dan niet gewoon een method (of nog beter *functie* ) ergens met de naam `GetIdBySomething` of zoiets?
* Documentatie is super maar moet wel makkelijk toe te voegen en vooral ook in echt bruikbaar zijn. 
* Bij een nieuw systeem wil ik als ontwikkelaar eigenlijk in eerste instantie maar twee dingen weten: **waarom** bestaat dit systeem/applicatie/stuk software en **hoe kan ik het gebruiken** (dus niet hoe werkt het maar hoe kan ik het gebruiken).
* Documentatie behoeft wat mij betreft geen release-pipeline - het zou al heel mooi zijn als elke *solution* (eenheid van applicaties en gerelateerde projecten) een readme bestandje heeft waarin beschreven staat hoe iemand op gang kan komen (een *getting started* of *tutorial* met wat simpele voorbeelden zoals gebruikelijk is voor bijna elk zichzelf respecterend open-source project).
* Dat zoiets *uiteindelijk* uitgroet naar een hele documentatie site met alle toeters en bellen is top maar is dit werkelijk een prijs die we *up-front* willen (**moeten**) betalen?
* Als je me vertelt hoe een systeem werkt maar ik snap nog niet hoe ik het kan installeren, opstarten of uberhaupt gebruiken dan is die informatie over de werking vrij nutteloos. 
* Als je me vertelt hoe een systeem lokaal geinstalleerd en gebruikt kan worden dan ben ik tenminste in staat als ontwikkelaar om zelf het systeem te doorgronden en zelfs eventueel de aanvullende documentatie omtrend werking (indien nodig) te produceren.
* Lego niet Playmobile. Dat wil zeggen: een set van blokjes die op creatieve manieren gecombineerd kunnen worden; niet een set van blokken die op een bepaalde vooraf uitgedachte manier bij elkaar passen.

# Database-driven applicaties
Sommige ontwikkelaars (wellicht voornamelijk de meer jongere generatie) heeft een hekel aan database omdat deze vaak geassocieerd worden met een bepaald soort legacy applicatie. 

Vaak is de gedachtengang bij het onstaan van zo'n applicatie als volgt geweest:

1. Ik heb logica nodig maar eigenlijk wil ik geen release/deploy doen want die zijn enorm lastig.
2. Weetje wat? Ik maak een *switch* colum in de database.
3. Eerst een tabel met daarin de enumeratie voor elke switch.
4. Dan op de juiste manier krijgen alle relevante records in de database de juiste switch waarde.
5. Er wordt een `enum` in code gedefinieerd.
6. Er is ergens een `if` ... `else` of `switch` die aan de hand van de enum het juiste code-pad kiest.

Op kleine schaal werkt dit redelijk maar als je dit twee keer toepast dan worden de verschillende code-paden al snel heel erg moeilijk om over te redeneren. Stel dat je `zwart` en `wit` hebt en `rond` en `vierkant`. 

* Je begint met twee code paden: `zwart` en `wit`. 
* Vervolgens krijg je `rond` en `vierkant`. Nu heb je `2**2 = 8` code-paden. 
* Nu krijg je ook nog eens `rounded-corners` (`true` of `false`) erbij.
* Dan heb ineens `2**3 = 16` (!) code-paden. 
* Nou stel je voor dat je die code-paden zomaar kunt veranderen zonder uberhaupt een release te kunnen doen door effe in SQL Sever Mananger te neuzelen?
* En dat die mutaties niet echt traceerbaar of herleidbaar of gedocumenteerd zijn?
* Of dat database data en applicatie zo nauw gekoppeld zijn dat je in feite programmeert door cellen in een tabel te muteren?
* Let wel: soms is dit een juiste call maar meestal heb je dat soort vormen van abstractie niet meteen nodig.