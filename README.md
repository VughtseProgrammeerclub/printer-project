# printer-project
Printen met een MTP401-G256.

## Documentatie
* [Documentatie MTP201](MTP201.pdf)
* Voor (ambitieuze) project ideeën met een thermische printer: https://hackaday.com/tag/thermal-printer/
* De printer is onder andere gebruikt in HP calculators: https://www.keesvandersanden.nl/calculators/hp82240b_v2_inside.php

## Links uit presentatie Chris (20-8-2024)
* https://hackaday.com/2010/08/30/arduino-based-thermal-printer/
* https://thepihut.com/products/thermal-receipt-printer-guts
* https://www.makerfabs.com/mini-58mm-thermal-printer-module.html
* https://www.eeworldonline.com/thermal-printers-part-4-components-and-circuitry-faq/

## Hardware driver
In de documentatie worden de hardware drive LB1257 voor de thermische printkop genoemd. Deze bestaan in feite uit 8 transistorversterkers die het signaal uit de processor geschikt maken voor de printkop. 
- **LB1257**: Ik heb de datasheet toegevoegd en één IC besteld (https://www.okaphone.com/artikel.xhtml?id=481770).
  
Alternatief:
- **ULN 2803 en ULN 2804**: Deze zijn beter beschikbaar. Hiervan heb ik een paar exemplaren besteld via hackerstore.nl. Hiervan heb ik ook een datsheet toegevoegd

## Spreadsheet om pulslengte te berekenen
https://docs.google.com/spreadsheets/d/15NiBSNJHw0S57qPAjDkXndj6-DcM1xwRnpWNPoLl7HU/edit?usp=sharing

![logo vpc](https://github.com/VughtseProgrammeerclub/printer-project/blob/main/vughtse%20programmeer%20club%20-%20logo.png)
# Clubvond 3-9-2024
## Programma
* Ervaringen
* Volgende keer Software Defined Radio
* Volgende week start cursus Code & Educatie
* Maker Days Eindhoven 13, 14 en 15 september

# Naar een printje voor het printerproject
* **Motor, eindschakelaar en tacho**
* **Motor:** geen verschil gedrag printer plus en min
* **Eindschakelaar:** Als printerkop in beginpositie staat is schakelaar open.
* ![connector](https://github.com/VughtseProgrammeerclub/printer-project/blob/main/vpc%20-%20printerproject%20schema.JPG)

* **Tacho:** Geeft geen pulsen maar sinusvormig signaal (demo)
* ![tachosignaal](https://github.com/VughtseProgrammeerclub/printer-project/blob/main/printerprojectTachosignaal.jpg)
* ![tachosignaal omzetten](https://github.com/VughtseProgrammeerclub/printer-project/blob/main/printerprojectTachosignaalOmzetten.jpg)
* Demo opengewerkte motor met tachogenerator

* Koppelen aan Arduino
* Bepalen aantal pulsen voor heen-en-weerbeweging
  
* Printen!
* ![Formule pulslengte](https://github.com/VughtseProgrammeerclub/printer-project/blob/main/printerprojectFormule.png)
* ![Afleiding formule](https://github.com/VughtseProgrammeerclub/printer-project/blob/main/formules.png)
* Spreadsheet: https://docs.google.com/spreadsheets/d/15NiBSNJHw0S57qPAjDkXndj6-DcM1xwRnpWNPoLl7HU/edit?usp=sharing
* https://github.com/VughtseProgrammeerclub/printer-project/blob/main/printerprojectStuursignaalKop.png
* 8-input transistor array
* ![Besturing kop](https://github.com/VughtseProgrammeerclub/printer-project/blob/main/printerprojectStuursignaalKop.png)
* LB1257: https://github.com/VughtseProgrammeerclub/printer-project/blob/main/LB1257.pdf
* ULN2803: https://github.com/VughtseProgrammeerclub/printer-project/blob/main/ULN%202801%202802%202803%202804.pdf

## Printplaat
* Hoe werkt de eindschakelaar op Pico en Arduino?
* Voeding 5 Volt voor printer en eventueel Arduino
* Hoe zit het dan met Pico (ESP32?)
* Poistie printplaat t.o.v. printerloopwerk?
