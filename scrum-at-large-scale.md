# Scrum at large scale
Dit is een kleine samenvatting van de punten die in ieder geval voor mij zijn blijven hangen. Ik moet eerlijk toegeven dat ik meer (enige) notities had moeten maken maar het praatje was dusdanig interessant dat ik dat dus helemaal verzuimd hebt.

Toch ga ik proberen om nog wat zaken op te rakelen waarvan ik denk dat die wellicht wel relevant zijn voor onze organizatie - al is het alleen maar om dingen te benoemen. 

Hoewel het onderwerp op het eerste gezicht misschien niet eens op onze organisatie van toepassing blijkt te zijn denk ik wel dat er zeker een paar aspecten naar voren kwamen die ook voor ons vrij herkenbaar zijn. Daarnaast bleek ook dat we al enorm veel goed doen, alle credits daarvoor behoren aan de mensen die dit (voordat ik aansloot bij deze fantastische groep van ontwikkelaars) al klaargespeeld hebben. Ik ben professioneel gezien wat dat betreft echt onder de indruk.

# Component teams
Vaak bestaat meerwaarde voor de klant niet uit een enkele applicatie maar ook in ons geval zien we vaak dat een combinatie van systemen nodig is om uiteindelijk echt bruikbare functionaliteit op te leveren. Sommige van onze systemen zijn in dat opzicht componenten van een ander systeem. Dit is wat mij betreft een goeie zaak.

Echter, er ontstaat onnodige frictie als je teams ook inderdaad fysiek gaat indelen aan de hand van de componenten van het systeem/applicatie of de systemen waarmee je te maken hebt.

Het (voor mij althans) meest herkenbare probleem is dat er dan zogenaamde *asynchrone* afhankelijkheden ontstaan waardoor zaken meestal langer gaan duren (en duurder worden) dan strict noodzakelijk. Als bijvoorbeeld twee componenten (bijvoorbeeld app en een interne service) bijgewerkt moeten worden om meerwaarde te scheppen dan wordt deze feature over twee teams met elk hun eigen ritme verspreidt. Daardoor gaan afhankelijkheden en aansluitpunten in de tijd uit elkaar lopen en kost het uiteindelijk (vaak behoorlijk wat later) teveel moeite om alsnog te integreren.

Daarnaast is het, en sorry als ik ietwat bot ben, ook heel herkenbaar hoe er zo makkelijk dan *intern geneuzel* ontstaat waar onze klanten uiteindelijk ook niet zoveel aan hebben.

# Feature teams
Wat als we teams anders in zouden delen? In plaats van de focus te leggen op de technische aard van het systeem zouden we de focus kunnen leggen op de functionele aard van waar de klant (wie dat ook moge zijn) om vraagt.

# Travelers
We zien nu al dat bepaalde specialisten bij springen bij teams waar nodig. Ik denk dat we dit heel goed doen. Ik had hier sinds gister nog geen mooie naam voor.

# Component mentors
Ondanks dat je features binnen het team wilt houden kan het helemaal geen kwaad om mensen te hebben die specialistisch zijn met betrekking tot bepaalde componenten binnen je systeem.

# Area product owners
Onze product owner heeft ook meerdere diverse producten onder zijn hoede en vertrouwt daardoor ook op zogenaamde *area expertise* als het op features aankomt.

# Doing the right thing
Er was ook nog een stukje over clean-coding en best practices. Afgezien van het feit dat ik hierzelf enorm op faal door niet eerst tests te schrijven denk ik wel dat we van al deze zaken een heel eind al stevig goed op weg zijn:

* Continuous Integration
* Test Driven
* What had 'ie allemaal nog meer...