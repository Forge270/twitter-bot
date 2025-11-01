import schedule
import time
from twitter_bot import TwitterBot
import config

def run_bot_cycle():
    """Bot dongusu"""
    bot = TwitterBot()
    bot.run_automation_cycle()

def main():
    print("="*60)
    print("TWITTER BOT SCHEDULER")
    print("="*60)
    print(f"\nBot will run every {config.TWEET_INTERVAL_HOURS} hours")
    print("Press Ctrl+C to stop\n")
    print("="*60)
    
    # Schedule ayarla
    schedule.every(config.TWEET_INTERVAL_HOURS).hours.do(run_bot_cycle)
    
    # Hemen bir kere calistir
    print("\nRunning initial cycle...")
    run_bot_cycle()
    
    # Loop
    while True:
        schedule.run_pending()
        time.sleep(60)  # Her 60 saniyede kontrol et

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nBot stopped by user")
    except Exception as e:
        print(f"\nError: {e}")
        import traceback
        traceback.print_exc()