# put your python code here
num_class_1 = int(input())
num_class_2 = int(input())
num_class_3 = int(input())

tables_class_1 = (not(num_class_1 % 2) and (num_class_1 // 2)) or (num_class_1 and (num_class_1 // 2 + 1))
tables_class_2 = (not(num_class_2 % 2) and (num_class_2 // 2)) or (num_class_2 and (num_class_2 // 2 + 1))
tables_class_3 = (not(num_class_3 % 2) and (num_class_3 // 2)) or (num_class_3 and (num_class_3 // 2 + 1))

print(tables_class_1 + tables_class_2 + tables_class_3)
