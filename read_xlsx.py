import openpyxl

"""
python read_xlsx.py /Users/yangmingming03/Downloads/执行结果1.xlsx,/Users/yangmingming03/Downloads/执行结果2.xlsx,/Users/yangmingming03/Downloads/执行结果3.xlsx,/Users/yangmingming03/Downloads/执行结果4.xlsx
"""

def read_file(file, sheet_name = "Sheet1"):
    results = []
# 打开 Excel 文件
    xlsx_file = file
    workbook = openpyxl.load_workbook(xlsx_file)

    if sheet_name not in workbook:
        print(f"not found sheet {sheet_name} in file {file}")
        return results

# 选择工作表（可以使用工作表的名字或索引）
    sheet = workbook[sheet_name]  # 替换成你的工作表名字

# 遍历工作表的行
    for row in sheet.iter_rows(min_row=2, values_only=True):
        col1_value = row[0]
        col2_value = row[1]
        col3_value = row[2]
        #print(f"Column 1: {col1_value}, Column 2: {col2_value}, Column 3: {col3_value}")
        results.append((col1_value, col2_value, col3_value))

# 关闭工作簿
    workbook.close()

    return results

import sys
if len(sys.argv) == 1:
    print(f"please set eg. files")
    sys.exit(0)

name_to_id = {}
for file in sys.argv[1].split(","):
    print(f"begin to process file {file}")
    #  ('59f28d8fe627a52bebd43ca6be8193573c882eb0fa85041ffe9ccec0306c6015i0', '0000.bitverse', '1691283602000')
    ret = read_file(file, sheet_name = "SheetJS")
    for item in ret:
        name = item[1]
        id = item[0]
        if name in name_to_id:
            print(f"already process {name}")
            continue
        name_to_id[name] = id
name_to_id_my = {}
# 获取自己统计的信息
# 21588357        801852  59f28d8fe627a52bebd43ca6be8193573c882eb0fa85041ffe9ccec0306c6015i0      6040    bc1prs4953qq9wfp3m4hnq8l5wkulf4e4nuryvnuep60nuzrze4q0tksleqtw9   13 bytes        text/plain;charset=utf-8        0000.bitverse
with open('0000-9999.bitverse_tab.txt', 'r') as fd:
    for line in fd:
        arr = line.strip("\n").split("\t")
        name_to_id_my[arr[7]] = arr[2]

# 校验
for key,value in name_to_id_my.items():
    if key not in name_to_id:
        print(f"not found {key}")
        continue
    if value != name_to_id[key]:
        print(f"key {key} -> my {value} -> other {name_to_id[key]}")

print(f"my len {len(name_to_id_my)}, other len {len(name_to_id)}")
