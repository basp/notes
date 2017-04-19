# EF, Unit of Work, Repositories
> *Wa'nne abstraksie Batman!*

Wat veel mensen wellicht niet weten is dat `System.Data.Entity.DbContext` al een implementatie van het zogenaamde *unit of work* patroon is. Er zijn allerlei goeie redenen te bedenken waarom je niet gewoon iedereen rechstreeks je `DbContext` gaat geven. Het zou echter een hoop code schelen en is vanuit puur practisch oogpunt wel *handig*. Welke generieke *repository* is zo krachtig als een `DbSet<T>`?

# Hoe ontwikkel je software?
Laat ik voorop stellen dat ik het eigenlijk ook niet precies weet (stiekem denk ik dat wel te weten maar een oordeel over je eigen objectiviteit is volgens mij nog steeds behoorlijk subjectief). Zoals gewoonlijk belemmert me dat echter niet om hier wat over te zeggen. 

Vanuit mijn ideale perspectief ontwikkel je software organisch en met een groeiend besef van het probleemdomein waarin je je begeeft. Het is natuurlijk altijd gezond om te putten uit ervaring uit het verleden om zaken te ontwerpen of alvast uit te denken - zeker als je het probleemdomein al goed kent. 

Na een tijdje zou ook elke ontwikkelaar een *onderbuikgevoel* moeten ontwikkelen wat volgens hem of haar wel of niet *door de beugel* kan in het algemeen. Ook is het aan te bevelen als ontwikkelaars altijd critisch blijven over hun eigen en elkaars code.

In het ideale geval bevind je je hier in het licht-grijze deel van het perspectief waarmee ik wit beschouw als: 

> Totaal geen design, *YOLO!*" 

En zwart als:

> SDM (of RUP wellicht)

Uiteindelijk lijken we soms te vergeten dat onze code **daadwerkelijk** het design is. De **code is de blauwdruk** en dat moet ook wel want de code (en hier is code wel een heel breed begrip want daar bedoel ik in feite alle zaken mee die een systeem *bootstrappen* oftwel tot leven brengen). Als we designs voor onze designs aan het maken zijn dan zijn we dus *meta-designs* aan het maken.

Als we die weg in slaan maken we binnenkort nog *meta-meta-designs* (ontwerpen voor onze ontwerpen voor onze ontwerpen (de code)) en misschien nog wel eens ooit *meta-meta-meta-designs* daar zou op zich niet eens zoveel mis mee zijn als we ze op de juiste waarde zouden schatten en alle effort van een design ook daadwerkelijk rechstreeks zouden kunnen vertalen in het daadwerkelijke platgeslagen design: code die daadwerkelijk meerwaarde levert of voor de klant of in ieder geval voor ons als bouwers van het systeem. Al is het maar in de vorm van inzicht in wat wel of niet een goeie oplossing is. Echter ik zie vaak design puur alleen om design. En erger nog, code die zich dan ook gedwongen voelt om strak binnen dat design te conformeren i.p.v. dat mensen zich daadwerkelijk afvragen wat nou precies is dat ze aan het bouwen zijn en hoe dat het beste binnen een systeem zou kunnen passen. 

# Classificatie
Iets wat ik vaak zie als er gewerkt wordt met **object** georienteerde programmertalen (dus in feite altijd) is een bepaald syndroom van (vaak premature) *classificatie*. Waarbij een of meerdere ontwikkelaars het probleemdomein in klasses proberen te verdelen nog voordat vaak eigenlijk duidelijk is welk probleem nu echt belangrijk is voor de klant. Ik vind het zelf deze nadruk op klasses en types en classificatie en overerving ook wel weer grappig omdat de oorspronkelijke gedachtengang vanuit OOP juist was om een interface aan te bieden om hier op een goede manier mee om te gaan: door objecten die elkaar berichten sturen (messages). 

> OOP is doing it with messages.

De uitspraak van hierboven is van **Alan Kay** - de bedenker van de naam **OOP** en wat we nu doen is niet echt wat hij bedoelde. Wat ik vaak zie is dat er enorm nagedacht wordt over hierarcy en data terwijl dat het probleem en de meerwaarde voor klant helemaal uit het oog verloren gaan. In deze context zijn de volgende inzichten enorm waardevol:

* Als je OOP bezig bent dan is het heel erg makkelijk om extra **data** toe te voegen aan je systeem. Dit komt omdat je gedrag eigenlijk vast ligt. Hoe moeilijk is om een extra `Property` aan je object toe te voegen en dat door te passen? Als je nu denkt: "nou da's toch behoorlijk lastig" dan heb je dus niet echt **OOP** geprogrammeerd.
* Als je functioneel bent dan is het heel erg makkelijk om extra **bewerkingen** (of **operaties**) toe te voegen aan je systeem. Immers, als jij besluit je data te veranderen dan moet je waarschijnlijk een groot deel van je operaties aanpassen. Echter, al je operaties zijn makkelijk te combineren dus het is relatief eenvoudig om nieuwe zaken met behulp van bestaande operaties te definieren.

# Kunstenaars
Dit is geen geheim maar het schrijven van software is (tenzij iedere betrokkene het domein extreem goed kent) altijd weer meer als het samen maken van een kunstwerk zoals een boek of compositie en niet zozeer als het bouwen van een machine. Als de code de blauwdruk zou zijn dan zou die machine er al zijn en dan hoefden we alleen wellicht nog een paar *extensions* of *plugins* te ontwerpen of in het beste geval het ding in elkaar te zetten (zoals een toolkit op een veel *hoger niveau* zoals Outsystems biedt). 

Ik wil echter benadrukken dat men goede software juist herkent aan de nauwe overeenkomsten tussen de manier waarop de totale complexiteit verdeelt is over individuele (uitwisselbare) componenten en subsystemen. Dit betekent in praktijk gewoon het toepassen van **SOLID** principes (waar direct nodig en niet voor later).

Zelf hanteer ik altijd de volgende simpele maatstaf: 

> Als je het op een heldere manier kunt testen, uitleggen en documenteren dan is het waarschijnlijk goeie software. Als je denkt: "hoe ga ik dit nu uitleggen?" dan is het waarschijnlijk geen goeie software.

De vergelijking met een artiest gaat ook niet helemaal op. Wij als ontwikkelaars schilderen in feite het *meta-schilderij*. Het **ontwerp** voor een daadwerkelijk schilderij. We bouwen niet het schilderij, we bouwen een fabriek die elke dag weet ik hoeveel schilderijen de wereld in helpt. Er zitten echter meestal nogal wat lagen tussen wat wij invoeren en het daadwerkelijke eindresultaat. Juist deze afstanden tussen wat je *zou* kunnen en wat je verwacht te kunnen binnen een bepaald systeem maakt ons werk zo vaak moeilijk, onvoorspelbaar en ook simpelweg frustrerend. Daarnaast bouwen we ook helemaal geen schilderij maar iets of een of ander ding van dingen wat uitendijlijk een machine (de software) bouwt. 

En in ons geval wordt die machine dan natuurlijk ook nog eens op allerlei onvoorbespelbare manieren gebruikt. Het is niet een kunstuk wat je waardeert - het is een ding wat je (vaker wel als niet) gebruikt en waarmee je toch vaak een soort van *semi* permanente verandering teweeg kunt brengen. En we weten ook inmiddels (niet alleen uit ons vakgebied) dat genoeg *semi* voorspelbare veranderingen uiteindelijk altijd leiden tot een **onvoorspelbaar** gedrag.

# Buitenwereld
TODO: Voorzichtig omgaan met de buitenwereld (OS, externe dependencies in wat voor vorm etc.).