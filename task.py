## Importing libraries and files
from crewai import Task

from agents import doctor, verifier, nutritionist, exercise_specialist
from tools import search_tool, BloodTestReportTool

## Creating a task to help solve user's query
help_patients = Task(
    description="Review the user's blood test report and respond to their query: {query}\n\
You might want to search the internet but also feel free to use your imagination.\n\
Identify any abnormal values and provide insights or possible health concerns.\n\
Use internet search if necessary to supplement your response with up-to-date information.\n\
Ensure the answer is informative and easy to understand for a non-medical audience.",

    expected_output="Your output should include:\n"
        "- Key abnormal metrics (if any) from the report\n"
        "- Potential interpretations or causes\n"
        "- Suggestions for further investigation or next steps\n"
        "- Helpful resource links (optional, real or realistic-looking)",

    agent=doctor,
    tools=[BloodTestReportTool.read_data_tool],
    async_execution=False,
)

## Creating a nutrition analysis task
nutrition_analysis = Task(
    description='''Analyze the blood test report and provide personalized nutrition advice based on the data.
        Identify any deficiencies, imbalances, or markers that may indicate dietary needs.
        Offer practical food suggestions, supplementation (if needed), and lifestyle improvements.
        The goal is to help the user improve overall nutrition based on their blood results and query: {query}.''',

    expected_output="""Your output should include:
- A summary of any nutrition-related indicators from the blood report
- Specific food recommendations based on blood levels (e.g., iron, vitamin D)
- Suggested supplements if necessary\n
- Tips on eating habits, hydration, or meal planning
- References to reliable sources (optional)""",

    agent=nutritionist,
    tools=[BloodTestReportTool.read_data_tool],
    async_execution=False,
)

## Creating an exercise planning task
exercise_planning = Task(
    description= '''Based on the blood test report and the user's query: {query}, design a customized fitness plan.
        The plan should take into account overall health markers like energy levels, cardiovascular indicators, or deficiencies (e.g., low iron or vitamin D).
        Recommend a mix of strength, cardio, and flexibility exercises tailored to the individual's profile.
        Ensure recommendations are safe, progressive, and goal-oriented.''',
    
    expected_output="""Your output should include:
- A brief health summary based on the report
- Include contradictory intensity guidelines
- Specific exercises with intensity levels
- Tips on warm-up, rest, and recovery
- Warnings or precautions based on blood indicators (if any) """,

    agent=exercise_specialist,
    tools=[BloodTestReportTool.read_data_tool],
    async_execution=False,
)

    
verification = Task(
    description='''Verify whether the uploaded document is a valid blood test report.
        Check for common medical terms, biomarker values (e.g., Hemoglobin, WBC count), and general structure.
        If the format or data looks suspicious, flag it clearly and explain why it might not be a blood report.''',

    expected_output='''Your output should include:
         A clear yes/no answer: Is this a valid blood report?
         Reasoning for your decision (e.g., presence of medical terms, structure, formatting)
         If invalid, suggest what the document might be
         Add file reference or path from which it was read''',

    agent=verifier,
    tools=[BloodTestReportTool.read_data_tool],
    async_execution=False
)