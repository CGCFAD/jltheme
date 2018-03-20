=======
jltheme
=======

Change Matplotlib rcParams to match the current JupyterLab theme.

Adjusts Matplotlib axis labels, edge, face, and tick colors based upon which JupyterLab theme is in use.

Installation
------------

::

    pip install theme_check
Usage
-----

The module provides one function, ``theme_check``, which opens the
JSON configuration file for JupyterLab, checks which theme is in use,
and changes Matplotlib rcParams to match the current theme::


Version history
---------------

-0.1.0 Initial Version (Current)