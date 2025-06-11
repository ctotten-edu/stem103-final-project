# Final Assignment Diagnostic Tool

## Overview
The Final Assignment Diagnostic Tool is a Python-based application designed to assist users in reporting issues related to customer items. The tool collects essential information such as customer details, item specifics, priority levels, and issue descriptions. It generates diagnostic repair forms and invoices, providing a structured approach to issue reporting and resolution.

## Features
- User-friendly interface for inputting customer and item information.
- Priority level selection to categorize issues.
- Detailed issue description input.
- Generation of diagnostic repair forms and invoices.
- Error management for file handling to ensure data integrity.
- Optional logging form for tracking purposes.

## Project Structure
```
final-assignment-diagnostic-tool
├── src
│   ├── main.py                # Entry point of the application
│   ├── diagnostic_tool.py      # Functions for creating diagnostic forms and invoices
│   ├── utils.py                # Utility functions for input validation and formatting
│   └── data
│       └── reports.txt         # File for storing generated reports and invoices
├── requirements.txt            # List of dependencies required for the project
└── README.md                   # Documentation for the project
```

## Installation
To set up the project, clone the repository and install the required dependencies. You can do this by running:

```
pip install -r requirements.txt
```

## Usage
1. Run the application by executing the `main.py` file:
   ```
   python src/main.py
   ```
2. Follow the prompts to enter customer and item information, select priority levels, and describe the issue.
3. Upon completion, the tool will generate a diagnostic repair form and an invoice, which will be saved in the `reports.txt` file for future reference.

## Error Handling
The application includes error management features to handle potential issues during file operations and user input. This ensures that the tool remains robust and user-friendly.

## Contributing
Contributions to enhance the functionality of the tool are welcome. Please submit a pull request or open an issue for discussion.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.