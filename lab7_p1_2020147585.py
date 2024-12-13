import re

def calculate_def_call(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
        function_def = {}
        function_call = {}
        def_definition = re.compile(r'^\s*def\s+(\w+)\s*\(')
        call_definition = re.compile(r'(?<!def\s)\b(\w+)\s*\(')

        for line_number, line in enumerate(lines, start=1):
            match = def_definition.search(line)
            if match:
                func_name = match.group(1)
                function_def[func_name] = line_number
                function_call[func_name] = []

            calls = set()
            for call_match in call_definition.finditer(line):
                func_name = call_match.group(1)
                if func_name in function_def and func_name not in calls:
                    calls.add(func_name)
                    function_call[func_name].append(line_number)

        for func_name, def_line in function_def.items():
            calls = function_call[func_name]
            print(f"{func_name}: def in {def_line}, calls in {calls}")

    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")

if __name__ == "__main__":
    calculate_def_call("input_7_1.txt")
