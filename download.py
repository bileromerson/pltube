import yt_dlp

def baixar_musica():

    try:
        ydl_opts = {
            'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
            # 'cookiefile':'./cookie',
            'writethumbnail': True,
            'addmetadata': True,
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp4',},
                {'key': 'EmbedThumbnail'},
                {'key': 'FFmpegMetadata'}],
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([''])
    except Exception as e:
        print(e,"err")
baixar_musica()