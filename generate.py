from diffusers import StableDiffusionPipeline
import torch

# load model free
pipe = StableDiffusionPipeline.from_pretrained(
    "runwayml/stable-diffusion-v1-5",
    torch_dtype=torch.float16
).to("cuda")

def predict(prompt: str):
    img = pipe(prompt).images[0]
    img.save("output.png")
    return "output.png"