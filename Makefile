# Makefile
# Diabetic classification data pipe
# Angela Chen, Ella Hein, Scout McKee, and Sharon Voon. 2023 Dec
# Adapted from Tiffany Timbers

#INSERT A DETSILED DESCRIPTION HERE ABOUT OUR WHOLE PROCESS AFTER WE WRAP UP :)


all: report/_build/html/index.html

# Download, drop duplicate and split data into train and test data frame
data/raw/diabetes_raw.csv data/processed/train_df.csv data/processed/test_df.csv : scripts/download_split_data.py
	python scripts/download_split_data.py \
	--id=891 \
	--write-to=data/raw \
	--random=123 \
	--split-data-to=data/processed \
	--split-ratio=0.35

# Perform preprocessing train data, EDA, and save plot and results.
results/models/diabetes_preprocessor.pickle results/figures/feature_histogram_by_class.png : data/processed/train_df.csv scripts/eda.py
	python scripts/eda.py \
	--train-data=data/processed/train_df.csv \
	--preprocessor-to=results/models \
	--fig-to=results/figures \
	--table-to=results/tables

# # Perform hyperparameter optimization and get the hyperparameters of the optimal models. 
results/models/tree_model.pickle results/models/knn_pipeline.pickle results/tables/best_hyperparams.csv : scripts/hyperparam_optimization.py data/processed/train_df.csv results/models/diabetes_preprocessor.pickle
	python scripts/hyperparam_optimization.py \
	--training_data=data/processed/train_df.csv \
	--preprocessor=results/models/diabetes_preprocessor.pickle \
	--models_to=results/models \
	--table_to=results/tables

# Compare optimized k-nn and decision tree models with logistic regression. 
results/tables/model_comparison_results.csv results/tables/feature_importances.csv : scripts/model_comparison.py
	python scripts/model_comparison.py \
	--training_data=data/processed/train_df.csv \
	--preprocessor=results/models/diabetes_preprocessor.pickle \
	--optimized_knn=results/models/knn_pipeline.pickle \
	--optimized_tree=results/models/tree_model.pickle \
	--table_to=results/tables

# Evaluation and scoring of the model.
results/tables/confusion_matrix_knn.csv results/tables/confusion_matrix_DT.csv : data/processed/train_df.csv \
data/processed/test_df.csv results/models/knn_pipeline.pickle results/models/tree_model.pickle scripts/evaluate_diabetes_classifier.py
	python scripts/evaluate_diabetes_classifier.py \
	--train_df=data/processed/train_df.csv \
	--test_df=data/processed/test_df.csv \
	--knn_from=results/models/knn_pipeline.pickle \
	--dt_from=results/models/tree_model.pickle \
	--results_to=results/tables


# write the report
report/_build/html/index.html : report/diabetes_classification_model_report.ipynb \
report/_toc.yml \
report/_config.yml \
results/figures/feature_histogram_by_class.png \
results/models/diabetes_preprocessor.pickle \
results/models/tree_model.pickle \
results/models/knn_pipeline.pickle \
results/tables/best_hyperparams.csv \
results/tables/model_comparison_results.csv \
results/tables/feature_importances.csv \
results/tables/confusion_matrix_knn.csv \
results/tables/confusion_matrix_DT.csv
	jupyter-book build report


# Cleaning up resources
clean:
	rm -f data/processed/*.csv
	rm -f data/data/*.csv
	rm -f results/tables/*.csv
	rm -f results/processed/*.csv
	rm -f results/figures/feature_histogram_by_class.png
	rm -f results/models/*.pickle
	rm -f report/_build/html/index.html


