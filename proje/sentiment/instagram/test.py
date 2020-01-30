from get import GetComment

getter = GetComment()
print("??")


for i in range(2):
	comments = getter.getComments()
	for comment in comments:
		print(comment["node"]["text"])
