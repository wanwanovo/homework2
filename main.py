from time import strftime, sleep
import requests
import json
headers = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36',
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
}
r = requests.get('https://j1.pupuapi.com/client/product/storeproduct/detail/f8f0656f-d30e-497a-a536-e9edec17b74d/ed60af11-25b0-48b8-bc5b-f9136d9f89ad',headers=headers)
result = json.loads(r.content)
print(result)
spec = result["data"]["spec"]  # 规格
price = str(int(result["data"]["price"]) / 100)  # 折扣价
market_price = str(int(result["data"]["market_price"]) / 100)  # 原价
share_content = result["data"]["share_content"]  # 详细内容
name = result["data"]["name"]  # 商品名称
print("-------------商品：" + name + "-------------")
print("规格：" + spec)
print("原价：" + price)
print("原价/折扣价：" + price + "/" + market_price)
print("详细内容：" + share_content)

try:  # 终止程序时，不会报错
    while (True):
        nowTimeAndPrint = strftime('%Y' + '-' + '%m' + '-' + '%d' + ' %H:%M:%S,价格为' + price)
        print(nowTimeAndPrint)
        sleep(5)
except:
    print("程序结束")