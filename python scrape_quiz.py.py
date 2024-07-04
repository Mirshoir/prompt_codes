from langchain_community.llms import Ollama

# Initialize the LLM model
llms = Ollama(model="phi")


def generate_response(llms, role_inputs):
    # Combine the role-based inputs
    prompt = ""
    for role, text in role_inputs:
        prompt += f"{role}: {text}\n"

    # Invoke the model
    response = llms.invoke(prompt)

    # Return the response
    return response


# Example usage
role_inputs = [
    ("system",
     "You are a sentiment analysis model. You classify the given text into one of three categories: neutral, negative, or positive."),
    ("user", "Classify the text into neutral, negative, or positive.\nText: I think the food was okay.\nSentiment:")
]

# Get the response
response = generate_response(llms, role_inputs)

# Print the conversation with roles
for role, text in role_inputs:
    print(f"{role.capitalize()}: {text.strip()}")
print(f"Assistant: {response.strip()}")
