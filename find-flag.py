﻿#for構文をフラグで分岐する場合
#お弁当の食材からリストを作成
foodstuff = ["Banana", "Mango", "Fish", "Carrot", "cabbage"]

#マンゴーがないか確認する
flag_food =False
for food in foodstuff:

	if food == "Mango":
		flag_found = True
		break

if flag_found:
	print("マンゴーが入っています")
else:
	print("ありません")