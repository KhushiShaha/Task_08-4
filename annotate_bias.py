# Bias Term Annotator Script
import re

BIAS_TERMS = ["struggling", "improved", "failure", "deserves", "talented", "lacks", "excellent", "unreliable"]

def find_bias_terms(text):
    return [term for term in BIAS_TERMS if re.search(rf"\b{term}\b", text, re.IGNORECASE)]

# Run on Claude output
with open("../outputs/claude_confirmation_output.txt", "r") as f:
    content = f.read()
    terms = find_bias_terms(content)
    print("Claude bias terms:", terms)

# Run on ChatGPT output
with open("../outputs/chatgpt_framing_output.txt", "r") as f:
    content = f.read()
    terms = find_bias_terms(content)
    print("ChatGPT bias terms:", terms)
