#https://leetcode.com/problems/find-common-characters/
my_dict={}
words = ["cool","lock","cook"]
for keys in words[0]:
        my_dict[keys] = my_dict.get(keys, 0)+1 
for i in range(1,len(words)):
    new_dict={}
    for keys in words[i]:
        new_dict[keys] = new_dict.get(keys, 0)+1
        #"dictionary.get(keyname, value)" value(Optional) : A value to return if the specified key does not exist
    for keys in my_dict.copy():#.copy() creates a new instance of a dictionary so that the original dictionary doesn't change
        if new_dict.get(keys,0)==0:
            del my_dict[keys]
    for keys in words[i]:
        if my_dict.get(keys,0)==0:
            continue
        if new_dict[keys] >=my_dict[keys]:
            continue
        elif new_dict[keys]<my_dict[keys]:
            my_dict[keys]=new_dict[keys]
list=[]
for keys in my_dict:
    list+=my_dict[keys]*[keys]
print(list)