from flask import Flask, render_template, request, redirect, url_for
import processor

app = Flask(__name__, template_folder='templates', static_folder="static")

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == 'POST':
        # Handle form submission or any other POST request here if needed
        pass
    return render_template('index.html', **locals())

@app.route('/quiz')
def quiz():
    return render_template('quiz.html')

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(processor.chatbot_response(userText))

if __name__ == '__main__':
    app.run(debug=True)