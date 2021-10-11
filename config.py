import os

TOKEN = os.environ.get("2066417340:AAERvi25V1oe1iV_chpl1VF44Q7FyUHS-xk")
API_HASH = os.environ.get("6ac53d0c86a0afb6c3f1d956304912e0")
API_ID = int(os.environ.get("8973350"))
START_MESSAGE = os.environ.get("START_MESSAGE", "<b>Hi ! I am a simple torrent searcher using @chirag's Torrent Searcher api.\n\n\nMade with 🐍 by @KeralasBots</b>")
FOOTER_TEXT = os.environ.get("search anything", "<b>Made with ❤️ by @chirag</b>")
TORRENTS = {}
