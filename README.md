# Diabetes Classification Models

  - author: Angela Chen, Ella Hein, Scout McKee, and Sharon Voon.

## About

This repository contains machine learning models for predicting whether an individual has diabetes, developed as part of the DSCI 522 course. Our project explores various classification models, including logistic regression, k-nearest neighbors (k-NN), and decision trees. Through evaluation, we identified the decision tree with a `max_depth` of 5 as the most accurate model with general health factor (1 being excellent and 5 being poor) as the most important feature.

The project's primary goal is to predict diabetes using healthcare statistics, demographic information, and survey reponses. We utilized a dataset funded by the CDC to better understand the lifestyle-diabetes relationship in the US. The dataset, comprising 35 features for each patient, is available in the [UC Irvine Machine Learning Repository](https://archive.ics.uci.edu/dataset/891/cdc+diabetes+health+indicators). Each row in the dataset represents a person participating in this study for the year 2015.

## Report

For detailed insights and results, refer to our [final report](https://ubc-mds.github.io/diabetes_classification_model/diabetes_classification_model_report.html).

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
docker-compose run --rm jupyter make all
```

4. To reset the repository to its original clean state, run the following command from the root directory of this project:

``` bash
docker-compose run --rm jupyter make clean
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

### Working with the project using Jupyter lab

1. Run the following from the root directory of this project:
``` bash
docker compose up jupyter
```

2. Click on the link provided in the terminal that starts with `http://127.0.0.1:8888/lab` or copy and paste it into your web browser.

3. Jupyter Lab IDE should open up in your browser. Navigate into the `work` folder and you can find all project files located on the left side of the panel.

4. Run the following command from terminal after typing `Ctrl + C` to shut down the container and free up the resources:
``` bash
docker compose rm -f
```

### Running the tests

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
 - myst-nb==0.17.2
 - click=8.1.7
 - jupyter-book=0.15.1
 - make=4.3

 ### Adding new dependency
1. Switch to a new branch and add the dependency to the [Dockerfile](Docker).
2. Run the following command from the root directory of this project to ensure the Docker image build properly:
```bash
docker build --tag test .
```
3. Commit and push the changes to GitHub. This repository have an action workflow setup such that new Docker image will be built and pushed to Docker Hub automatically. This `docker-compose.yml` is set up to use the latest Docker image available on the Docker Hub.
4. Send a pull request to merge the changes into the `main` branch.

## License

The Diabetes Prediction materials here are licensed under the Creative Commons Attribution-NonCommercial-NoDerivs 4.0 International (CC BY-NC-ND 4.0 DEED) and the MIT license. If re-used/re-mixed please provide attribution and link to this webpage.

## Contributing

Contributions are always welcome but please do refer to [CONTRIBUTING.md](CONTRIBUTING.md) for more details.

## References

Nilka Rios Burrows, Israel Hora, Linda S Geiss, Edward W Gregg, and Ann Albright. Incidence of end-stage renal disease attributed to diabetes among persons with diagnosed diabetes—united states and puerto rico, 2000–2014. Morbidity and Mortality Weekly Report, 66(43):1165, 2017. URL: https://pubmed.ncbi.nlm.nih.gov/29095800/, doi:10.15585/mmwr.mm6643a2.

Fabian Pedregosa, Gaël Varoquaux, Alexandre Gramfort, Vincent Michel, Bertrand Thirion, Olivier Grisel, Mathieu Blondel, Peter Prettenhofer, Ron Weiss, Vincent Dubourg, and others. Scikit-learn: machine learning in python. the Journal of machine Learning research, 12:2825–2830, 2011. doi:10.5555/1953048.2078195.

A. Sapra and P. Bhandari. Diabetes. 2023. [Updated 2023 Jun 21]. In: StatPearls [Internet]. Treasure Island (FL): StatPearls Publishing; 2023 Jan-. URL: https://www.ncbi.nlm.nih.gov/books/NBK551501/.

Jacob VanderPlas, Brian Granger, Jeffrey Heer, Dominik Moritz, Kanit Wongsuphasawat, Arvind Satyanarayan, Eitan Lees, Ilia Timofeev, Ben Welsh, and Scott Sievert. Altair: interactive statistical visualizations for python. Journal of open source software, 3(32):1057, 2018. URL: https://joss.theoj.org/papers/10.21105/joss.01057, doi:10.21105/joss.01057.

Wes McKinney. Data Structures for Statistical Computing in Python. In Stéfan van der Walt and Jarrod Millman, editors, Proceedings of the 9th Python in Science Conference, 56 – 61. 2010. doi:10.25080/Majora-92bf1922-00a.
