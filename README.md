# Twitter Bot | Twitter Botu

[English](#english) | [Türkçe](#turkish)

---

<a name="english"></a>
## 🇬🇧 English

Automated Twitter bot for engagement, posting, and account management.

### Features

- 🐦 Automated tweet posting
- 🔄 Auto-retweet & like from monitored accounts
- 💬 Keyword-based auto-replies
- ⏰ Scheduled posting
- 📊 Activity logging
- 🛡️ Rate limiting protection

### Tech Stack

- Python 3.10+
- Tweepy (Twitter API v2)
- Schedule (task scheduling)
- python-dotenv (config management)

### Installation

```bash
pip install -r requirements.txt
```

### Twitter API Setup

1. Go to https://developer.twitter.com
2. Create a new App
3. Get API credentials
4. Create `.env` file:

```env
TWITTER_API_KEY=your_key
TWITTER_API_SECRET=your_secret
TWITTER_ACCESS_TOKEN=your_token
TWITTER_ACCESS_TOKEN_SECRET=your_token_secret
TWITTER_BEARER_TOKEN=your_bearer_token
```

### Configuration

Edit `config.py`:

```python
ACCOUNTS_TO_MONITOR = ['elonmusk', 'naval', 'paulg']
TWEET_INTERVAL_HOURS = 4
AUTO_REPLY_KEYWORDS = {
    'hello': 'Hi! How can I help?',
    'help': 'Visit our website!',
}
```

### Usage

**Manual Mode:**
```bash
python twitter_bot.py
```

**Automated Mode (Scheduler):**
```bash
python scheduler.py
```

Bot runs automatically every 4 hours.

### Features Explained

**Auto-Engagement:**
- Monitors specified accounts
- Auto-likes their recent tweets
- Occasionally retweets (30% chance)

**Auto-Reply:**
- Detects keywords in mentions
- Sends predefined responses

**Scheduled Posting:**
- Posts random tweets from predefined list
- Configurable interval

### Safety

- Built-in rate limiting
- Activity logging to file
- Respects Twitter API limits

### Use Cases

- Brand presence automation
- Content distribution
- Community engagement
- Influencer interaction
- Personal brand building

### ⚠️ Warnings

- Don't exceed Twitter API limits
- Avoid spam-like behavior
- Test in sandbox mode first
- Review Twitter's automation rules

### License

MIT

---

<a name="turkish"></a>
## 🇹🇷 Türkçe

Etkileşim, paylaşım ve hesap yönetimi için otomatik Twitter botu.

### Özellikler

- 🐦 Otomatik tweet paylaşımı
- 🔄 İzlenen hesaplardan oto-retweet ve beğeni
- 💬 Anahtar kelime bazlı otomatik yanıtlar
- ⏰ Zamanlanmış paylaşım
- 📊 Aktivite kayıt tutma
- 🛡️ Hız sınırı koruması

### Teknolojiler

- Python 3.10+
- Tweepy (Twitter API v2)
- Schedule (görev zamanlama)
- python-dotenv (yapılandırma yönetimi)

### Kurulum

```bash
pip install -r requirements.txt
```

### Twitter API Ayarları

1. https://developer.twitter.com adresine gidin
2. Yeni bir App oluşturun
3. API bilgilerini alın
4. `.env` dosyası oluşturun:

```env
TWITTER_API_KEY=api_anahtariniz
TWITTER_API_SECRET=api_secret
TWITTER_ACCESS_TOKEN=access_token
TWITTER_ACCESS_TOKEN_SECRET=token_secret
TWITTER_BEARER_TOKEN=bearer_token
```

### Yapılandırma

`config.py` dosyasını düzenleyin:

```python
ACCOUNTS_TO_MONITOR = ['elonmusk', 'naval', 'paulg']
TWEET_INTERVAL_HOURS = 4
AUTO_REPLY_KEYWORDS = {
    'merhaba': 'Merhaba! Nasıl yardımcı olabilirim?',
    'yardım': 'Web sitemizi ziyaret edin!',
}
```

### Kullanım

**Manuel Mod:**
```bash
python twitter_bot.py
```

**Otomatik Mod (Zamanlayıcı):**
```bash
python scheduler.py
```

Bot her 4 saatte bir otomatik çalışır.

### Özellik Açıklamaları

**Otomatik Etkileşim:**
- Belirtilen hesapları izler
- Son tweetlerini otomatik beğenir
- Zaman zaman retweet yapar (%30 şans)

**Otomatik Yanıt:**
- Mention'larda anahtar kelimeleri tespit eder
- Önceden tanımlı yanıtlar gönderir

**Zamanlanmış Paylaşım:**
- Önceden tanımlı listeden rastgele tweet atar
- Yapılandırılabilir aralık

### Güvenlik

- Yerleşik hız sınırlama
- Dosyaya aktivite kaydı
- Twitter API limitlerini respects

### Kullanım Alanları

- Marka varlığı otomasyonu
- İçerik dağıtımı
- Topluluk etkileşimi
- Influencer iletişimi
- Kişisel marka oluşturma

### ⚠️ Uyarılar

- Twitter API limitlerini aşmayın
- Spam benzeri davranışlardan kaçının
- Önce test modunda deneyin
- Twitter'ın otomasyon kurallarını inceleyin

### Lisans

MIT

---

Built with ⚡ by [Forge270](https://github.com/Forge270)
