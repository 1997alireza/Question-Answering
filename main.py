from tools import euclidean_distance
from xlrd import open_workbook

input_q = input()
wb = open_workbook('./QA-samples.xlsx')
sheet = wb.sheet_by_index(1)
best_index = 0
best_score = euclidean_distance(input_q, str(sheet.cell(0, 0).value))
for row in range(1, sheet.nrows):
    q = str(sheet.cell(row, 0).value)
    ed = euclidean_distance(input_q, q)
    if best_score > ed:
        best_score = ed
        best_index = row
# print(best_index)
print(wb.sheet_by_index(0).cell(best_index, 1))
# print(wb.sheet_by_index(1).cell(best_index, 0))


