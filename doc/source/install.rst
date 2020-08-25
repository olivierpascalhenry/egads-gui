=============
Installation
=============

The latest version of the EGADS GUI can be obtained from https://github.com/EUFAR/egads-gui/tree/Lineage and from https://github.com/EUFAR/egads-gui/releases for the Stand-alone version (look for the EGADS Lineage GUI STA System vX.X.X package, STA means stand-alone).


*************
Prerequisites
*************

The use of the EGADS GUI as a standard Python script requires the following packages:

* Python 3.7 or newer. Available at https://www.python.org/
* PyQt 5.15 or newer. Available at https://www.riverbankcomputing.com/software/pyqt/download5
* EGADS Lineage 1.2.7 or newer. Available at https://pypi.python.org/pypi/egads
* Matplotlib 3.3 or newer. Available at https://pypi.python.org/pypi/matplotlib
* Cartopy 0.18 or newer. Available at https://pypi.org/project/Cartopy/
* Simplekml 1.3.5 or newer. Available at https://pypi.org/project/simplekml/
* Requests 2.24 or newer. Optional, only for update checking. Available at https://pypi.org/project/requests/
* Markdown 3.2.2 or newer. Optional, only to have a nice changelog in the GUI. Available at https://pypi.org/project/Markdown/
* Pillow 7.2 or newer. Optional, only to save figures in JPEG and TIFF format. Available at https://pypi.org/project/Pillow/


*************
Compatibility
*************

The EGADS GUI has been tested on Linux and Windows. Even if it has not been tested on MacOS, it should be compatible with the OS made by Apple.


************
Installation
************

The EGADS GUI is actually available as a common Python script, thus it doesn't need any particular installation. To use it, the package must be downloaded and uncompressed somewhere on the hard drive, and the script executed with the usual command ``python egads_gui.py`` from a terminal launched in the EGADS GUI directory. This version can be executed on any version of Linux, Windows and MacOS as soon as prerequisites are installed and working.

To learn how to install EGADS, please read the EGADS documentation available at the following places: https://github.com/EUFAR/egads/tree/Lineage/Documentation & https://egads.readthedocs.io/en/lineage/

Anaconda3 can be a good alternative, in particular if the use of Cartopy is mandatory and if the user can't build Cartopy himself. For Windows, an already-built version of Cartopy exists at the followind address : https://www.lfd.uci.edu/~gohlke/pythonlibs/.


***********
Stand-alone
***********

Since version 1.0.0, a stand-alone package is available for those who wants to use the GUI without a Python installation. In that case, look for ``EGADS Lineage GUI STA`` in the release part of the repository. For Windows (from Windows 7 32), donwload the .msi package and launch the installation, it should be installed outside ProgramFiles to avoid issues with admin rights, then the GUI can be run by double clicking on egads_gui.exe or from the shortcut in the Startup menu. A .zip package is also available for those who don't want to install it. For Linux (from Linux 4.15), download the tar.gz package somewhere on your hard drive (preferably in your home directory), extract it and run egads_gui.
The stand-alone versions for Linux and Windows have been created with PyInstaller, Windows 7 and Ubuntu 18.04.


*******
Testing
*******

No test system has been introduced at this time.


*******
Options
*******

Since version 0.10.0, an .ini file has been added to EGADS GUI to welcome few options: log level and path, automatic check for a new EGADS GUI version on GitHub, and few other options. If the file is not present in EGADS GUI directory, when importing, EGADS GUI will create it automatically with default options. The modification of the file is made through the option window of the GUI. Since version 0.13.0, the GUI can control the EGADS options. Information about each option in the Option window of the GUI is available through info buttons.


***
Log
***

A logging system has been integrated in the EGADS GUI since the version 0.7.0. By default, the output file is available in the GUI directory and the logging level has been set to DEBUG. Options for logging level and location are set in a config_file ``egads_gui.ini`` and can be change directly through the Option window in the GUI.

Actual options to control the logging system are for now:

* ``level``: the logging level ( ``DEBUG``, ``INFO``, ``WARNING``, ``CRITICAL``, ``ERROR`` ).
* ``path``: the path of the file containing all logs.

The GUI has to be restarted to take into account the new path and new log level.


******
Update
******
Since version 0.11.0, EGADS GUI can check for an update on GitHub. The check system is launched in a separate thread and can run automatically at each startup if the option to do so has been set accordingly. To install the update, the user has to follow the install instructions found in actual document. The module Requests is optional for EGADS GUI but is mandatory to check for an update.

In the Stand-alone version, the update system can check for an update automatically at startup or manually any time, and if an update is available, it can be downloaded and installed automatically.
