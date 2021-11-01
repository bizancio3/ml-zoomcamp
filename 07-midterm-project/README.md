**Outline (project purpose):** \
To deploy a machine learning model as web microservice to determine whether water is safe to drink based on a physicochemical analysis

## 0. Contents of this repository
- README.md
- Pipfile, Pipfile.lock 
- notebook.ipynb
- train.py, predict.py, predict-localtest.py  
- Dockerfile
- catboost_info/ (directory with Catboost log files)

**Important remarks:** \
a) notebook.ipynb describes DEA and modeling process b) Run "pipenv install" to create virtual environment c) Run "pipenv shell" to activate d) Run "python train.py" to generate binary water1.bin e) Run "docker build -t midterm-p7 ." to create docker image f) Run "docker run --rm -d -p 8000:8000" to deploy service on local machine g) Run "python predict-localtest.py" for testing on localhost:8000
  

## 1. Use case motivation
**How the solution could be used?** \
Features included in the dataset are quite basic analytic parameters, not liable to complex procedures.
The data product described above could prove to be very useful to get a quick evaluation of water potability, could potentially be deployed to edge devices to evaluate water samples on site 
<br />

**Problem statement** 
> ### Can we conclude based on basic analytics whether a sample is safe to drink? (level of potability)

## 2. Source
`water_potability.csv` - contains water quality metrics for 3276 different water bodies

Dataset source: \
https://www.kaggle.com/adityakadiwal/water-potability

## 3. Predictors (brief description)

**1. `pH value`:**

PH is evaluating the acid–base balance of water. \
WHO recommends a pH interval from 6.5 to 8.5. All current samples are in theory conforming WHO standards regarding pH

**2. `Hardness`:**

Hardness is caused by calcium and magnesium salts. These are dissolved from geologic deposits through which water travels. Hardness was originally defined as the capacity of water to precipitate soap caused by calcium and magnesium

**3. `Solids`:**

Water has the ability to dissolve a wide range of inorganic and some organic minerals or salts such as potassium, calcium, sodium, bicarbonates, chlorides, magnesium, sulfates etc. Desirable limit for TDS is 500 mg/l and maximum limit is 1000 mg/l which prescribed for drinking purpose

**4. `Chloramines`:**

Chlorine and chloramine are the major disinfectants used in public water systems. Chloramines are most commonly formed when ammonia is added to chlorine to treat drinking water. Chlorine levels up to 4 milligrams per liter (mg/L or 4 parts per million (ppm)) are considered safe in drinking water

**5. `Sulfate`:**

Sulfates are naturally occurring substances that are found in minerals, soil, and rocks. They are present in ambient air, groundwater, plants, and food. It ranges from 3 to 30 mg/L in most freshwater supplies, although much higher concentrations (1000 mg/L) are found in some geographic locations

**6. `Conductivity`:**

Increase in ions concentration enhances the electrical conductivity of water. Electrical conductivity (EC) actually measures the ionic process of a solution that enables it to transmit current. According to WHO standards, EC value should not exceeded 400 μS/cm

**7. `Organic_carbon`:**

Total Organic Carbon (TOC) in waters comes from decaying natural organic matter (NOM) as well as synthetic sources. TOC is a measure of the total amount of carbon in organic compounds in pure water. \ According to US EPA < 2 mg/L as TOC in treated / drinking water, and < 4 mg/Lit in source water which is use for treatment

**8. `Trihalomethanes`:**

THMs are chemicals which may be found in water treated with chlorine. The concentration of THMs in drinking water varies according to the amount of chlorine required to treat the water, and the temperature of the water that is being treated. \
THM levels up to 80 ppm is considered safe in drinking water.

**9. `Turbidity`:**

The turbidity of water depends on the quantity of solid matter present in the suspended state. It is a measure of light emitting properties of water and the test is used to indicate the quality of waste discharge with respect to colloidal matter

   
