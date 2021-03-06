import sys
from utils import codon_table, fasta_to_dict, reverse_comp 

def get_orfs(s):
	
	s = s.replace('T', 'U')
	orfs = []
	for p in range(len(s)):
		if s[p:p+3] == 'AUG':
			prot = []
			p2 = p
			for x in range(len(s[p2:])):
				codon = s[p2:p2+3]
				if len(codon) == 3:
					if codon in ['UAG', 'UAA', 'UGA']:
						orfs.append(''.join(prot))
						break
					prot.append(codon_table[codon]) 
					p2 += 3
	
	return set(orfs)

# s = fasta_to_dict(sys.argv[1]).value()
s = 'GATAAGTATCCTCGCATTTCCACGACGTCTTAGGTATCCTCCTAACGCACGGGCAGAAGG\
ATAGCTGAGATAATTTAGGTAGCCAATCAGTCAAGAAAATCGTCGCTGGTGGTCGGCATC\
AACTAATACAGTGACGGTTCACCATGCGGAAGTCCGGTATAGGCCGGATGGTTACTCGCT\
CCAGCGTTAACAATGTGAATTGCATGTGTCCGTTTCCTTGGCTTGTCTGAGTCCTAACTC\
AATATGACGACTGTGCAGGTACGTCGTAACGGGAGACAGTGTCGAGAGTCGGTACCTTAC\
GATTGTAAATTAAATACGCCTCATTAGGGCCTGCTATTTACTATGTGGATATTCAAGTCT\
CATGAGATTCCTTATTTCTGCCCGAAGGTTATCTGTACCTATGCGAATGAATCCGAGGTT\
ACCGACAGCCCGCGGGTAGCTACCCGCGGGCTGTCGGTAACCTCGGATTCATCAAGTCTC\
ATCCTCAATCCCCACACGACGGCGTGATGCACCTCCCGTGGGCCGTCTTACATATCCATG\
ATTCGTGGCAAGGACCCTTGCTTCAAAGTCGACAACGAGGTTTTTGGAATCAGTCTTTGG\
GCCATCTAGCGGGGATGGAGCGCCCGGTCCGACGTCCCGACCCTGTAAAGGGGAATCGAC\
TCCTTAGGGTCGGTCCGCTTACCGTAAGGGTCCGGCATGACAAGGATCCACTGCCACACT\
CGGGGCGAGCCCTACTGCGAGGTGGATTGGACTAACAACACGAGAGAGGCTAATGCACCT\
TATACTCGGATGCCCTGATATTTGCCGGTTTCCATTCCTGCGTGGAGTCTTCTGAGCGCC\
TGTGTCTAAATACGTAGATGTTCTCGTTCCAAGGTTCG'
orfs = set()
for string in [s, reverse_comp(s)]:
	orfs.update(get_orfs(string))
for orf in orfs:
	print(orf)
