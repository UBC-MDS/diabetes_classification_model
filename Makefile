# diabetes classification pipe
# authors: Angela Chen, Ella Hein, Scout Mckee, Sharon Voon
# date: 2023-12-06

# Compare optimized k-nn and decision tree models with logistic regression.

data/raw/wdbc.feather: src/download_data.py
	python src/download_data.py --out_type=feather --url=http://mlr.cs.umass.edu/ml/machine-learning-databases/breast-cancer-wisconsin/wdbc.data --out_file=data/raw/wdbc.feather

# Compare optimized k-nn and decision tree models with logistic regression. 
results/tables/model_comparison_results.csv results/tables/feature_importances.csv : src/model_comparison.py
	python src/download_data.py \
	--training_data=data/processed/train_df.csv \
	--preprocessor=results/models/diabetes_preprocessor.pickle \
	--optimized_knn=results/models/knn_pipeline.pickle \
	--optimized_tree=results/models/tree_model.pickle \
	--table_to=results/tables






