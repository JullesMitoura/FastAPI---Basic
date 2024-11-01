### Curso Básico de FastAPI
---

O objetivo principal deste repositório é compartilhar com você o meus primeiros passos nos estudos de elaboração de APIs com FastAPI.

Documentação básica: https://fastapi.tiangolo.com

A documentação acima é de fato uma das melhores fontes de informação acerca de FastAPI.

---

#### Libraries Necessárias:

* uvicorn:
* fastapi:

Os exemplos discutios aqui são:

* ### Projeto 01 - Do Zero ao Deploy:

1. #### Elaboração de API

Em FastAPI podemos criar nossa primeira API somente com o código abaixo:

```python
from fastapi import FastAPI

# Create an instance of FastAPI
app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```


* ### Projeto 02 - API customizada para consumo de LLMs + RAG:

* ### Projeto 03 - Chatbot com LangChain + OpenAI:


---

Comands:

* pip freeze | grep fast -> Comando para buscar a versao das libs. Utilizamos o `grep` para filtrar por `fast`. Poderiamos fazer `pip freeze | grep uvi`, o resultado seria a versao do `uvicorn`.