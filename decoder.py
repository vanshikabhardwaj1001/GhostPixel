from PIL import Image


def decode(image_path):
    """
    Extract hidden binary data from an image.
    """

    image = Image.open(image_path).convert("RGB")

    pixels = list(image.getdata())

    bits = []

    # Extract LSB from every RGB channel
    for pixel in pixels:

        for value in pixel:

            bits.append(
                str(value & 1)
            )

    # Need at least 32 bits for the length header
    if len(bits) < 32:

        raise ValueError(
            "Image does not contain enough data."
        )

    # First 32 bits contain payload length
    length_bits = ''.join(
        bits[:32]
    )

    data_length = int(
        length_bits,
        2
    )

    # Calculate required number of bits
    required_bits = 32 + (
        data_length * 8
    )

    if required_bits > len(bits):

        raise ValueError(
            "Invalid or corrupted hidden data."
        )

    payload_bits = bits[
        32:required_bits
    ]

    payload = bytearray()

    # Convert binary back to bytes
    for i in range(
        0,
        len(payload_bits),
        8
    ):

        byte = int(
            ''.join(
                payload_bits[i:i + 8]
            ),
            2
        )

        payload.append(byte)

    return bytes(payload)