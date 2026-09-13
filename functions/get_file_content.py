def get_file_content(working_directory: str, file_path: str) -> str:
    if file_path != working_directory:
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

    if not os.path.isfile(file_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'
