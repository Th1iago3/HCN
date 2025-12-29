
---
# Hencrypt (HCN – HTML Cryptographic Network)

Hencrypt é uma biblioteca Python para **ofuscação e proteção agressiva de HTML no lado do cliente**, baseada em **criptografia em bytes** e **execução apenas em memória no navegador**.

O objetivo do projeto é **dificultar engenharia reversa, inspeção via DevTools, scraping e automação**, mantendo HTML, CSS e JavaScript funcionais.

Este projeto **não promete segurança absoluta**, pois qualquer conteúdo renderizado no navegador pode ser analisado por um atacante experiente. O foco é **elevar significativamente o custo da análise**.

---

## Características

- HTML nunca entregue em texto legível
- Criptografia em bytes (compressão + XOR + Base64)
- Descriptografia apenas em runtime
- Execução totalmente em memória
- Loader JavaScript dinâmico
- Preservação de CSS, JS e `<title>` original
- Detecção de DevTools
- Detecção de browsers headless (Puppeteer, Playwright, Phantom, WebDriver)
- Proteção contra scraping simples
- Payload inútil fora do ambiente de execução
- Limpeza de memória após execução

---

## Estrutura do Projeto

```

Hencrypt/
│
├── hcn/
│   ├── **init**.py
│   ├── **HCN**.py
│   ├── **ENCRYPTION**.py
│   ├── **BUILDER**.py
│   └── viewer/
│       ├── **init**.py
│       ├── **VIEWER**.py
│       ├── **VIRTUAL**.py
│       └── **DECRYPTOR**.py
│
├── index.html
├── server.py
└── README.md

````

---

## Requisitos

- Python 3.8 ou superior
- Flask (para testes locais)

Instalação da dependência de teste:

```bash
pip install flask
````

---

## Uso Básico

### Exemplo de servidor local

```python
from flask import Flask, Response
from hcn import HCN

app = Flask(__name__)
hcn = HCN.start()

protected_html = hcn.show("index.html")

@app.route("/")
def index():
    return Response(protected_html, mimetype="text/html")

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000, debug=False)
```

A aplicação ficará disponível em:

```
http://127.0.0.1:8000
```

---

## Funcionamento Técnico (Resumo)

1. O HTML original é lido em bytes
2. O conteúdo é comprimido
3. Uma chave dinâmica é gerada
4. Os dados são cifrados via XOR
5. O resultado é codificado em Base64
6. Um loader JavaScript é gerado
7. O navegador descriptografa apenas em runtime
8. O DOM é recriado dinamicamente
9. O HTML nunca aparece em texto plano

---

## Camadas de Proteção

| Proteção                | Nível       |
| ----------------------- | ----------- |
| View Source             | Alto        |
| HTML legível            | Alto        |
| DevTools                | Médio       |
| Headless browsers       | Médio       |
| Scrapers simples        | Médio       |
| Replay HTTP             | Médio       |
| Dump simples de memória | Parcial     |
| Análise manual avançada | Não coberto |

---

## Limitações Conhecidas

* Não impede engenharia reversa avançada
* Não protege contra browsers modificados
* Não substitui validações server-side
* O HTML precisa existir em memória no cliente

---

## Uso Responsável

Este projeto foi desenvolvido para:

* Proteção de propriedade intelectual
* Dificultar scraping automatizado
* Estudos de ofuscação e segurança client-side

O autor não se responsabiliza pelo uso indevido do software.

---

## Autor

Th1iago3
GitHub: [https://github.com/Th1iago3](https://github.com/Th1iago3)

---

## Contribuições

Contribuições são bem-vindas via Pull Request.

---
