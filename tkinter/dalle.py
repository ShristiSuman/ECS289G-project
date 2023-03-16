import os
import openai

# openai.api_key = "my_key"
openai.api_key = "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"

def generate_visual_character(input_prompt):
    response = openai.Image.create(
        prompt=input_prompt,
        n=1,
        size="256x256",
    )

    return response["data"][0]["url"]
