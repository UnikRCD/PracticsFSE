file_commands = 'commands.0.txt'
file_prot = 'sequences.0.txt'

def read_sequences(filename):
    prot = []
    file = open(filename, 'r', encoding='utf-8')

    for line in file:
        frags = line.strip().split('\t')
        protein_data = (
            frags[0].strip(),
            frags[1].strip(),
            frags[2].strip()
        )
        prot.append(protein_data)
    return prot

def read_commands(filename):
    commands = []
    file = open(filename, 'r',encoding='utf-8')

    for line in file:
       frags=line.strip().split('\t')
       
       if frags[0] == 'search' or frags[0] == 'mode':
        commands_data= (
         frags[0].strip(),
         frags[1].strip(),
         )
       else:
           commands_data = (
               frags[0].strip(),
               frags[1].strip(),
               frags[2].strip()
           )
       commands.append(commands_data)
    return commands

def decode (x):
    word=""
    for i in range(len(x)):
        if x[i].isdigit():
            word =word+x[i+1]*(int(x[i])-1)
        else:
            word=word+x[i]
        
    return word

def searches_data(prot):
    search=""
    prot=decode(prot)
    prots=read_sequences(file_prot)
    
    for i in range(len(prots)):
        if prot in (prots[i])[2]:
            search=(prots[i])[1]+" "+ (prots[i])[0]
    return search

    if search=="":
        return 'NOT FOUND'
