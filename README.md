# Python Paint Application

A simple yet functional digital paint application built with Python's tkinter library. This lightweight drawing tool allows users to create freehand drawings with an intuitive mouse-based interface.

## Features

- **Freehand Drawing**: Draw smoothly using mouse click and drag
- **Save Functionality**: Save your artwork as PNG or JPEG files
- **Clear Canvas**: Reset the drawing surface with a single button click
- **Responsive Interface**: Real-time drawing with immediate visual feedback
- **Cross-Platform**: Works on Windows, macOS, and Linux systems

## Requirements

- Python 3.6 or higher
- tkinter (usually included with Python installations)
- Pillow (PIL) for image processing and saving functionality

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/robertisaacs-hash/python_paint.git
   cd python_paint
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Verify Python installation**:
   ```bash
   python --version
   ```

4. **Check tkinter availability** (optional):
   ```bash
   python -c "import tkinter; print('tkinter is available')"
   ```

## Usage

Run the application from the command line:

```bash
python paint.py
```

### How to Use

1. **Drawing**: Click and hold the left mouse button while moving the mouse to draw
2. **Save Drawing**: Click the "Save" button to save your artwork as PNG or JPEG file
3. **Clear Canvas**: Click the "Clear" button to erase all drawings and start fresh
4. **Exit**: Close the application window to exit

## Technical Details

- **GUI Framework**: tkinter
- **Drawing Method**: Line segments created between mouse positions
- **Canvas**: Expandable white background that fills the window
- **Line Properties**: Black color with 2-pixel width

## Project Structure

```
python_paint/
├── paint.py          # Main application file
├── requirements.txt  # Python dependencies
└── README.md         # Project documentation
```

## Contributing

Contributions are welcome! Feel free to:

- Report bugs or issues
- Suggest new features
- Submit pull requests

## License

This project is open source and available under the [MIT License](LICENSE).

## Future Enhancements

Potential improvements for future versions:

- Color palette selection
- Adjustable brush sizes  
- Load existing images for editing
- Different drawing tools (rectangle, circle, etc.)
- Undo/redo functionality
- Multiple file format support

## Author

Created by [robertisaacs-hash](https://github.com/robertisaacs-hash)

---

*A simple paint application demonstrating Python GUI development with tkinter.*