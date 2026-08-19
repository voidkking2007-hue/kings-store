from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def store():
    lista_scripturi = [
        {
            "title": "Elite Admin Hub",
            "category": "Admin",
            "price": "50 Robux",
            "description": "Comenzi avansate de moderare, ban, kick, fly.",
            "link": "https://discord.gg/dgUp2hUqH"
        },
        {
            "title": "Auto-Farm Pro",
            "category": "Farming",
            "price": "100 Robux",
            "description": "Farming automat optimizat pentru performanță maximă.",
            "link": "https://discord.gg/dgUp2hUqH"
        }
    ]
    return render_template('store.html', scripts=lista_scripturi)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
