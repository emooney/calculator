# Flask Calculator App

A complete web-based calculator built with **Python + Flask** that includes:

- Standard operations: addition, subtraction, multiplication, division
- Power (`x^y`)
- Percent support (`50% -> 0.5` and `x * y%` behavior)
- Scientific operations: square root, `sin`, `cos`, `tan` (angles in **degrees**)
- Circle calculations using **PI = 3.14** exactly

## Project Structure

```text
.
├── app.py
├── operations.py
├── requirements.txt
├── README.md
├── static/
│   └── style.css
├── templates/
│   └── index.html
└── tests/
    └── test_operations.py
```

## Requirements

- Python 3.10+

## 1) Create and Activate a Virtual Environment

### Windows PowerShell

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### macOS/Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
```

## 2) Install Dependencies

```bash
pip install -r requirements.txt
```

## 3) Run the Flask App

You can run with Python directly:

```bash
python app.py
```

Or using Flask CLI:

### Windows PowerShell

```powershell
$env:FLASK_APP = "app.py"
flask run
```

### macOS/Linux

```bash
export FLASK_APP=app.py
flask run
```

## 4) Open in Browser

Open:

- `http://127.0.0.1:5000`

## 5) Run Tests

```bash
python -m unittest
```

## Example Walkthrough

1. Start the app and open `http://127.0.0.1:5000`.
2. In **Standard Calculator**:
   - Enter `10` and `20`, choose **Add (+)**, click calculate.
   - Result should show `30`.
3. In **Standard Calculator** percent behavior:
   - Enter `200` and `15`, choose **Percent of (x * y%)**.
   - Result should show `30` because `200 * 15% = 30`.
4. In **Scientific Calculator**:
   - Enter `30`, choose **sin (degrees)**.
   - Result should show approximately `0.5`.
5. In **Circle Calculator**:
   - Enter radius `2`, choose **Area (πr²)**.
   - Result should show `12.56` using `PI = 3.14`.
6. Error handling examples:
   - Division by zero shows a friendly message.
   - Negative square root shows a clear error.
   - `tan(90)` shows undefined tangent warning behavior.
