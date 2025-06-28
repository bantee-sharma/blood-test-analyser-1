# 🧪 Blood Test Analyzer using CrewAI

A FastAPI-based project that uses CrewAI agents to analyze uploaded blood test reports and provide medical, nutritional, and fitness recommendations.

---

## ✅ What This Project Does

- Accepts PDF blood test reports via API.
- Uses LLM-powered agents (Doctor, Nutritionist, Fitness Coach, Verifier) to analyze and respond.
- Provides intelligent health feedback, nutrition tips, and exercise plans.

##  Bugs Fixed & Changes Made (Comprehensive)

 **❌ Missing document loader import for PDF reading ** 
   ✅ Added:  
   ```python
   from langchain_community.document_loaders import PyPDFLoader as PDFLoader
```

**❌ Tool functions were not static**

✅ Added @staticmethod decorators to allow CrewAI to use them directly without class instances.

❌ Method .read_data_tool was incorrectly called on NutritionTool and ExerciseTool

✅ Fixed by passing correct method references:

tools=[NutritionTool.analyze_nutrition_tool]

tools=[ExerciseTool.create_exercise_plan_tool]Agent-Level Fixes

**❌ Agents had sarcastic/unprofessional roles like "Doctor Who Knows Everything"**

✅ Rewritten with professional titles:

"Senior Medical Consultant"

"Clinical Nutritionist"

"Certified Fitness Coach"

"Blood Report Verifier"

**❌ Some agents had missing or incorrect tools**

✅ Fixed tools assigned to each agent to match their responsibilities.


## Task-Level Fixes

**❌ Task descriptions were humorous or vague (e.g., “make up scary-sounding diagnoses”)**

✅ Rewritten with clear, responsible, goal-oriented task descriptions.

**❌ expected_output strings were unstructured or contained syntax errors**

✅ Cleaned all expected_output to guide LLMs correctly

✅ Removed extraneous quote in verification task string

**❌ Tasks used incorrect or default tools**

✅ Explicitly assigned relevant tool:

All tasks now use BloodTestReportTool.read_data_tool

Nutrition and fitness tasks use domain-appropriate agents

## Main API Fixes
**❌ main.py did not pass file_path to Crew context**

✅ Updated to include file_path inside run_crew()

**❌ File reading and saving logic had no error handling**

✅ Wrapped in try-except-finally block to safely remove temporary files


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
