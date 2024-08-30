from PIL import Image
def encrypt_image(input_path, output_path):
    img = Image.open(input_path)
    pixels = img.load()

    width, height = img.size
    for i in range(width):
        for j in range(height):
            r, g, b = pixels[i, j]

            encrypted_pixel = (b, g, r)

            pixels[i, j] = encrypted_pixel

    img.save(output_path)
    print("Image encrypted successfully!")

def decrypt_iamge(input_path, output_path):
    img = Image.open(input_path)
    pixels = img.load()

    width, height = img.size
    for i in range(width):
        for j in range(height):
            r, g, b = pixels[i, j]

            decrypted_pixel = (b, g, r)

            pixels[i, j] = decrypted_pixel

    img.save(output_path)
    print("Image decrypted successfully!")
    input_image = r"/home/mrprofessor/Desktop/Demo/input image"
    encrypted_image = r"/home/mrprofessor/Desktop/Demo/input image"
    decrypted_image = r"/home/mrprofessor/Desktop/Demo"

    encrypt_image(input_image, encrypted_image)
    decrypt_iamge(encrypted_image, decrypted_image)
