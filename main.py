import qrcode
import os

# URL you want to convert
url = "https://www.google.com"

# Folder location where you want to save the QR
save_folder = r"C:\Users\Matadeen Yadav\Desktop\Qr_codes"

# Create folder if it does not exist
os.makedirs(save_folder, exist_ok=True)

# File path
file_path = os.path.join(save_folder, "my_qr_code.png")

# Generate QR code
qr_img = qrcode.make(url)

# Save QR code image
qr_img.save(file_path)

print("QR Code saved at:", file_path)


# import qrcode
# from qrcode.constants import ERROR_CORRECT_H

# qr = qrcode.QRCode(
#     version=1,
#     error_correction=ERROR_CORRECT_H,
#     box_size=10,
#     border=4,
# )

# qr.add_data("https://youtube.com")
# qr.make(fit=True)

# img = qr.make_image(fill_color="black", back_color="white")
# img.save("custom_qr.png")
