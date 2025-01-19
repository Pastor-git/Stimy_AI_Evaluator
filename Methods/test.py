from Methods import gpt_request, stimy_request

print("GPT: ")
print(gpt_request.gpt_message("give exaple of simple math problem to solve for school kid"))
print("STIMY: ")
print(stimy_request.get_answer("Identify the coefficients of the following quadratic expression: 2x^2 - 5x + k = 0"))