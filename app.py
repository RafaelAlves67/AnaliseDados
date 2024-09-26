import pandas as pd
import pyodbc


#credenciais no banco
username=''
password=''
server=''
database='' 

# parametros da query 
data_inicial = '2024-09-01'
data_final = '2024-09-05' 
empresa = 3


db = pyodbc.connect(f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}')
print("Banco de dados SQL SERVER CONECTADO.") 

query = """
SELECT 
CASE 
	WHEN FU_ES_COD_EMPRESA = 2 THEN 'Zammi'
	WHEN FU_ES_COD_EMPRESA = 3 THEN 'Labcor'
END as 'Empresa',
FU_MATRICULA as 'Número da matricula', 
PE_NOME as 'Nome Funcionário', 
 Convert(char(40), CA.CAR_NOME) as 'Cargo',
FU_ADMISSAO as 'Data Admissão',
FU_SALARIO as 'Salário'

FROM FO_FUNCIONARIO FU 
LEFT JOIN FO_CARGO CA with (nolock) on CA.CAC_CODIGO = FU_CAC_CODIGO
WHERE FU_DT_DEMISSAO is NULL
and (FU_ES_COD_EMPRESA = 2 or FU_ES_COD_EMPRESA = 3)  
ORDER BY PE_NOME asc  
 """

df_func = pd.read_sql(query, db)

#media salarial
df_func["Salário"].mean() 

# quantos funcionarios labcor 
df_func[df_func["Empresa"] == 'Labcor'].count()

# 205 funcionários ativos Labcor
# 286 funcionários ativos Zammi
# media salario: 2440 
# salario maximo: 12802 RAFAEL DA SILVA REBELLO	
# salario minimo:  1180 ADNAN 
# cargos com mais pessoas = Auxiliar de produção (87 pessoas) 

# limpas dados 
# removendo valores nulos
df_func = df_func.dropna(axis = 0)
# removendo salarios = 1
df_func = df_func[df_func["Salário"] != 1]


# calculando salario maximo e minimo Zammi e Labcor
df_func[["Salário"]].max()  
int(df_func["Salário"].min())

funcionario_salario_minimo = df_func[df_func["Salário"] == df_func["Salário"].min()]
funcionario_salario_minimo 

funcionario_salario_maximo = df_func[df_func["Salário"] == df_func["Salário"].max()]
funcionario_salario_maximo 

# maior salario labcor 
df_func[df_func["Salário"] == df_func["Salário"].max()]

funcionarios_labcor = df_func[df_func["Empresa"] == 'Labcor']

funcionarios_labcor[funcionarios_labcor["Salário"] == funcionarios_labcor["Salário"].max()]

# maior salario zammi 
funcionarios_zammi = df_func[df_func["Empresa"] == 'Zammi']

funcionarios_zammi[funcionarios_zammi["Salário"] == funcionarios_zammi["Salário"].max()]

# funcionarios labcor
funcionarios_labcor["Nome Funcionário"].count()
float(funcionarios_labcor["Salário"].sum())


# funcionarios zammi
funcionarios_zammi["Nome Funcionário"].count()
float(funcionarios_zammi["Salário"].sum())



df_func[df_func["Empresa"] == 'Zammi'].count()

df_func["Cargo"]

df_func["Cargo"].value_counts()

custo_total_analistas = df_func[df_func["Cargo"].str.contains('', case=False)]["Salário"].sum()
float(custo_total_analistas)
df_func[df_func["Cargo"].str.strip() == 'Analista de sistemas Junior'][["Cargo", "Nome Funcionário", "Salário"]] 
df_func[df_func["Cargo"].str.contains('Pleno', case=False)]


df_func[df_func["Nome Funcionário"].str.contains('Aline', case=False)]

int(df_func["Salário"].sum())