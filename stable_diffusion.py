from diffusers import StableDiffusionPipeline
import torch

model_id = "runwayml/stable-diffusion-v1-5"
pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
pipe = pipe.to("cuda")

prompt = "Blockchain technology has the potential to revolutionize the way banks operate, especially in terms of reducing infrastructure costs. The implementation of blockchain in the banking industry can lead to significant cost savings by streamlining processes and eliminating the need for intermediaries."
image = pipe(prompt).images[0]
plt.imshow(image)
plt.show()
image.save("Social Media stablediffusion v1.5.png")