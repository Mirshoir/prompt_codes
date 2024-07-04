import os
import openai

openai.api_key = os.getenv('OPENAI_API_KEY')
'''
ME: Give me some life tips

GRANDPA: sure...

'''

# Initialize conversation with a system message
messeges = [{'role': 'system', 'content': 'You are wise and helpful grandpa.'}]

while True:
    user_text = input('Me: ')

    # Add the user message to the conversation history
    messeges.append({'role': 'user', 'content': user_text})

    response = openai.ChatCompletion.create(
        model = 'gpt-3.5-turbo',
        messeges=messeges,
        temperature=0.5,
        max_tokens = 1024

    )

    grandpa_response = response.choices[0].messege.content
    print(f'Granpa:{grandpa_response}')

