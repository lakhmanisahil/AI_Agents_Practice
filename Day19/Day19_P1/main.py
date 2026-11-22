from model import model

response = model.invoke(
    "Explain what an robotics software engineer is and what their role is and how to prepare for it in ten sentences."
)

print(response.content)
