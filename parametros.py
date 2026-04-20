import argparse

def main():

    parser = argparse.ArgumentParser(description="Meu script de automação")

    parser.add_argument("-u", "--url", help="A URL para processar")
    
    # Ex: Um argumento que espera uma lista ou nome (ex: Lista de reprodução)
    parser.add_argument("", "--lista", help="Caminho para o arquivo de lista")

    parser.add_argument("-a", "--append", action="store_true", help="Ativar modo de atualizacao de dos arquivos")
    
    args = parser.parse_args()

    # 4. Usa os valores no seu código

if __name__ == "__main__":
    main()