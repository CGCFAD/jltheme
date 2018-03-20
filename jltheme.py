import json
from matplotlib import rcParams
import os


def jltheme():
    homedir = os.path.expanduser('~')
    try:
        from win32com.shell import shellcon, shell

        homedir = shell.SHGetFolderPath(0, shellcon.CSIDL_APPDATA, 0, 0)

    except ImportError:
        homedir = os.path.expanduser("~")
    try:
        with open(
                        homedir + r'\.jupyter\lab\user-settings\@jupyterlab\apputils-extension\themes.jupyterlab-settings') as json_data:
            theme = json.load(json_data)
            theme = theme['theme']
            if theme == 'JupyterLab Dark':
                rcParams['axes.edgecolor'] = 'white'
                rcParams['axes.labelcolor'] = 'white'
                rcParams['xtick.color'] = 'white'
                rcParams['ytick.color'] = 'white'
                rcParams['text.color'] = 'white'
                rcParams['axes.facecolor'] = '#111111'
    except OSError:
        with open(
                        homedir + r'/.jupyter/lab/user-settings/@jupyterlab/apputils-extension/themes.jupyterlab-settings') as json_data:
            theme = json.load(json_data)
            theme = theme['theme']
            if theme == 'JupyterLab Dark':
                rcParams['axes.edgecolor'] = 'white'
                rcParams['axes.labelcolor'] = 'white'
                rcParams['xtick.color'] = 'white'
                rcParams['ytick.color'] = 'white'
                rcParams['text.color'] = 'white'
                rcParams['axes.facecolor'] = '#111111'
