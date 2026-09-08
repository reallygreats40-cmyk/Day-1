"""
Closures Notes Section 6: Closures as Function Factories
Demonstrating dynamic creation of customized mathematical or logical processors.
"""

def make_line_formatter(prefix, suffix):
    def formatter(text):
        return f"{prefix}{text}{suffix}"
    return formatter

def main():
    # Dynamically generate specialized string formatters
    html_bold = make_line_formatter("<b>", "</b>")
    json_key = make_line_formatter('"', '":')
    
    print(html_bold("Closure Classroom"))  # Output: <b>Closure Classroom</b>
    print(json_key("port_number"))        # Output: "port_number":

if __name__ == "__main__":
    main()
