with open ("/home/yazid/agro/rag/prompts/answer.md","r",encoding="utf-8") as f:
    expansion_prompt=f.read()

with open("/home/yazid/agro/rag/prompts/expansion.md","r",encoding="utf-8") as f:
    answer_prompt=f.read()

print(f"Our expansion prompt is {expansion_prompt}")
print(f"Our prompt is {answer_prompt}")
