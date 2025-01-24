import pandas as pd
from datetime import datetime

# Definindo as datas não livres
nao_livres = [
    ("07/10/2024", "11/10/2024"),
    ("29/11/2024", "04/12/2024"),
    ("28/12/2024", "03/01/2025"),
    ("04/01/2025", "09/01/2025"),
    ("05/12/2024", "10/12/2024"),
    ("14/10/2024", "18/10/2024"),
    ("04/11/2024", "05/11/2024"),
    ("11/12/2024", "12/12/2024"),
    ("10/01/2025", "11/01/2025"),
    ("13/12/2024", "23/12/2024"),
    ("23/10/2024", "01/11/2024"),
    ("23/10/2024", "01/11/2024"),
    ("13/12/2024", "23/12/2024"),
    ("13/01/2025", "22/01/2025"),
    ("23/10/2024", "01/11/2024"),
]

# Converter as datas para o formato datetime
nao_livres = [(datetime.strptime(start, "%d/%m/%Y"), datetime.strptime(end, "%d/%m/%Y")) for start, end in nao_livres]

# Gerar todas as datas no intervalo de 01/10/2024 a 31/01/2025
inicio = datetime(2024, 10, 1)
fim = datetime(2025, 1, 31)
todas_datas = pd.date_range(inicio, fim).to_list()

# Filtrar os dias livres
dias_livres = []

for data in todas_datas:
    livre = True
    # Verificar se é domingo (onde 6 representa domingo)
    if data.weekday() == 6:
        livre = False
    # Verificar se a data está no intervalo das datas não livres
    for inicio_nao_livre, fim_nao_livre in nao_livres:
        if inicio_nao_livre <= data <= fim_nao_livre:
            livre = False
            break
    # Adicionar data se for livre
    if livre:
        dias_livres.append(data.strftime("%d/%m/%Y"))  # Formatar para dd/mm/yyyy

# Criar o DataFrame com os dias livres
df = pd.DataFrame(dias_livres, columns=["Data"])

# Salvar o DataFrame como um arquivo Excel
df.to_excel("dias_livres.xlsx", index=False)

print("Planilha com os dias livres foi criada com sucesso!")
