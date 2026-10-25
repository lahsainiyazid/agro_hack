from pathlib import Path 
PROMPT_DIR=Path(__file__).resolve().parent
with open (PROMPT_DIR/"answer_prompt.md","r",encoding="utf-8") as f:
    answer_prompt=f.read()
with open (PROMPT_DIR/"expansion_prompt.md","r",encoding="utf-8") as f:
    expansion_prompt=f.read()



print (answer_prompt)
print(expansion_prompt)
