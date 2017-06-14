# Waarom zijn refinements lastig
* We hebben te maken met een grote diversiteit van systemen
* Er is niet altijd veel kennis over die systemen
* Vaak is ook de *staat* van de systemen onbekend (hoeveel achterstallig onderhoud en ontwikkeling heeft er plaats gevonden t.o.v. de productie/acceptatie versie?)
* Daarnaast hebben we ook te maken met de natuurlijke onzekerheidscurve.

# LINQ-pad demo

# The Zen of Programming
* Functies zijn goed, pure functies die geen staat nodig hebben of die de staat expliciet als argument ontvangen.
* Een if-statement manipuleert bijna altijd staat.
* Een if-statement dat geen staat manipuleert nodigt uit om staat te manipuleren.
* Een if-expressie is als een pure functie en wekt ook de suggestie aan lezers van de code dat op die plek een manipulatie van staat wellicht niet gewenst is.
* Explicite scopes zijn goed (alle vormen om ook maar welke vorm van potentiele fouten weg te halen zijn goed).
* Manieren om leesbaarheid te vergroten zijn altijd beter.
* Als je data veranderlijk is programmeer je relatief object-georienteerdj.
* Als je data statisch of *well-known* is dan programmeer je functioneel.
* Als je object-georienteerd programmeert is het makkelijk om extra attributen aan je data toe te kennen.
* Als je object-georienteerd programmeert is het vaak lastig om nieuwe functionaliteit omtrendt je model te implementeren.
* Als je functioneel programmeert is het makkelijk om functionaliteit p,trendt je data-model toe te kennen.
* Als je functioneel programmeert is het vaak lastig om extra eigenschappen aan je model toe te voegen.
* Statische functies zijn niet slecht zolang ze **puur** zijn.
* Vermijdt het bijhouden van staat indien mogelijk want dit maakt concurrency (gelijktijdigheid) erg lastig.
* Overevering en classes en prototyping (zoals in java) zijn geen onderdeel van de essentie object-georienteerd programmeren - het zijn tools om duplicatie te vermijden.
* Interfaces zijn de enige echte vorm van ware ontkoppeling.
* Polymorphisme (in de OOP zin) is overschat.
* Compositie (aggregaten) zijn onderschat.
* Microservices zijn goed voor bepaalde grote systeemdomeinen maar niet zozeer op applicatieniveau.
* DDD denken is ets wat zeker zeer nuttig is - met name op applicatie niveau (dat bounded contexts uiteindelijk als micro-services geimplementeerd worden kan ik me goed voorstellen).
* Dit laatste heeft ook te maken met het contrast tussen FP & OOP: als we OOP bezig zijn dan moeten we nadenken over functionaliteit en niet over of een bepaald object nu wel of niet een omschrijving veld heeft (het toevoegen van extra data is in OOP modus vele malen simpeler als extra functionaliteit).
