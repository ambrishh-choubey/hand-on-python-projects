import time
from plyer import notification
while True:
    print("please sips some water: ")
    notification.notify(title="please drink some water",message="you need to drink some water",)

    time.sleep(10)
    