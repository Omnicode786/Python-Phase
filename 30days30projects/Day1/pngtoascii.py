from PIL import Image

# Load image and convert to grayscale
img = Image.open("30days30projects\\Day1\\nevergonnagiveuup.jpeg")
img = img.resize((100, 50))
img = img.convert('L')

chars = "@%#*+=-:. "
pixels = list(img.getdata())
new_pixels = [chars[pixel * len(chars) // 256] for pixel in pixels]

# Convert to ASCII string
ascii_image = "\n".join("".join(new_pixels[i:i+100]) for i in range(0, len(new_pixels), 100))

# Output result
print(ascii_image)

with open("ascii.txt", "w") as asci:
    asci.write(ascii_image)