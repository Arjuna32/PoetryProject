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

My implementations:
1. cli1: changes your desktop wallpaper
2. cli2: gets the weather for a city you input
3. cli3: converts US dollars to euros
4. cli4:generates a random password of 12 characters
5. cli5:displays the top news headlines


As a first step, run these commands to get the CLI up and started.

        cd cmsc475-202320-final-Arjuna32
        poetry install
        poetry shell  (or sometimes *poetry run pwsh* on windows, if necessary)
        pip install requests
        pip install forex-python



Here are some sample calls with the new CLI commands.

                        
        cli1 --image "C:\Users\amaan\OneDrive\Pictures\fgo shenanigans\mash wallpaper.jpg" 
        cli2 --city "London" 
        cli3 --usd 45.5 
        bigcli cli4 
        bigcli cli5 
        

