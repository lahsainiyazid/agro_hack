with open ("./answer_prompt.md","r",encoding="utf-8") as f:
    answer_prompt=f.read()
with open ("./expansion_prompt.md","r",encoding="utf-8") as f:
    expansion_prompt=f.read()



print (answer_prompt)
print(expansion_prompt)
