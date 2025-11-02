import re, os, time
from os import environ, getenv
id_pattern = re.compile(r'^.\d+$') 



# Fetch initial admin list
ADMIN = [6299192020]  # TemporLoad admins when the bot starts

TOKEN_VERIFY=True
API = environ.get("API", "5a7508a173d6462e4cd4b723766b92541c389a6b") # shortlink api
URL = environ.get("URL", "arolinks.com") # shortlink domain without https://
VERIFY_TUTORIAL = environ.get("VERIFY_TUTORIAL", "https://t.me/+Gt55OVP7VTAyNmNl") # how to open link 
BOT_USERNAME = environ.get("BOT_USERNAME", "Ghjjjoooo_bot") # bot username without @
VERIFY = environ.get("VERIFY", "True") # set True Or False and make sure spelling is correct and first letter capital.
USER_LIMIT_TIME = int(os.environ.get("USER_LIMIT_TIME", "1"))#enter time based on hours

class Config(object):
    # pyro client config
    API_ID    = os.environ.get("API_ID", " 24435985")
    API_HASH  = os.environ.get("API_HASH", "0fec896446625478537e43906a4829f8")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7758738938:AAGwhb8vXtHw9INX8SzCr82PKYtjQJHE-3c") 

    # database config
    DB_NAME = os.environ.get("DB_NAME","Speedwolf1")     
    DB_URL  = os.environ.get("DB_URL","mongodb+srv://Speedwolf1:speedwolf24689@cluster0.rgfywsf.mongodb.net/")
    PORT = os.environ.get("PORT", "8050")
    OWNER = int(os.environ.get("OWNER", "6299192020"))
    PRIVATE_USE = False #If Bot is private use set True otherwise False
 
    # other configs
    BOT_UPTIME  = time.time()
    START_PIC   = os.environ.get("START_PIC", "https://telegra.ph/file/feb6dd0a1cb8576943c0f.jpg")
    
    FORCE_SUB_CHANNELS = os.environ.get('FORCE_SUB_CHANNELS', "anime_warrior_tamil").split(',')
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002201298270" ))
    DUMB_CHANNEL = os.environ.get("DUMB_CHANNEL", "")
    
    # wes response configuration     
    WEBHOOK = bool(os.environ.get("WEBHOOK", "True"))


class Txt(object):
    # part of text configuration
        
    START_TXT = """Hello {} 👋 

➻ This Is An Advanced Auto rename Bot.

➻ Using This Bot You Can Able to Rename Your Files one by one or multi.

➻ You Can Also Select the file type is need to upload.

➻ This Bot is only for Admin use other can use with low limitation 

<b>Bot Is Made By :</b> @Tech_Freak_Tamil"""

    ABOUT_TXT = f"""<b>😈 My Name :</b> <a href='https://t.me/Tech_Freak_Tamil'>Auto Renamer bot ⚡</a>
<b>📝 Language :</b> <a href='https://python.org'>Python 3</a>
<b>📚 Library :</b> <a href='https://pyrogram.org'>Pyrogram 2.0</a>
<b>🚀 Server :</b> <a href='https://heroku.com'>Heroku</a>
<b>📢 Channel :</b> <a href='https://t.me/Tech_Freak_Tamil'>TFT BOTS</a>
<b>🛡️ Disscussion :</b> <a href='https://t.me/+ov2l_dY_8jA3MGVl'>TFT Discussion</a>
    
<b>😈 Bot Made By :</b> https://t.me/+ov2l_dY_8jA3MGVl"""

    HELP_TXT = """
🌌 <b><u>How To Set Thumbnail</u></b>
  
➪ /start - Start The Bot And Send Any Photo To Automatically Set Thumbnail.
➪ /settings - Set Queue, Upload type and metadata 
➪ /del_thumb - Use This Command To Delete Your Old Thumbnail.
➪ /view_thumb - Use This Command To View Your Current Thumbnail.

📑 <b><u>How To Set Custom Caption</u></b>

➪ /set_caption - Use This Command To Set A Custom Caption
➪ /see_caption - Use This Command To View Your Custom Caption
➪ /del_caption - Use This Command To Delete Your Custom Caption
➪ Example - <code>/set_caption 📕 Name ➠ : {filename}

🔗 Size ➠ : {filesize} 

⏰ Duration ➠ : {duration}</code>

"""

    PROGRESS_BAR = """\n
 <b>🔗 Size :</b> {1} | {2}
️ <b>⏳️ Done :</b> {0}%
 <b>🚀 Speed :</b> {3}/s
️ <b>⏰️ ETA :</b> {4}
"""

    DONATE_TXT = """
<b>🥲 Thanks For Showing Interest In Donation! ❤️</b>

If You Like My Bots & Projects, You Can 🎁 Donate Me Any Amount From 10 Rs Upto Your Choice.

<b>🛍 UPI ID:</b> `Now off❌`
"""


    SEND_METADATA = """<b><u>🖼️  HOW TO SET CUSTOM METADATA</u></b>

For Example :-

<code>By :- @Tech_Freak_Tamil</code>

💬 For Any Help Contact @Tech_Freak_Tamil
"""


# Tech freak 
# Don't Remove Credit!!!
# Telegram Channel @Tech_freak_tamil
# Developer @devilo7


