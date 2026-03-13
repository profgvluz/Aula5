from validador_aula4 import validar_cep_cidade
import pytest

# Teste 1: CEP válido para Alumínio (Conforme PDF: 18125-000)
def test_cep_valido_aluminio():
    assert validar_cep_cidade("18125-000", "Aluminio", "ceps.xlsx") == False

# Teste 2: CEP válido para Itu (Conforme PDF: 13300-000)
def test_cep_valido_itu():
    assert validar_cep_cidade("13300-000", "Itu", "ceps.xlsx") == True

# Teste 3: CEP de uma cidade na busca de outra (Deve falhar)
def test_cep_errado_cidade_certa():
    # CEP de Itu tentando validar em Alumínio
    assert validar_cep_cidade("13300-000", "Aluminio", "ceps.xlsx") == False

# Teste 4: Cidade que não existe na planilha
def test_cidade_inexistente():
    assert validar_cep_cidade("18000-000", "CidadeFantasma", "ceps.xlsx") == False

def test_cidade_Piracicaba():
    assert validar_cep_cidade("18000-000", "Piracicaba", "ceps.xlsx") == False

def test_cidade_Sorocaba():
    assert validar_cep_cidade("18051-610", "Sorocaba", "ceps.xlsx") == True
    assert validar_cep_cidade("18051-610", "Sorocab", "ceps.xlsx") == False
    assert validar_cep_cidade("18051-610", "SOROCABA", "ceps.xlsx") == True
    assert validar_cep_cidade("18051-610", "", "ceps.xlsx") == False
    assert validar_cep_cidade("", "Sorocaba", "ceps.xlsx") == False
    assert validar_cep_cidade("10000-000", "Sorocaba", "ceps.xlsx") == False