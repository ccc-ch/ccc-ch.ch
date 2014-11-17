Website of CCC Swiss association based on [Pelican Static Site Generator](http://blog.getpelican.com/)

|environment | URL|
|---|---|
|stage|[ccc.dbrgn.ch](http://ccc.dbrgn.ch/)|
|live|[ccc-ch.ch](http://ccc-ch.ch/)|

# Depencies

* [Virtualbox](https://www.virtualbox.org/) is required to run with Vagrant
* [Vagrant](http://www.vagrantup.com/) is requierd to initialize the development VM

# Installation

1. ``git clone https://github.com/peponi/ccc-ch.ch.git``
2. ``cd ccc-ch.ch``
3. ``vagrant up``
4. ``vagrant ssh``
5. ``cd /var/www/site/; ./develop_server.sh start``
6. open http://10.14.10.5:8000

for **scss compilation** change to a second terminal tab

7. ``vagrant ssh``
8. ``cd /var/www/site/``
9. ``grunt watch``

# Mardown use

please use some [Markdown Editor](http://jbt.github.io/markdown-editor/#bVPLbtswELzzK7ZwANmtLfWcntqkaQMkQNHHKSgQWqQkWiJXIFdWkqL/3l0qcHoIYIIGOZzZ2VmtYP3F0ddpv7sa9BGjNRu41bE3OAf4bBxhVOqTTq6GKdlmGqCxmqZoYXCJzpWCt3BBcaguvIF38AMIIemjBeosNG6wAriMugUdDJiII+h8Di4wtLPMxPuA2oAjAV/JZY2BbKAEmu+Fj29D5vz1/QYSwiNOUOsAqROEECal1HXhISC0iAY0wRwdudAygR+ZtBLcYCOQfaCtsLSYMSyB3lInWCaOyQ5NqdQNYr/lcsXpm+y0QZRtr+OyPSn1kW2JiyJlEq7cWAbf398f9FGnOrqR1Nm6mUJNDsN680cBnK0L447FpuzID+viGrRnHT4qi80H9ZcXv1fqZ+cS8O8OAywp/V53RGM6r6rWUTftyxp9ddhT5Z8z29mc2UbcDZaAK+oDzuAauC44lv372EszKVc7S+XsVH3jYJIEcRtLuETc57hE/k4MwcK6qLO4j4YxWXyMeLA1pUpwz+rVZgtNRA9z5+pOSWwupNFFLS0QGe512maN3LSO/z2Ck5Q8x77AOA5iUK29lLhareAHTU0jc2iEw+veZqJlCu+kBda82qG6Oxw2nF58me1Rx8R555cXXPqti/E/h+LG56MyWKqWx2JEzzaXnB65zodd59pu4EVc02I+M56Oy0M6cSZsaOZx9To4XacSY5vPqhO6suFZaqGH042MJn8BONE4UR4y2A9Y9ynLHdLO2GbQZF+1b3TosdWuesEtKu2TG0ehxgaMJn1qK89Hw4sV+XtL6h8=) and the [Guidelines](#) to write articles and protocols

# Todo Vagrant

* in der vagrant provision muss noch  ...
 * ein start script in die VM kopiert werden für den develop_server
 * npm installiert werden
 * 'npm install' im /var/www/ccc-ch.ch order ausgeführt werden
 * ein startscript für 'grunt watch' in die VM kopiert werden

# Todo CCC-CH Site

* neues logo
* farbschema gemeinsam auswählen
* im moment ist das grid wie flolg aufgeteilt 
 * |1 spalte|9 spalten|2 spalten|
 * der letzte 2 spalten block ist für das pelican include "extras" vorgesehen
 * wird das überhaupt verwendet werden? wenn nicht kommt die spalte weg, sähe besser aus
