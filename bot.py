import discord
from discord.ext import commands
import os, random

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba! Ben {bot.user}, bir Discord sohbet botuyum!')
    


@bot.command()
async def repeat(ctx, times: int, content: str):
    """Repeats a message multiple times."""
    for i in range(times):
        await ctx.send(content)

@bot.command()
async def roll(ctx, dice: str):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('Format has to be in NdN!')
        return
    
@bot.command()
async def bölme(ctx, sayı1: float, sayı2: float):
    """İki sayıyı böler ve sonucu gönderir."""
    if sayı2 == 0:
        await ctx.send("Hata: Bir sayıyı sıfıra bölemezsiniz!")
    else:
        sonuç = sayı1 / sayı2
        await ctx.send(f"{sayı1} / {sayı2} = {sonuç}")

@bot.command()
async def duck(ctx):
    img_name = random.choice(os.listdir('duck'))
    with open(f'duck/{img_name}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def yardımkomut(ctx):
    await ctx.send(f'komutlar şöyledir: her komut $ işareti ile çalışır $kitap $led $ elektriklicihaz $tekkullanımlıkürünler bu komutlar kirlilik hakkında bilgi edinmemmizi sağlar $kirlilik ise kirlilik hakkında görseller atar $mem komik görseller atar $bölme 2 sayı ekleyin ve onları böler $roll ise dediğiniz kelimeyi kaç kere tekrar etmesini istiyorsanız yazın ve tekrar eder.')

@bot.command()
async def kitap(ctx):
    await ctx.send(f'Basılı kitaplar ve dergiler yerine dijital formatları tercih etmek kağıt kullanımını azaltmamız gereklidir.')

@bot.command()
async def led(ctx):
    await ctx.send(f'LED lambalar gibi enerji tasarruflu aydınlatmalar kullanmak, enerji tüketimini önemli ölçüde azaltır.')

@bot.command()
async def elektriklicihaz(ctx):
    await ctx.send(f' Elektrikli cihazları kullanırken enerji verimli modelleri seçmek, gereksiz enerji israfını engeller.')

@bot.command()
async def tekkullanımlıkürünler(ctx):
    await ctx.send(f'Tek kullanımlık ürünler yerine yeniden kullanılabilir ürünler (su şişesi, torba) kullanın.')

@bot.command()
async def kirlilik(ctx):
    img_name = random.choice(os.listdir('kirlilik'))
    with open(f'kirlilik/{img_name}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')


@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)

@bot.command()
async def mem(ctx):
    img_name = random.choice(os.listdir('images'))
    with open(f'images/{img_name}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

print

    
bot.run('')