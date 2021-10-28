def ip_decoder(ip):
   
    ip = ip.replace('\n', '')

    bin_header = [
        f'VER: {int(ip[0:4], 2)} / {ip[0:4]}',
        f'HLEN: {int(ip[4:8], 2)} / {ip[4:8]}',
        f'DS: {int(ip[8:16], 2)} / {ip[8:16]}',
        f'TL: {int(ip[16:32], 2)} / {ip[16:32]}',
        f'ID: {int(ip[32:48], 2)} / {ip[32:48]}',
		f'FLAG: {ip[48:51]} / {ip[48:51]}',
        f'FRAG OFFSET: {int(ip[51:64], 2)} /{ip[51:64]}',
        f'TTL: {int(ip[64:72], 2)} / {ip[64:72]}',
        f'PRO: {int(ip[72:80], 2)} / {ip[72:80]}',
        f'CHECKSUM: {int(ip[80:96], 2)} / {ip[80:96]}',   
        f'SOURCE IP: {int(ip[96:104], 2)}.{int(ip[104:112], 2)}.{int(ip[112:120], 2)}.{int(ip[120:128], 2)}\n{ip[96:104]}.{ip[104:112]}.{ip[112:120]}.{ip[120:128]}',
        f'DESTINATION IP: {int(ip[128:136], 2)}.{int(ip[136:144], 2)}.{int(ip[144:152], 2)}.{int(ip[152:160], 2)}\n{ip[128:136]}.{ip[136:144]}.{ip[144:152]}.{ip[152:160]}',
	]

    header = ''
    for entry in bin_header:
	    header = header + entry + '\n'

    return header

# random example:
decoded_ip_header = ip_decoder("0110100101110000001000000110100001100101011000010110010001100101011100100110010010001001001100101001000100101010010001010011001010111100010010001001010010011110")
print(decoded_ip_header)
# prints:
# VER: 6 / 0110
# HLEN: 9 / 1001
# DS: 112 / 01110000
# TL: 8296 / 0010000001101000
# ID: 25953 / 0110010101100001
# FLAG: 011 / 011
# FRAG OFFSET: 1125 /0010001100101
# TTL: 114 / 01110010
# PRO: 100 / 01100100
# CHECKSUM: 35122 / 1000100100110010
# SOURCE IP: 145.42.69.50
# 10010001.00101010.01000101.00110010
# DESTINATION IP: 188.72.148.158
# 10111100.01001000.10010100.10011110