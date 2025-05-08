# ✅ Validador Automático de Documentos KYC

Automação para validação de documentos KYC (Know Your Customer), utilizando OCR e análise de consistência de dados entre arquivos digitalizados (PDF, imagens) e planilhas de cadastro (Excel). O sistema identifica divergências entre o que está no documento e o que foi registrado no formulário, gerando um relatório detalhado e visual.

---

## 🎯 Objetivo

Automatizar o processo de validação de documentos como RG, CPF e comprovantes de residência, comparando o texto extraído via OCR com os dados do cadastro. Gera relatórios claros e interpretáveis, eliminando a verificação manual que toma tempo e é sujeita a erros.

---

## 🧩 Estrutura do Projeto

```
kyc_validador/
├── dados/
│   ├── documentos/              # PDF e imagens dos documentos
│   └── cadastro.xlsx            # Planilha com os dados oficiais dos clientes
│
├── src/
│   ├── ocr_handler.py           # Extração de texto com OCR e tratamento de imagem
│   ├── comparador.py            # Comparação de dados com margem de similaridade
│   ├── relatorio.py             # Geração de relatório detalhado e visual
│   ├── organizador.py           # Identificação e agrupamento dos documentos por cliente
│   └── main.py                  # Orquestrador do fluxo completo
│
├── output/
│   └── relatorio_validacao.xlsx
│
├── README.md
└── requirements.txt
```

---

## 📅 Cronograma de Desenvolvimento

| Etapa | Descrição | Dias estimados |
|-------|-----------|----------------|
| **1** | Coleta e simulação de documentos e cadastro | 1–2 |
| **2** | Implementação da extração de texto via OCR | 3–6 |
| **3** | Lógica de comparação com limiares de similaridade | 7–10 |
| **4** | Geração de relatório final com status por campo | 11–13 |
| **5** | Testes completos e documentação do fluxo | 14–15 |

---

## 🛠️ Tecnologias e Bibliotecas

- **OCR e Imagem**: `pytesseract`, `Pillow`, `pdfplumber`
- **Manipulação de Planilhas**: `pandas`, `openpyxl`
- **Comparações Textuais**: `fuzzywuzzy`, `regex`, `unidecode`
- **Utilidades**: `os`, `datetime`, `argparse`

---

## 🧠 Diferenciais Técnicos

- Suporte a dois modos de uso:
  - **Organizado**: documentos nomeados ou separados por pasta/cliente
  - **Desorganizado**: sistema localiza o CPF via OCR e associa aos dados
- Comparação aproximada com **margem ajustável de similaridade**
- Relatório visual em `.xlsx` com destaque para divergências por cor
- Pipeline flexível, modular e pronto para expansão

---

## 📈 Resultados Esperados

- Redução drástica do tempo de validação documental
- Aumento da acurácia na comparação de dados sensíveis
- Eliminação de tarefas manuais repetitivas em setores de compliance
