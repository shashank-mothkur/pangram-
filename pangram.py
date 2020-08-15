sentence=str(input("enter the string")).lower()
converting_string_into_set=set(sentence)
if(len(converting_string_into_set)<=27):
    print("pangram")
else:
    print("not pangram")
