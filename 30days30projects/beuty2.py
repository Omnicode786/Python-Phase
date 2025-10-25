input_file = "bootstrap.min.css"
output_file = "bootstrap_formatted.css"

with open(input_file, "r", encoding="utf-8") as f:
    css_content = f.read()

formatted_css = css_content.replace("{", "{\n").replace("}", "}\n").replace(";", ";\n")

with open(output_file, "w", encoding="utf-8") as f:
    f.write(formatted_css)

print(f"Formatted CSS saved as {output_file}")
