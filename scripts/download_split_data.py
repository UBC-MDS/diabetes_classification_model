from ucimlrepo import fetch_ucirepo
from sklearn.model_selection import train_test_split
import click
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

@click.command()
@click.option('--id', type=int, help='UCI repository ID') 
@click.option('--write-to', type=str, help='Path to directory where raw data will be stored in')
@click.option('--random', type=int, help="Random seed", default=123)
@click.option('--split-data-to', type=str, help="Path to directory where split data will be stored")
@click.option('--split-ratio',type=float, help="Ratio used to split data into test data")

def main(id,write_to, random, split_data_to, split_ratio):
    """Download data from uci repo to local filepath and split it into 
    train and test data after dropping duplicate rows"""

    #Reading diabetes raw data from uci repository
    cdc_diabetes_health_indicators = fetch_ucirepo(id=id)
    diabetes_data = cdc_diabetes_health_indicators.data.original
    diabetes_data.set_index("ID",inplace=True)

    #Outputting raw data into data/raw folder
    diabetes_data.to_csv(os.path.join(write_to,"diabetes_raw.csv"))

    #Dropping duplicate rows in raw data
    diabetes_data.drop_duplicates(inplace=True)

    #Splitting raw data into train and test data
    train_df, test_df = train_test_split(diabetes_data, 
                                     test_size = split_ratio, 
                                     random_state=random)
    
    #Outputting train data and test data into data/processed folder
    train_df.to_csv(os.path.join(split_data_to,"train_df.csv"))
    test_df.to_csv(os.path.join(split_data_to,"test_df.csv"))

if __name__ == '__main__':
    main()