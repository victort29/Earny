import openai
import json
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app)


openai.organization = ORG_ID
openai.api_key = API_KEY

ENG_Q = [
    {
        "role": "system",
        "content": "You are a financial assistant to help the user make an educated decision to better their finances. Based on the conversation offer your financial advice and add measurable metrics."
    },
    {
        "role": "assistant",
        "content": "Hello! To provide you with the best investment advice, please tell me your age."
    },
    {
        "role": "user",
        "content": "#age"
    },
    {
        "role": "assistant",
        "content": "At what age do you expect to need money for retirement?"
    },
    {
        "role": "user",
        "content": "#retire"
    },
    {
        "role": "assistant",
        "content": "What is your expected net annual income?"
    },
    {
        "role": "user",
        "content": "#income"
    },

    {
        "role": "assistant",
        "content": "content =  Based on your criteria I think To secure a prosperous financial future, start by saving 20 percent of your $60,000 annual income. Your retirement goal of $2 million by age 60 is achievable through a balanced investment mix of 70 percent in stocks and 30 percent in bonds, targeting annual returns of 6-8%. Additionally, maintain an emergency fund equal to three months of living expenses. These steps will set you on a path to financial stability and retirement readiness."

    }
]


@app.route("/this", methods=["GET"])
def get_api_key():

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages= get_array(0,23,45,56000),
        temperature=1.5,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.6,
    )
     
    return json.dumps(response)

    # return json.dumps(response.choices[0].message.content)  # talks to api


def get_array(index, age, retire_age, income):
    global ENG_Q
    if index == 0:
        ENG_Q = solve_message(ENG_Q, age, retire_age, income)
    return ENG_Q


def solve_message(message, age, retire_age, income):
   for item in message:
        if item["role"] == "user":
            if item["content"] == "#age":
                item["content"] = str(age)
            elif item["content"] == "#retire":
                item["content"] = str(retire_age)
            elif item["content"] == "#income":
                item["content"] = str(income)
        return message

if __name__ == "__main__":
    app.run(debug=True)


