from config import client

prompt_ = 'quero um leão perto de uma fogueira em uma noite escura'

response = client.images.generate(
    model='dall-e-3', prompt=prompt_, size='1024x1024', quality='standard', n=1
)

image_url = response.data[0].url
print(image_url)
