import pandas as pd
import os

def get_dataframe(file_path, sep):
    
    return pd.read_csv(
        file_path,
        sep=sep,
        names=['word', 'qtd'])



if __name__ == '__main__':

    base_path = './data'
    
    files = os.listdir(base_path)
    
    part_files = list(filter(lambda x: True if 'part' in x else False, files))
    part_files = list(map(lambda x: f'{base_path}/{x}', part_files))
    
    dataframes = [get_dataframe(part_file, "\t") for part_file in part_files]

    df_concat = pd.concat(dataframes)

    sorted_df = df_concat.sort_values(by='qtd', ascending=False)
    sorted_df.to_excel('sorted_df.xlsx', index = False)
