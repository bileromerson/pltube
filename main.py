import os
from pltube import *

BASE_DIR = os.getcwd()
SONGS_DIR = os.path.join(BASE_DIR, 'songs')
PLAYLISTS_DIR = os.path.join(BASE_DIR, 'playlists')
LOG_FILE = os.path.join(BASE_DIR, 'links_falhos.txt')
LOG_FILE = os.path.join(BASE_DIR, 'Logs.txt')
ROW = 2 # coluna da URL


def main():
    
    parser = argparse.ArgumentParser(description="How to use Pltube")

    parser.add_argument("-b", "--BaseDir", help="Diretorio base( Diretorio dos CSVs ); padrao e o seu doretorio atual")
    parser.add_argument("-s", "--SongsDir", help="Diretorio para musicas; padrao e /songs")
    parser.add_argument("-p", "--PlaylistDir", help="Diretorio para playlist; padrao e /playlists")
    parser.add_argument("-l", "--LogFile", help="Arquivo de log de error; padrao e /Logs.txt")
    parser.add_argument("-Pl", "--Plataform", help="Plataforma que vai ser feito o download")
    parser.add_argument("-Pp", "--PeriodicPauses", help="Fala para o programa ser cauteloso e faser pausas a cada certa quantidade de musicas, voce tera que aperta enter para sair da pausa; padrao 100")
    parser.add_argument("-u", "--url", help="url do video que voce quer")

    parser.add_argument("--lista", help="Caminho para o arquivo de lista")
    parser.add_argument("--row", help="Pega a coluna responsavelpela url; padrao 2, use - para comessar de tras para frente")
    parser.add_argument("--PlName", help="Indica que o CSV contém o nome da playlist em uma coluna expecifica, criando a playlist a partir do que esta no csv e nao no nome do csv; Ex. --PlName 2")
    parser.add_argument("--mp4", action="store_true", help="baixa os arquivos em mp4")

    parser.add_argument("-a", "--append", action="store_true", help="Ativar modo de atualizacao de dos arquivos")
    parser.add_argument("-Id", action="store_true", help="Indica que o CSV contém apenas os IDs dos vídeos/músicas")
    parser.add_argument('-v', '--version', action='version', version='%(prog)s 2.1')

    return parser.parse_args()

if __name__ == "__main__":
    
    mainVar = main()
    verificar_diretorios(mainVar)

    criar_diretorios()
    csvs = obter_csvs()
    if not csvs:
        print(f"Nenhum arquivo .csv encontrado em: {BASE_DIR}")
    for csv_file in csvs:
        print(f"Processando arquivo: {csv_file}")
        processar_csv(csv_file, mainVar.Id)


# python3 plpython.py --PlName 3 -Id --row 5 -Pp
