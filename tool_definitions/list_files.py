import os

def list_files(args):
    path = args.get("path", ".")
    try:
        entries = []
        for root, dirs, files in os.walk(path):
            for name in dirs:
                entries.append(os.path.join(root, name) + "/")
            for name in files:
                entries.append(os.path.join(root, name))
            break
        return "\n".join(entries)
    except Exception as e:
        return f"Error: {e}"

definition = {
    "name": "list_files",
    "description": "Lists files in a directory",
    "input_schema": {
        "path": {"type": "string", "description": "Directory path to list files from"}
    },
    "function": list_files
}
