import pandas as pd

file1="//ZHLEVRPADW022/RPA_Projeler/BtypReport/IstekListesi1.xlsx"
file2="//ZHLEVRPADW022/RPA_Projeler/BtypReport/IstekListesi2.xlsx"
file3="//ZHLEVRPADW022/RPA_Projeler/BtypReport/IstekListesi3.xlsx"
file4="//ZHLEVRPADW022/RPA_Projeler/BtypReport/IstekListesi4.xlsx"
file5="//ZHLEVRPADW022/RPA_Projeler/BtypReport/IstekListesi5.xlsx"



df1=pd.read_excel(file1, header=None)
df2=pd.read_excel(file2, header=None)
df3=pd.read_excel(file3, header=None)
df4=pd.read_excel(file4, header=None)
df5=pd.read_excel(file5, header=None)

df1=df1.drop(range(6))
df2=df2.drop(range(7))
df3=df3.drop(range(7))
df4=df4.drop(range(7))
df5=df5.drop(range(7))


birlesik_df=pd.concat([df1,df2,df3,df4,df5], axis=0)
birlesik_df=birlesik_df.iloc[1:]
#birlesik_df=birlesik_df.drop(birlesik_df.index[0])
birlesik_df.to_excel("//ZHLEVRPADW022/RPA_Projeler/BtypReport/Concatenated_file.xlsx", index=False, header=False)

