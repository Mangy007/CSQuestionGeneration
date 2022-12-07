import json

file = open("/mnt/D/d/Backup/Personal/Work/CS_Project/CSQuestionGeneration/assests/module_2_template.json")

data = json.load(file)

for key in data:
    print(data[key])