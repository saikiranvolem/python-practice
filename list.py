my_list = ['apple']
vowels = "aeiou"
unique_found = []
for words in my_list:
    for letter in words:
        if letter in vowels and letter not in unique_found:
            unique_found.append(letter)
print(unique_found)

nums = [1, 2, 3, 4, 5]
print(sum(nums))

nums = [1, 2, 3, 4, 5]
print(min(nums))
print(max(nums))



