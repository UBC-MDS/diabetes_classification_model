import click
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from sklearn.compose import make_column_transformer
from sklearn.preprocessing import StandardScaler
from sklearn import set_config
import pandas as pd
import pickle
from src.count_null import count_null
import altair as alt
alt.data_transformers.enable("vegafusion")


@click.command()
@click.option('--train-data', type=str, help="Path to train data")
@click.option('--preprocessor-to', type=str, help="Path to directory where the preprocessor object will be stored")
@click.option('--fig-to', type=str, help="Path to directory where figure will be stored")
@click.option('--table-to', type=str, help="Path to directory where tables will be stored")
def main(train_data,preprocessor_to, fig_to, table_to):
    """Preprocessed the train dataframe and carries out exploratory data analysis. Plot histogram distribution of 
    all numeric features in the train data and display them as grid of plots. Plot is save in the result/figures 
    folder.
    """

    #Read in train data
    train_data = pd.read_csv(train_data)
    train_data.set_index("ID",inplace=True)

    #EDA - describing train data
    train_info = pd.DataFrame(train_data.describe())
    train_info.to_csv(os.path.join(table_to,"train_describe.csv"))

    #EDA - checking for null values in train data
    train_null = count_null(train_data)
    train_null.to_csv(os.path.join(table_to,"train_null.csv"))

    #Preprocessor for features
    continuous_cols = ['BMI', 'Age', 'GenHlth', 'MentHlth',
                   'PhysHlth', 'Education', 'Income']

    diabetes_preprocessor = make_column_transformer(
        (StandardScaler(), continuous_cols),
        remainder='passthrough',
        verbose_feature_names_out=False
    )

    #Output preprocessor.pickle file
    set_config(transform_output="pandas")
    pickle.dump(diabetes_preprocessor, open(os.path.join(preprocessor_to,"diabetes_preprocessor.pickle"),"wb"))

    #Transforming train data for plotting to avoid scaling bias
    scaled_train=diabetes_preprocessor.fit_transform(train_data)

    #Plotting histogram distributions of each features
    numeric_cols = diabetes_preprocessor.get_feature_names_out()
    fig = alt.Chart(scaled_train).mark_bar(opacity=0.7).encode(
            x=alt.X(alt.repeat()).type('quantitative'). 
                    bin(maxbins=16),
            y=alt.Y('count()').stack(False),
            color=alt.Color('Diabetes_binary:N')
        ).properties(
            width=100,
            height=100
        ).repeat(
            numeric_cols,
            columns=4
        )

    #Saving plot to result folder
    fig.save(os.path.join(fig_to,"feature_histogram_by_class.png"))

if __name__ == '__main__':
    main()
