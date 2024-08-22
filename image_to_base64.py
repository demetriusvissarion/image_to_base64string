import base64
import os

def image_to_base64(image_path):
    """
    Converts an image to a base64 string and saves it to a text file.

    Parameters:
    image_path (str): The file path to the image you want to convert.

    Returns:
    None
    """
    # Read the image file and encode it to base64
    with open(image_path, "rb") as image_file:
        base64_string = base64.b64encode(image_file.read()).decode('utf-8')

    # Get the directory, filename, and extension
    directory, file_name = os.path.split(image_path)
    file_base_name, _ = os.path.splitext(file_name)

    # Construct the output file path
    output_file_path = os.path.join(directory, f"{file_base_name}_base64string.txt")

    # Save the base64 string to the new text file
    with open(output_file_path, "w") as text_file:
        text_file.write(base64_string)

    print(f"Base64 string saved to: {output_file_path}")

# Example usage:
image_path = r'image_file_path'  # Your actual image path
image_to_base64(image_path)

# run in terminal: python image_to_base64.py