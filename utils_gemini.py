import vertexai
from vertexai.preview.generative_models import GenerativeModel, GenerationConfig, Part, Image

def generate_text(project_id: str, location: str, prompt_text: str, image_path: str) -> str:
    vertexai.init(project=project_id, location=location)
    model = GenerativeModel("gemini-pro-vision")
    prompt = [prompt_text]
    prompt.append(Part.from_image(Image.load_from_file(image_path)))
    response = model.generate_content(
        contents=prompt,
        generation_config=GenerationConfig(
            temperature=0.2,
            top_p=0.6,
            top_k=20,
            max_output_tokens=1000,
        )
    )
    return response.text