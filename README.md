---

```markdown
<div align="center">

# 🔐 Hencrypt (HCN)
### HTML Cryptographic Network

Proteção, ofuscação e criptografia agressiva de HTML  
Execução apenas em memória • Anti DevTools • Anti Bots • Anti Headless

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](#)
[![Status](https://img.shields.io/badge/Status-Active-success)](#)
[![License](https://img.shields.io/badge/License-MIT-lightgrey)](#)

</div>

---

## 📌 Sobre o Projeto

**Hencrypt (HCN – HTML Cryptographic Network)** é uma biblioteca escrita em **Python** cujo objetivo é **dificultar ao máximo a inspeção, engenharia reversa e extração de código HTML no lado do cliente**.

O projeto utiliza **criptografia em bytes**, **execução somente em runtime**, **loader virtual em JavaScript** e **mecanismos anti-análise**, mantendo **HTML, CSS e JavaScript totalmente funcionais**.

> ⚠️ Importante  
> Nenhuma proteção client-side é 100% inviolável.  
> O HCN **não promete impossibilidade**, e sim **dificuldade extrema**.

---

## 🚀 Principais Recursos

- 🔒 HTML nunca entregue em texto legível
- 🧠 Criptografia em bytes (compressão + XOR + Base64)
- ⚙️ Descriptografia apenas em memória
- 🧪 Execução dinâmica via loader virtual
- 🛡️ Anti DevTools (timing + viewport)
- 🤖 Anti bots e scrapers simples
- 🕶️ Anti Headless Browsers  
  (Puppeteer, Playwright, PhantomJS, WebDriver)
- 🔁 Payload inútil fora do runtime
- 🧹 Limpeza automática de memória
- 🎨 Preserva CSS, JS e `<title>` original
- 📦 Fácil de usar como biblioteca Python

---

## 📂 Estrutura do Projeto

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

## 📦 Requisitos

- Python **3.8+**
- Flask (para testes locais)

```bash
pip install flask
````

---

## ⚙️ Uso Básico

### Exemplo `server.py`

```python
from flask import Flask, Response
from hcn import HCN

app = Flask(__name__)
hcn = HCN.start()

protected = hcn.show("index.html")

@app.route("/")
def home():
    return Response(protected, mimetype="text/html")

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000, debug=False)
```

Acesse no navegador:

```
http://127.0.0.1:8000
```

---

## 🧠 Funcionamento Interno (Resumo)

1. O HTML original é lido em **bytes**
2. O conteúdo é comprimido
3. Aplicado XOR com chave dinâmica
4. Codificado em Base64
5. Um loader JavaScript é gerado
6. O navegador descriptografa apenas em runtime
7. O DOM é recriado dinamicamente
8. O HTML nunca aparece em texto plano

---

## 🛡️ Camadas de Proteção

| Proteção                | Status     |
| ----------------------- | ---------- |
| View Source             | ✅          |
| HTML legível            | ✅          |
| DevTools aberto         | ✅          |
| Headless Browsers       | ✅          |
| WebDriver               | ✅          |
| Scrapers simples        | ✅          |
| Replay HTTP             | ✅          |
| Dump simples de memória | ⚠️ Parcial |
| Análise avançada manual | ❌          |

---

## ⚠️ Limitações

* Não impede análise avançada por especialistas
* Não protege contra browsers customizados
* Não substitui segurança server-side
* O HTML precisa existir em memória no cliente

---

## 📜 Aviso Legal

Este projeto foi criado para:

* Proteção de propriedade intelectual
* Dificultar scraping automatizado
* Estudos de segurança e ofuscação client-side

❌ Não utilize para fins ilegais
❌ Não utilize para violar termos de serviço

O autor não se responsabiliza pelo uso indevido.

---

# 🌍 English Documentation

## Hencrypt (HCN)

**HCN** is a Python library focused on **aggressive HTML obfuscation and client-side protection**, using **byte-level encryption and runtime-only execution**.

### Key Features

* Encrypted HTML payload
* Runtime-only decryption
* Anti DevTools
* Anti headless browsers
* Anti bots and scrapers
* Memory cleanup
* Fully functional JS and CSS

> Client-side security is never absolute.
> HCN focuses on difficulty, not impossibility.

---

# 🌎 Documentación en Español

## Hencrypt (HCN)

**HCN** es una biblioteca en Python orientada a la **ofuscación agresiva de HTML**, utilizando **cifrado en bytes y ejecución solo en memoria**.

### Características

* HTML cifrado
* Ejecución en tiempo de ejecución
* Anti DevTools
* Anti bots
* Anti navegadores headless
* Limpieza de memoria

> Ninguna protección del lado del cliente es completamente segura.

---

## 👤 Autor

**Th1iago3**
GitHub: [https://github.com/Th1iago3](https://github.com/Th1iago3)

---

## ⭐ Contribuições

Pull Requests são bem-vindos.
Ideias para futuras versões:

* WebAssembly decryptor
* Loader 100% offline
* Chave por sessão
* Worker isolado
* Payload mutável por request
* Modo paranoia

---

<div align="center">

🛡️ **Hencrypt – dificulte, não prometa o impossível**

</div>
```

---
