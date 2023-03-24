# Galveston Nonethnic CGE Model for the Year of 2019

## **Caveat**

This open-source CGE model will replace the capital shock values for the 3 housing sectors HS1I, HS2I, and HS3I with the arithmetic mean of the original shocks on those 3 sectors. See line 1831 to line 1834 in "**galveston_2019_nonethnic.py**".
<br/><br/>

## Introduction

The folder "Galveston_2019_Nonethnic_CGE_Model" contains all the necessary files for running the computable general equilibrium (CGE) model for Galveston County, Texas, for the year of 2019. The model can be used to simulate the economic impact of natural disasters that happened in 2020. For more information about the model, see [Galveston Nonethnic CGE Model](#galveston-nonethnic-cge-model).

The main script is "**galveston_2019_nonethnic.py**". The model is created and executed with `run_solver` at the bottom of the script. The model will import the value of "shocks" on capital stocks in "Simulation_Data.csv" and run simulations. `iNum` is used to indicate the number of simulations. For example, `iNum =  3` is to ask the model to run three simulations. To run simulations with all sets of "shocks" in "Simulation_Data.csv", use `iNum = len(sims.columns)`.

Outputs will be created on the same directory after running the main script. The [Outputs](#outputs) section has more information. 

The solver for this model is **Ipopt**, which is part of the [COIN-OR project](https://www.coin-or.org/). For detailed information about the solver, visit [Ipopt Documentation](https://coin-or.github.io/Ipopt/) or [its GitHub](https://github.com/coin-or/Ipopt).
<br/><br/>


## Required Dependencies

The following dependencies are required to run this model:

- [NumPy](https://numpy.org/)
- [pandas](https://pandas.pydata.org/)
- [Pyomo](http://www.pyomo.org/)
- [Ipopt](https://github.com/coin-or/Ipopt)
- [xlsxwriter](https://xlsxwriter.readthedocs.io/)

Two options are available for installing the required dependencies.


### Option 1

Anaconda and Miniconda are the preferred package managers for Python 3. They can be downloaded from [anaconda.com](https://www.anaconda.com/distribution/), and the installation instructions are here: [docs.anaconda.com](https://docs.anaconda.com/anaconda/navigator/install/).

After installing one of the conda applications, search the required dependencies in [Anaconda website](https://anaconda.org/conda-forge) and install the packages. To download the packages through the recommended channel **conda-forge**, visit the following links: 

- [NumPy on conda-forge](https://anaconda.org/conda-forge/numpy)
- [pandas on conda-forge](https://anaconda.org/conda-forge/pandas)
- [Pyomo on conda-forge](https://anaconda.org/conda-forge/pyomo)
- [Ipopt on conda-forge](https://anaconda.org/conda-forge/ipopt)
- [xlsxwriter on conda-forge](https://anaconda.org/conda-forge/xlsxwriter)

The documentations for each package can be found at [conda-forge.org](https://conda-forge.org/). 


### Option 2

Alternative methods for downloading and installing the required dependencies are available. Visit the following links for details:

- [NumPy - alternative ways to install](https://numpy.org/install/)
- [pandas - alternative ways to install](https://pandas.pydata.org/docs/getting_started/install.html)
- [Pyomo - alternative ways to install](http://www.pyomo.org/installation)
- [Ipopt - alternative ways to install](https://coin-or.github.io/Ipopt/INSTALL.html)
- [xlsxwriter - alternative ways to install](https://xlsxwriter.readthedocs.io/getting_started.html)
<br/><br/>


## Galveston Nonethnic CGE Model

The Galveston Nonethnic CGE model is constructed by using the data in 2019. The model has 2 regions that are classified by [2010 Public Use Microdata Areas (PUMA)][PUMA]:

[PUMA]: https://www.census.gov/geographies/reference-maps/2010/geo/2010-pumas.html

<div align="center">

| Region   | PUMA Code  |
| :---:    | :---:      |
| Island (I)   | 48 04701 (partial)                |
| Mainland (M) | 48 04701 (partial), <br> 48 04702 |

</div>


The industrial sectors are divided into 2 groups:
1. Commercial: classified by [2017 North American Industry Classification System (NAICS)][NAICS]

[NAICS]: https://www.census.gov/naics/

<div align="center">

| Sector in Region $i$ <br> $(i = I, M)$ | NAICS Code             |
| :---:                                  | :---:                  |
| iAgMin                                 | 11, 21                 |
| iUtil                                  | 22                     |
| iCons                                  | 23                     |
| iManu                                  | 31, 32, 33             |
| iWhole                                 | 42                     |
| iRetail                                | 44, 45                 |
| iTrans                                 | 48, 49                 |
| iProfSer                               | 51, 52, 54, 55, 56, 81 |
| iRealE                                 | 53                     |
| iEdu                                   | 61                     |
| iHealth                                | 62                     |
| iArt                                   | 71                     |
| iAcco                                  | 72                     |

</div>

2. Residential: HS1*i*, HS2*i*, HS3*i* in Region $i$ $(i = I, M)$.

This model employs a production function with the property of constant elasticity of substitution. **The labors and households in the model does not have racial or ethnic classifications.**
<br/><br/>


## Outputs

After running the simulations, the following files will be generated:

* domestic-supply.csv
* gross-income.csv
* household-count.csv
* pre-disaster-factor-demand.csv
* post-disaster-factor-demand.csv

### **domestic-supply.csv**
The first column from the left is the industrial sectors. Two other attributes are:

* **DS0**: the initial value of domestic supply
* **DSL**: the result of domestic supply

The values are measured in millions of U.S. dollars.


### **gross-income.csv**
The first column from the left is household groups. Two other attributes are:

* **Y0**: the initial value of nominal household income
* **YL**: the simulation value of nominal household income

The values are measured in millions of U.S. dollars.


### **household-count.csv**
The first column from the left is household groups. Two other attributes are:

* **HH0**: the initial value of number of households
* **HHL**: the simulation value of number of households


### **pre-disaster-factor-demand.csv**
The fist column from the left is labor groups. The rest of the columns are industrial sectors. This file shows the initial value of the number of employment.


### **post-disaster-factor-demand.csv**
The fist column from the left is labor groups. The rest of the columns are industrial sectors. This file shows the simulation value of the number of employment.