# Hatseflatsen
Manne, jullie zijn stuk voor stuk geweldig slimme en kundige mensen. Maar kunnen we allemaal a.u.b. niet zo veel *hatseflatsen* in onze code?

Wat bedoel ik met hatseflatsen? Dat zal ik laten zien maar eerst wil ik uitleggen hoe ik tot deze gist gekomen ben. Sinds een dag of twee wordt ik gelukkig weer op de hoogte gehouden van checkins op onze code. En kan daar nu ook weer iets strakker op zijn.

Vanavond werdt ik *getriggert* door een commit zonder commit message. Deze vallen altijd meteen op dus ik besloot een kijkje te nemen en trof het volgende aan:

    var activiteitdeelnames = Activiteit.Activiteitdeelnames.Where(x => x.Relatie.RelatieOrganisatieeenheden.Any(y =>
                    y.OrganisatieEenheidId == Activiteit.Organisatieeenheid.OrganisatieeenheidId
                    && ((!relatiesoorten.Contains(y.Relatiesoort.KorteOmschrijving) && x.Relatie.LidTot < DateTime.Now) || (relatiesoorten.Contains(y.Relatiesoort.KorteOmschrijving) && y.EindDatum < DateTime.Now)))).ToList();
                    && (x.Relatie.LidTot < DateTime.Now || (relatiesoorten.Contains(y.Relatiesoort.KorteOmschrijving) && y.EindDatum < DateTime.Now)))).ToList();

Ik moet eerlijk zeggen dat ik over het algemeen vrij comfortabel ben met LINQ expressies dus dat is niet het probleem. Het probleem is in dit geval het predicaat van de `Where` aanroep. Wat mij betreft overschrijdt dit predicaat de grenzen van wat ik als een redelijk argument voor een `Where` aanroep zou beschouwen.

Het grootste probleem met dit predicaat is dat er veel en veel aspecten zonder naam rondzweven. Daarnaast trekt zo'n conditie nog meer clausules aan en zal hij er over het algemeen alleen maar complexer op worden. Dit is wat mij betreft leuk in een hobby project maar ik vind dat we als team moeten waken voor dit soort "slimmigheden" in onze code.

> Onze code dient expliciet en eenvoudig te zijn. Makkelijk om te begrijpen, makkelijk om aan te passen, makkelijk om te testen en nooit meer of uitbundiger ontworpen als strict noodzakelijk om te voldoen aan de eisen en wensen van de klant.

En als dit nu een incident was dan had ik dit niet geschreven. Ik besloot om eens verder te kijken naar wat er zowel in dezelfde codebase ingecheckt is afgelopen tijd. Het goeie nieuws is: het is een goudmijn aan voorbeelden om van te leren. Het slechte nieuws is: het is tevens een goudmijn aan WTF's.

En ik zie het heel vaak op predicaten (condities) stuk gaan. Neem deze volgende prachtige `if` aanhef:

    if ((selectedRapportId == 10 || selectedRapportId == 24 || selectedRapportId == 38 || selectedRapportId == 42) &&//Rapport -> 1, 5, 9 of 20

En ergens moet ik eerlijk toegeven dat ik dit soort dingen ook wel schattig vindt. Ze zijn gelukkig heel eenvoudig op te lossen op diverse manieren. 

In het laatste probleem schuilt het grootste probleem dat sowieso de conditie behoorlijk "wazig" is met all die *magic numbers* en dat het bijbehorende commentaar weinig verduidelijkt zonder dat je de applicatie goed kent. Het zou veel beter geweest zijn om te beschrijven waarom het blijkbaar voor deze specifieke elementen - in wat eigenlijk een homogene lijst van elementen zou moeten zijn (en misschien ooit was) - er nu een hele `if` uitzonderingssituatie ingebouwd is. Daarnaast is de consument van de lijst verbonden met instanties van elementen die in de lijst van mogelijke elementen kunnen optreden.

Nog beter zou het geweest zijn om te zoeken naar een manier om de uitzondering inherent te maken aan *elk element* in de lijst/set van mogelijke elementen die dit stuk code moet behandelen. Waarschijnlijk naar een extra stukje data of gedrag wat meegegeven wordt met elk element in de lijst zodat de uitzondering in principe geld voor elk element maar dat deze gewoon geen *effect* heeft in het geval van (hopelijk) de meeste elementen die mogelijk als input kunnen verschijnen. 

In het eerste (LINQ) voorbeeld zou ik sterk aanbevelen om te zoeken naar *labels* voor de verschillende clausules en/of aspecten van het het (gecombineerde) predicaat om het totaal te verduidelijken.

    static bool IsGeldigeDeelnemer(..)
    static bool IsBekendeRelatie(...)
    static bool IsGeldigAbonnement(...)
    static bool IsInDienstVanDeelnemersorganisatie(...)

Dit zijn maar wat hypothetische voorbeelden maar hopelijk is het idee duidelijk. Ik denk dat je veel medeontwikkelaars helpt als je complexe predicaten vermijdt en ze netjes achter simpele methods verstopt. Deze kleine methods kunnen later weer gecombineerd worden en als de scope klein is dan kun je ook de namen vrij simpel houden:

    static bool IsGeldigAbonnement(abo) {
        return IsGeldigeDeelnemer(abo.Deelnemer) 
            && IsBekendeRelatie(abo.Deelnemer.Relatie)
            && IsInDienstVanDeelnemersorganisatie(abo.Organisatie);
    }

    var ongeldig = Abonnementen.Where(x => !IsGeldigAbonnement(x)).ToList();
