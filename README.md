# AlbumGAN

## I'm Proud Of You
You actually came to read the readme, proud of you! Reading is hard, but so is life.

## Quick Start Guide
Python is an absolute nightmare to manage and I have some opinions on it. I am thinking the local version of this app we play around in should use pyenv and pipenv.

### [Pyenv](https://github.com/pyenv/pyenv)
Manages your path for you to point to version of python, because Macs already have python, and it's old.

### [Pipenv](https://pipenv.pypa.io/en/latest/)
Manages virtual environments for your python project. Kinda like npm, but also manages your node version (which in this case is python).

### How to actually start quick
Install Pyenv and Pipenv (use the links above), navigate to the directory and type `pipenv shell` to start the virtual environment and then install all deps using `pipenv install`.

### Run scripts
`pythin main.py` from root project folder

Make copies of any `config/*.template files` and create a .json file extension version with your actual credientials. This will be git ignored.
