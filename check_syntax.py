import ast

try:
    with open('app.py', 'r') as f:
        source_code = f.read()
    
    # Try to parse the code
    ast.parse(source_code)
    print("No syntax errors found.")
except SyntaxError as e:
    line_number = e.lineno
    offset = e.offset
    
    print(f"Syntax error on line {line_number}:")
    
    # Get the problematic line
    with open('app.py', 'r') as f:
        lines = f.readlines()
        if line_number <= len(lines):
            # Print the error line and a few lines before and after for context
            start_line = max(0, line_number - 5)
            end_line = min(len(lines), line_number + 5)
            
            print("Context:")
            for i in range(start_line, end_line):
                prefix = ">>> " if i + 1 == line_number else "    "
                print(f"{prefix}{i+1}: {lines[i].rstrip()}")
            
            # Indicate the position of the error
            if offset:
                error_indicator = " " * (len(prefix) + len(str(line_number)) + 2 + offset - 1) + "^"
                print(error_indicator)
            
            print(f"Error message: {e}")
        else:
            print(f"Error line {line_number} is beyond the file length.")
except Exception as e:
    print(f"Error checking syntax: {e}") 
