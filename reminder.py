import time
import os
import random


def send_reminder():
    prompts = [
        "Are you focusing on your most important task right now?",
        "Have you set clear goals for today's work?",
        "What's your main priority for the next hour?",
        "Are you adhering to your planned schedule today?",
        "How can you minimize distractions right now?",
        "Have you taken a short break to recharge?",
        "What task can you complete in the next 30 minutes?",
        "Are you making progress on your key objectives?",
        "Is there a smaller task you can finish quickly to boost momentum?",
        "Have you reviewed and adjusted your priorities for the day?",
        "What's the next actionable step on your current task?",
        "Are you managing your time effectively today?",
        "How can you organize your workspace to improve focus?",
        "What's one goal you can achieve by the end of the day?",
        "Are you keeping track of your accomplishments and learnings?",
    ]

    prompt = random.choice(prompts)
    script = f"""osascript -e 'tell app "System Events" to display dialog "{prompt}" buttons {{"OK"}} default button 1 with title "Accountability Coach Reminder"' -e 'if button returned of result is "OK" then' -e 'tell app "Google Chrome" to open location "https://chat.openai.com"' -e 'end if' """
    os.system(script)


def start_reminders(interval):
    while True:
        send_reminder()
        time.sleep(interval)


reminder_interval = 3600  # 1 hour
start_reminders(reminder_interval)
