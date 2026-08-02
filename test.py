import urllib.request
import json

def obter_titulo_yt_music(video_id_ou_url: str) -> str | None:
    # Extrai o ID do vídeo da URL caso passe o link completo
    if "v=" in video_id_ou_url:
        video_id = video_id_ou_url.split("v=")[-1].split("&")[0]
    elif "youtu.be/" in video_id_ou_url:
        video_id = video_id_ou_url.split("youtu.be/")[-1].split("?")[0]
    else:
        video_id = video_id_ou_url

    # Endpoint interno do YouTube Music
    url = "https://music.youtube.com/youtubei/v1/player"
    
    # Payload mínimo simulando a interface da web
    payload = {
        "context": {
            "client": {
                "clientName": "WEB_REMIX", # Cliente do YouTube Music
                "clientVersion": "1.20240101.01.00"
            }
        },
        "videoId": video_id
    }
    
    headers = {
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
    }

    try:
        data_encoded = json.dumps(payload).encode('utf-8')
        req = urllib.request.Request(url, data=data_encoded, headers=headers, method='POST')
        print(url)
        with urllib.request.urlopen(req) as response:
            res_json = json.loads(response.read().decode())
            
            # Pega o título exato e original do vídeo no YouTube
            video_details = res_json.get("videoDetails", {})
            titulo = video_details.get("title")
            
            return video_details

    except Exception as e:
        print(f"Erro ao consultar API: {e}")
        return None

# --- Teste de Exemplo ---
url = "https://www.youtube.com/watch?v=puId0yGZUiY"
titulo = obter_titulo_yt_music(url)

print(f"📌 Título Real: {titulo}")