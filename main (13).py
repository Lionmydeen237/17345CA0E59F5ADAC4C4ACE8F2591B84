def linear_search_product(product_list, target_product):
    indices = []
    for i, product in enumerate(product_list):
        if product['name'] == target_product:
            indices.append(i)
    return indicesproducts = [
    {'name': '', 'price': 10},
    {'name': 'Product B', 'price': 15},
    {'name': 'Product A', 'price': 12},
    {'name': 'Product C', 'price': 20},
]

target_product = 'Product A'
result = linear_search_product(products, target_product)
print(result)  # Output: [0, 2]