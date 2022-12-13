# Chaining for Shelby MMSA CGE Model

The folder "**Chaining_Shelby_MMSA**" contains all the necessary files for converting the building functionality data to a capital shock table for CGE model to run simulation.
<br/><br/>

### **chaining.py**
This is the Python script for the conversion.
<br/><br/>

### **Shelby_MMSA_building_to_sector.csv**
This file provides the linkage between buildings and industrial sectors. It has two attributes:
* **guid**: IN-CORE's unique identifier for buildings.
* **sector**: industrial sectors in Shelby MMSA CGE model.
<br/><br/>

### **standard_format.csv**
This file is the output provided by the civil engineering team. It has two attributes:
* **guid**: IN-CORE's unique identifier for buildings.
* **building_functionality**: the estimate of remaining functionality of buildings.
<br/><br/>

### **sector_shocks.csv**
This is the output of **chaining.py**, a capital shock table. It has two attributes:
* **sector**: industrial sectors in Shelby MMSA CGE model.
* **shock**: the multipliers for each industrial sector in Shelby MMSA CGE model.