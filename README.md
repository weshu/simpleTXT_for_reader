# 豆包阅读器

轻量级豆包阅读器。
将需要朗读的内容paste到页面中，然后在豆包中点击“全文阅读”，即可朗读。
Built with Flask and TailwindCSS.

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/simple-txt-reader.git
cd simple-txt-reader
```

2. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Start the application:
```bash
python app.py
```

2. Open your web browser and navigate to `http://localhost:5000`

3. The application will display the contents of `read.txt`. You can:
   - Click "Toggle Edit Mode" to switch between viewing and editing
   - Make changes in edit mode
   - Click "Save Changes" to update the content

## Project Structure

```
simple-txt-reader/
├── app.py              # Main application file
├── read.txt           # Text file to be displayed
├── requirements.txt   # Python dependencies
├── templates/         # HTML templates
│   └── index.html    # Main page template
└── README.md         # Project documentation
```

## Contributing

1. Fork the repository
2. Create a new branch
3. Make your changes
4. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details. 