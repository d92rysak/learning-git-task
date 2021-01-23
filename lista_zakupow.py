shopping_dict = {
    "piekarnia": ["chleb","pączek","bułki"],
    "warzywniak": ["marchew","seler","rukola"]
}
items_quantity=0
for sklep in shopping_dict:
    """Shopping_list=[]
    for item in shopping_dict[sklep] : 
        item=item.title()   
        Shopping_list.append(item)"""
    print(f"Idę do {sklep.title()} i kupuję tu następujące rzeczy: {shopping_dict[sklep]}")
    items_quantity=items_quantity+len(shopping_dict[sklep])
print(f"W sumie kupuję {items_quantity} produktów")
print("robię pierwszy commit")
