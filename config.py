from distutils.util import strtobool
from os import getenv

from dotenv import load_dotenv

load_dotenv(".env")


ALIVE_EMOJI = getenv("ALIVE_EMOJI", "👑")
ALIVE_LOGO = getenv("ALIVE_LOGO", "https://telegra.ph//file/a50cdc13cb969841cb577.jpg")
ALIVE_TEKS_CUSTOM = getenv("ALIVE_TEKS_CUSTOM", "Hey bro, I am Arab.")
API_HASH = getenv("API_HASH", "947327cf5ff0053a66bf7951f9db5658")
API_ID = getenv("API_ID", "17896688")
BLACKLIST_CHAT = getenv("BLACKLIST_CHAT", None)
if not BLACKLIST_CHAT:
    BLACKLIST_CHAT = [-1001507828862, -1001571197486]
BLACKLIST_GCAST = {int(x) for x in getenv("BLACKLIST_GCAST", "-1001571197486").split()}
BOTLOG_CHATID = int(getenv("BOTLOG_CHATID") or 0)
BOT_TOKEN = getenv("BOT_TOKEN", None)
BOT_VER = "1.0.3@zika"
BRANCH = getenv("BRANCH", "main") # jangan di ganti kalo ga mau error tolol
CH_SFS = getenv("CH_SFS", "cehaarab") # kalo lu mau ganti minimal follow dulu lah kontol
IG_ALIVE = getenv("IG_ALIVE", "fadhilabdat") # kalo lu mau ganti minimal follow dlu lah kontol
CHANNEL = getenv("CHANNEL", "jasasiarab") # kalo lu mau ganti minimal follow dulu lah kontol
CMD_HANDLER = getenv("CMD_HANDLER", ".")
DB_URL = getenv("DATABASE_URL", "mongodb+srv://fadhil01:fadhil123@fadhil01.s6lkqsq.mongodb.net/?retryWrites=true&w=majority")
GIT_TOKEN = getenv("GIT_TOKEN", "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") # optional punya lo ya kontol
GROUP = getenv("GROUP", "SiArab_Support") # kontol klo lu ganti 
HEROKU_API_KEY = getenv("HEROKU_API_KEY", None)
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", None)
PMPERMIT_PIC = getenv("PMPERMIT_PIC", "https://telegra.ph//file/09e81cc7fd18e90e814e5.jpg")
OPENAI_API_KEY = getenv("OPENAI_API_KEY", "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")
PM_AUTO_BAN = strtobool(getenv("PM_AUTO_BAN", "True"))
REPO_URL = getenv("REPO_URL", "https://github.com/fadhilarab47/PyroUbot")
STRING_SESSION1 = getenv("STRING_SESSION1", "BQAP-GEAWKk1o3ejpMQR4vILM57-8FAQvuwwIoCyX4MRoxu98IJApE84qv0vYgM673PiTNPNL9Fqoc1Ce5gMA5IMUaHoGKsnXPRk3rruhJQKxX8uIvydXx0iizZsZ2ZXgRUkgOHpeYGzCtCAExFjv1uOUaMfE5NHd63eh3cYRRbezjQabggPb-5UkXhIhogn3S-0l27FSUbOL140RojfVPIzjkilqhPZbBKE8ntCN_gZNyM1coSAXNoSwhjmcCqUr3UFk4_SiR07_kjHLmMs7m3xvlY46F-5ZybAeJQmCkaPL88ZYL7iQi7VPfdCyPVZTG7nf04zuB_woSC4Ka8iNxUBC1HojAAAAABr5tUGAA")
STRING_SESSION2 = getenv("STRING_SESSION2", "")
STRING_SESSION3 = getenv("STRING_SESSION3", "")
STRING_SESSION4 = getenv("STRING_SESSION4", "")
STRING_SESSION5 = getenv("STRING_SESSION5", "")
STRING_SESSION6 = getenv("STRING_SESSION6", "")
STRING_SESSION7 = getenv("STRING_SESSION7", "")
STRING_SESSION8 = getenv("STRING_SESSION8", "")
STRING_SESSION9 = getenv("STRING_SESSION9", "")
STRING_SESSION10 = getenv("STRING_SESSION10", "")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1948147616").split()))
