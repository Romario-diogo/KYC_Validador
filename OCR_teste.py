from PIL import Image
import pytesseract
import re
import pytesseract

# Define o caminho absoluto do Tesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


# Caminho do RG
caminho_rg = r"E:\Pasta (R)\Projetos\KYC_Validador\KYC_Validador\Documentos_modelos\Modelos_RGs\RG3.png"

# Abrir imagem
imagem = Image.open(caminho_rg)

# OCR (use 'por' se você tiver o idioma instalado)
texto_ocr = pytesseract.image_to_string(imagem, lang='por')

# Exibir texto extraído (para depuração)
print("🔍 Texto extraído:")
print(texto_ocr)

# Função para extrair o nome
def extrair_nome(texto):
    match = re.search(r"NOME\s*:?\s*(.+)", texto, re.IGNORECASE)
    return match.group(1).strip() if match else None

# Função para extrair o CPF (formato com ou sem pontuação)
def extrair_cpf(texto):
    match = re.search(r"\b(\d{3}\.?\d{3}\.?\d{3}-?\d{2})\b", texto)
    return match.group(1) if match else None

# Aplicar extrações
nome = extrair_nome(texto_ocr)
cpf = extrair_cpf(texto_ocr)

# Resultado
print(f"\n✅ Nome encontrado: {nome if nome else 'Não encontrado'}")
print(f"✅ CPF encontrado: {cpf if cpf else 'Não encontrado'}")





