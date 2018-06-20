Title: Merkblatt Schleuder
Slug: schleuder
Lang: de
Date: 2015-12-14

## Präambel
Bei der [Schleuder](http://schleuder2.nadir.org/) handelt es sich um eine PGP-verschlüsselte Mailing Liste. Die erste Schleuder im Umfeld des Schweizer Chaos war die Schleuder der digitalen Gesellschaft. Später hat der CCCZH eigene Schleuder Instanzen in Betrieb genommen: 'intern', 'agserver' und 'members'. 

 * intern - Eine Liste für 'vertrauenswürdige' Personen
 * agserver - Eine Liste für die AGServer-Leute
 * members - Eine Liste für die Mitglieder des CCCZH

Im Unterschied zur Swisschaos Liste sind dabei die Policies direkt ersichtlich. Im Rahmen der Einführung der Schleuder hat der CCCZH den PGP-Fingerprint auf dem Mitgliederformular zur notwendigen Angabe heraufgestuft, eine Regel die allerdings nicht strikt durchgesetzt wird.

Die CCCZH Members Liste ist entstanden um schnell und relativ niederschwellig Meinungen und anderen Vereinsfoo kundig zu machen - z.B. um zu einer Erfa-Meinung zu kommen, wenn uns der CCC fragt, quasi Vereinsentscheide Light. So ähnlich hat sich das Ari auch für die CCC-CH-members-Schleuder gedacht.

## Scope
verschlüsselte Mailingliste für alle zum CCC-CH gehörenden Menschen, also alle indirekten Mitglieder. Es sollten drauf: 

  * Diskussionen, die den ganzen Verein angehen, aber (noch) nicht öffentlich sind
  * Unterhaltungen zu nicht öffentlichen Angelegenheiten
  * Konsensfindung mittels einfachen Abstimmungen/Umfragen.

Alle Mitglieder der Liste sind mitverantwortlich für die nicht-öffentlichkeit der Inhalte. Falls das vom Autor nicht explizit gewünscht wird, so sind Emails nicht weiterzuleiten und Inhalte nicht zu veröffentlichen!

Für öffentliche Dinge ist nach wie vor die Swisschaos ML zu verwenden. 

## Subscribers
Alle indirekten Mitglieder des CCC-CH haben die Möglichkeit, sich in die Liste eintragen zu lassen. Personen die einem Mitglied des CCC-CH beitreten sollten darüber in Kenntnis gesetzt werden. Zu diesem Zweck sollen sich die indirekten Mitglieder mit dem jeweiligen List-Admin in Verbindung setzen, der auch das jeweilige Keysigning übernimmt. 

Für Subscriber werden auch 1024 Bit RSA Keys akzeptiert.

Leute, die bei einem Mitglied austreten müssen vom jeweiligen List-admin unsubscribed werden. Sollte es in Einzelfällen zu Problemen mit der Anwesenheit auf der Liste kommen, so sind die Probleme individuell zu adressieren und lösen.

## Public keys

 * Die Schlüssel von Subscribern müssen mindestens 1024 Bit starke RSA Keys sein
 * Alle Schlüssel müsse ein realistisches Ablaufdatum (weniger als 5 Jahre in der Zukunft) aufweisen

Wir wollen keine zentrale Datenbank der Hacker in der Schweiz anlegen. Aus diesem Grund müssen die Personalangaben im PGP Schlüssel nicht den realen Personaldaten entsprechen. Es ist ausserdem erlaubt, sich mit verschiedenen Schlüsseln und über verschiedene CCC-CH Mitgliedsorganisationen zugleich einzutragen.

Die Admins brauchen auch kein tatsächliches Keysigning (mit Prüfung der Personaldaten) durchführen. Sie brauchen lediglich zu kontrollieren, dass die Schlüssel die sie eintragen tatsächlichen Mitgliedern ihrer Organisation gehören. Sie sollen ausserdem den Überblick behalten darüber wen sie mit welchem Key eingetragen haben, damit sie die Person bei Austritt aus der Organisation auch von der Schleuder entfernen können.

## E-Mails Senden

Um den aktuellen Public Key der Liste zu erhalten, sende eine unverschlüsselte
E-Mail an `members-sendkey@schleuder.ccc-ch.ch` (inhalt egal).

Um eine Nachricht an die Schleuder-Mitglieder zu senden, sende eine
verschlüsselte und signierte E-Mail an `members@schleuder.ccc-ch.ch`. Da die
Schleuder verschlüsselte Header nicht mag, deaktiviere bitte das Verschlüsseln
des Betreffs deiner Nachricht.

Weitere Dokumentation zur Schleuder-Software gibt's
[hier](https://schleuder2.nadir.org/documentation/v2.2/index.html).

## List-Admins
Jedes CCC-CH Mitglied sollte einen (1) oder zwei (2) Listadmins haben. Die Schlüssel der List-Admins müssen 2048 (oder stärkere) RSA Keys sein. Ausserdem müssen die Listadmins mit Arian Sanusi Keysigning gemacht haben.

List-Admins sind dafür verantwortlich, Mitglieder ihrer Organisation auf die Liste einzutragen wenn diese das wünschen. Ausserdem müssen die List-Admins Personen entfernen die aus der jeweiligen Organisation austreten. Dies gilt insbesondere für Personen die ohne Klarnamen eingetragen wurden, da in diesem Falle keine anderen Admins einen Plausibilitätstest durchführen können.

Die Dokumentation zu den Administrations-Commands gibt's
[hier](https://schleuder2.nadir.org/documentation/v2.2/special_commands.html).

## Betrieb/Server
Aus Gründen der Transparenz sei hier folgendes vermerkt: Die CCC-CH Schleuder läuft auf den Servern des CCCZH. Aus diesem Grund verfügen alle CCCZH AGServer-Admins über administrativen Zugriff auf die Liste.

## Mehr Schleudern
Falls ihr für bestimmte Topics eine dedizierte Schleuder möchtet, selbst aber keinen Mail Server betreibt, so solltet ihr einen eigenen Mail Server in Betrieb nehmen. Falls das nicht in Frage kommt, so kontaktiert Ari damit er euch eine Schleuder einrichtet.
