import base64
import io

from PIL import Image


def watermark():
    """
    Method 1: Method to watermark photos using the Image.paste
    """
    base_image = Image.open("photo.jpeg")
    logo_image = Image.open("logo.png")

    (width, height) = base_image.size

    #   Resizing the logo image to make sure it size should be half of base photo
    logo_image = logo_image.resize((int(width / 2), int(height / 2)))

    # Image object to make water mark image using the logo
    watermark = Image.new('RGB', base_image.size, (0, 0, 0))
    watermark.paste(base_image, (0, 0))

    # add transparency to logo
    logo_image = add_image_transparency(logo_image)

    # get the center position from the images
    position = get_center_position(watermark, logo_image)
    watermark.paste(logo_image, position, mask=logo_image)

    # return the base64 image
    im_file = io.BytesIO()
    watermark.save(im_file, format="JPEG")
    im_bytes = im_file.getvalue()  # i
    watermark.show()
    return base64.b64encode(im_bytes)


def watermark2():
    base_image = Image.open(io.BytesIO(base64.b64decode(image_b64))).convert("RGBA")
    transparent = Image.new('RGBA', base_image.size, (0, 0, 0, 0))

    (width, height) = base_image.size
    watermark = Image.open(io.BytesIO(base64.b64decode(logo_b64)))
    watermark = watermark.resize((int(width / 2), int(height / 2)))
    watermark = self.add_image_transparency(watermark)
    position = get_center_position(transparent, watermark)
    transparent.paste(watermark, position, mask=watermark)

    watermarked = Image.alpha_composite(base_image, transparent)
    im_file = io.BytesIO()
    watermarked.save(im_file, format="PNG")
    im_bytes = im_file.getvalue()  # im_bytes: image in binary format.
    return base64.b64encode(im_bytes)


def add_image_transparency(image, alpha=128):
    # Load image and extract alpha channel
    image_alpha = image.getchannel('A')
    new_alpha = image_alpha.point(lambda i: alpha if i > 0 else 0)
    image.putalpha(new_alpha)
    return image


def get_center_position(image, image2):
    width, height = image.size
    width2, height2 = image2.size
    x = (width - width2) / 2
    y = (height - height2) / 2
    return int(x), int(y)


if __name__ == "__main__":
    watermark()