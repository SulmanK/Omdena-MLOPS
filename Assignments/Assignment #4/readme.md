
### Problem

Solar energy is a renewable energy source that depends on the irradiation data parameters to be efficient. Therefore, before investing in a new solar plant, it is necessary to gather the most solar data possible.
Acquisition of data

1) Process a "raw" satellite image of the location.

2) Use a collection of past satellite images at that location to create a "background"

3) Determine the cloud opacity - Decomposition of cloudy and cloud-free regions. Then, apply a 3D decomposition model to cloudy regions to characterize the thickness of each layer to sunlight.

4) Apply a modified version of the REST2 clear-sky radiation model, that allows us to use the latest global aerosol (dust, salt, smoke, etc.) and water vapor content to generate precise estimates of the solar radiation available to cloud-free regions.

### Purpose:

Using the data collected, we want to predict solar irradiance.


### Goals (+ Technologies used for each step)
* Complete data cleaning and feature engineering
	* Pandas
* Complete EDA
	* Matplotlib
	* Seaborn
* Complete model development
	* Sci-kit Learn
* Complete model validation
	* Sci-kit Learn
* Complete monitoring and automation lifecycle
	* Neptune
	* Mlflow
* Complete deployment
	* Heroku


### Contents:
dataset - contains the raw and cleaned dataset
model - dump files of the algorithms used for prediction + plots
notebook - Data cleaning, EDA, Model Dev, and Model Val notebooks
screenshots - Screenshots of Mlflow, Neptune, and Heroku deployment
solar-app - Deployed App on Heroku
