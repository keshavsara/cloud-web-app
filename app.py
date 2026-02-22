from flask import Flask

# create flask app FIRST
app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>🚀 Flask Web Application</h1>
    <p>Deployed on AWS EC2</p>
    <p>Status: Running ✅</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
