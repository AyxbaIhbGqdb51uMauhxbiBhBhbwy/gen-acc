from flask import Flask, jsonify
import random

app = Flask(__name__)

def get_random_account(filename):
    try:
        with open(filename, 'r') as file:
            accounts = file.readlines()

        if not accounts:
            return {"error": "No accounts found"}, 404

        random_account = random.choice(accounts).strip()

        if ":" in random_account:
            username, password = random_account.split(":", 1)
            return {
                "username": username,
                "password": password,
                "combo": random_account
            }, 200
        else:
            return {"error": "Invalid account format"}, 400
    except Exception as e:
        return {"error": str(e)}, 500

@app.route('/api/<platform>', methods=['GET'])
def random_account(platform):
    platform = platform.lower()
    valid_platforms = {
        "roblox": "Account/Roblox.txt",
    }

    if platform in valid_platforms:
        return jsonify(*get_random_account(valid_platforms[platform]))
    else:
        return jsonify({"error": "Invalid platform"}), 400

if __name__ == '__main__':
    app.run(debug=True)
