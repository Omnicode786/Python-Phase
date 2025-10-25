# First install cssbeautifier if not already installed:
# pip install cssbeautifier

import cssbeautifier

# Input and output file paths
input_file = "bootstrap.min.css"          # your minified CSS file
output_file = "bootstrap_formatted.css"   # the formatted output file

# Read minified CSS
with open(input_file, "r", encoding="utf-8") as f:
    css_content = f.read()

# Beautify CSS
formatted_css = cssbeautifier.beautify(css_content)

# Save formatted CSS
with open(output_file, "w", encoding="utf-8") as f:
    f.write(formatted_css)

print(f"Formatted CSS saved as {output_file}")
