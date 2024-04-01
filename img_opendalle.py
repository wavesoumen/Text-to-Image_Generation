'''
download the libraries:
!pip install diffusers
!pip install diffusers --upgrade
'''
import torch
from matplotlib import pyplot as plt
from matplotlib import image as mpimg
from matplotlib import image

# download the model,
from diffusers import AutoPipelineForText2Image
import torch
pipeline = AutoPipelineForText2Image.from_pretrained('dataautogpt3/OpenDalle', torch_dtype=torch.float16).to('cuda')

# use prompt for result,
image = pipeline('Blockchain technology has the potential to revolutionize the way banks operate, especially in terms of reducing infrastructure costs. The implementation of blockchain in the banking industry can lead to significant cost savings by streamlining processes and eliminating the need for intermediaries.').images[0]
plt.imshow(image)
plt.show()
image.save("Social Media OpenDalle.png")