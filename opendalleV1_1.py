'''
download the libraries:
!pip install diffusers
!pip install diffusers --upgrade
'''
import torch
from matplotlib import pyplot as plt
from matplotlib import image as mpimg
from matplotlib import image

from diffusers import AutoPipelineForText2Image
import torch
pipeline = AutoPipelineForText2Image.from_pretrained('dataautogpt3/OpenDalleV1.1', torch_dtype=torch.float16).to('cuda')

prompt = "Blockchain technology has the potential to revolutionize the way banks operate, especially in terms of reducing infrastructure costs. The implementation of blockchain in the banking industry can lead to significant cost savings by streamlining processes and eliminating the need for intermediaries."
image = pipeline(prompt, guidance_scale=3.0, num_inference_steps=100).images[0]
plt.imshow(image)
plt.show()
image.save("Social Media OpenDalle-v1.1 gs3n100.png")