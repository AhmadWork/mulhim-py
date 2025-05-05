from tool_definitions.read_file import definition as read_file_def
from tool_definitions.list_files import definition as list_files_def
from tool_definitions.edit_file import definition as edit_file_def

ALL_TOOLS = [read_file_def, list_files_def, edit_file_def]

def get_all_tools():
    tools = []
    for tool in ALL_TOOLS:
        properties = {
            k: {
                "type": v.get("type", "string"),
                "description": v.get("description", "")
            } for k, v in tool["input_schema"].items()
        }
        tools.append({
            "type": "function",
            "function": {
                "name": tool["name"],
                "description": tool["description"],
                "parameters": {
                    "type": "object",
                    "properties": properties,
                    "required": list(tool["input_schema"].keys())
                }
            }
        })
    return tools

def execute_tool(name, args):
    for tool in ALL_TOOLS:
        if tool["name"] == name:
            return tool["function"](args)
    return "Tool not found"
