import base64
from openai import AsyncOpenAI
from config import OPEN_API_KEY

client = AsyncOpenAI(api_key=OPEN_API_KEY)

async def generate_thubmnail(prompt : str, style_prompt: str ,
headshot_url: str) ->  bytes:
    """
    Use the Responses API with gpt-image-2 as a built-in image generation tool.
    Pass the headshot URl directly ad an input-image.
    Returns raw PNG bytes.
    """
    