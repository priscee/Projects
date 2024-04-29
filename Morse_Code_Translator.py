'''
Morse Code Chart
'''
morse_dict = {
  #letters
  'A': '*-', 'B': '-***', 'C': '-*-*', 'D': '-**',
  'E': '*', 'F': '**-*', 'G': '--*', 'H': '****',
  'I': '**', 'J': '*---', 'K': '-*-', 'L': '*-**',
  'M': '--', 'N': '-*', 'O': '---', 'P': '*--*',
  'Q': '--*-', 'R': '*-*', 'S': '***', 'T': '-',
  'U': '**-', 'V': '***-', 'W': '*--', 'X': '-**-',
  'Y': '-*--', 'Z': '--**', 
  #numbers
  '1': '*----', '2': '**---','3': '***--', '4': '****-',
  '5': '*****', '6': '-****', '7': '--***', '8': '---**',
  '9':'----*', '0': '-----',
  #punctuations
  '.': '*-*-*-', ',': '--**--','?': '**--**', "'": '*----*',
  '!': '-*-*--', '/': '-**-*', '(': '-*--*', ')': '-*--*-',
  '&': '*-***',':': '---***', ';': '-*-*-*', '=': '-***-',
  '+': '*-*-*', '-': '-****-', '_': '**--*-', '"': '*-**-.',
  '$': '***-**-', '@': '*--*-*', ' ': '/'
}

'''
Start of Program
'''
print('Morse Code Translator\n')

print("What do you wantto do?\n")
print('1) Encrypt to Morse')
print('2) Decrypt to English\n')
select = int(input("Enter selection: "))
print('\n')

'''
Encryt to Morse
'''
def encrpyt_to_morse(message1):
  morse_code = ''
  for char in message1.upper():
      if char != ' ':
        morse_code += morse_dict[char] + ' '
      else:
        morse_code += '/ '
  return morse_code

'''
Decrypt to English
'''
def decrypt_to_english(message2):
  english_text = ''
  citext = ''
  for letter in message2:
    if (letter != ' '):
      citext += letter
    elif citext != '':
      english_text += list(morse_dict.keys())[list(morse_dict.values()).index(citext)]
      citext = ''
  if citext != '':
    english_text += list(morse_dict.keys())[list(morse_dict.values()).index(citext)]
  return english_text

if select == 1:
  message1 = input("Enter word or phrase: ")
  print(encrpyt_to_morse(message1))
else:
  message2 = input("Enter morse (* or -): ")
  print(decrypt_to_english(message2))