Version:
-------

EGADS Lineage GUI 1.4.0 (Python 3).


Developments:
-------------

As the EUFAR project ended the 31st of January 2018, developments involving EGADS GUI are now done in a new branch and the current version of EGADS GUI is called EGADS Lineage GUI. It is developed and maintained by Olivier Henry and is not developed under the scope of EUFAR. Merging of the Master and Lineage branch can happen in the next EUFAR project.


Project Overview:
-----------------

EGADS (EUFAR General Airborne Data-processing Software) is a Python-based toolbox for processing airborne atmospheric data. EGADS provides a framework for researchers to apply expert-contributed algorithms to data files, and acts as a platform for data intercomparison. Algorithms in EGADS will be contributed by members of the EUFAR Expert Working Group if they are found to be mature and well-established in the scientific community.

EGADS GUI is a Python-based graphical user interface dedicated to EGADS. The project is still young, but it is stable and ready to be used in a production environment. 

EGADS and EGADS GUI are under development by EUFAR (European Facility for Airborne Research), an Integrating Activity funded by the European Commission. Specifically, the networking activity Standards & Protocols within EUFAR is responsible for development of toolbox, in addition to developing standards for use within the EUFAR community. A compilation of these standards and other Standards & Protocols products is available on the different Standards & Protocols webpages: 
* Standards & Protocols presentation: http://www.eufar.net/cms/standards-and-protocols/
* Standards & Protocols good practices: http://www.eufar.net/cms/good-practices/
* Standards & Protocols glossary: http://www.eufar.net/cms/glossary/
* Standards & Protocols tools: http://www.eufar.net/software-tools/list-matrix ; search for ASMM, EMC, EGADS-CORE and EGADS-GUI
  

More Information:
-----------------

Not yet.


Features:
---------

* read/write NetCDF files
* read/write Hdf5 files
* read/write NASA/Ames files
* use of algorithms
* creation of new algorithms
* display/plot/print data (time series and gridded data)
* batch processing
* export to KML/KMZ format (Google Earth)


Installation:
-------------

Actually, EGADS GUI is a simple python script. Just open a terminal in the EGADS GUI directory and launch the script as usual: python egads_gui.py.

Do not forget to install dependancies:
* Python (3.7 or newer)
* PyQt5 (5.15.0 or newer)
* EGADS Lineage (1.2.7 or newer)
* Matplotlib (3.3.0 or newer)
* Cartopy (0.18 or newer)
* Simplekml (1.3.5 or newer)
* Markdown (3.2.2 or newer, optional, only to read the changelog in the GUI)
* Requests (2.24.0 or newer, optional, only to check updates if the user activates the option)
* Pillow (7.2 or newer, optional, only to save figures in JPEG and TIFF format)

Anaconda3 can be a good alternative, in particular if the use of Cartopy is mandatory and if the user can't build Cartopy himself. For Windows, an already-built version of Cartopy exists at the followind address : https://www.lfd.uci.edu/~gohlke/pythonlibs/


Stand-alone package:
--------------------

Since version 1.0.0, a stand-alone package is available for those who wants to use the GUI without a Python installation. In that case, look for EGADS Lineage GUI STA in the release part of the repository.
For Windows (from Windows 7 32), donwload the .msi package and launch the installation, it should be installed outside ProgramFiles to avoid issues with admin rights, then the GUI can be run by double clicking on egads_gui.exe or from the shortcut in the Startup menu. A .zip package is also available for those who don’t want to install it.
For Linux (from Linux 5.3), download the tar.gz package somewhere on your hard drive (preferably in your home directory), extract it and run egads_gui.
The stand-alone versions for Linux and Windows have been created with PyInstaller, Windows 7 and Ubuntu 18.04.4.


Documentation:
--------------

The documentation of EGADS Lineage GUI is available as a PDF in the Documentation folder or on Read The Docs (https://egads-gui.readthedocs.io/en/lineage/).
