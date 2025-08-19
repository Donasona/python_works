product={"code":"sku120","title":"redmi note 14 pro",
         "brand":"mi","price":22000,"offer":200}
# print(product["code"])
# product["discount"]="5%"
# print(product)
if "offer"in product:
    product["offer"] += 500
else:
    product["offer"] = 100
print(product)