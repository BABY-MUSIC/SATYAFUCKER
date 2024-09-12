import logging

from telethon import TelegramClient

from os import getenv
from UTTAM.data import ALTRON


logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s', level=logging.WARNING)


# VALUES REQUIRED FOR XBOTS
API_ID = "16457832"
API_HASH = "3030874d0befdb5d05597deacc3e83ab"
CMD_HNDLR = getenv("CMD_HNDLR", default=".")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", None)
HEROKU_API_KEY = getenv("HEROKU_API_KEY", "HRKU-efe7e773-ab14-432e-b4be-9197a78d9c41")

BOT_TOKEN = getenv("BOT_TOKEN", default=None)
BOT_TOKEN2 = getenv("BOT_TOKEN2", default=None)
BOT_TOKEN3 = getenv("BOT_TOKEN3", default=None)
BOT_TOKEN4 = getenv("BOT_TOKEN4", default=None)
BOT_TOKEN5 = getenv("BOT_TOKEN5", default=None)
BOT_TOKEN6 = getenv("BOT_TOKEN6", default=None)
BOT_TOKEN7 = getenv("BOT_TOKEN7", default=None)
BOT_TOKEN8 = getenv("BOT_TOKEN8", default=None)
BOT_TOKEN9 = getenv("BOT_TOKEN9", default=None)
BOT_TOKEN10 = getenv("BOT_TOKEN10", default=None)

SUDO_USERS = list(map(lambda x: int(x), getenv("SUDO_USERS", default="7400383704").split()))
for x in ALTRON:
    SUDO_USERS.append(x)
OWNER_ID = int(getenv("OWNER_ID", default="7400383704"))
SUDO_USERS.append(OWNER_ID)


# ------------- CLIENTS -------------

X1 = TelegramClient('X1', API_ID, API_HASH).start(bot_token=7313428181:AAHPAqj8RcB3sK89ST8NQp6dvEl6cu541mg)
X2 = TelegramClient('X2', API_ID, API_HASH).start(bot_token=7490888218:AAFboGV-9eHoTiFNgBxzy4vZEAsbg0PwbzQ)
X3 = TelegramClient('X3', API_ID, API_HASH).start(bot_token=7142412211:AAE4cmjCb2Zp4batwEgfIhlDknmg13Ba8wU)
X4 = TelegramClient('X4', API_ID, API_HASH).start(bot_token=7356183264:AAEYcFcefOmuG2uYg5QpZIw4rTk1tO0aXk4)
X5 = TelegramClient('X5', API_ID, API_HASH).start(bot_token=7471498613:AAGS1iZwhK9nQfm82NpCPbbn6ffm2Krptb4)
X6 = TelegramClient('X6', API_ID, API_HASH).start(bot_token=7445601741:AAElf5QSBA-t1pkpVfe7kBqPoznz6NuKKbc)
X7 = TelegramClient('X7', API_ID, API_HASH).start(bot_token=7448812799:AAHxgrESPhMVBgnneFluxCMHEe5w_fuRs8M)
X8 = TelegramClient('X8', API_ID, API_HASH).start(bot_token=6443871444:AAGLEmtZfBLHkMDdav6Bf8eSD7DC8SckZiM)
X9 = TelegramClient('X9', API_ID, API_HASH).start(bot_token=6620616856:AAF-0qqP3VCatW_P0uNd5EczHLs-S3bLS1k)
X10 = TelegramClient('X10', API_ID, API_HASH).start(bot_token=7200164571:AAGr-MwIUW4vcqFx-N-oly5c9EA3SI7O_Ys)
