from PIL import Image


def encode(input_image, output_image, data):
    """
    Hide binary data inside a PNG image using LSB steganography.
    """

    image = Image.open(input_image).convert("RGB")

    pixels = list(image.getdata())

    # Store data length in the first 4 bytes
    data_length = len(data)

    length_header = data_length.to_bytes(
        4,
        byteorder="big"
    )

    payload = length_header + data

    # Convert payload to binary
    binary = ''.join(
        format(byte, '08b')
        for byte in payload
    )

    capacity = len(pixels) * 3

    if len(binary) > capacity:
        raise ValueError(
            "Image does not have enough capacity for this message."
        )

    encoded_pixels = []

    bit_index = 0

    for pixel in pixels:

        r, g, b = pixel

        new_pixel = []

        for value in (r, g, b):

            if bit_index < len(binary):

                bit = int(binary[bit_index])

                # Replace LSB
                value = (value & 0xFE) | bit

                bit_index += 1

            new_pixel.append(value)

        encoded_pixels.append(
            tuple(new_pixel)
        )

    encoded_image = Image.new(
        "RGB",
        image.size
    )

    encoded_image.putdata(
        encoded_pixels
    )

    # Always save as PNG
    encoded_image.save(
        output_image,
        "PNG"
    )

    return True