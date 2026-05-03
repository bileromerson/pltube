from ytmusicapi import YTMusic

# Isso vai abrir um prompt no terminal.

# Você cola os headers que copiou do navegador lá.

try:
    ytm = YTMusic("headers.json")
    
    # Teste de conexão
    playlists = ytm.get_library_playlists()
    print(f"Conectado com sucesso! Encontradas {len(playlists)} playlists.")
    
except Exception as e:
    print(f"Erro: {e}")