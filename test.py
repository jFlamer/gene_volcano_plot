import pandas as pd

df = pd.read_excel(r"data/NIHMS1635539-supplement-1635539_Sup_tab_4.xlsx", sheet_name="S4B limma results", skiprows=2)

print(df['adj.P.Val'])