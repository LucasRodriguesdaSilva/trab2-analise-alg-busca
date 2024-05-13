import pandas as pd
import matplotlib.pyplot as plt
import os
from utils.arguments import arguments_plot
from utils.dicionarios_utilizados import dicionarios_utilizados

# camminho_absoluto = os.path.dirname(os.path.abspath(__file__))
def plotar_uso_memmoria(df, pasta_saida):
     # Calcular a média do Uso de Memória - Inicial
    uso_memoria_atual = df["Uso de Memoria - atual (MB)"] 
    uso_memoria_pico =   df['Uso de Memoria - Pico (MB)']
    media_memoria_inicial = uso_memoria_pico.mean()

    largura_polegadas = 8
    altura_polegadas = 6

    # Cria a figura com o tamanho especificado
    fig, ax = plt.subplots(figsize=(largura_polegadas, altura_polegadas))

    # Plotar gráfico de linha para Uso de Memória
    plt.plot(df['Iteracao'], uso_memoria_atual , label='Atual', marker='o')
    plt.plot(df['Iteracao'], uso_memoria_pico , label='Pico', marker='x')
    # plt.plot(df['Iteracao'], df['Uso de Memoria - Diferenca (bytes)'], label='Diferença', marker='.')
    plt.axhline(y=media_memoria_inicial, color='r', linestyle='--', label=f'Média: {media_memoria_inicial:.5f} Megabytes')
    plt.xlabel('Iteração')
    plt.ylabel('Uso de Memória (MB)')
    plt.title('Uso de Memória')
    plt.legend()
    plt.xticks(df['Iteracao'][::1], df['Iteracao'][::1], rotation=45) 
    plt.tight_layout()
    caminho_imagem = os.path.join(pasta_saida, 'uso_memoria.png')
    # Salvar o gráfico em um arquivo PNG
    plt.savefig(caminho_imagem)
    plt.close()

def plotar_tempo_execucao(df, pasta_saida):
    media_tempo_execucao = df['Tempo de Execucao (s)'].mean()

    # Define o tamanho da figura em polegadas
    largura_polegadas = 8
    altura_polegadas = 6

    # Cria a figura com o tamanho especificado
    fig, ax = plt.subplots(figsize=(largura_polegadas, altura_polegadas))

    # Plotar gráfico de linha para Tempo de Execução
    plt.plot(df['Iteracao'], df['Tempo de Execucao (s)'], marker='o')
    plt.axhline(y=media_tempo_execucao, color='r', linestyle='--', label=f'Média: {media_tempo_execucao:.5f} segundos')
    plt.xlabel('Iteração')
    plt.ylabel('Tempo de Execução (s)')
    plt.title('Gráfico de Linha - Tempo de Execução')
    plt.legend()
    plt.xticks(df['Iteracao'][::1], df['Iteracao'][::1], rotation=45) 
    plt.tight_layout()

    caminho_imagem = os.path.join(pasta_saida, 'tempo_execucao.png')
    # Salvar o gráfico em um arquivo PNG
    plt.savefig(caminho_imagem)

    # Fechar a figura para evitar sobreposição em iterações posteriores
    plt.close()

def getCaminhoOutput(pasta):
    caminho_relativo = os.path.join(pasta, 'output')
    return caminho_relativo


def plotar_imagem(caminho_arquivo):
    caminho = caminho_arquivo
    nome_arquivo = 'dados.csv'
    pasta_saida = os.path.join(caminho,'imagens')

    caminho_arquivo = os.path.join(caminho_arquivo, nome_arquivo)
    print('Lendo Arquivo no Caminho: ', caminho_arquivo)
    df = pd.read_csv(caminho_arquivo)

    if not os.path.exists(pasta_saida):
        os.makedirs(pasta_saida)

    print('Salvando imagens ...')
    plotar_uso_memmoria(df=df, pasta_saida=pasta_saida)
    plotar_tempo_execucao(df=df, pasta_saida=pasta_saida)
    print('Concluído!')


def main():
    print('Iniciando ...')
    args = arguments_plot()
    dicionarios = dicionarios_utilizados()

    tipo_lista = dicionarios['t']['no']

    if args.a == 'a':
        pasta = 'maxVal1'
    elif args.a == 'b':
        pasta = 'maxVal2'

    diretorio_base = getCaminhoOutput(pasta=pasta)

    for subdiretorio in os.listdir(diretorio_base):
        if subdiretorio.isdigit() and subdiretorio == '100000000':
            caminho_arquivo = os.path.join(diretorio_base, subdiretorio)
            print('Verificando se existe o caminho')

            if os.path.exists(caminho_arquivo):
                print('Caminho encontrado ...')
                plotar_imagem(caminho_arquivo=caminho_arquivo)
                    
            else:
                print('Caminho Não Existe: ', caminho_arquivo)
        print('\n')






if __name__ == "__main__":
    main()