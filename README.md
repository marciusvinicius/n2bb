# Desafio

Nesse desafio iremos disponibilizar os dados do dataset Wine Reviews através de uma API para consulta.

## Dataset

https://www.kaggle.com/zynicide/wine-reviews (arquivo winemag-data-130k-v2.csv)

## Critérios de avaliação

- Qualidade do código e da solução proposta.
- Proximidade da solução com os requisitos.
- Utilização de boas práticas.

## Requisitos

- Desenvolva uma API que retorne os dados do dataset de forma paginada, sendo possível adicionar filtros pelos seguintes campos:
	- country 
	- description  (busca de palavra-chave)
	- points
	- price
	- variety

- Demonstre uma possível arquitetura para essa aplicação para que ela se torne resistente a muitos acessos simultâneos, explicando o porquê de cada uma das tecnolgias escolhidas.

- Adicione o passo a passo para rodar a aplicação localmente.

## Observações

- O único requisito de tecnologia é utilizar a linguagem python para programação, a utilização de qualquer tecnologia complementar poderá ser feito de acordo com seu gosto.
- Não é necessário tratar outros aspectos da aplicação como autenticação.


# Resolução


### Da escolha da framework
- Flask é uma framework simples em meu julgamento, é uma das mais rápidas para começar um projeto pequeno e ao mesmo tempo não limitar futuro crescimento.

- Mongo DB foi escolhido por não existir a necessidade de um banco relacional e o fato do banco ser um NOSQL escalar será muito mais fácil.

- A escolha para o cache é bem pessoal, eu poderia ter usado o memcache e atenderia muito bem para essa situação, mas, o redis nos permite no futuro, usar a plataforma para armazenar dados de preparação de dados (data prep)


### Arquitetura principal
- `Flask`
- `Docker`
- `Redis`
- `MongoDB`

### Modificações a longo prazo
- Incluir mais testes, eu acabei dando pouco foco para os testes, e acho que foi uma falha.

- Eu basicamente recriei um mecanismo de filtro e sort, para um projeto pequeno, isso funciona perfeitamente e foi divertido fazer, mas, no longo prazo seria legal trocar por algo de mercado como flesk-filter.

- Usar um padrão de projeto como Repository para a comunicação entre a camada de dados e o controler, achei que não era necessário criar esse tipo de abstração para um unico Resource então não fiz, mas, no longo prazo isso seria ideal.

- Load data: Mover o que hoje está em um script para um pipeline, eu queria fazer algo simples para dar load nos dados e trata-los, então coloquei em um script python mesmo, mas, ao longo prazo, criar um pipeline de dados seria ótimo, assim poderiamos garantir que os dados sempre estariam atualizados com o arquivo cv e etc...

### Instruções

É necessário ter o docker e o docker-compose para rodar a aplicação dessa forma.

- Subir o servidor `make up`
- Rodar os testes `make test`
- Load dos dados do csv `make loaddata` ( É necessário colocar o arquivo csv na pasta dataset, achei melhor não versionar o mesmo)
- Apagar os dados `make down`

### Exemplo te chamada com filtros

`localhost:8000/wines?page=2&per_page=100&points__gt=20&variety__contains=Merlot&sort=+price&sort=-points&country__contains=Chile`

```
{
    "count": 267,
    "current_page": 2,
    "data": [
    {
            "_id": {
                "$oid": "5eaae0e2ccb4473f36c00e00"
            },
            "country": "Chile",
            "description": "Wild berry aromas come with a cool hint of herbal mint. This is full, grabby and solid in the mouth. Flavors of dark fruits come across lightly stewed and pruny, while the finish dishes up a final taste of prune and foresty notes.",
            "points": 86,
            "price": 11.0,
            "title": "Concha y Toro 2012 Casillero del Diablo Reserva Merlot (Central Valley)",
            "variety": "Merlot"
        }
    ],
    "next_page": 3,
    "previous_page": 1,
    "total_pages": 3
}
```

### Filtros permitidos
```
    "price",
    "price__gte",
    "price__gt",
    "price__lte",
    "price__lt",
    "points",
    "points__lt",
    "points__lte",
    "points__gt",
    "points__gte",
    "title",
    "title__contains",
    "variety",
    "variety__contains",
    "description",
    "description__contains",
    "country",
    "country__contains",
```