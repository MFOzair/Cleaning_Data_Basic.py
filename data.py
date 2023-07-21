#Data need to be clean
highlighted_poems = "Afterimages:Audre Lorde:1997,  The Shadow:William Carlos Williams:1915, Ecstasy:Gabriela Mistral:1925,   Georgia Dusk:Jean Toomer:1923,   Parting Before Daybreak:An Qi:2014, The Untold Want:Walt Whitman:1871, Mr. Grumpledump's Song:Shel Silverstein:2004, Angel Sound Mexico City:Carmen Boullosa:2013, In Love:Kamala Suraiyya:1965, Dream Variations:Langston Hughes:1994, Dreamwood:Adrienne Rich:1987"
print(highlighted_poems )

#make list of each poems 
highlighted_poems_list = highlighted_poems.split(",")
print(highlighted_poems_list)
highlighted_poems_stripped=[]
for poems_list in highlighted_poems_list:
    highlighted_poems_stripped.append(poems_list.strip())
print(highlighted_poems_stripped)
highlighted_poems_details = []
for poems_stripped in highlighted_poems_stripped:
    highlighted_poems_details.append(poems_stripped.split(":"))
print(highlighted_poems_details)

titles =[]
poets=[]
dates=[]

for poems_details in highlighted_poems_details:
    titles.append(poems_details[0])
    poets.append(poems_details[1])
    dates.append(poems_details[2])
print(titles, poets, dates)
for poem_final in highlighted_poems_details:
    finanl_output= "The poem {} was published by {} in {}.".format(poem_final[0],poem_final[1],poem_final[2])
    print(finanl_output)
