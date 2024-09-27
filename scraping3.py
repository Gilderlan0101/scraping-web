from bs4 import BeautifulSoup
import requests

def tags():
    url = "https://gauchazh.clicrbs.com.br/ultimas-noticias/tag/gemeos/" 

    try:
        response = requests.get(url)
#       Retorno um erro caso a requisição nõa seja 200
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")
        all_title = soup.find_all({'h1','h2','h3','h4','h5', 'h6'}) # pegando todas os titulos do site do g1
# eu posso pegar dois atributos ao mesmo tempo que tenha uma tag h3, tanto como valores de text-base e red
        all_tags_and_class = soup.find_all('h3',  {'class': 'text-base', 'class': 'text-lg'})
        
        for titulo in all_title:
            print(titulo.get_text())
        print()
        print('--------------------------')
        print()
        for atributos in all_tags_and_class:
            print(atributos.get_text())

    
    except requests.exceptions.RequestException as e:
        return f'Erro ao tenta acesar o site: {e}'
    except AttributeError as e:
        return f'Erro ao tenta acesar a tag na linha 12 {e} '
    
tags()