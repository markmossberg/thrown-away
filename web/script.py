def main():
	usernames = get_usernames()
	print(usernames)


def add_row():
	list_str = '<li><input type="text" name="name" id="name" placeholder="usr"/></li>'
	doc['input_list'].html += list_str

def get_usernames():
	usernames = []
	inputs = doc.get(name="name")
	for input in inputs:
		if input.value == '':
			continue
		else:
			usernames.append(input.value)
	return usernames

def on_complete(req):
	if req.status == 200 or req.status == 0:
		print(dir(req))
		print(req.text)
	else:
		print("error")

def test():
	# print(doc['bod'].html)
	add = '<script src="http://www.reddit.com/user/mmosskicker/about.json?jsonp=callback"></script>'
	print(add)
	doc['bod'].html += add
	return
	doc['bod'].html += add
	return
	data = JSObject(req)
	print(data.data.name)

test()
