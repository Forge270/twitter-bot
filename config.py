import os
from dotenv import load_dotenv

load_dotenv()

# Twitter API credentials
API_KEY = os.getenv('TWITTER_API_KEY', 'your_api_key')
API_SECRET = os.getenv('TWITTER_API_SECRET', 'your_api_secret')
ACCESS_TOKEN = os.getenv('TWITTER_ACCESS_TOKEN', 'your_access_token')
ACCESS_TOKEN_SECRET = os.getenv('TWITTER_ACCESS_TOKEN_SECRET', 'your_access_token_secret')
BEARER_TOKEN = os.getenv('TWITTER_BEARER_TOKEN', 'your_bearer_token')

# Bot ayarlari
BOT_USERNAME = 'YourBotName'

# Takip edilecek hesaplar (retweet/like icin)
ACCOUNTS_TO_MONITOR = [
    'elonmusk',
    'naval',
    'paulg',
]

# Anahtar kelimeler (otomatik yanit icin)
AUTO_REPLY_KEYWORDS = {
    'hello': 'Hi! Thanks for reaching out! How can I help you?',
    'help': 'Need assistance? Visit our website or DM us!',
    'thanks': 'You are welcome! Happy to help!',
}

# Otomatik tweet ayarlari
AUTO_TWEET_ENABLED = True
TWEET_INTERVAL_HOURS = 4

# Ornek tweet'ler (rastgele secilir)
SAMPLE_TWEETS = [
    "Building in public is the best way to learn and grow. What are you working on today?",
    "Consistency beats intensity. Small daily progress adds up to big results.",
    "The best time to start was yesterday. The second best time is now.",
    "Success is not final, failure is not fatal. Keep pushing forward!",
    "Your network is your net worth. Connect with amazing people today!",
]

# Rate limiting
MAX_TWEETS_PER_HOUR = 10
MAX_FOLLOWS_PER_DAY = 50
MAX_LIKES_PER_HOUR = 30

# Log ayarlari
LOG_FILE = 'bot_activity.log'