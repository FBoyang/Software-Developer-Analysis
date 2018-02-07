
#######################################
#Boyang's part
key_word_dict = {}

job_dis_file = open("job.txt", 'r', encoding = 'utf8')
while True:
    job_dis = job_dis_file.readline()
    if (job_dis == ""):
        break
    else:
        for word in job_dis.split():
            if not word in job_dis_file:
                #if the key word not in dictionary, add it 
                key_word_dict.update({word: 1})
            else:
                #if the key word in the dictionary, increment it
                job_dis_file[word] += 1
                
#######################################
#Ruoting's part
#Parse noise words into a LIST
noiseWords = []
noise_file = open("noisewords.txt", "r")

while True:
    n_word = noise_file.readline()
    if n_word == "":
        break
    if n_word not in noiseWords:
        noiseWords.append(n_word)        
