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