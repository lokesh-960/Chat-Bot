import os

from flask import Flask, render_template, request
from google import genai

app = Flask(__name__)

api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key) if api_key else None

@app.route("/", methods=["GET", "POST"])
def home():

    answer = ""

    if request.method == "POST":

        if client is None:
            answer = "Set the GEMINI_API_KEY environment variable to use the chatbot."
            return render_template(
                "index.html",
                answer=answer
            )

        user_message = request.form["message"]

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=user_message
        )

        answer = response.text

    return render_template(
        "index.html",
        answer=answer
    )

if __name__ == "__main__":
    app.run(debug=True)