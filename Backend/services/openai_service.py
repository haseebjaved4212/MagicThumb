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

    response = await client.response.create(
        model="gpt-4o",
        input=[
            {"role": "user", 
            "content": [
                {"type": "input_image" , "url": headshot_url},
                {"type": "text", "text": full_prompt},
            ]},
        ],

        tools=[
            {
                "type": "image_generation",
                "model": "gpt-image-2",
                "size": "1536x1024",
                "quality": "high",
                "output_format": "png"
                
                
                
                },],
    )

    for content_block in response.output["content"]:
        if content_block["type"] == "file_generation":
            image_bytes = content_block["file_contents"]
            return image_bytes

    raise ValueError("No image generated")
        