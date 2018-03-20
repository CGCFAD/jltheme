try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

console_scripts = ['jltheme = jltheme:_main']

setup(name='jltheme',
      version='0.1.0',
      description='Change Matplotlib rcParams to match the current JupyterLab theme. Adjusts Matplotlib axis label, '
                  'edge, face, and tick colors based upon which JupyterLab theme is in use.',
      long_description=open("README.rst", "r", encoding="utf-8").read().replace("`_", "`"),
      author='CGCFAD',
      author_email='cgcfad@protonmail.com',
      url='https://github.com/CGCFAD/theme_check',
      license='MIT',
      classifiers=["Development Status :: 4 - Beta",
                   "License :: MIT License",
                   "Operating System :: OS Independent",
                   "Programming Language :: Python :: 2",
                   "Programming Language :: Python :: 2.7",
                   "Programming Language :: Python :: 3.3",
                   "Programming Language :: Python :: 3.4",
                   "Programming Language :: Python :: 3",
                   "Programming Language :: Python :: 3.5",
                   "Programming Language :: Python :: 3.6",
                   "Topic :: Software Development :: Libraries"],
      py_modules=['jltheme'],
      entry_points={'console_scripts': console_scripts})
