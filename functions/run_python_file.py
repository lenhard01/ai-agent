import os
import subprocess


def run_python_file(
    working_directory: str, file_path: str, args: list[str] | None = None
) -> str:
    try:
        base_dir = os.path.abspath(working_directory)
        target_path = os.path.normpath(os.path.join(base_dir, file_path))

        if os.path.commonpath([base_dir, target_path]) != base_dir:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

        if not os.path.isfile(target_path):
            return f'Error: "{file_path}" does not exist or is not a regular file'

        if not target_path.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file'

        command = ["python", target_path]

        if args:
            command.extend(args)

        result = subprocess.run(
            command,
            cwd=base_dir,
            capture_output=True,
            text=True,
            timeout=30,
        )

        output = ""
        if result.returncode != 0:
            output += f"Process exited with code {result.returncode}"

        if not result.stdout and not result.stderr:
            output += "No output produced"

        if result.stdout:
            output += f"STDOUT:\n{result.stdout}"

        if result.stderr:
            output += f"STDERR:\n{result.stderr}"

        return output
    except Exception as e:
        return f"Error: executing Python file: {e}"


schema_run_python_file = {
    "type": "function",
    "function": {
        "name": "run_python_file",
        "description": "Executes a Python file, with optional command-line arguments, relative to the working directory.",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "Path to the Python file to execute, relative to the working directory.",
                },
                "args": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "Optional list of command-line arguments to pass to the Python file when it is executed.",
                },
            },
            "required": ["file_path"],
        },
    },
}
