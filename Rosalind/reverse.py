s = 'GTTCGCAACCGAAGAGCGTAGANNNNNNNNNNTTGCACTATAGGTGCACGAACTCTCCGGTCTCGTAAGCTTGCACTAAAAAAAAAAAAAAAACCCCCATTCACTCTGCGTTGATACCACTGCTT'
tso = 'AAGCAGTGGTATCAACGCAGAGTGAATGGGG'
end = 'AAAAAAAAAAAAAAAATCACGTTCGAATGCTCTGGCCTCTCAAGCACGTGGATATCACGTTNNNNNNNNNNAGATGCGAGAAGCCAACGCTTG'
mid = ''.join(['N' for n in range(75)])

oligo = tso + mid + end

def reverse(string):
	new = []
	for c in string[::-1]:
		new.append(c)
	new = ''.join(new)
	return new

print(reverse('CAAGCAGAAGACGGCATACGAGATTCGCCTTAGTCTCGTGGGCTCGGAGATGTGTATAAGAGACAGCAAGCGTTGGCTTCTCGCATCT'))