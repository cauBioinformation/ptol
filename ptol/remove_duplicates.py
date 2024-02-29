import pandas as pd

def run_remove_duplicates(args):

    file_path = args.inputFilePath

    df = pd.read_excel(file_path)

    df = df.dropna(subset=['DOI'])

    df = df.drop_duplicates(subset=['DOI'])

    output_file = args.outputFilePath

    df.to_csv(output_file, index=False, sep='\t', encoding='utf-8')

    # Made by Huilong Chen.

