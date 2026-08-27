# Amostragem e Interpolação de Imagens

**Dupla:** Cayke Veras e Filipe Coelho

## Descrição

Este projeto implementa e compara dois métodos fundamentais de interpolação de imagens:
- **Vizinho Mais Próximo (VMP)**: Método rápido que copia o valor do pixel vizinho mais próximo
- **Interpolação Bilinear**: Método que interpola os 4 vizinhos mais próximos com pesos baseados na distância

O projeto demonstra como estes métodos funcionam tanto para **ampliação** (upscaling) quanto para **redução** (downscaling) de imagens.

## Estrutura do Projeto

```
amostragem/
├── interpolacao.py           # Implementação dos algoritmos de interpolação
├── transformacoes.html       # Visualização interativa dos resultados
├── original.png              # Imagem original (8×8)
├── vmp_ampliacao.png         # VMP ampliado para 16×16
├── vmp_reducao.png           # VMP reduzido para 4×4
├── bilinear_ampliacao.png    # Bilinear ampliado para 16×16
├── bilinear_reducao.png      # Bilinear reduzido para 4×4
└── README.md                 # Este arquivo
```

## Como Executar

### Gerar as imagens processadas:
```bash
python interpolacao.py
```

Este comando irá:
1. Criar uma imagem de teste 8×8 com gradiente de cinza
2. Aplicar os dois métodos de interpolação para ampliação e redução
3. Salvar 5 imagens PNG com os resultados

### Visualizar os resultados:
Abra o arquivo `transformacoes.html` em um navegador web para ver uma apresentação visual interativa com:
- Comparação lado a lado dos métodos
- Análise de vantagens e desvantagens
- Tabela comparativa
- Imagens processadas com descrições

## Conceitos Principais

### Vizinho Mais Próximo
- **Velocidade:** Muito rápida
- **Qualidade:** Baixa (resultado pixelado)
- **Melhor para:** Ampliação em pixel art, processamento em tempo real
- **Algoritmo:** Para cada pixel destino, copia o valor do vizinho mais próximo na imagem origem

### Interpolação Bilinear
- **Velocidade:** Moderada
- **Qualidade:** Boa (transições suaves)
- **Melhor para:** Ampliação e redução com qualidade visual
- **Algoritmo:** Interpola os 4 vizinhos mais próximos usando pesos proporcionais às distâncias fracionárias

## Resultados Comparativos

| Critério | Vizinho Mais Próximo | Interpolação Bilinear |
|----------|---------------------|----------------------|
| Velocidade | Muito Rápida | Moderada |
| Qualidade Visual | Baixa | Boa |
| Ampliação | Ruim | Bom |
| Redução | Aceitável | Melhor |
| Preservação de Cores | Exata | Aproximada |


## Autores

- **Cayke Veras**
- **Filipe Coelho**

**Disciplina:** Processamento de Imagens
**Instituição:** UFT (Universidade Federal do Tocantins)  
**Professor:** Dra. Glenda Botelho

## Notas Técnicas

- A imagem de teste é uma matriz 8×8 pixels com gradiente de cinza (valores de 0 a 255)
- Ampliação realizada de 8×8 para 16×16 pixels
- Redução realizada de 8×8 para 4×4 pixels
- Implementação em Python usando NumPy e PIL (Pillow)