import os
import markdown
import argparse

# This function creates the CSS file, and is called by convert_md_to_html
def create_css(md_file_path, output_dir):
    css_content = """
@import url('https://fonts.googleapis.com/css2?family=Roboto&display=swap');

body {
    font-family: "Roboto", sans-serif;
    background-color: black;
    color: white;
}
"""
    # Create the CSS directory if needed
    css_dir_path = os.path.join(output_dir, 'css')
    os.makedirs(css_dir_path, exist_ok=True)
    # Name the CSS file based on the Markdown file's name
    css_file_name = os.path.splitext(os.path.basename(md_file_path))[0] + '.css'
    # Write the CSS file to the full path, return the directory for use in convert_md_to_html
    css_file_path = os.path.join(css_dir_path, css_file_name)
    with open(css_file_path, 'w') as css_file:
        css_file.write(css_content)
    return css_file_path

def convert_md_to_html(md_file_path, output_dir):
    # Read the Markdown file contents and store them as a string
    with open(md_file_path, 'r') as md_file:
        md_content = md_file.read()
    # Run the create_css function to generate the CSS directory and file
    css_file_path = create_css(md_file_path, output_dir)
    # Get the returned name of the CSS file generated, so it can be linked in the HTML
    css_file_name = os.path.basename(css_file_path)
    html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet" href="css/{css_file_name}">
</head>
<body>
{markdown.markdown(md_content)}
</body>
</html>
"""
    # Write the HTML file
    html_file_path = os.path.join(output_dir, os.path.splitext(os.path.basename(md_file_path))[0] + '.html')
    with open(html_file_path, 'w') as html_file:
        html_file.write(html_content)

# Get the command line arguments object and store it
parser = argparse.ArgumentParser()
parser.add_argument('input_dir')
parser.add_argument('output_dir')
args = parser.parse_args()

# Search the directory given for Markdown files, begin the script functions for those files
for filename in os.listdir(args.input_dir):
    if filename.endswith('.md'):
        convert_md_to_html(os.path.join(args.input_dir, filename), args.output_dir)