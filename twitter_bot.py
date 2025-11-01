import tweepy
import random
import time
from datetime import datetime
import config

class TwitterBot:
    def __init__(self):
        # Twitter API v2 authentication
        self.client = tweepy.Client(
            bearer_token=config.BEARER_TOKEN,
            consumer_key=config.API_KEY,
            consumer_secret=config.API_SECRET,
            access_token=config.ACCESS_TOKEN,
            access_token_secret=config.ACCESS_TOKEN_SECRET,
            wait_on_rate_limit=True
        )
        
        # API v1.1 for media upload
        auth = tweepy.OAuth1UserHandler(
            config.API_KEY,
            config.API_SECRET,
            config.ACCESS_TOKEN,
            config.ACCESS_TOKEN_SECRET
        )
        self.api = tweepy.API(auth)
        
        self.log_activity("Bot initialized")
    
    def log_activity(self, message):
        """Aktiviteyi logla"""
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        log_message = f"[{timestamp}] {message}"
        print(log_message)
        
        with open(config.LOG_FILE, 'a', encoding='utf-8') as f:
            f.write(log_message + '\n')
    
    def post_tweet(self, text):
        """Tweet gonder"""
        try:
            response = self.client.create_tweet(text=text)
            self.log_activity(f"Tweet posted: {text[:50]}...")
            return response.data['id']
        except Exception as e:
            self.log_activity(f"Error posting tweet: {e}")
            return None
    
    def reply_to_tweet(self, tweet_id, text):
        """Tweet'e cevap ver"""
        try:
            response = self.client.create_tweet(
                text=text,
                in_reply_to_tweet_id=tweet_id
            )
            self.log_activity(f"Replied to tweet {tweet_id}")
            return response.data['id']
        except Exception as e:
            self.log_activity(f"Error replying: {e}")
            return None
    
    def like_tweet(self, tweet_id):
        """Tweet'i beğen"""
        try:
            self.client.like(tweet_id)
            self.log_activity(f"Liked tweet {tweet_id}")
            return True
        except Exception as e:
            self.log_activity(f"Error liking tweet: {e}")
            return False
    
    def retweet(self, tweet_id):
        """Retweet yap"""
        try:
            self.client.retweet(tweet_id)
            self.log_activity(f"Retweeted {tweet_id}")
            return True
        except Exception as e:
            self.log_activity(f"Error retweeting: {e}")
            return False
    
    def follow_user(self, user_id):
        """Kullaniciyi takip et"""
        try:
            self.client.follow_user(user_id)
            self.log_activity(f"Followed user {user_id}")
            return True
        except Exception as e:
            self.log_activity(f"Error following: {e}")
            return False
    
    def get_user_tweets(self, username, max_results=10):
        """Kullanicinin son tweet'lerini al"""
        try:
            user = self.client.get_user(username=username)
            user_id = user.data.id
            
            tweets = self.client.get_users_tweets(
                id=user_id,
                max_results=max_results,
                tweet_fields=['created_at', 'public_metrics']
            )
            
            return tweets.data if tweets.data else []
        except Exception as e:
            self.log_activity(f"Error fetching tweets: {e}")
            return []
    
    def search_tweets(self, query, max_results=10):
        """Tweet ara"""
        try:
            tweets = self.client.search_recent_tweets(
                query=query,
                max_results=max_results,
                tweet_fields=['created_at', 'author_id', 'public_metrics']
            )
            return tweets.data if tweets.data else []
        except Exception as e:
            self.log_activity(f"Error searching tweets: {e}")
            return []
    
    def auto_engage_with_accounts(self):
        """Belirlenen hesaplarla otomatik etkilesim"""
        self.log_activity("Starting auto-engagement...")
        
        for username in config.ACCOUNTS_TO_MONITOR:
            try:
                tweets = self.get_user_tweets(username, max_results=3)
                
                for tweet in tweets:
                    # Like
                    self.like_tweet(tweet.id)
                    time.sleep(2)
                    
                    # Bazen retweet
                    if random.random() < 0.3:  # 30% sansla
                        self.retweet(tweet.id)
                        time.sleep(2)
                
                time.sleep(5)  # Hesaplar arasi bekleme
                
            except Exception as e:
                self.log_activity(f"Error engaging with {username}: {e}")
        
        self.log_activity("Auto-engagement completed")
    
    def auto_reply_to_mentions(self):
        """Mention'lara otomatik cevap ver"""
        try:
            me = self.client.get_me()
            my_id = me.data.id
            
            mentions = self.client.get_users_mentions(
                id=my_id,
                max_results=10,
                tweet_fields=['created_at', 'text']
            )
            
            if not mentions.data:
                self.log_activity("No new mentions")
                return
            
            for mention in mentions.data:
                text = mention.text.lower()
                
                # Anahtar kelime kontrolu
                for keyword, reply in config.AUTO_REPLY_KEYWORDS.items():
                    if keyword in text:
                        self.reply_to_tweet(mention.id, reply)
                        time.sleep(3)
                        break
        
        except Exception as e:
            self.log_activity(f"Error handling mentions: {e}")
    
    def post_random_tweet(self):
        """Rastgele bir tweet gonder"""
        if not config.AUTO_TWEET_ENABLED:
            return
        
        tweet_text = random.choice(config.SAMPLE_TWEETS)
        self.post_tweet(tweet_text)
    
    def run_automation_cycle(self):
        """Tam otomasyon dongusu"""
        self.log_activity("=== Starting automation cycle ===")
        
        # 1. Rastgele tweet at
        if config.AUTO_TWEET_ENABLED:
            self.post_random_tweet()
            time.sleep(5)
        
        # 2. Hesaplarla etkilesim
        self.auto_engage_with_accounts()
        time.sleep(5)
        
        # 3. Mention'lari kontrol et
        self.auto_reply_to_mentions()
        
        self.log_activity("=== Automation cycle completed ===\n")

if __name__ == '__main__':
    bot = TwitterBot()
    
    print("="*60)
    print("TWITTER BOT")
    print("="*60)
    print("\n1. Post Tweet")
    print("2. Auto Engage")
    print("3. Check Mentions")
    print("4. Run Full Cycle")
    print("5. Exit")
    print("="*60)
    
    choice = input("\nSelect option: ")
    
    if choice == '1':
        text = input("Tweet text: ")
        bot.post_tweet(text)
    elif choice == '2':
        bot.auto_engage_with_accounts()
    elif choice == '3':
        bot.auto_reply_to_mentions()
    elif choice == '4':
        bot.run_automation_cycle()
    else:
        print("Exiting...")