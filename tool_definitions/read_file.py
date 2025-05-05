def read_file(args):
    path = args.get("path")
    if not path:
        return "Path is required."
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    except Exception as e:
        return f"Error: {e}"

definition = {
    "name": "read_file",
    "description": "Reads a file from the local file system",
    "input_schema": {
        "path": {"type": "string", "description": "Relative path to the file"}
    },
    "function": read_file
}
