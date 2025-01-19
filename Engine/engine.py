from Engine.evaluator import MathEvaluation
from Methods.create_data import create_excel_file

# VARIABLES
path_to_create = "./Data"
path_to_data = "./Data/data.xlsx"
create_excel_file(path_to_create, "data", sheet_names=["problems", "gpt_aswers", "stimy_answers", "ev-gpt->stimy", "ev-stimy->gpt"])

evaluator = MathEvaluation("./Data", "./Data/data.xlsx")
evaluator.add_problems()
evaluator.generate_answers()
evaluator.evaluate_answers()