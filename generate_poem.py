def create_poem_file(file_path, content):
    """
    Creates a new text file and writes the given content to it.

    Args:
        file_path (str): The absolute path for the new file.
        content (str): The text content to write to the file.
    """
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f"Successfully generated the poem in '{file_path}'")
    except IOError as e:
        print(f"An error occurred while writing to the file: {e}")

# A simple poem about the art of coding
poem_text = """The cursor blinks, a steady beat,
On screens where logic and art meet.
A world of symbols, black and white,
A silent language in the night."""

# Define the filename and create the file
create_poem_file('d:\\dt-batch15\\poem.txt', poem_text)