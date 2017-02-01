SelectionView -> Target


RelationView -> Volgende stap

#btnUpdateAll .btnAction.generated.button
De verwachting van Gerrie was dat deze niet de klasse .generated.button zou hebben.

.btnUpdate heeft niet de .generated aanduiding. 

Er zit een hoop logica in de PM omtrend het tonen van allerlei knoppen (voodoo) en die hoort daar niet in thuis.

Je weet niet hoeveel areas er zijn maar alle content wordt altijd in een bepaalde area geladen. De manier waar dit kan gebeuren vind op de volgende manierne plaats:

Replace

Append

Prepend

De basket is verantwoordelijk voor het onthouden van "default" waardes voor velden. Als het zelfde veld verschijnt dan wordt de waarde uit de basket gebruikt om het veld te vullen indien deze leeg is.

