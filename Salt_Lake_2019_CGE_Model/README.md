# Salt Lake CGE Model for the Year of 2019

## Introduction

The folder "Salt_Lake_2019_CGE_Model" contains all the necessary files for running the computable general equilibrium (CGE) model for Salt Lake City, Utah, for the year of 2019. The model can be used to simulate the economic impact of natural disasters that happened in 2020. For more information about the model, see [Salt Lake CGE Model](#salt-lake-cge-model).

The main script is "**salt_lake_2019.py**". The model is created and executed with `run_solver` at the bottom of the script. The model will import the value of "shocks" on capital stocks in "Simulation_Data.csv" and run simulations. `iNum` is used to indicate the number of simulations. For example, `iNum =  3` is to ask the model to run three simulations. To run simulations with all sets of "shocks" in "Simulation_Data.csv", use `iNum = len(sims.columns)`.

An output "Salt_Lake_Results.csv" will be created on the same directory after running the main script. The [Outputs](#outputs) section has more information about "Salt_Lake_Results.csv". 

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


## Salt Lake CGE Model

The Salt Lake CGE model is constructed by using the data in 2019. The model has 7 regions that are classified by Public Use Microdata Areas (PUMA): 

<div align="center">

| Region | PUMA Code    |
| :---:  |   :---:      |
| 1      | 35001        |
| 2      | 35002        |
| 3      | 35003, 35004 |
| 4      | 35005        |
| 5      | 35008, 35009 |
| 6      | 35007        |
| 7      | 35006        |

</div>

The industrial sectors are divided into 2 groups:
1. Commercial: classified by North American Industry Classification System (NAICS) 

<div align="center">

| Sector in Region $i$ <br> $(i = 1, 2, ..., 7)$ | NAICS Code                                           |
| :---:                                          |    :---:                                             |
| AG_MI_Ri                                       | 11, 21                                               |
| UTIL_Ri                                        | 22                                                   |
| CONS_Ri                                        | 23                                                   |
| MANU_Ri                                        | 31, 32, 33                                           |
| COMMER_Ri                                      | 42, 44, 45, 48, 49, <br> 51 - 56, 81 (excluding 813) |
| EDU_Ri                                         | 61                                                   |
| HEALTH_Ri                                      | 62                                                   |
| ART_ACC_Ri                                     | 71, 72                                               |
| RELIG_Ri                                       | 813                                                  |

</div>

2. Residential: HS1_Ri, HS2_Ri in Region $i$ $(i = 1, 2, ..., 7)$.

This model employs a production function with the property of constant elasticity of substitution.
<br/><br/>


## Outputs

After running the simulations, an output file "Salt_Lake_Results.csv" will be created. The first column from the left is the oder of the simulations, starting from zero. That is, the first simulation is labelled as zero, the second simulation is labelled as one, etc. 

In "Salt_Lake_Results.csv", there are five attributes: **DSC**, **DSR**, **MIG**, **EMP**, **HHINC**.

### **DSC**
**DSC** represents the difference of aggregate domestic supply in commercial sectors. It is the result of simulation value of aggregate domestic supply in commercial sectors (DSL) minus the initial value of aggregate domestic supply in commercial sectors (DS0). **DSC** is measured in millions of U.S. dollars.
- DSC $=$ DSL(commercial) $-$ DS0(commercial)

### **DSR**
**DSR** represents the difference of aggregate domestic supply in residential sectors. It is the result of simulation value of aggregate domestic supply in residential sectors (DSL) minus the initial value of aggregate domestic supply in residential sectors (DS0). **DSR** is measured in millions of U.S. dollars.
- DSR $=$ DSL(residential) $-$ DS0(residential)

### **MIG**
**MIG** shows the number of in-migration or out-migration. It is the result of simulation value of total households (HHL) minus the initial value of total households (HH0). Therefore, a positive number implies that households move into the region (in-migration), and a negative number implies that households leave the region (out-migration).
- MIG $=$ HHL $-$ HH0

### **EMP**
**EMP** represents the change in the number of employment. It is the result of simulation value of total employment (FDL) minus the initial value of total employment (FD0).
- EMP $=$ FDL(labor) $-$ FD0(labor)

### **HHINC**
**HHINC** represents the difference of aggregate household income. It is the result of simulation value of real aggregate household income (YL/CPIL) minus the initial value of aggregate household income. The simulation value of real aggregate household income is the simulation value of nominal aggregate household income (YL) divided by the simulation value of consumer price index (CPIL). **HHINC** is measured in millions of U.S. dollars.
- HHINC $=$ (YL/CPIL) $-$ Y0