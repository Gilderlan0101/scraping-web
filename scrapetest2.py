from bs4 import BeautifulSoup
import requests

def buscando_tags():    
    url = "http://www.pythonscraping.com/pages/warandpeace.html" 

    try:
        response = requests.get(url)

    # Verifica se o status é 200: caso contrario retorne um erro
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        #Lista de nomes             tag     atributo   valor
        lista_nomes = soup.find_all('span', {'class': 'green'})

        for nome in lista_nomes:
            print(nome.get_text()) #  método get_text() retorna apenas o texto legível por humanos

    except requests.exceptions.RequestException as e: # Erro ao tenta fazer requisição
        return f'Erro ao tenta fazer uma requisição: {e}'
    
    except AttributeError as e: # erro de tag html
        return f'Erro ao tenta acessar um atributo HTML'
    
    except requests.exceptions.HTTPError as e: # status 400,500
        return f'Erro ao tenta acesar o site [erro]: {e}'

buscando_tags()
