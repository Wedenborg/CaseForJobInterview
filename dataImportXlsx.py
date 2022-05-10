import pandas as pd
def dataImportXlsx(file, sheet):
    #Load the data from the excel file with header = 0
    df = pd.read_excel(file, sheet_name = sheet,header = 0)
    cols = df.columns[0].split(",")
    data = df[df.columns[0]].str.split(',', expand=True)
    data.columns = cols
    return data