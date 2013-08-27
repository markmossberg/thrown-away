#!/usr/bin/env python

# Mark Mossberg
# 8/26/13

import json
import sys
import urllib

### functions ##########

def die(message):
	pre = "ERROR: "
	print pre + message
	sys.exit(1)

def is_redditor(username):
	req_url = "http://www.reddit.com/user/%s/about.json" % username
	request = urllib.urlopen(req_url)
	resp = request.read()
	response = json.loads(resp)

	if len(response) == 1:
		return False
	else:
		return True

def collect_karma(usernames):
	pairs = {}
	reddit_url = "http://www.reddit.com/user/%s/about.json"

	for name in usernames:
		if not is_redditor(name):
			die(name + " is not a redditor. Exiting...")

		req_url = "http://www.reddit.com/user/%s/about.json" % name
		request = urllib.urlopen(req_url)
		resp = request.read()
		response = json.loads(resp)
		try:
			link_karma = response['data']['link_karma']
			comment_karma = response['data']['comment_karma']
		except KeyError:
			die("There was a mysterious error, try again!")
		pairs[name] = [link_karma, comment_karma]

	return pairs

def output(pairs):
	total_link = 0
	total_comment = 0

	print """Karma Count (user, link, comment):\n-----------"""
	for pair in pairs:
		output_str = "%s:\t%d\t%d" % (pair, pairs[pair][0], pairs[pair][1])
		total_link += pairs[pair][0]
		total_comment += pairs[pair][1]
		print output_str

	print "\nTotal Link Karma: %s" % total_link
	print "Total Comment Karma: %s" % total_comment

### main ##########

def main():
	# primitive arg parsing
	if len(sys.argv) < 2:
		print "Usage: ./throw-away.py [username 1] [username 2] [etc]"
		sys.exit()

	usernames = sys.argv[1:]
	pairs = collect_karma(usernames)

	output(pairs)

if __name__ == '__main__':
	main()
