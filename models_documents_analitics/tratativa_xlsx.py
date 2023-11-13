import pandas as pd 

class TratativaXLSX:

    def __init__(self, archive_name) -> None:
        self.archive_name = archive_name
    
    def returning_data_xlsx(self):
        df = pd.read_excel(f'./data_temp/{self.archive_name}.xlsx')
        df.head() 
        return df.values