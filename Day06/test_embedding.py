from openai import OpenAI

client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama"
)


text1 = "Python is a programming language."

text2 = "Python is used for software development."

embedding1 = client.embeddings.create(
    model="nomic-embed-text",
    input=text1
).data[0].embedding

embedding2 = client.embeddings.create(
    model="nomic-embed-text",
    input=text2
).data[0].embedding

# print("Embedding for text1:")
# print(embedding1)
# print("Embedding for text2:")
# print(embedding2)
print ("Type of embedding1:", type(embedding1))
print ("Type of embedding2:", type(embedding2))
print("Length of embedding1:", len(embedding1))
print("Length of embedding2:", len(embedding2))

#check first 5 elements of the embedding vectors
for i in range(5):
    print(f"Embedding1[{i}]: {embedding1[i]}")

print()
for i in range(5):
    print(f"Embedding2[{i}]: {embedding2[i]}")
