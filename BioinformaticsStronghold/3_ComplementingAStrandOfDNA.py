

DNA = list('TGTGGTACACCATACCTTAGCACGGAGGATTTGCCTCCCCATGAAAGGGGATGGAGTAGGGCGACCACGGCGCGGTCTAATAGACAACCTCCGCTACTGCCGTGGATTCGCGTGTAAAAAGGGCTCGCTCCATGAAGAATGAGAGTATTAAGAAAACTCTGCATCGTGAGCCGCAGTCTAAGGGGATCCCCGCAAAAGTACGATATGATCAAACGAAAATTTTAGGGATGACCATTGTACTTGGTTGCTAGCTTTAAGGTTCGCGTACAATTGTGACTAGACCGTCGCAGCGGGATTGCTCGTTCTTTATATGGTCTTTTTACATGCTAGTGTGCGTTAACCTCGAAGCCTTGGGGGAAATCACGTAAGGGACTTCAAACTCCGTCATATGGATCGTGCATTTTATCTCAGCATATTGTGTTTCGGTGCGACAGTTGATTCAGGTCTAGTAGCTGTTGCGTGCGAGCGAGACCGCTAATAGGCAGCGCGGTCCCCCGCGTTACAACAACTTCTTATGATGTTCTACAAAGTACAATAATAAATGGATACAGGACAGAAGGCTTCGTCACTCACGTGAATGTTTAAATGGCAGCCCTTCACCAGTGAGCGGCGGAGAGGGAACAACACGATTTTTGGTCTAGATCAACTATACTGGTAGTAAGGCTTAGTCTTAAGCAGGCCGTCGCGAGATAGTCTCCGTAGAAGGACTGTGCCTCACAGTTTGTTGATCAACGATAAAGCGCTAAAATCGTCTAACGCTACATACCATATAGCGTCCTTACCGCGCGAACTTCATAGCGTACCCACGCCCTGCTGCCGCGGCTCCCTGATGATAAGTTCGGCGTAGGTTGGTCCCACGGCTGATAACTAAGACCTAACGGCCAAAACGGGCCGATAGAGAGGTTTGTTACGTGTCCGACCCCGCATAAACTG')

DNAcomp = DNA

for i, nucleotideo in enumerate(DNA):
    if nucleotideo == 'A':
        DNAcomp[i] = 'T'
    elif nucleotideo == 'C':
        DNAcomp[i] = 'G'
    elif nucleotideo == 'G':
        DNAcomp[i] = 'C'
    elif nucleotideo == 'T':
        DNAcomp[i] = 'A'

DNAcomp.reverse()
print(''.join(DNAcomp))
