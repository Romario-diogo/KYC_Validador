from PIL import Image, ImageDraw, ImageFont

# Abrir a imagem
caminho_imagem = r"E:\Pasta (R)\Projetos\KYC_Validador\KYC_Validador\Documentos_modelos\Modelos_RGs\RG1.png"
imagem = Image.open(caminho_imagem).convert("RGB")


# Criar objeto de desenho
desenho = ImageDraw.Draw(imagem)

# Fonte
try:
    fonte = ImageFont.truetype("arial.ttf", 11)  # Ajuste o tamanho aqui se quiser
except:
    fonte = ImageFont.load_default()

# Novo nome e coordenadas
novo_nome = "JOÃO CARLOS DOS SANTOS"
coordenadas = (388, 502)

# Inserir texto
desenho.text(coordenadas, novo_nome, fill=(0, 0, 0), font=fonte)

# Salvar nova imagem
imagem.save("RG1_nome_editado.png")
