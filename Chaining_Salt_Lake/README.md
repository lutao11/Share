# Chaining for Salt Lake 2019 CGE Model

The folder "**Chaining_Salt_Lake**" contains all the necessary files for converting the building functionality data to a capital shock table for CGE model to run simulation.
<br/><br/>

### **chaining.py**
This is the Python script for the conversion.
<br/><br/>

### **buildings_to_sectors_SLC.csv**
This file provides the linkage between buildings and industrial sectors. It has two attributes:
* **guid**: IN-CORE's unique identifier for buildings.
* **sector**: industrial sectors in Salt Lake 2019 CGE model.
<br/><br/>

### **standard_format.csv**
This file is the output provided by the civil engineering team. It has two attributes:
* **guid**: IN-CORE's unique identifier for buildings.
* **building_functionality**: the estimate of remained functionality of buildings.
<br/><br/>

### **sector_shocks.csv**
This is the output of **chaining.py**, a capital shock table. It has two attributes:
* **sector**: industrial sectors in Salt Lake 2019 CGE model.
* **shock**: the multipliers for each industrial sector's capital stock in Salt Lake 2019 CGE model.