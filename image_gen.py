from PIL import Image, ImageDraw

# Define the dimensions of the image
width = 6000
height = 12000

# Create a new blank image with white background
image = Image.new("RGB", (width, height), "white")

# Save the image
image.save("custom_image.png")

print(f"Custom image with dimensions {width}x{height} created and saved as 'custom_image.png'.")
