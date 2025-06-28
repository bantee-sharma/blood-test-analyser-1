# 🧪 Blood Test Analyzer using CrewAI

A FastAPI-based project that uses CrewAI agents to analyze uploaded blood test reports and provide medical, nutritional, and fitness recommendations.

---

## ✅ What This Project Does

- Accepts PDF blood test reports via API.
- Uses LLM-powered agents (Doctor, Nutritionist, Fitness Coach, Verifier) to analyze and respond.
- Provides intelligent health feedback, nutrition tips, and exercise plans.



---

## 🚀 How to Run Locally

### 1. Clone Repository
```bash
git clone https://github.com/bantee-sharma/blood-test-analyzer.git
cd blood-test-analyzer
```

## Create Virtual Environment (Recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

## Install Dependencies
```bash
pip install -r requirements.txt
```

## Set Up Environment Variables

While the libraries are installing, we need to set up our environment variables.

Create a .env File In the project directory, create a new file named .env Add your environment variables to this file in the following format:
```bash
GOOGLE_API_KEY="YOUR_GOOGLE_API_KEY"
SERPER_API_KEY="YOUR_SERPER_API_KEY"
```
## Start the Server
