## Importing libraries and files
import os
from dotenv import load_dotenv
load_dotenv()


from crewai.tools.base_tool import Tool
from langchain_community.document_loaders import PyPDFLoader as PDFLoader # Added missing import


## Creating custom pdf reader tool
class BloodTestReportTool():
    @staticmethod
    def read_data_tool(path='data/sample.pdf') -> str:
        """Tool to read data from a pdf file from a path

        Args:
            path (str, optional): Path of the pdf file. Defaults to 'data/sample.pdf'.

        Returns:
            str: Full Blood Test report file
        """
        docs = PDFLoader(file_path=path).load()

        full_report = ""
        for data in docs:
            content = data.page_content

            # Remove extra newlines
            while "\n\n" in content:
                content = content.replace("\n\n", "\n")

            full_report += content + "\n"

        return full_report

## Creating Nutrition Analysis Tool
class NutritionTool:
    @staticmethod
    def analyze_nutrition_tool(blood_report_data: str) -> str:
        """Analyze the blood report for nutrition-related markers"""
        processed_data = blood_report_data.replace("  ", " ").strip().lower()

        recommendations = []

        if "vitamin d" in processed_data and ("low" in processed_data or "deficient" in processed_data):
            recommendations.append("Vitamin D is low. Recommend sunlight exposure and D3 supplements.")

        if "vitamin b12" in processed_data and ("low" in processed_data or "deficient" in processed_data):
            recommendations.append("Vitamin B12 is low. Suggest B12 shots or fortified foods like cereals.")

        if "hemoglobin" in processed_data and "low" in processed_data:
            recommendations.append("Hemoglobin is low. Recommend iron-rich foods like spinach, lentils, and red meat.")

        if "calcium" in processed_data and "low" in processed_data:
            recommendations.append("Calcium is low. Suggest dairy products, almonds, or calcium supplements.")

        if not recommendations:
            return "No specific nutrition deficiencies found in the blood report."
        return "\n".join(recommendations)

## Creating Exercise Planning Tool
class ExerciseTool:
    @staticmethod
    def create_exercise_plan_tool(blood_report_data: str) -> str:
        """Recommend basic exercise routines based on general report indicators"""
        processed_data = blood_report_data.lower()

        if "cholesterol" in processed_data and ("high" in processed_data or "elevated" in processed_data):
            return "Cholesterol is high. Recommend 30 minutes of cardio daily like brisk walking, cycling, or swimming."

        if "blood pressure" in processed_data and "high" in processed_data:
            return "Blood pressure is high. Suggest yoga, breathing exercises, and moderate walking."

        if "glucose" in processed_data and "high" in processed_data:
            return "Glucose levels are high. Advise 45 minutes of daily physical activity and avoid sugary foods."

        return "No major issues found. Recommend general fitness: 20 minutes of walking, 3x weekly strength training."