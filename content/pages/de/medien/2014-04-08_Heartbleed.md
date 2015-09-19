Title: Heartbleed: Schlimmste anzunehmende Cryptocalypse
Slug: 2014-04-08_heartbleed
Lang: de
Date: 2015-04-08

Liebe Medienschaffende,<br/>
Liebe interessierte Öffentlichkeit,

Auf Grund der schier inexistenten oder inadäquaten Schweizer Berichterstattung über eine schwerwiegende Sicherheitslücke, welche die Sicherheit der IT-Infrastrukturen (auch eben in der Schweiz) massgeblich beeinflusst, hat sich das Presseteam des Chaos Computer Club Schweiz CCC-CH gefordert gesehen, mit der folgenden Medienmitteilung sensibilisierned zu wirken und eine breite Bevölkerung zu erreichen.

In vielen Versionen von OpenSSL (vgl. [Wikipedia](https://de.wikipedia.org/wiki/OpenSSL)) gibt es einen krassen Bug, der es erlaubt, Teile des Arbeitsspeichers von richtig vielen Computern auszulesen. Damit können Passwörter und zum Aufbau von verschlüsselten Verbindungen genutzte geheime Schlüssel in die Hände von Angreifer*innen fallen. Mit Kenntnissen dieser Geheimnisse wird es für Angreifer*innen möglich, verschlüsselte Verbindungen zu entschlüsseln und mitzulesen. Auf den meisten Servern wird es mit den erlangten Informationen möglich, sich anzumelden und beliebige Daten zu verändern. Es betrifft die bis gestern aktuellen Versionen 1.0.1 (bis einschliesslich 1.0.1f und 1.0.2-beta). Alle sollten ihre Systeme sofort aktualisieren und (am einfachsten) neu starten: Mit dem Update auf OpenSSL 1.0.1g wurde veröffentlicht, wo der Fehler war: deshalb sind jetzt alle Informationen öffentlich, mit denen beliebige Angreifer*innen den Fehler selber ausnutzen können.

Nach einem Update müssen ausserdem vorsichtshalber geheime Schlüssel und Passwörter geändert werden. Diese konnten nämlich leicht über den Bug ausgelesen werden.

Diese Sicherheitslücke besteht seit der Unterstützung der TLS-Erweiterung "Heartbeat" mit [OpenSSL 1.0.1](https://www.openssl.org/news/openssl-1.0.1-notes.html) . Es ist somit nicht ausgeschlossen, dass sie bereits rege ausgenutzt wird.

Den Speicher auszulesen, heisst: ungehashte Passwörter und Passwörter, die gerade eingegeben werden, private Schlüssel (sobald sie geladen sind) zu lesen. Betroffen sind nicht nur Server, sondern allgemein alle Geräte, die OpenSSL verwenden: herkömmliche Computer, Smartphones, Router und Steuergeräte mit Login-geschützter Benutzeroberfläche, ... Betroffen sind auch nicht nur HTTPS-Anwendungen, sondern auch manche VPN-Systeme wie OpenVPN, Mailsysteme, Chatsysteme wie Jabber/XMPP, und alles andere, was OpenSSL nutzt.

Es gibt Webservices, die prüfen, ob man selbst betroffen ist. Hier empfiehlt es sich erst zu upgraden und dann den Check zu machen, denn sonst wissen allfällige Überwacher*innen sofort, dass man angreifbare Software verwendet. Und: Diese Check-Services sind sicherlich sehr interessante Ziele für Überwacher*innen.

Auf Systemen mit der Debian-Version testing/Jessie, muss man zudem aktuell aufpassen, tatsächlich auf 1.0.1g zu upgraden. Diese ist aktuell nur in den Versionen stable/wheezy und unstable/sid enthalten.

Verständnisfragen seitens der Medienschaffenden können an das Presseteam des CCC-CH gestellt werden: Erreichbar unter presse@ccc-ch.ch oder tel. +41 79 191 23 70.

Links:

* [http://www.golem.de/news/sicherheitsluecke-keys-auslesen-mit-openssl-1404-105685.html](golem-Artikel mit Update)<br/>
* [http://www.heise.de/newsticker/meldung/Der-GAU-fuer-Verschluesselung-im-Web-Horror-Bug-in-OpenSSL-2165517.html](heise-Artikel)<br/>
* [http://heartbleed.com/](Announcement und dedizierte Webseite zur Lücke)
* [http://filippo.io/Heartbleed/](http-server-check)<br/>
* [https://www.openssl.org/news/secadv_20140407.txt](openssl-Announcement)<br/>
* [http://is.gd/Qg0QnE](Twitter-Livefeed "Heartbleed" zur Sache)<br/>
* [http://is.gd/YVCPDz](Twitter-Livefeed "OpenSSL" zur Sache)<br/>
