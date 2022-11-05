
assert abs(-42) == 42

# вывод текста

actual_result = "abrakadabra"
print("Wrong text, got " + actual_result + ", something wrong")

print("Let's count together: {}, then goes {}, and then {}".format("one", "two", "three")) # использование функции .format()
# Let's count together: one, then goes two, and then three

str1 = "one"
str2 = "two"
str3 = "three"
print(f"Let's count together: {str1}, then goes {str2}, and then {str3}") # вывод с использованием f-strings
# Let's count together: one, then goes two, and then three

actual_result = "abrakadabra"
f"Wrong text, got {actual_result}, something wrong"
#Wrong text, got abrakadabra, something wrong

a = f"типо можно так выводить сразу текст?"
print(a)