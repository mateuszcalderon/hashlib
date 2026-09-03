import hashlib

def calculate_hash(file_path: str) -> str | None:
    """
    Calculates the SHA-256 hash code for the given file.
    Args:
        file_path (str): The path to the target file.
    Returns:
        str: The SHA-256 hash code in hexadecimal format if successful.
        None: If the file is missing or an error occurs.
    """
    hash_object = hashlib.sha256()

    try:
        with open(file_path, "rb") as file:
            while chunk := file.read(8192):
                hash_object.update(chunk)
        return hash_object.hexdigest()
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None
    except OSError as error_message:
        print(f"An unexpected error occurred: {error_message}")
        return None

if __name__ == "__main__":
    # Replace my files with your own ones:
    file_a = "example_1.txt"
    file_b = "example_2.txt"

    hash_code_a = calculate_hash(file_a)
    hash_code_b = calculate_hash(file_b)

    if hash_code_a and hash_code_b:
        if hash_code_a == hash_code_b:
            print("Both your files have the exact same hash code")
        else:
            print("Your files have different hash codes")

        print(f"Hash code for {file_a}: {hash_code_a}")
        print(f"Hash code for {file_b}: {hash_code_b}")
    else:
        print("Couldn't calculate the hash codes for your files")