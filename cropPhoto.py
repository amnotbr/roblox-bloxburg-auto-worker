import cv2
from PIL import Pillow


def crop_image():
    try:
        img = Image.open(image_path)
        cropped_img = img.crop((left, upper, right, lower))
        cropped_img.save(output_path)
        print(f"Image cropped and saved to {output_path}")
    except FileNotFoundError:
        print(f"Error: image not found at {image_path}")
    except Exception as e:
        print(f"ERROR: {e}")

def main():
	pass
	

if __name__ == "__main__":
	main()
