"""
This code is a slight modification of perplexity by hugging face
https://huggingface.co/docs/transformers/perplexity

Both this code and the original code are published under the MIT licence.

by Burhan Ul tayyab and Nicholas Chua
"""

from gpt2ppl_fixed import GPT2PPL

# initialize the model
model = GPT2PPL()

print("Please enter your sentence: (Press Enter twice to start processing)")
contents = []
while True:
    line = input()
    if len(line) == 0:
        break
    contents.append(line)
sentence = "\n".join(contents)

model(sentence)
