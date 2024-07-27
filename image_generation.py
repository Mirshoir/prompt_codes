from openai import OpenAI

client = OpenAI()
api_key = 'your-api-key-here'

response = client.images.generate(
    model="dall-e-3",
    prompt="Generate an insect robot preparing a delicious meal",
    size="512x512",
    quality="standard",
    n=1,

)

image_url = response.data[0].url
print(image_url)
