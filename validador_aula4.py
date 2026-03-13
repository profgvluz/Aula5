import pandas as pd

def validar_cep_cidade(cep_input, cidade_input, caminho_planilha="ceps.xlsx"):
    try:
        # Verifica a extensão para usar o motor correto do pandas
        if caminho_planilha.endswith('.xlsx'):
            df = pd.read_excel(caminho_planilha)          
        else:
            df = pd.read_csv(caminho_planilha)

        # Limpeza: remove caracteres não numéricos do CEP
        cep_limpo = int(''.join(filter(str.isdigit, str(cep_input))))
        # Deixa a cidade em maiúsculo e sem espaços nas pontas
        cidade_limpa = str(cidade_input).strip().upper()

        # Filtra pela coluna LOCALIDADE_SEM_ACENTOS
        filtro = df[df['LOCALIDADE_SEM_ACENTOS'].str.upper() == cidade_limpa]

        if filtro.empty:
            return False

        # Verifica se o CEP está dentro de alguma das faixas daquela cidade
        for _, linha in filtro.iterrows():
            # Remove espaços que podem vir da planilha antes de converter para int
            inicio = int(str(linha['CEP_INICIAL']).strip())
            fim = int(str(linha['CEP_FINAL']).strip())

            if inicio <= cep_limpo <= fim:
                return True
        
        return False
        
    except Exception as e:
        print(f"Erro ao ler planilha: {e}")
        return False

print(validar_cep_cidade("18051-610", "Sorocaba", "ceps.xlsx"))