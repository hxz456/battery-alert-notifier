from plyer import battery, notification
import time

def send_notification(message):
    """Send a system notification with the given message."""
    notification.notify(
        title="Battery Alert",
        message=message,
        app_name="Battery Alert Notifier",
        app_icon="low-battery.ico",  # Ensure this icon exists in the script directory
        timeout=5,
        toast=True
    )

# Track last notified level to avoid duplicate notifications
last_notified_level = None

while True:
    batt_status = battery.status  

    if batt_status and not batt_status.get('isCharging', False):  # Check if running on battery
        percentage = batt_status.get('percentage', 100)

        if percentage <= 5 and last_notified_level != 5:
            send_notification("🚨 Critical Alert! Battery is below 5%! 🔴\nYour device may shut down soon. Please connect the charger immediately! ⚡")
            last_notified_level = 5
        
        elif percentage <= 10 and last_notified_level != 10:
            send_notification("⚠️ Battery Low! (Below 10%)\nYour device is running low on power. Consider plugging in your charger soon to avoid interruptions. 🔌")
            last_notified_level = 10
        
        elif percentage <= 20 and last_notified_level != 20:
            send_notification("🔋 Battery below 20% ⚡\nYou're getting low on battery. It's a good time to find your charger before it gets critical.")
            last_notified_level = 20
        
        elif percentage <= 30 and last_notified_level != 30:
            send_notification("🔋 Battery below 30%\nYour battery level is getting lower. If you're using a power-intensive app, consider charging soon. ⚡")
            last_notified_level = 30
        
        elif percentage <= 40 and last_notified_level != 40:
            send_notification("🔋 Battery below 40%\nStill in a safe range, but be mindful of prolonged usage without charging. 🔌")
            last_notified_level = 40
        
        elif percentage <= 50 and last_notified_level != 50:
            send_notification("✅ Battery below 50%\nYou're at a balanced battery level! Keep using your device comfortably, but plan ahead for charging.")
            last_notified_level = 50

    time.sleep(90)  # Check every 90 seconds
