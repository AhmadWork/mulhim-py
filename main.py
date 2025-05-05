import os
import json
import ollama
from tools import get_all_tools, execute_tool

def get_user_input():
    try:
        return input("\033[94mYou\033[0m: ")
    except EOFError:
        return None

def main():
    base_url = os.getenv("OLLAMA_HOST", "http://localhost:11434")
    client = ollama.Client(host=base_url)
    history = []
    tools = get_all_tools()

    print(" Hello My Writer, welcome to Mulhim,")
    print(" Where Writer get inspired.")

    read_user_input = True

    while True:
        if read_user_input:
            user_input = get_user_input()
            if user_input is None:
                break
            history.append({"role": "user", "content": user_input})

        response = client.chat(model="qwen2.5:14b", messages=history, tools=tools)
        message = response["message"]
        history.append(message)

        tool_calls = message.get("tool_calls", [])
        if tool_calls:
            for call in tool_calls:
                name = call["function"]["name"]
                arguments = call["function"]["arguments"]
                print(f"\033[92mtool\033[0m: {name}({arguments})")
                result = execute_tool(name, arguments)
                history.append({"role": "tool", "content": result})
            read_user_input = False
        else:
            print(f"\033[93mAssistant\033[0m: {message['content']}")
            read_user_input = True

if __name__ == "__main__":
    main()
