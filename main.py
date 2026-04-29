import requests
import time

# --- بياناتك اللي شغالة تمام ---
bot_token = '8144029970:AAEYdWFWkqCHm54c2Tm59enruFzOH2ZmDPU'
chat_id = '5097916056'

# النادي المفضل
target_club = "Al Ahly" 

# الهيدرز عشان نخدع الموقع إنه داخل من متصفح حقيقي
headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36',
    'Accept': 'application/json, text/plain, */*',
    'Referer': 'https://www.tazkarti.com/'
}

def send_alert(match_name):
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    # الرسالة اللي طلبتها يا يوسف
    msg = f"🚨 الحق يا يوسف ماتش الأهلي نزل حالاً! 🦅🔥\n\nادخل احجز بسرعة من هنا:\nhttps://www.tazkarti.com/#/matches"
    params = {'chat_id': chat_id, 'text': msg}
    try:
        requests.get(url, params=params)
        print("✅ تم إرسال التنبيه لتيلجرام!")
    except:
        print("❌ فشل في إرسال رسالة تيلجرام")

def radar():
    api_url = "https://tazkarti.com/api/Matches/GetMatches"
    
    print(f"🦅 رادار الأهلي شغال يا يوسف.. بفتش كل 15 ثانية...")
    
    while True:
        try:
            # طلب فحص الماتشات
            response = requests.get(api_url, headers=headers, timeout=10)
            
            if response.status_code == 200:
                content = response.text
                # لو لقى كلمة Al Ahly في البيانات اللي جاية من الموقع
                if target_club.lower() in content.lower():
                    print(f"🎯 لقطت الماتش! ببعتلك حالا...")
                    send_alert("الأهلي")
                    # هينبهك ويوقف فحص لمدة 5 دقايق عشان ميغرقش التيلجرام رسايل
                    time.sleep(300) 
                else:
                    print(f"🔍 فحص {time.strftime('%H:%M:%S')}: لسه الماتش منمشيش..")
            else:
                print(f"⚠️ الموقع مبيفتحش (كود {response.status_code})، هحاول تاني كمان شوية.")
                
        except Exception as e:
            print(f"📡 مشكلة في النت: {e}")
            
        # الوقت اللي طلبته (15 ثانية)
        time.sleep(15)

# تشغيل البوت
if __name__ == "__main__":
    radar()

