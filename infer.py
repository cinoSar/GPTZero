"""
This code a slight modification of perplexity by hugging face
https://huggingface.co/docs/transformers/perplexity

Both this code and the orignal code are published under the MIT license.

by Burhan Ul tayyab and Nicholas Chua
"""
import warnings
from gpt2ppl_fixed import GPT2PPL

warnings.filterwarnings("ignore", category=FutureWarning, module="huggingface_hub")
# initialize the model
model = GPT2PPL()

sentence = "your text here"

model(sentence)
