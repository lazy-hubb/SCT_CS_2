from PIL import Image

my_picture = Image.open("/home/juveriak/Desktop/test_images/input.jpg")
width, height = my_picture.size
pixels = my_picture.load()

for x in range(width):
    for y in range(height):
        r, g, b = pixels[x, y]
        # XOR encryption - NO COLOR LOSS!
        pixels[x, y] = (r ^ 50, g ^ 50, b ^ 50)

my_picture.save("/home/juveriak/Desktop/test_images/encrypted.jpg")
print("✅ XOR Encryption done!")
