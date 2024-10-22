import discord
import feedparser
import asyncio

TOKEN = #Token del bot
RSS_URL = ['https://rss.app/feeds/kBdLV7ZZZBlnHSN0.xml','https://rss.app/feeds/tKfsoEf15ehcMaOd.xml'] #RSS de las paginas
ID_CHANNEL = #ID del canal

client = discord.Client()

def obtener_noticias():
    todas_las_noticias = []
    for feed_url in RSS_URL:
        feed = feedparser.parse(feed_url)
        todas_las_noticias.extend(feed.entries)
    return todas_las_noticias

async def publicar_noticias():
    await client.wait_until_ready()
    canal = client.get_channel(ID_CHANNEL)
    publicadas = []
    while not client.is_closed():
     noticias = obtener_noticias()
     for noticia in noticias[:5]:  # Limita a las 5 últimas noticias de cada feed
        if noticia.link not in publicadas:
            await canal.send(f"**{noticia.title}**\n{noticia.link}")
            publicadas.append(noticia.link)
        await asyncio.sleep(3600)  # Espera 1 hora entre publicaciones


@client.event #Inicializacion del bot
async def on_ready():
    print(f'Bot conectado como {client.user}')

client.loop.create_task(publicar_noticias())
client.run(TOKEN)
