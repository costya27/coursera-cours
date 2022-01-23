s = input()
if s.find('f') == s.rfind('f') and 'f' in s:
    print(s.find('f'))
elif 'f' in s:
    print(s.find('f'), s.rfind('f'))
a