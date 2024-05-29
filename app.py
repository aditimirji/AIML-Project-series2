from flask import Flask, request, render_template
import aiml

app = Flask(__name__)

# Initialize the AIML kernel
kernel = aiml.Kernel()
kernel.learn("aiml_files/startup.xml")
kernel.respond("LOAD AIML")  # Ensure AIML files are loaded

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get", methods=["GET", "POST"])
def chat():
    user_message = request.args.get('msg')
    bot_response = kernel.respond(user_message)
    return bot_response

if __name__ == "__main__":
    app.run(debug=True)
