from crunchDoorApp.models import *
from django.shortcuts import get_object_or_404
import urllib2, sys
from BeautifulSoup import BeautifulSoup
import json
from pprint import pprint

###FOR CRAWLING THE GLASSDOOR API
for i in range(22,23):
	url = "http://api.glassdoor.com/api/api.htm?t.p=49299&t.k=apikey&format=json&v=1&action=employers&q=Software&city=San_Francisco&pn=%d"%(i) 
	hdr = {'User-Agent': 'Mozilla/5.0'}
	print 'URL: %s' % (url)
	req = urllib2.Request(url,headers=hdr)
	response = urllib2.urlopen(req)
	soup = BeautifulSoup(response)
	data_file = json.loads(str(soup))
	ourResult = data_file['response']['employers'] 
	for rs in ourResult:
		name = rs['name']
		website = rs['website']
		total_Reviews = rs['numberOfRatings']
		average = rs['overallRating']
		logo = rs['squareLogo']
		industry = rs['industryName']
		c = Company(name=name, 
		website=website, total_Reviews=total_Reviews, 
		average=average, logo=logo, industry=industry)
		c.save()
		pprint(name)


###FOR CRAWLING THE CRUNCHBASE API
for i in range(200,201):
	company = Company.objects.get(pk=i)
	print company.name
	pprint(company.company_id)
	companyPermalink = company.name.replace(" ", "-").lower()
	# print companyPermalink
	url = "https://api.crunchbase.com/v/3/organizations/%s?user_key=apikey"%(companyPermalink)
	print 'URL: %s' % (url)
	req = urllib2.Request(url)
	response = urllib2.urlopen(req)
	soup = BeautifulSoup(response)
	data_file = json.loads(str(soup))
	ourResult = data_file['data']['properties']['name']
	pprint(company.name)
	pprint(ourResult)
	founded = data_file['data']['properties']['founded_on']
	employees = data_file['data']['properties']['num_employees_max']
	funding = data_file['data']['properties']['total_funding_usd']
	symbol = data_file['data']['properties']['stock_symbol']
	extra_id = company.company_id
	c = Crunch(crunch_id = company, extra_id = extra_id, permalink = companyPermalink, founded = founded, employees = employees, funding = funding, symbol = symbol)
	c.save()
	pprint(c)




## DELETE A COMPANY
# company = Company.objects.get(pk=198)
# print company.name
# company.delete()
