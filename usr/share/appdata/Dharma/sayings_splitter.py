import sqlite3

con = sqlite3.connect("bud_lit.db")
cur = con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS sayings(no INTEGER, verse TEXT)")
con.commit()
res = cur.execute("SELECT name FROM sqlite_master")
table = res.fetchall()
#print(table)

#Open text
with open("sayings-of-the-dhamma.txt") as text:
    content =text.readlines()

#Variables
saying=0
stanza=[]

#Split
for line in content:
    line_cln = line.strip()
    if line_cln == "":
        if stanza:
            saying+=1
            verse_text = " ".join(stanza)
            con.execute("INSERT INTO sayings VALUES(?, ?)",(saying, verse_text))
            stanza=[]
    else:
        #saying_change=False
        stanza.append(line_cln)

#In case the last line is not a blank        
if stanza:
    saying += 1
    cur.execute("INSERT INTO sayings VALUES(?, ?)", (saying, str(stanza)))
    
con.commit()

ver = cur.execute("SELECT verse FROM sayings")
verse_vals = ver.fetchall()

output = verse_vals[7]
print(output[0])

con.close()