### Estrutura do pacote de processamento de imagens
# Diretório: processamento_imagem/
# Arquivo: __init__.py

from .filtros import aplicar_grayscale
from .redimensionamento import redimensionar
from .utils import carregar_imagem, salvar_imagem

__all__ = [
    "aplicar_grayscale",
    "redimensionar",
    "carregar_imagem",
    "salvar_imagem"
]


# Arquivo: filtros.py
from PIL import Image

def aplicar_grayscale(imagem):
    return imagem.convert("L")


# Arquivo: redimensionamento.py
from PIL import Image

def redimensionar(imagem, largura, altura):
    return imagem.resize((largura, altura))


# Arquivo: utils.py
from PIL import Image

def carregar_imagem(caminho):
    return Image.open(caminho)

def salvar_imagem(imagem, caminho):
    imagem.save(caminho)


# Arquivo: exemplo_uso.py (fora do pacote, em /exemplos)
from processamento_imagem import carregar_imagem, salvar_imagem, aplicar_grayscale, redimensionar

# Exemplo de uso
img = carregar_imagem("exemplo.jpg")
img = aplicar_grayscale(img)
img = redimensionar(img, 200, 200)
salvar_imagem(img, "resultado.jpg")
