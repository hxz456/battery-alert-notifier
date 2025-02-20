from plyer import battery, notification
import time

def send_notification(message):
    """Send a system notification with the given message."""
    notification.notify(
        title="Battery Alert",
        message=message,
        app_name="Battery Alert Notifier",
        app_icon="low-battery.ico",
        timeout=5,
        toast=True
    )

while True:
    batt_status = battery.status  

    if batt_status and not batt_status.get('isCharging', False):
        percentage = batt_status.get('percentage', 100)

        if percentage == 5:
            send_notification("🚨 Critical Alert! Battery is below 5%! 🔴\nYour device may shut down soon. Please connect the charger immediately! ⚡")
        elif percentage == 10:
            send_notification("⚠️ Battery Low! (10%)\nYour device is running low on power. Consider plugging in your charger soon to avoid interruptions. 🔌")
        elif percentage == 20:
            send_notification("🔋 Battery at 20% ⚡\nYou're getting low on battery. It's a good time to find your charger before it gets critical.")
        elif percentage == 30:
            send_notification("🔋 Battery at 30%\nYour battery level is getting lower. If you're using a power-intensive app, consider charging soon. ⚡")
        elif percentage == 40:
            send_notification("🔋 Battery at 40%\nStill in a safe range, but be mindful of prolonged usage without charging. 🔌")
        elif percentage == 50:
            send_notification("✅ Battery at 50%\nYou're at a balanced battery level! Keep using your device comfortably, but plan ahead for charging.")

    time.sleep(90)