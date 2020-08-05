raw_data = b'6519816517811619'

PTOR_data = [0x00 for _ in range(8)]

print(raw_data)


def decode_and_split():
    for i in range(len(PTOR_data)):
        j = i*2
        PTOR_data[i] = raw_data[j:(j+2)]
        PTOR_data[i] = int(PTOR_data[i], 16)

decode_and_split()

print(PTOR_data)

def check_whether(data, ):
    