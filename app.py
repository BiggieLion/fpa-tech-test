from flask import Flask

from api.api_controller import api_bp

app = Flask(__name__)
app.register_blueprint(api_bp)

if __name__ == "__main__":
    print("Hi")
    app.run(debug=True)
