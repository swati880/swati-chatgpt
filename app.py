from flask import Flask
import openai

openai.api_key = ''


app = Flask(__name__)
@app.route("/") 
def chatcompletion():
  content = input("User:")
  completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
      {"role": "user", "content": content}
    ]
  )

  return print(completion.choices[0].message.content)

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)