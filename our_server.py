from sanic import Sanic
from sanic.response import json
import json as js

small_server = Sanic("Small_Amazon_Server")

@small_server.route('/login')
async def login_to_amazon(request):
	return json({'success':True})

@small_server.route('/products')
async def show_products(request):
	fp = open('amazon_data.json','r')
	content = fp.read()
	fp.close()
	content_dict = js.loads(content)
	return json(content_dict)

small_server.run()