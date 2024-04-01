
- ## Important Warning/Notice:
These models use the GPU (`cuda`), so keep in mind that you must have gpu in your local system if you wanna run the models on your system,
####
or you can use the `Google-colab` and enable the `T4 GPU` for the best experience.
# Text-to-Image (T2I) Generation:
Text-to-image generation is a machine learning technique that uses neural networks to create images from text descriptions.
#### 
Image generators are computer programs that use deep learning algorithms to produce digital images from scratch (usually text) or modify existing ones (usually images). These generators can create highly realistic and complex images, including landscapes, faces, objects, and more.
# 
- Google Colab is here [`Text to Image Generator g-colab`](https://github.com/wavesoumen/Text-to-Image_Generation/blob/main/Text_to_Image_part2.ipynb) for reference.
#
- ### Complete Example:
- Input Prompt (Amla):
```
Amla is a rich source of vitamin C, B complex and antioxidants. These nutrients flush harmful toxins from the body and help fight the harmful free radicals. The presence of anti-inflammatory compounds in amla helps in lowering the levels of inflammation in the body and thus, preventing infections. It also contains immune-enhancing properties, which have a regenerative effect on the immune system and help fight infections better.
```
- Output Generated Image:
![Image3](https://github.com/wavesoumen/Text-to-Image_Generation/blob/main/images/Amla.png)
#
- ## Important Libraries you have to download and install before using the models:
```
pip install diffusers
pip install diffusers --upgrade
pip install GPUtil
import torch
from matplotlib import pyplot as plt
from matplotlib import image as mpimg
from matplotlib import image
from GPUtil import showUtilization as gpu_usage
from numba import cuda
```

## Explanation:
### The most used and popular model for generating Images:
- [Open Dalle](https://github.com/wavesoumen/Text-to-Image_Generation/blob/main/img_opendalle.py)
- [Open Dallev1.1](https://github.com/wavesoumen/Text-to-Image_Generation/blob/main/opendalleV1_1.py)
- [Stable Diffusion](https://github.com/wavesoumen/Text-to-Image_Generation/blob/main/stable_diffusion.py)
- [SDXL Turbo](https://github.com/wavesoumen/Text-to-Image_Generation/blob/main/sdxl_turbo.py)
- SDXL Base 1.0.
- SDXL DPO Turbo
- Playground-v2-1024px-aestheti.

### GPU Checker: Check the GPU from the [mentioned function](https://github.com/wavesoumen/Text-to-Image_Generation/blob/main/gpu_checker.py).
- ## Suggesion:
Firstly, download the libraries to use the models and change the mode from `cpu` to `GPU` or `T4 gpu`. </s>

### Example1 (open-dalle):
- Input Prompt:
```
Blockchain technology has the potential to revolutionize the way banks operate, especially in terms of reducing infrastructure costs. The implementation of blockchain in the banking industry can lead to significant cost savings by streamlining processes and eliminating the need for intermediaries.
```
- Generated Image:
![Image1](https://github.com/wavesoumen/Text-to-Image_Generation/blob/main/images/preview1.png)


### Example2 (open-dallev1.1):
- Input Prompt:
```
Blockchain technology has the potential to revolutionize the way banks operate, especially in terms of reducing infrastructure costs. The implementation of blockchain in the banking industry can lead to significant cost savings by streamlining processes and eliminating the need for intermediaries.
```
- Generated Image:
![Image1](https://github.com/wavesoumen/Text-to-Image_Generation/blob/main/images/preview2.png)

#### 
For any further queries or Explanation, contact me.
#
## - [Soumen Kayal.](https://github.com/wavesoumen)
##### 
https://wavesoumen.github.io/
