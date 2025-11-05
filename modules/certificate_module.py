from PIL import Image, ImageDraw, ImageFont
import os

def generate_certificate(record):
    # Image size
    width, height = 800, 600
    img = Image.new('RGB', (width, height), color='white')
    draw = ImageDraw.Draw(img)

    # Fonts (adjust if needed)
    try:
        title_font = ImageFont.truetype("arialbd.ttf", 40)
        body_font = ImageFont.truetype("arial.ttf", 24)
    except:
        title_font = ImageFont.load_default()
        body_font = ImageFont.load_default()

    # Certificate title
    draw.text((width//2, 50), "VACCINATION CERTIFICATE", font=title_font, fill="black", anchor="ms")

    # Patient information
    draw.text((100, 150), f"ID: {record['ID']}", font=body_font, fill="black")
    draw.text((100, 200), f"Name: {record['Name']}", font=body_font, fill="black")
    draw.text((100, 250), f"Vaccine: {record['Vaccine']}", font=body_font, fill="black")
    draw.text((100, 300), f"Dose: {record['Dose']}", font=body_font, fill="black")
    draw.text((100, 350), f"Date: {record['Date']}", font=body_font, fill="black")

    # Footer
    draw.text((width//2, 500), "Certified by Ministry of Health", font=body_font, fill="black", anchor="ms")

    # Save certificate image
    file_name = f"certificate_{record['ID']}.png"
    img.save(file_name)
    print(f"Certificate image saved: {file_name}")
    return file_name
