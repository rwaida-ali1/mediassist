# MediAssist AI

MediAssist AI is an AI-powered medical assistant designed to provide initial assessments and recommendations related to diabetes. It leverages advanced language models and a crew of specialized AI agents to analyze user-provided information, including symptoms, risk factors, and family history.

## Features

- **Multilingual Support:** Available in both English and Arabic.
- **Intelligent Agents:** Employs a team of AI agents for data analysis, diagnosis, and recommendation.
- **Sequential Task Processing:** Follows a structured process to ensure thorough evaluation.
- **API Endpoint:** Exposes a FastAPI endpoint for integration with other applications.

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/rwaida-ali1/mediassist.git
   cd mediassist-ai
   ```

2. **Install dependencies using Poetry:**

   ```bash
   poetry install
   ```

3. **Set up environment variables:**

   - Create a `.env` file in the project root directory.
   - Copy the contents of `.env.example` into `.env`.
   - Replace the placeholder values with your actual API keys.

## Usage

### Running the API

```bash
poetry run uvicorn mediassist.api.main:app --reload
```
