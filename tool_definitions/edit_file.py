import os

def edit_file(args):
    path = args.get("path")
    old_str = args.get("old_str")
    new_str = args.get("new_str")

    if not path or new_str is None:
        return "Missing required fields"

    try:
        if not os.path.exists(path) and not old_str:
            os.makedirs(os.path.dirname(path), exist_ok=True)
            with open(path, "w", encoding="utf-8") as f:
                f.write(new_str)
            return f"Created new file at {path}"
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
        if not old_str:
            return "Old string must be specified when editing an existing file."
        updated = content.replace(old_str, new_str)
        with open(path, "w", encoding="utf-8") as f:
            f.write(updated)
        return "File updated successfully"
    except Exception as e:
        return f"Error: {e}"

definition = {
    "name": "edit_file",
    "description": "Edits or creates a file",
    "input_schema": {
        "path": {"type": "string", "description": "Path to the file"},
        "old_str": {"type": "string", "description": "Text to be replaced"},
        "new_str": {"type": "string", "description": "Replacement text"},
    },
    "function": edit_file
}
