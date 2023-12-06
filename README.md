# Diabetes Classification Models

  - author: Angela Chen, Ella Hein, Scout McKee, and Sharon Voon.

## About

This repository contains machine learning models for predicting whether an individaul has diabetes, developed as part of the DSCI 522 course. Our project explores various classification models, including logistic regression, k-nearest neighbors (k-NN), and decision trees. Through evaluation, we identified the decision tree with a `max_depth` of 5 as the most accurate model with general health factor (1 being excellent and 5 being poor) as the most important feature.

The project's primary goal is to predict diabetes using healthcare statistics, demographic information, and survey reponses. We utilized a dataset funded by the CDC to better understand the lifestyle-diabetes relationship in the US. The dataset, comprising 35 features for each patient, is available in the [UC Irvine Machine Learning Repository](https://archive.ics.uci.edu/dataset/891/cdc+diabetes+health+indicators). Each row in the dataset represent a person participating in this study for the year 2015.

## Report

For detailed insights and reults, refer to our [final report](https://ubc-mds.github.io/diabetes_classification_model/diabetes_classification_model_report.html).

## Usage

This analysis can be run with Docker or a virtual environment through the respective set-up instructions provided below.

### Initialization

1. Clone this GitHub repository using the command:
``` bash
git clone https://github.com/UBC-MDS/diabetes_classification_model.git
```

#### Method 1 - Using Docker:

1. Install Docker [here](https://www.docker.com/get-started/) and  follow the given instruction.
2. Launch  Docker on your local computer.
3. To replicate the analysis, run the following command from the root directory of this project:

``` bash
docker-compose run --rm jupyter make -C /home/jovyan/work all
```

4. To reset the repository to its original clean state, run the following command from the root directory of this project:

``` bash
docker-compose run --rm jupyter make -C /home/jovyan/work clean
```

#### Method 2 - Using Virtual Environment:

1. Run the following from the root directory of this project:
``` bash
conda env create --file environment.yaml
```

2. To activate the virtual environment:
``` bash
conda activate Diabetes_Prediction
```

3. To replicate the analysis, run the following command from the root directory of this project:
``` bash
make all
```

4. To reset the repository to its original clean state, run the following command from the root directory of this project:
``` bash
make clean
conda deactivate
conda remove --name Diabetes_Prediction --all
```

## Developer notes:

#### Running the tests

The test written for each function is stored in the tests folder. To run the tests, using `pytest` command from the root of this repository:

More details about the test suite can be found in the 
[`tests`](tests) directory.

## Dependencies

This project relies on Docker image that is built on quay.io/jupyter/minimal-notebook:2023-11-19. Additional dependencies can be found in the [DockerFile](Dockerfile).

 - pandas=2.1.3
 - altair=5.1.2
 - scikit-learn=1.3.2
 - vegafusion=1.4.5
 - vegafusion-python-embed=1.4.5
 - vl-convert-python==1.1.0
 - pip install pytest==7.4.3
 - ucimlrepo==0.0.3
 - myst-nb==1.0.0
 - click=8.1.7
 - jupyter-book=0.15.1
 - GNU make 4.2.1

## License

The Diabetes Prediction materials here are licensed under the Creative Commons Attribution-NonCommercial-NoDerivs 4.0 International (CC BY-NC-ND 4.0 DEED) and the MIT license. If re-used/re-mixed please provide attribution and link to this webpage.

## Contributing

Contributions are always welcome but please do refer to [CONTRIBUTING.md](CONTRIBUTING.md) for more details.

## References

Centers for Disease Control and Prevention. (2014). CDC Diabetes Health 
Indicators. University of California, Irvine, School of Information; 
Computer Sciences. Retrieved November 14, 2023, from 
https://archive.ics.uci.edu/dataset/891/cdc+diabetes+health+indicators

Sapra, A., & Bhandari, P. (2023, June 21). Diabetes. In StatPearls [Internet].
Treasure Island (FL): StatPearls Publishing. Available from: 
https://www.ncbi.nlm.nih.gov/books/NBK551501/

VanderPlas, J., Granger, B., Heer, J., Moritz, D., Wongsuphasawat,
K., Satyanarayan, A., ... Sievert, S. (2018). Altair: Interactive statistical
visualizations for Python. Journal of Open Source Software, 3(32), 1057.

Pedregosa, F., et al. (2011). Scikit-learn: Machine Learning in Python.
Journal of Machine Learning Research, 12, 2825-2830.

McKinney, W. (2010). Data structures for statistical computing in Python.
Proceedings of the 9th Python in Science Conference, Volume 445.
