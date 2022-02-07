﻿while True:
	try:
		weight = float(input("体重(kg)は？"))
		height = float(input("身長(cm)は？"))

		height = height / 100
		bmi = weight / (height * height)
		break;
	except:
		print("入力ミスがります。再入力てください")

result = ""
if bmi < 18.5: result = "やせ型"
elif bmi < 25: result = "標準体重"
elif bmi < 30: result = "肥満（軽）"
else: result = "肥満（重）"

print("BMI :", bmi)
print("判定:", result)