
with open("Shakespeare.txt") as f:
    tdata = f.read()
crap = []
for i in tdata:
    if not i.isalnum():
        crap.append(i)
        
craps = set(crap)
craps.remove(" ")
craps.remove("'")

tdata = tdata.replace("\n"," ")
str = ""
for char in tdata:
    if char not in craps:
        str += char
lst = str.lower().split()

with open("Shakespeare_word_count", "w+") as fo:
    fo.write(json.dumps(Counter(lst)))
    
wh = json.dumps(Counter(lst))

put = subprocess.Popen("hdfs dfs -put ~/Shakespeare_word_count /test2", bufsize = 0,stdout=subprocess.PIPE, stderr=subprocess.PIPE)
put.communicate()
