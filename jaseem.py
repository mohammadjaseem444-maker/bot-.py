import time
import random
import requests

# JASEEM BHAI CONFIG
ZONE_ID = "10672176"
TARGET_URL = "https://earnbucok.blogspot.com/"

def master_mind_bot():
    daily_target = random.randint(30, 100) 
    offset = random.randint(-20, 100)
    final_hits = max(10, daily_target + offset)
    
    print(f"--- OPERATION BOOM STARTING ---")
    for i in range(final_hits):
        try:
            requests.get(f"https://libtl.com/sdk.js?zone={ZONE_ID}", timeout=10)
            print(f"✅ Hit {i+1} Successful!")
            time.sleep(random.randint(180, 420))
        except:
            time.sleep(60)

if __name__ == "__main__":
    master_mind_bot()
  
