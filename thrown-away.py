#!/usr/bin/env python

# Mark Mossberg
# 8/26/13

import json
import sys
import urllib

def main():

	# primitive arg parsing
	if len(sys.argv) < 2:
		print "Usage: ./throw-away.py [username 1] [username 2] [etc]"
		sys.exit()

	usernames = sys.argv[1:]
	pairs = {}
	reddit_url = "http://www.reddit.com/user/%s/about.json"

	# collect info
	for name in usernames:
		req_url = "http://www.reddit.com/user/%s/about.json" % name
		request = urllib.urlopen(req_url)
		resp = request.read()
		response = json.loads(resp)
		try:
			link_karma = response['data']['link_karma']
			comment_karma = response['data']['comment_karma']
		except KeyError:
			print "There was a mysterious error, try again!"
			sys.exit()
		pairs[name] = [link_karma, comment_karma]

	# calculate & output 

	total_link = 0
	total_comment = 0

	print """Karma Count (user, link, comment):
-----------"""
	for pair in pairs:
		output_str = "%s:\t%d\t%d" % (pair, pairs[pair][0], pairs[pair][1])
		total_link += pairs[pair][0]
		total_comment += pairs[pair][1]
		print output_str

	print "\nTotal Link Karma: %s" % total_link
	print "Total Comment Karma: %s" % total_comment

if __name__ == '__main__':
	main()
