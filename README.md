# NYC AirBnB Analysis

## About this app

Welcome to our dashboard. The goal of this dashboard is to be able to analyze data from AirBnB accommodations. The intended end-user is an host that has accommodations listed on the AirBnB website.

## Requirements

* Python 3 (add it to your path (system variables) to make sure you can access it from the command prompt)
* Git (https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)

## How to run this app

We suggest you to create a virtual environment for running this app with Python 3. Clone this repository 
and open your terminal/command prompt in the root folder.


download a zip file of this folder, unzip it and copy it to a folder of choice on your computer

open a command prompt and run the following commands:

```
> cd <path to you folder of choice>\dashframework-main\dashframework-main 
> python -m venv venv

```
If python is not recognized use python3 instead

In Windows: 

```
> venv\Scripts\activate

```
In Unix system:
```
> source venv/bin/activate
```

(Instead of a python virtual environment you can also use an anaconda virtual environment.
 
Requirements:

• Anaconda (https://www.anaconda.com/) or Miniconda (https://docs.conda.io/en/latest/miniconda.html)

• The difference is that Anaconda has a user-friendly UI but requires a lot of space, and Miniconda is Command Prompt based, no UI, but requires considerably less space.

Then you should replace the lines: python -m venv venv and venv\Scripts\activate or source venv/bin/activate with the following:

```
> conda create -n yourenvname
> conda activate yourenvname
```
)

Install all required packages by running:
```
> pip install -r requirements.txt
```

Run this app locally with:
```
> python app.py
```
You will get a http link, open this in your browser to see the results. You can edit the code in any editor (e.g. Visual Studio Code) and if you save it you will see the results in the browser.

## Cleaning Process
Every action of cleaning is perfomed in the cleaning.py file. After cleaning the nan values and unnecessary attributes the dataset has been saved as a pickle file to avoid running the cleaning file every time. There's also some dataset exploration code (like descriptive statistics) at the end of the file. Codes in cleaning.py can be uncommented to see what changes have been made in the dataset.

## Important Files
menu.py: Makes the front-end of the dashboard 

scatterplot.py: Classes of visual encodings are created and stored here

data.py: imports the cleaned dataset from pickle file

main.py:

app.py: 
## Resources

* [Dash](https://dash.plot.ly/)
