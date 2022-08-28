import execjs
import json

item ={
	'name': '詹姆斯-哈登',
    'image': 'harden.png',
    'birthday': '1989-08-26',
    'height': '196cm',
    'weight': '99.8KG'
}

file='crypto.js'
node=execjs.get()
ctx=node.compile(open(file).read())

js=f"getToken({json.dumps(item,ensure_ascii=False)})"
print(js)
result=ctx.eval(js)
print(result)

