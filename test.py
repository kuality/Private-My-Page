from requests import get, post

r = get("https://example.com")

print(r.text)

r = post("https://httpbin.org/post", data={"hello":"world"})

print(r.json())