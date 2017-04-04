# Exceptions

1. Als er in de constructor een `Exception` optreed denk ik: "WTF?"
2. Als er bij het afvangen van een `Exception` een andere `Exception` optreed denk ik "WTFF!?"
3. Als er in de `Dispose` een `Exception` optreed denk ik: "das toch wel erg slecht."
4. Als er bij het loggen van een `Exception` een `Exception` optreed denk ik: "echt waar?"
5. Als er bij het loggen van een `Exception` een constuctor van een API controller aangeroepen wordt en
er vervolgens een nieuwe `Exception` optreed, wederom die constructor aangeroepen wordt en uiteindelijk
het hele proces met een `StackOverflowException` knalt dan denk ik: "das toch wel knap gedaan."