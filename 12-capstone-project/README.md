# Capstone project (#mlzoomcamp workshop 12)

[1. Problem statement](#1-problem-statement)
[2. Existing files & proceedings in this repository](#2-existing-files--proceedings-in-this-repository)
[3. Reproducibility](#3-reproducibility)
[4. Data source & literature](#4-data-source--literature)

## **Outline** 
> Develop an `early warning system` that allows climate data to be evaluated in real time, issuing the consequent warnings when conditions of high fire danger arise				
							
## 1. Problem statement

Although being developed for a specific dataset, it was explicitly formulated as part of the problem that the model and methodology should be exportable to new geographic and climatic conditions. \
A priority therefore is to obtain a model as generalizable as possible, this being the main difficulty, since we have highly skewed data and extreme outliers.

Once retrained to new geographic specific conditions, the data microserver must be able to evaluate given certain weather conditions:
- **effective fire potential**
- **level of severity according to a logarithmic scale** to generate an alarm in order to trigger the appropriate response 

## 2. Existing files & proceedings in this repository
- `README.md`
- `Pipfile`, `Pipfile.lock` 
- `notebook.ipynb`
- `train.py`, `predict.py`, `predict-test.py`  
- `Dockerfile`
- `water_probability.csv`
- `water1.bin`
- `cloud_deploy/`

Extensive exploratory data analysis (EDA) has been performed to understand the nature of the problem. In particular, an effort was made in order to determine the significance of a linear (baseline) model prior to any modeling attempts, including statistical testing for:
- linearity
- normality of the residuals
- homoscedasticity

All this was done with the purpose of establishing cause-effect relationships between the variables that would allow subsequent feature engineering. 

Read notebook.ipynb to access the full discussion. 

A k-neighbor predictor was chosen, because with equal accuracy in a low signal-to-noise context (high uncertainty, with likely hidden factors) it is at least a very light model and therefore optimal to be deployed.

## 3. Reproducibility
Please clone this repository and follow instructions below.


### **a) Deployment in local machine**

Once in the main folder, create a virtual environment with pipenv: \
(ideally you should have a python 3.8 interpreter installed for pipenv to make use)


    pipenv install

*Note: The list of requirements is specified in the Pipfile. But one can always use other tools to meet the same conditions.* \
Activate the pipenv shell, and run all subsequent code from within the created environment:

    pipenv shell

In order to create a docker image run: \
("capstone-p12" is here an arbitrary name for this exercise)

    docker build -t capstone-p12 .

Deploy the newly created docker image to your local machine:

    docker run --rm -d -p 8000:8000 capstone-p12

The service can be tested now by running:

    python predict-localtest.py

### **b) Cloud deployment**
For the purpose of this exercise, the service has been deployed to Heroku. \
Endpoint is available at this address:

Deployment to the cloud can be tested now by running:

    python predict-cloudtest.py

Should you need to reproduce the container deployment process on Heroku, please read the HEROKUAPP.md file in the "cloud-deploy/" folder

**NOTE:** \
The selected model to be deployed is included by default in this repository as pickle file (fire1.bin). \
If you want to generate the file again, run within the pipenv shell:

    python train.py


## 4. Data source & literature

The dataset is available from the UC Irvine machine learning repository, \
to download click [here](http://archive.ics.uci.edu/ml/datasets/Forest+Fires).

Reference to the original article: 

[Cortez and Morais, 2007] P. Cortez and A. Morais. A Data Mining Approach to Predict Forest Fires using Meteorological Data. In J. Neves, M. F. Santos and J. Machado Eds., New Trends in Artificial Intelligence, Proceedings of the 13th EPIA 2007 - Portuguese Conference on Artificial Intelligence, December, Guimarães, Portugal, pp. 512-523, 2007. APPIA, ISBN-13 978-989-95618-0-9. Available at: [http://www.dsi.uminho.pt/~pcortez/fires.pdf](http://www3.dsi.uminho.pt/pcortez/fires.pdf)
    
### Features description:

1. `X` >> x-axis spatial coordinate within the Montesinho park map: 1 to 9 
2. `Y` >> y-axis spatial coordinate within the Montesinho park map: 2 to 9 
3. `month` >> month of the year: 'jan' to 'dec' 
4. `day` >> day of the week: 'mon' to 'sun' 
5. `FFMC` >> FFMC index from the FWI system: 18.7 to 96.20 
6. `DMC` >> DMC index from the FWI system: 1.1 to 291.3 
7. `DC` >> DC index from the FWI system: 7.9 to 860.6 
8. `ISI` >> ISI index from the FWI system: 0.0 to 56.10 
9. `temp` >> temperature in Celsius degrees: 2.2 to 33.30 
10. `RH` >> relative humidity in %: 15.0 to 100 
11. `wind` >> wind speed in km/h: 0.40 to 9.40 
12. `rain` >> outside rain in mm/m2 : 0.0 to 6.4 
13. `area` >> burned area of the forest (in ha): 0.00 to 1090.84



