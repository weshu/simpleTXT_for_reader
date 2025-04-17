from flask import Flask, render_template, request

app = Flask(__name__)

def read_file(file_path):
    """Read and return the contents of a file.
    
    Args:
        file_path (str): Path to the file to read
        
    Returns:
        str: Contents of the file
    """
    with open(file_path, 'r') as file:
        return file.read()

@app.route('/', methods=['GET', 'POST'])
def home():
    """Handle the home page route.
    
    GET: Display the current content of read.txt
    POST: Update the content and display the new version
    """
    file_path = 'read.txt'
    if request.method == 'POST':
        content = request.form['new_content']
        return render_template('index.html', content=content)
    else:
        content = read_file(file_path)
        return render_template('index.html', content=content)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)