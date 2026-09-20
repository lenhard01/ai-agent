import os


def write_file(working_directory: str, file_path: str, content: str) -> str:
    try:
        base_dir = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(base_dir, file_path))

        if os.path.commonpath([base_dir, target_dir]) != base_dir:
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

        if os.path.isdir(target_dir):
            return f'Error: Cannot write to "{file_path}" as it is a directory'

        os.makedirs(os.path.dirname(target_dir), exist_ok=True)
        with open(target_dir, "w") as f:
            f.write(content)
        return (
            f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
        )
    except Exception as e:
        return f"Error: {e}"
