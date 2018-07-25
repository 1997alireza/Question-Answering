from tools import euclidean_distance, edit_distance, find_best_match
from xlrd import open_workbook


input_q = input()
wb = open_workbook('./QA-samples.xlsx')
sheet = wb.sheet_by_index(1)
q_col = 0
best_index, best_score = find_best_match(sheet, 0, input_q, euclidean_distance)
print('Answer:\n', wb.sheet_by_index(0).cell(best_index, 1).value)
print('Best match:\n', wb.sheet_by_index(1).cell(best_index, 0).value)
print('Score: ', best_score)
