import pandas as pd
import plotly.express as px

df = pd.read_csv('historico-alg1_SIGA_ANONIMIZADO.csv')

print("#1. Qual a média da nota dos aprovados? No período total e por ano\n")

# Filtrando o df, retirando as equivalencias e calculando as médias.
df_aprovados = df[(df['status'] == 'Aprovado') & (df['tipo'] != 'EQUIVALENCIA')]
media_aprovados = df_aprovados['nota'].mean()
print(f"A média da nota dos aprovados no período total é de: {media_aprovados:.2f}\n")
df_aprovados_gb = df_aprovados.groupby('ano').agg({'nota':'mean'}).reset_index()
print("Segue o dataframe com as notas média por ano dos aprovados: \n", df_aprovados_gb)

print("\n#2. Qual é a média de nota dos reprovados por nota (período total e ano)?\n")

#Criando o df de reprovados e calculando as médias;
df_reprovados = df[df['status'] == 'R-nota']
media_reprovados = df_reprovados['nota'].mean()
print(f"A média da nota dos reprovados no período total é de: {media_reprovados:.2f}\n")
df_reprovados_gb = df_reprovados.groupby('ano').agg({'nota':'mean'}).reset_index()
print("Segue o dataframe com as notas média por ano dos aprovados: \n", df_reprovados_gb)

print("\n#3. Qual é a frequência dos reprovados por nota (período total e por ano)?\n")

#Criando o df para calcular as frequencias. 
freq = df['status'].value_counts(normalize=True)
print(f"Frequencias da colunas 'status': \n{freq}\n")
print("A frequência dos reprovados por nota no período total é de: 17,82%\n")
df_grouped = df.groupby('ano')['status'].value_counts(normalize=True)
print("Frequencia dos reprovados por nota p/ano:\n 2012: 50%\n 2013: 27,27%\n 2014: 7,69%\n 2015: 17,14%\n 2016: 9,43%\n 2017: 22,82%\n 2018: 22,91%\n 2019: 11,76%\n 2020: 7,54%\n 2021: 28,26%\n 2022: 22,13%\n")

print("#4. Qual a porcentagem de evasões (total e anual)?\n")

#Calculando as evasões totais e por ano
df['situacaoDiscente'].value_counts('Evasão')
print("Porcentagem de evasões totais: 15,62%\n")

df_grouped_2 = df.groupby('ano')['situacaoDiscente'].value_counts(normalize=True)
print("Porcentagem das evasões por ano: \n2013: 63,63%\n 2014: 23,07%\n 2015: 20%\n 2016: 15,09%\n 2017: 18,47%\n 2018: 22,91%\n 2019: 16,38%\n 2020: 17,92%\n 2021: 12,31%\n 2022: 2,45%\n")

print("#5. Como os anos de pandemia impactaram no rendimento dos estudantes em relação aos anos anteriores, considerando o rendimento dos aprovados, a taxa de cancelamento e as reprovações? Considere como anos de pandemia os anos de 2020 e 2021.\n# 6- Compare a volta às aulas híbrida (2022 período 1) com os anos de pandemia e os anos anteriores.\n")
print("Nos gráficos é possível comparar os anos anteriores com os anos de pandemia e com o primeiro periodo de 2021, não existem dados de 2021.2, pois é um periodo 'em andamento'.\n")
#Plotando os gráficos.
def plot_line(df,x,y,titulo):
    fig = px.line(df, x = x, y= y, markers = True)
    fig.add_vrect(x0='2020', x1='2021', 
              annotation_text="Anos de pandemia", annotation_position='top left',
              fillcolor="green", opacity=0.20)
    fig.update_layout(title= titulo)
    fig.show()

plot_line(df_aprovados_gb, 'ano', 'nota', 'Média da nota dos estudantes aprovados por ano. Sem as equivalências')

df_gb = df.groupby("ano").agg(lambda x: (x == 'Cancelado').sum() / len(x) * 100).reset_index()
plot_line(df_gb, 'ano', 'status', 'Taxa de cancelamento')

df_reprovados_2 = df[(df['status'] == 'R-nota') | (df['status'] == 'R-freq')]
df_reprovados_2 = df_reprovados_2.groupby('ano').agg({'status':'count'}).reset_index()
plot_line(df_reprovados_2, 'ano', 'status', 'Reprovações por ano')




















