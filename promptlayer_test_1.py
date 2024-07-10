import openai
import promptlayer
PL_API_KEY = 'pl_**************'
OPENAI_API_KEY = 'sk-*******'

promptlayer.api_key = PL_API_KEY

openai.api_key = OPENAI_API_KEY

# Create a PromptLayer wrapper for OpenAI's ChatCompletion
pl_openai = promptlayer.openai.ChatCompletion
# Use the OpenAI library wrapped with PromptLayer
response = pl_openai.create(
    model='gpt-3.5-turbo',
    messages=[
        {'role': 'system', 'content': 'You are a helpful assistant.'},
        {'role': 'user', 'content': 'Who was the first president of the United States?'}
    ],
    temperature=0.5,
    max_tokens=64,
    pl_tags=['US Presidents']
)

print(response.choices[0].message['content'])
