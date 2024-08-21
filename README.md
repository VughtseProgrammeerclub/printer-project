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
In de documentatie worden twee hardware drivers voor de thermische printkop genoemd. Deze drivers bestaan in feite uit 8 transistorversterkers die het signaal uit de processor geschikt maken voor de printkop. 
* LB1257 (aanbevolen)

   Ik heb de datasheet toegevoegd en vier van deze ic's besteld (https://www.okaphone.com/artikel.xhtml?id=481770)
