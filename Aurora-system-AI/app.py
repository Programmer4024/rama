from flask import Flask, request, jsonify
from flask_cors import CORS
import pyautogui
import os
import psutil  # Import added at the top

app = Flask(__name__)
CORS(app)

@app.route('/execute', methods=['POST'])
def execute_task():
    data = request.json
    task = data.get("task", "").lower()

    # --- CHAT COMMANDS ---
    if "hello" in task or "hi" in task:
        return jsonify({"status": "Hello! I am Aurora."})
    
    # --- BATTERY COMMAND (The fix is here) ---
    elif "battery" in task:
        battery = psutil.sensors_battery()
        if battery:
            # We must return this as a 'status' so the HTML can see it
            return jsonify({"status": f"Battery found! Level: {battery.percent}%"})
        else:
            return jsonify({"status": "Battery not detected (Are you on a Desktop PC?)"})

    # --- SYSTEM COMMANDS ---
    elif "notepad" in task:
        os.system("start notepad")
        return jsonify({"status": "I have opened Notepad for you."})
    
    elif "search for" in task:
        import webbrowser
        query = task.split("search for")[-1].strip()
        webbrowser.open(f"https://www.google.com/search?q={query}")
        return jsonify({"status": f"Searching Google for {query}"})

    elif "screenshot" in task:
        pyautogui.screenshot("ai_screenshot.png")
        return jsonify({"status": "Screenshot saved!"})

    else:
        return jsonify({"status": f"I heard '{task}', but I don't know that command."})

if __name__ == '__main__':
    app.run(port=5000)
