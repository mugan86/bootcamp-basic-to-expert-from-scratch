list1 = ["java", "java", "python", "c++", "kotlin",
         "javascript", "c++", "c++", "c++", "kotlin"]

count_values = list1.count("java")  # 2
count_values = list1.count("javascript")  # 1
count_values = list1.count("python")  # 1
count_values = list1.count("kotlin")  # 2
count_values = list1.count("c++")  # 4

elements = [True, False, True, 2 + 3j, 2, 2.3, "anartz", True,
            [12, 23], True, 2 + 3j, 12, 23, "anartz", [12, 23] ]

count_values = elements.count(True)  # 4
count_values = elements.count("anartz")  # 2
count_values = elements.count(False)  # 1
count_values = elements.count(2 + 3j)  # 2
count_values = elements.count(12)  # 1
count_values = elements.count([12, 23])  # 2
print("******")

