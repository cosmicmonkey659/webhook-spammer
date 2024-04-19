from dhooks import Webhook, file
import time

print(""""
      _ _                 _                                                    
     | | |               | |                                                   
   __| | |__   ___   ___ | | __  ___ _ __   __ _ _ __ ___  _ __ ___   ___ _ __ 
  / _` | '_ \ / _ \ / _ \| |/ / / __| '_ \ / _` | '_ ` _ \| '_ ` _ \ / _ \ '__|
 | (_| | | | | (_) | (_) |   <  \__ \ |_) | (_| | | | | | | | | | | |  __/ |   
  \__,_|_| |_|\___/ \___/|_|\_\ |___/ .__/ \__,_|_| |_| |_|_| |_| |_|\___|_|   
                                    | |                                        
                                    |_|                                        
      """)

message = input("What do you want to spam: ")
webhook = Webhook(input("What's the webhook: "))
delay = int(input("Enter delay: "))

counter = 0

while True:
    time.sleep(delay)
    webhook.send(message)
    counter += 1
    print(f"{counter}")
