# Waarom zijn refinements lastig
* We hebben te maken met een grote diversiteit van systemen
* Er is niet altijd veel kennis over die systemen
* Vaak is ook de *staat* van de systemen onbekend (hoeveel achterstallig onderhoud en ontwikkeling heeft er plaats gevonden t.o.v. de productie/acceptatie versie?)
* Daarnaast hebben we ook te maken met de natuurlijke onzekerheidscurve.

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
* Als je functioneel programmeert is het makkelijk om functionaliteit p,trendt je data-model toe te kennen.
* Statische functies zijn niet slecht zolang ze **puur** zijn.
* Vermijdt het bijhouden van staat indien mogelijk want dit maakt concurrency (gelijktijdigheid) erg lastig.
* 

