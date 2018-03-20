try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

console_scripts = ['jltheme = jltheme:_main']

setup(
    name='jltheme',
    version='0.1.1',
    description='Change Matplotlib rcParams to match the current JupyterLab theme.',
    long_description=open("README.rst", "r", encoding="utf-8").read().replace("`_", "`"),
    author='CGCFAD',
    author_email='cgcfad@protonmail.com',
    url='https://github.com/CGCFAD/jltheme',
    license='MIT',
    classifiers=[],
    py_modules=['jltheme'],
    entry_points={'console_scripts': console_scripts})
