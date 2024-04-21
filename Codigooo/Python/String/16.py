



tr = 'jatin is in coding'
test=tr.split()
# initializing mid string
mid_str = "best"
# finding middle word
mid_pos = len(test) // 2
test.insert(mid_pos,mid_str)

print("Formulated String : " + str(" ".join(test)))

