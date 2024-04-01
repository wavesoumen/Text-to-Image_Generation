from diffusers import AutoPipelineForText2Image

pipe = AutoPipelineForText2Image.from_pretrained("stabilityai/sdxl-turbo", torch_dtype=torch.float16, variant="fp16")
pipe.to("cuda")

prompt = "Blockchain technology has the potential to revolutionize the way banks operate, especially in terms of reducing infrastructure costs. The implementation of blockchain in the banking industry can lead to significant cost savings by streamlining processes and eliminating the need for intermediaries."
image = pipe(prompt).images[0]
plt.imshow(image)
plt.show()
image.save("Social Media sdxl-turbo.png")