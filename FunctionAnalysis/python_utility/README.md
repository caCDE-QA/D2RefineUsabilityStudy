D2Refine Usability Study - Python Utility
=========================================

Instructions to calculate Functional coverage ratios for the three environments:

## Pre-requisites:

- [Python](https://www.python.org/) installed and configured properly.  
- Python `pip` is recommeded to install Python packages. Python 2.7.9 and later versions include `pip`.
- [MatPlot Lib](https://matplotlib.org/) should be installed. It can be installed using `pip` - `pip install matplotlib`.
- [Pallet](https://github.com/stardog-union/pellet/releases) reasoner. Download the archive and unzip in a directory to install.
- Edit the python script file `main.py`:
  - Replace all strings `<PATH_TO_PALLET_REASONER_INSTALL_DIRECTORY>` with the install directory path (where Pallet reasoner files from it's archive were extracted).
  - Replace `<PATH_TO_WORK_DOMAIN_ONTOLOGY>` with the location of the [___Work Domain Ontology___](https://github.com/caCDE-QA/D2RefineUsabilityStudy/blob/master/FunctionAnalysis/WorkDomainOntology.owl).

## Usage:
`python main.py`

## Output:

- The files in sub-folder `data` would be updated with domain function saturation numbers.
- The images of Venn diagrams would be updated in sub-folder `figures`
