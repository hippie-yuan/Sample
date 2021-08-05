import requests
import json


class Expert(object):
	def __init__(self, data):
		self.index = str(data[0])
		self.name = data[1]
		self.province = data[2]
		self.city = data[3]
		self.university = data[4]
		self.img = data[5]
		self.title = data[6]
		self.area = data[7]
		self.intro = str(data[8])
		self.token=None


	def get_token(self):
		url = ""

		payload = "{}"
		headers = {
			'Accept': 'application/json, text/plain, */*',
			'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
			'Content-Type': 'application/json;charset=UTF-8',
			'Cookie': 'JSESSIONID=eb3dbcbd-3bf5-47d5-9f0d-7934e3c52be4'}

		response = requests.request(
			"POST",
			url,
			headers=headers,
			data=payload).content
		response = json.loads(response.decode())["data"]["token"]
		return response

	def upload_expert(self):
		if self.token==None:
			self.token=self.upload_expert()
		url = ""

		payload=json.dumps({"type":2,
							"onlyAuthInfo":True,
							"userData":"{\"expertName\":\""+self.name+"\","
									   "\"areaIdProvince\":\""+areaIdProvince+"\","
									   "\"areaIdCity\":\""+areaIdCity+"\","
									   "\"email\":\"\","
									   "\"universityId\":\""+universityId+"\","
									   "\"universityName\":\"\","
									   "\"areaCode\":\"\",\"tel\":\"\","
									   "\"telephone\":\"\","
									   "\"domainIds\":\"1201328709007908865\","
									   "\"titleIds\":\"1201343134305681410\","
									   "\"expertLevelId\":\"\","
									   "\"tag\":\"\","
									   "\"academy\":\"\","
									   "\"summary\":\"aaaaaaaaaaaaa\","
									   "\"resume\":\"\","
									   "\"honor\":\"\","
									   "\"customTags\":\"\","
									   "\"areaText\":\"江苏省/苏州市\","
									   "\"avatar\":\"\","
									   "\"platformIds\":\"\"}"
							})
		headers = {
				'Accept': 'application/json, text/plain, */*',
				'Authorization': token,
				'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
				'Content-Type': 'application/json;charset=UTF-8'
		}
		response = requests.request("POST", url, headers=headers, data=payload)
		print(response.text)


token=login.get_token()
