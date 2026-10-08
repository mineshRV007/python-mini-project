# Shopping Bill Generator

A Python mini project with a Flask website and the original terminal program.
Add items, view the cart, calculate a discount, clear the cart, and print a dated bill or save it as PDF using the browser's print dialog.

## Deploy on Render

1. Extract the ZIP and upload the contents of `shopping-bill-generator-web` into your GitHub repository. Keep `app.py`, `requirements.txt`, `render.yaml`, and the `templates` folder together at the repository root.
2. Connect that repository to a Render Web Service with Python 3 as its language.
3. Leave Root Directory empty if you uploaded the files to the repository root.
4. Set Build Command to `pip install -r requirements.txt`.
5. Set Start Command to `gunicorn app:app --bind 0.0.0.0:$PORT`.
6. Choose the Free instance type if available for your account.
7. Add an environment variable named `SECRET_KEY` with a long random value (Render can generate one). Keep it private and stable between deployments.
8. Save the settings, then select Manual Deploy → Deploy latest commit.

Alternatively, create a Render Blueprint using the included `render.yaml`; it includes the commands and generates SECRET_KEY automatically.

If you uploaded the whole parent folder instead, set Root Directory to `shopping-bill-generator-web`.

Official guide: https://render.com/docs/deploy-flask

## Run locally

Requires Python 3.9 or newer.

```bash
python -m pip install -r requirements.txt
python app.py
```

Open http://localhost:5000 in your browser. Gunicorn is used on Render's Linux environment; it is not needed to start the app on Windows.

To run the original terminal version:

```bash
python main.py
```

## Discount rules

| Subtotal | Discount |
| --- | --- |
| Below ₹500 | 0% |
| ₹500 to below ₹1,000 | 5% |
| ₹1,000 or more | 10% |

The web version uses decimal arithmetic with prices rounded to two decimal places. Each browser session has its own cart, limited to 20 items. Carts are temporary; this project has no database, payments, or saved bill history. The bill date uses the server's clock. Configure SECRET_KEY to preserve session validity across restarts. Without it, a temporary key is generated at startup.

## Files

- `app.py`: Flask application and billing logic.
- `templates/index.html`: Responsive website and printable bill.
- `requirements.txt`: Python dependencies.
- `render.yaml`: Render deployment configuration.
- `main.py`: Original terminal project.
- `.gitignore`: Excludes generated files and local secrets.
