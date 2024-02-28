from dhooks import Webhook, file
import time
print(""""
█▀▄▀█ ▄▀█ █▀▄ █▀▀     █▄▄ █▄█     ░░█ █▄█ █▄█ █▄█ █▄█     █▀█ █▄░█     █▀▄ █ █▀ █▀▀ █▀█ █▀█ █▀▄
█░▀░█ █▀█ █▄▀ ██▄     █▄█ ░█░     █▄█ ░█░ ░█░ ░█░ ░█░     █▄█ █░▀█     █▄▀ █ ▄█ █▄▄ █▄█ █▀▄ █▄▀
      """)

message = input("What do you want to spam: ")
webhook = Webhook(input("what the webhook: "))
delay = int(input("Enter delay: "))

while True:
    time.sleep(delay)
    webhook.send(message)
    print("Send.")