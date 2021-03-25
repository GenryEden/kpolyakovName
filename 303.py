mapping = {
	'Л': "ИДЖК",
	"Б": "А",
	"В": "БАГ",
	"Г":"А",
	"Д":"БВ",
	"Е": "Г",
	"Ж": "ВЕ",
	"И": "Д",
	"К": "Е"
}

road = "Л"

while road.count('А') != len(road):
	for city in mapping:
		road = road.replace(city, mapping[city])

print(len(road))