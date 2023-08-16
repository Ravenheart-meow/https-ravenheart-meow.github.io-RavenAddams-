from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

# Set up your OpenAI API credentials
openai.api_key = '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'

@app.route('/get-response', methods=['POST'])
def get_response():
    user_message = request.json.get('message')
    
    # Generate a response from the AI
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=user_message,
        max_tokens=50,
        temperature=0.7
    )

    return jsonify({'response': response.choices[0].text.strip()})

if __name__ == '__main__':
    app.run(debug=True)
