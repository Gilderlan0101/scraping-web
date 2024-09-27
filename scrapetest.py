import requests
from bs4 import BeautifulSoup

def scrapin_web():
    url = "http://www.pythonscraping.com/pages/page1.html"
    
    try:
        # Usando requests em vez de urlopen
        response = requests.get(url)
        
        # Verifica se o status da resposta é 200 (OK)
        response.raise_for_status()  # Isso levantará um erro HTTP se o status não for 200

        # Cria o objeto BeautifulSoup para analisar o HTML
        soup = BeautifulSoup(response.text, 'html.parser')

      
       
        
        # Podemos pegar uma tag específica, como por exemplo o título
        title_tag = soup.find('h1')  # Tentando buscar uma tag h1
        if title_tag:
            return title_tag.get_text()  # Retorna o conteúdo do h1
        else:
            raise AttributeError(f'A tag na linha 18 não foi encontrada')
        
        

    except requests.exceptions.HTTPError as e:
        # Trata erros HTTP (status 404, 500, etc.)
        return f"Erro ao tentar acessar o site: {e}"

    except requests.exceptions.RequestException as e:
        # Trata erros gerais de requisições, como falha de conexão
        return f"Erro de conexão: {e}"

    except AttributeError as e:
        # Trata erros de atributos quando a tag não é encontrada
        return f"Erro de atributo: {e}"

# Executa a função de scraping
raspando = scrapin_web()

# Verifica o retorno da função e imprime o resultado
if raspando is None:
    print('URL não encontrada')
else:
    print(raspando)
