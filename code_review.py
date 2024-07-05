from langchain_community.llms import Ollama

# Initialize the LLM model
llms = Ollama(model="phi")

with open('./code.py', 'r') as file:
    code_content = file.read()

def generate_response(llms, role_inputs):
    # Combine the role-based inputs
    prompt = ""
    for role_input in role_inputs:
        role = role_input['role']
        content = role_input['content']
        prompt += f"{role}: {content}\n"

    # Invoke the model
    response = llms.invoke(prompt)

    # Return the response
    return response

# Example usage
role_inputs = [
    {'role': 'system',
     'content': 'You are a code review assistant. Provide detailed suggestions to improve the given Python code.'},
    {'role': 'user', 'content': code_content},
]

# Get the response
response = generate_response(llms, role_inputs)

# Print the conversation with roles
for role_input in role_inputs:
    role = role_input['role']
    content = role_input['content']
    print(f"{role.capitalize()}: {content.strip()}")
print(f"Assistant: {response.strip()}")
