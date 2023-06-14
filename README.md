# gerador-txt

Este repositório contém uma aplicação desenvolvida em Python para ler uma planilha em formato Excel (.xlsx) e gerar um arquivo de texto (.txt) com as informações coletadas. O objetivo é permitir que os usuários possam importar o arquivo TXT gerado pela aplicação no sistema ERP Protheus usando a rotina de contabilização TXT.

## Funcionalidades

A aplicação de leitura de planilha Excel e geração de TXT inclui as seguintes funcionalidades:

- Ler uma planilha em formato Excel (.xlsx)
- Extrair informações relevantes da planilha
- Gerar um arquivo de texto (.txt) com as informações coletadas

## Informações importantes

- A planilha deve estar nesse [formato](https://1drv.ms/x/s!Aq1dbgOsNoybgwK7OfwQZ0ti4h8G?e=7htjrJ)
- No Protheus deve ser criado um Lançamento Padrão com o código 004, parâmetros:

	- Tipo Lcto (CT5_DC): 3 - Partida dobrada
	- Cta Debito (CT5_DEBITO): LERSTR(5,10)
	- Cta Credito (CT5_CREDIT): LERSTR(16,10)
	- Item Debito (CT5_ITEMD): LERSTR(86,11)
	- Item Credito (CT5_ITEMC): LERSTR(98,11)
	- Cl Vlr Deb (CT5_CLVLDB): LERSTR(110,10)
	- Cl Vlr Crd (CT5_CLVLCR): LERSTR(121,10) 
	- Ent.Deb. 05 (CT5_EC05DB): LERSTR(132,12) 
	- Ent.Cred. 05 (CT5_EC05CR): LERSTR(145,12)
	- Lcto Moedas (CT5_MOEDAS): 12222
	- Vlr Moeda 1 (CT5_VLR01): LERVAL(27,8)
	- Historico (CT5_HIST): LERSTR(36,40)
	- Data Venc (CT5_DTVENC): LERDATA(77,8)

## Requisitos

Para executar a aplicação em sua máquina local, você precisará ter os seguintes requisitos:

- Python 3.6 ou superior
- Biblioteca Openpyxl

## Instalação

Siga as etapas abaixo para configurar e executar a aplicação:

1. Clone este repositório para o seu ambiente local usando o seguinte comando:

   ```
   git clone https://github.com/eduardoranucci/gerador-txt.git
   ```

2. Navegue até o diretório raiz do projeto:

   ```
   cd gerador-txt
   ```

3. Opcionalmente, crie e ative um ambiente virtual:

   ```
   python -m venv venv
   .\venv\Scripts\activate
   ```

4. Instale as dependências do projeto:

   ```
   pip install -r requirements.txt
   ```

5. Renomeie a planilha Excel que você deseja processar para `base.xlsx` e coloque na pasta raiz do projeto.

6. Execute a aplicação:

   ```
   python main.py
   ```

7. O arquivo `base.txt` será gerado na pasta raiz, contendo as informações extraídas da planilha.

8. Importe o arquivo gerado no Protheus usando a rotina Contabilização TXT (CTBA500).

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

## Agradecimentos

Este projeto utiliza a biblioteca Openpyxl para manipulação de dados de planilha em Python. Agradecemos aos desenvolvedores por disponibilizarem essa biblioteca de código aberto.
