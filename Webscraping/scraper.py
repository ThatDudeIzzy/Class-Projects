
import webbrowser

# HTML content - whitespace is irrelevant
html_content = '  <!-- This is the example.html file. --> <html><head><title>The Website Title</title></head><body> <p>Download the book <strong>The American</strong> from <a href="https://www.gutenberg.org/files/177/177-0.txt">Project Gutenberg</a>.</p><p class="slogan">Read more 19th century fiction!</p> <p>By <span id="author">Henry James</span></p></body></html>'

# Write HTML content to a file
with open('example.html', 'w') as file:
    file.write(html_content)

# check if the file is there
import os
print(os.path.isfile('example.html'))

# check where you are - get current working directory
print(os.getcwd())

# Open the file in the web browser
webbrowser.open('example.html')