from flask import Flask, jsonify
import random

app = Flask(__name__)

def get_random_account(filename):
    try:
        # Membaca file
        with open(filename, 'r') as file:
            accounts = file.readlines()

        # Memastikan file tidak kosong
        if not accounts:
            return {"error": "No accounts found"}, 404

        # Memilih satu baris acak
        random_account = random.choice(accounts).strip()

        # Memisahkan username dan password
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

@app.route('/api/Roblox', methods=['GET'])
def random_roblox_account():
    return jsonify(*get_random_account('Account/Roblox.txt'))

@app.route('/api/Steam', methods=['GET'])
def random_steam_account():
    return jsonify(*get_random_account('Account/Steam.txt'))

@app.route('/api/Crunchyroll', methods=['GET'])
def random_crunchyroll_account():
    return jsonify(*get_random_account('Account/Crunchyroll.txt'))

@app.route('/api/Netflix', methods=['GET'])
def random_netflix_account():
    return jsonify(*get_random_account('Account/Netflix.txt'))

if __name__ == '__main__':
    app.run(debug=True)
