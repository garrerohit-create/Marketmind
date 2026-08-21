# Marketmind

Marketmind is a Flask-based prototype that demonstrates AI-assisted go-to-market workflows: campaign ideation, sales-pitch drafting, lead prioritisation, SDR-style outreach planning, multi-step GTM planning, and a simple ROI illustration.

> **Prototype disclaimer:** This is a portfolio/hackathon-style demonstration, not a production autonomous sales system. AI outputs can be inaccurate and must be reviewed before use. Do not use it to make automated outreach, qualification, or financial decisions.

## Features

- Campaign ideas tailored to a product, audience, and platform
- Sales-pitch drafting
- AI-assisted lead-scoring illustration
- SDR-style outreach-plan drafting (`Jazon`)
- Multi-role GTM planning and ROI illustration
- Optional offline demo mode for presentations

## Tech stack

- Python + Flask
- Groq API (optional; used for live generation)
- Chart.js (loaded from CDN for the UI)

## Run locally

1. Clone the repository and enter its folder.
2. Create and activate a virtual environment.
3. Install the dependencies:

   ```bash
      pip install -r requirements.txt
         ```

         4. Copy `.env.example` to `.env` and add a **newly created** Groq API key:

            ```bash
               cp .env.example .env
                  ```

                  5. Run the app:

                     ```bash
                        python finalcode.py
                           ```

                           Then open `http://127.0.0.1:5000`.

                           ### Offline demo mode

                           Set `DEMO_MODE = True` in `finalcode.py` to use fixed sample responses without a Groq key.

                           ## Security notes

                           - Never commit `.env` files or API keys. The repository ignores local environment files.
                           - If a key was ever committed, revoke it in the provider dashboard and create a replacement; removing the file from the latest commit does **not** remove it from Git history.
                           - Run production deployments with a proper WSGI server and `debug=False`.

                           ## Repository structure

                           ```text
                           finalcode.py      # Flask application and single-page UI
                           requirements.txt  # Python dependencies
                           .env.example      # Environment-variable template
                           ```

                           ## Future improvements

                           - Split frontend templates, styles, and API routes into separate modules
                           - Add input validation, error handling, and tests
                           - Move configuration to environment variables
                           - Add authentication, rate limiting, and an audit trail before any real deployment

                           ## License

                           No license has been selected yet. Add one before accepting external contributions or reuse.
                           
