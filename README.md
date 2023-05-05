# CMSC 475 - Spring 2023 - Final project

Welcome to the final project! This repo contains two working CLIs and will serve as a starting point for your final project.

The project assumes that you've got PYENV, PYTHON and POETRY installed.

See the final project assignment for more details:

<https://lowkeylabs.github.io/cmsc475-202320-materials/finalproject.html>

Before you get started, you should verify:

1. pyenv --version
1. python --version
1. poetry --version

Some of you are using conda and other python development environments. That is OK, too. My autograder will be using poetry, so if you use something different, please provide documentation in your README on how to build and run the code in your virtual environment.

As a first step, run these commands to get the CLI up and started.

        cd cmsc475-202320-final-Arjuna32
        poetry install
        poetry shell  (or sometimes *poetry run pwsh* on windows, if necessary)
        pip install requests
        pip install forex-python



Using poetry you can also create a Wheel and then install the cli into your machine on the path.


        poetry build
        cd dist
        pip install cms475-202320-final-0.1.0-py3-none-any.whl

Look in the *./dist* folder to get the actual name of the wheel you created.
