# Gerador de Dias Livres

Este projeto foi criado a pedido para gerar uma lista de dias livres entre o intervalo de **01/10/2024 a 31/01/2025**, com base em um conjunto de datas fornecido, representando períodos de cursos onde esses dias não podiam ser utilizados.

## Como Funciona

Recebi uma planilha contendo várias duplas de colunas, onde cada linha representa o **período de início e fim** de um curso. O objetivo era criar uma nova planilha com todos os **dias livres**, ou seja, aqueles que não coincidiam com os períodos de curso e que também não fossem domingos.

### O que o Script Faz:

1. **Leitura das Datas de Cursos**: O script recebe uma lista de intervalos de datas representando os períodos não disponíveis para uso (por exemplo, cursos).
2. **Filtragem de Dias Livres**: O script gera uma lista de datas no intervalo de **01/10/2024 a 31/01/2025**. Durante esse processo, ele filtra os dias que:
   - Não são domingos.
   - Não estão dentro de nenhum intervalo de datas de cursos (períodos não livres).
3. **Criação de Planilha**: A lista de dias livres é então salva em uma planilha Excel (`dias_livres.xlsx`).

## Como Usar

### 1. Instalar as Dependências

Este projeto utiliza a biblioteca **Pandas** para manipulação de dados e criação da planilha Excel. Para instalá-la, siga os passos abaixo.

Se você estiver usando **pip**, basta rodar:

```bash
pip install pandas openpyxl
```

### 2. Clonar o Repositório

Clone este repositório em seu ambiente local:

```bash
git clone https://github.com/seu_usuario/gerador-dias-livres-compel.git
cd gerador-dias-livres-compel
```

### 3. Executar o Script

Após instalar as dependências e clonar o repositório, execute o script:

```bash
python app.py
```

Isso gerará um arquivo chamado `dias_livres.xlsx` com a lista de dias livres.

## Exemplo de Saída

A planilha gerada (`dias_livres.xlsx`) terá um formato semelhante ao seguinte:

| Data       |
|------------|
| 01/10/2024 |
| 02/10/2024 |
| 03/10/2024 |
| ...        |
| 31/01/2025 |

Os dias na planilha representam os dias livres que podem ser utilizados, excluindo os domingos e os períodos dos cursos.
