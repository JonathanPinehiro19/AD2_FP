def localizar_inicio_linhas(caminho_arquivo):
    marcadores = []
    with open(caminho_arquivo, 'r', encoding='utf-8') as f:
        while True:
            posicao_atual = f.tell()
            conteudo = f.readline()
            if not conteudo:
                break
            marcadores.append(posicao_atual)
    return marcadores

def gerar_arquivo_reverso(origem, destino, indices):
    with open(origem, 'r', encoding='utf-8') as original, open(destino, 'w', encoding='utf-8') as novo:
        for indice in reversed(indices):
            original.seek(indice)
            linha = original.readline()
            novo.write(linha)

def iniciar_processo():
    entrada = input("Informe o nome do arquivo de texto: ").strip()
    saida = "invertido.txt"
    try:
        referencias = localizar_inicio_linhas(entrada)
        gerar_arquivo_reverso(entrada, saida, referencias)
        print("Conteúdo invertido salvo em:", saida)
    except FileNotFoundError:
        print("Arquivo não localizado.")
    except Exception as erro:
        print("Erro inesperado:", erro)

if __name__ == "__main__":
    iniciar_processo()
