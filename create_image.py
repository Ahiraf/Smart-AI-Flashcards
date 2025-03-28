from PIL import Image, ImageDraw, ImageFont
import textwrap

def create_term_image(term, meaning, output_path="output.png"):
    img_width, img_height = 800, 500
    bg_color = "#eef6e7"
    
    img = Image.new("RGB", (img_width, img_height), bg_color)
    draw = ImageDraw.Draw(img)

    term_font = ImageFont.load_default(40)
    meaning_font = ImageFont.load_default(20)

    term_x, term_y = 50, 50
    draw.text((term_x, term_y), f"{term}", fill="#2d7f4f", font=term_font)

    max_width = 80
    wrapped_text = textwrap.fill(f"{meaning}", width=max_width)
    
    meaning_x, meaning_y = 50, 150
    draw.text((meaning_x, meaning_y), wrapped_text, fill="#123b4f", font=meaning_font)

    output_path = f"/Users/_kodiko_/Desktop/ Code/FlashCards/{term}.png"
    img.save(output_path)
    print(f"Image saved as {output_path}")