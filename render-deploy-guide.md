# Render.com Pe Deploy Kaise Karein

## Quick Deploy Steps:

### 1. Render Account Banao
- https://render.com pe jao
- GitHub se signup karo

### 2. New Web Service Banao
- Dashboard pe "New +" button click karo
- "Web Service" select karo
- GitHub repository connect karo: `manish96852/bothero`

### 3. Settings Fill Karo
- **Name**: `vc-notifier-bot`
- **Environment**: `Python 3`
- **Build Command**: `pip install -r requirements.txt`
- **Start Command**: `python main.py`
- **Instance Type**: Free

### 4. Environment Variables Add Karo
"Environment" tab mein jao aur add karo:

```
API_ID = your_api_id
API_HASH = your_api_hash
SESSION_STRING = your_session_string
CHAT_ID = your_group_chat_id
HEROKU = True
```

### 5. Deploy Button Click Karo!

Bot automatically start ho jayega aur 24/7 chalega! 🚀

## Environment Variables Kaise Milenge:

### API_ID & API_HASH:
1. https://my.telegram.org/apps pe jao
2. Login karo
3. Create application
4. API ID aur API Hash copy karo

### SESSION_STRING:
```bash
python generate_string_session.py
```
Ye run karo aur session string copy karo

### CHAT_ID:
1. Apne group mein @userinfobot add karo
2. Kuch message send karo
3. Bot group ID dega (negative number)

---

**Note:** Render free tier mein bot 15 minutes inactivity ke baad sleep mode mein ja sakta hai. Active rakhne ke liye paid plan ($7/month) ya cron job setup karo.
