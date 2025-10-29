# api/chat.py - Vercel Serverless AI
from flask import Flask, request, jsonify
from mcp import MCP
from agent import needs_search, is_weather_question, is_small_talk, search_wiki
from weather import get_weather
from transformers import pipeline

app = Flask(__name__)
generator = pipeline("text2text-generation", model="google/flan-t5-small")
mcp = MCP()

@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.get_json()
        user_input = data.get('message', '').strip()
        if not user_input:
            return jsonify({'error': 'No message'}), 400

        mcp.add_user(user_input)

        if is_small_talk(user_input):
            response = is_small_talk(user_input)
            mcp.add_assistant(response)
            return jsonify({'response': response})

        if is_weather_question(user_input):
            city = user_input.split("in")[-1].strip() if "in" in user_input.lower() else "London"
            fact = get_weather(city)
            mcp.add_fact(fact)
            response = f"Weather in {city}: {fact.split(':')[-1]}"
            mcp.add_assistant(response)
            return jsonify({'response': response})

        if needs_search(user_input):
            fact = search_wiki(user_input)
            mcp.add_fact(fact)

        context = mcp.get_context()
        prompt = f"Answer in 1 short sentence using this: {context}"
        result = generator(prompt, max_length=60, do_sample=False)[0]['generated_text']
        mcp.add_assistant(result)

        return jsonify({'response': result})

    except Exception as e:
        return jsonify({'error': str(e)}), 500
