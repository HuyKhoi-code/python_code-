def check_panlidrome(str):
    if (str == str[::-1]):
        return True
    return False

ori_str = 'abb'
for i in range (0, len(ori_str), 1):
    new_str = ori_str + ori_str[i::-1]
    if (check_panlidrome(new_str) == True):
        print (new_str)
        break
        