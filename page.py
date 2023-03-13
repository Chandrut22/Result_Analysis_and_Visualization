import tabula
import pandas as pd
import numpy as np


def process_pdf(file,str_page,end_page):
    data = pd.DataFrame()
    for i in range (str_page,end_page+1):
       df = tabula.read_pdf(file,pages=i)[0]
       col = list(df.columns)
       df.rename(columns={col[0]:"Unnamed"},inplace = True)
       data = pd.concat([data,df],ignore_index=True)
    data.columns = data.iloc[0]
    data.drop(1,inplace=True)
    data.rename(columns = {data.columns[0]:'Reg.Number','Subject Code - >':'Stud.Name'},inplace=True)
    data.drop(0,inplace=True)
    data.reset_index(drop=True, inplace=True)
    data.replace(np.nan,1,inplace=True)
    data.replace('O',10,inplace=True)
    data.replace('A+',9,inplace=True)
    data.replace('A',8,inplace=True)
    data.replace('B+',7,inplace=True)
    data.replace('B',6,inplace=True)
    data.replace('C',5,inplace=True)
    data.replace('U',0,inplace=True)
    data['Reg.Number'] = data['Reg.Number'].apply(pd.to_numeric)
    data.to_csv('Student_Result.csv', encoding='utf-8')
    #data.to_excel('Student_Result.xlsx', encoding='utf-8')
    return data