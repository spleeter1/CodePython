def get_word_set(sentence):
    words = sentence.lower().split()
    word_set = list(dict.fromkeys(words))
    return sorted(word_set)


# Nhập hai dòng ký tự
line1 = input()
line2 = input()

# Lấy tập từ từ hai dòng ký tự
set1 = get_word_set(line1)
set2 = get_word_set(line2)

# Tìm hợp và giao của hai tập từ
union_set = sorted(set(set1) | set(set2))
intersection_set = sorted(set(set1) & set(set2))

# In kết quả
print(' '.join(union_set))
print(' '.join(intersection_set))