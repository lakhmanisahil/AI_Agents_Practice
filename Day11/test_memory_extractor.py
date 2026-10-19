from memory_extractor import extract_memory


memory = extract_memory(
    "What is my name?",
    "Your name is John Doe."

)

print("Extracted Memory:")
print(memory)
