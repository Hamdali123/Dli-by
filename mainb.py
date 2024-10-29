#contoh class minilang

class MiniLang:
    def __init__(self):
        self.variables = {}

    def run(self, code):
        lines = code.splitlines()
        for line in lines:
            line = line.strip()
            if line.startswith("print"):
                self.print_command(line)
            elif line.startswith("add"):
                self.add_command(line)
            else:
                print(f"Unrecognized command: {line}")

    def print_command(self, line):
        # Mengambil isi dalam tanda kurung
        content = line[6:-1]  # Menghilangkan "print(" dan ")"
        if content in self.variables:
            print(self.variables[content])
        else:
            print(content)

    def add_command(self, line):
        # Mengambil variabel dan nilai
        parts = line.split()
        var_name = parts[1]
        value = int(parts[2])
        self.variables[var_name] = value
        print(f"Variable {var_name} set to {value}")

# Contoh penggunaan
if __name__ == "__main__":
    lang = MiniLang()
    code = """
    add x 5
    add y 10
    print(x)
    print(y)
    print(Hello, World!)
    """
    lang.run(code)
