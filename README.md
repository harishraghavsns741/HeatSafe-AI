# HeatSafe AI — Heat-Risk Awareness Prototype

HeatSafe AI is a student prototype that demonstrates how temperature and relative humidity can be turned into a simple, transparent heat-risk awareness screen with English and Tamil guidance.

> **Safety notice:** The included score and categories are illustrative software-demo rules only. They are not a validated heat-stress model, a medical diagnosis, or an official occupational safety assessment. The app does **not** calculate Wet Bulb Globe Temperature (WBGT), fetch live weather, or replace local authority/workplace guidance. Do not use the demo score to decide whether work is safe.

## Features

- Web form for temperature and relative humidity.
- Transparent, deterministic demonstration rules.
- English and Tamil guidance.
- Input validation and explanatory disclaimer.
- Unit tests and sample data.
- No API key required for the demo.

## Requirements

- Python 3.10 or newer
- pip

## Setup

### 1. Download and enter the project folder

```bash
cd heatsafe-ai
```

### 2. Create a virtual environment

Windows:
```bash
py -m venv .venv
.venv\Scripts\activate
```

macOS/Linux:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Configure environment variables

Copy `.env.example` to `.env` and set a random `SECRET_KEY`. The app does not automatically load `.env`; export variables in your terminal or install and configure `python-dotenv` if you want automatic loading.

macOS/Linux:
```bash
export SECRET_KEY="replace-with-a-random-secret"
```

PowerShell:
```powershell
$env:SECRET_KEY="replace-with-a-random-secret"
```

### 5. Run the application

```bash
python app.py
```

Open `http://127.0.0.1:5000` in your browser.

## Run tests

```bash
pytest -q
```

## Sample data

See `data/sample_conditions.csv`. Values are illustrative test examples, not verified real-world observations or official labels.

## Architecture

See `docs/TECHNICAL_DESIGN.md` for the architecture diagram, data flow, limitations, and future enhancements.

## Repository checklist

- [x] README with setup instructions and environment-variable example
- [x] Technical design document and Mermaid architecture diagram
- [x] Sample data and test cases
- [x] MIT license
- [ ] Live weather API integration (not implemented)
- [ ] Validated heat-stress model (not implemented)
- [ ] Verified local cooling-resource dataset (not implemented)

## Suggested next steps

1. Test the prototype locally.
2. Replace the demo rules only after selecting a defensible reference method and validating it.
3. If adding a weather API, document the provider, terms, units, failure handling, and required API-key environment variable.
4. Do not publish private API keys or personal data.
5. Create a public GitHub/GitLab repository and upload these files.

## License

Released under the MIT License. See `LICENSE`.
