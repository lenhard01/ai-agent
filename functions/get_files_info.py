import os


def get_files_info(working_directory: str, directory: str = ".") -> str:
    try:
        base_dir = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(base_dir, directory))
        entries = []

        # Will be True or False
        valid_target_dir = os.path.commonpath([base_dir, target_dir]) == base_dir

        if not valid_target_dir:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

        if not os.path.isdir(target_dir):
            return f'Error: "{directory}" is not a directory'

        for entry in os.listdir(target_dir):
            entry_path = os.path.join(target_dir, entry)
            is_dir = os.path.isdir(entry_path)
            size = os.path.getsize(entry_path)
            entries.append(f"- {entry}: file_size={size} bytes, is_dir={is_dir}")
        return "\n".join(entries)

    except Exception as e:
        return f"Error: {e}"
