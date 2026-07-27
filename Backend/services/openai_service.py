import base64
from openai import AsyncOpenAI
from config import OPEN_API_KEY

client = AsyncOpenAI(api_key=OPEN_API_KEY)

async def generate_thubmnail(prompt : str, style_prompt: str ,
headshot_url: str) ->  bytes:
    """
    Use the Responses API with gpt-image-2 as a built-in image_generation tool.
    Pass the headshot URl directly ad an input-image.
    Returns raw PNG bytes.
    """
    full_prompt = (
        f"{style_prompt}\n\n"
        f"User reguest : {prompt}\n\n"
        "IMPORTANT : The generated thumbnail  MUST prominently featre the person ."
        "shown in the provided reference headshot photo . keep their likeness accurate. "
''
    ) 

    response = client.response.create(
        model="gpt-4o",
        input="Generate an image of gray tabby cat hugging an other with an orange scarf",
        tools=[{"type": "file_generation"}],
    )