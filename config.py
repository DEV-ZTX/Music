import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = "23568641"
API_HASH = "a39098e8752a45c2d6d1889941547bbc"

# Get your token from @BotFather on Telegram.
BOT_TOKEN = "7833291072:AAEn_HE-Z0mtHkITLzO1gT_nXc9mRjRNLnw"

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = "mongodb+srv://theriyamusic94:f67KlgTyzr3TTutn@cluster0.lym5x.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 60000))

# Set this to true if you want post ads automatically
ADS_MODE = getenv("ADS_MODE", None)

# Chat id of a group for logging bot's activities
LOGGER_ID = int(getenv("LOGGER_ID", "-1002323856532"))

# Get this value from @FallenxBot on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID", 8177810307))

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/DEV-ZTX/Music",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/RIYA_NETWORK")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/RIYA_CHAT_SUPPORT")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", None))


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from @StringFatherBot on Telegram
STRING1 = "1BZWaqwUAUH1Yq3eT21XTtqiQDSauBgvjaADFyutSszGMFg23n2CnVmCjpQnZJJ_7WIGo7kXve8EfpszRpTQGj3UApCOv1DfDj-520yLs3B2efFuRihWSxET_GXR7kQ0ZsPFsFBNAolB5c_i-551x0-fGSJLzgAZX-ovy24BKaNQfJOJEAQy1aDBkjaPKNQs-wL34WM9janIQwGadLAas21xmpNMG5czsFTpnLcrxs4K9Xf12AgtZ2sVIPn48rLIq_8AGGUmioV_FBKI1e4Xizi6FxyIVgFvEZWCbMPPZ4-2Lio-vU_mRpRuvdHxdTFRWAAYhvbOOIPMhUvM4NykGogWAhrg1jMM="
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}

START_VIDEO_URL = getenv(
    "START_VIDEO_URL", "https://files.catbox.moe/9z4hr1.mp4"
)
START_IMG_URL = getenv(
    "START_IMG_URL", "https://files.catbox.moe/8rg2ht.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://files.catbox.moe/8rg2ht.jpg"
)
PLAYLIST_IMG_URL = "https://files.catbox.moe/8rg2ht.jpg"
STATS_IMG_URL = "https://files.catbox.moe/8rg2ht.jpg"
TELEGRAM_AUDIO_URL = "https://files.catbox.moe/8rg2ht.jpg"
TELEGRAM_VIDEO_URL = "https://files.catbox.moe/8rg2ht.jpg"
STREAM_IMG_URL = "https://files.catbox.moe/8rg2ht.jpg"
SOUNCLOUD_IMG_URL = "https://files.catbox.moe/8rg2ht.jpg"
YOUTUBE_IMG_URL = "https://files.catbox.moe/8rg2ht.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://files.catbox.moe/8rg2ht.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://files.catbox.moe/8rg2ht.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://files.catbox.moe/8rg2ht.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
