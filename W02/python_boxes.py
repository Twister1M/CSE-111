item_count = int(input('Enter the number of items:\n    '))
items_per_box = int(input('Enter the maximum number of items you would like in each box:\n    '))

if item_count % items_per_box > 0:
    total_boxes = 1
else:
    total_boxes = 0

total_boxes = total_boxes + (item_count // items_per_box)

print(f'For {item_count} items, packing {items_per_box} items in each box, you will need {total_boxes} boxes.')