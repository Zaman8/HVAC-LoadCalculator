# HVAC-LoadCalculator
Command line Python script for estimating the heat load of a zoned building in BTU/hr

<b>What this is:</b>
  This is a super simple command line script for taking limited data and calculating an estimate of the heating capacity of a building
  
<b>What it does:</b>
  Takes input from the data.txt file, must be in that specific form. More zones may be added as needed, but each zone must have the same spacing as the example
  
<h1>Assumptions We're Making</h1>
<p>31.25 BTU/m^2 </br>
600 BTU/(hr * Person) </br>
3.4 BTU/watt </br>

</p>

<h1>data.txt format</h1>
<p>Zone 1: </br>
RoomLength: </br>
_int_ </br>
RoomWidth: </br>
_int_ </br>
WallSA's: </br>
_int_, _int_, ... </br>
tempDifs: </br>
_int_, _int_, ... (same length as WallSA's required) </br>
WindowSA's: </br>
_int_, _int_, ... </br>
wtempDifs: </br>
_int_, _int_, ... (same length as WindowSA's required) </br>
Persons: </br>
_int_ </br>
machineWatts: </br>
_int_, _int_, ... </br> </p>
