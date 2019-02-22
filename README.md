# HVAC-LoadCalculator
Command line Python script for estimating the heat load of a zoned building in BTU/hr

<b>What this is:</b>
  This is a super simple command line script for taking limited data and calculating an estimate of the heating capacity of a building
  
<b>What it does:</b>
  Takes input from the data.txt file, must be in that specific form. More zones may be added as needed, but each zone must have the same spacing as the example
  
<h1>Assumptions We're Making</h1>
<p>31.25 BTU/ft^2 </br>
600 BTU/(hr * Person) </br>
3.4 BTU/watt </br>

All walls and windows have the same R value </br>

</p>

<h1>data.txt format</h1>
<p>Wall R value: </br>
_int_ </br>
Window R Value: </br>
_int_ </br>
Level Height(ft): </br>
_int_ </br>
(The above block must be placed at the beginning of the file and in this order) </br></br>
Zone 1: </br>
Room Length (ft): </br>
_int_ </br>
Room Width (ft): </br>
_int_ </br>
Wall Lengths (ft): </br>
_int_ _int_, ... </br>
tempDifs (F):  (length must match Wall Lengths)</br>
_int_ _int_, ...</br>
Window SA(ft): </br>
_int_ _int_, ...</br>
wtempDifs (F):  (length must match Window SA)</br>
_int_ _int_, ... </br>
Persons: </br>
_int_ </br>
Machine Watts: </br>
_int_ _int_, ...</p>
