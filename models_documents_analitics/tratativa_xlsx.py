import pandas as pd 

class TratativaXLSX:

    def __init__(self, nome_arquivo) -> None:
        df = pd.read_excel(nome_arquivo)
        print(df.head())