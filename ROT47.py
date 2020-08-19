'''
A tool to apply the ROT47 caesar cipher
'''
filename = r'/home/kali/cybersploit2/custom_wordlist.txt'
new_filename = r'/home/kali/cybersploit2/custom_wordlist_modified.txt'
decrypted_word = ''
decrypted_word_list = []

with open(filename, 'r') as f:
    wordlist = f.readlines()
    # print(f' wordlist = {wordlist}')
    for i in range(len(wordlist)):
        # strip the newline character out
        wordlist[i] = wordlist[i].rstrip('\n')
    for word in wordlist:
        for i in range(len(word)):
            value = ord(word[i])
            if value >= 80:
                new_value = value - 47
                decrypted_word += chr(new_value)
            else:
                new_value = 126 - (47 - (value - 33)) + 1
                decrypted_word += chr(new_value)
        decrypted_word_list.append(decrypted_word)
        decrypted_word = ''
    # print(f' decrypted_word_list = {decrypted_word_list}')

with open(new_filename, 'w') as w:
    for word in decrypted_word_list:
        w.writelines(word + '\n')