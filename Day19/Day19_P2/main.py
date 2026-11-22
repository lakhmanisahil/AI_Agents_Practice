from model import model
from prompt import prompt

messages = prompt.invoke(
    {
        "question": "What is an autonomous AI agent? How will it impact robotics? and is it a good idea to use it in robotics? and what are the benefits and limitations of using it in robotics?"
    }
)

response = model.invoke(messages)

print(response.content)

