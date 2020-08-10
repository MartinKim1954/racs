
def split_and_decode():
    for i in range(len(PTOR_data)):
        j = i*2
        PTOR_data[i] = raw_data[j:(j+2)]
        PTOR_data[i] = int(PTOR_data[i], 16)


raw_data=b'F88359FE38778317'
PTOR_data = [0 for _ in range(8)]
# print(len(raw_data))
split_and_decode()
print(PTOR_data)

encodedRTOP_data = ""
for i in range(len(PTOR_data)):
    PTOR_data[i] = str(hex(PTOR_data[i]))
    PTOR_data[i] = PTOR_data[i][2:]
    encodedRTOP_data += PTOR_data[i]
encodedRTOP_data.encode()

print(type(encodedRTOP_data))
print(encodedRTOP_data)



# interpreted_PTOR_data = int(PTOR_data, 16)
# print(interpreted_PTOR_data) # 248

# interpreted_PTOR_data = str(hex(interpreted_PTOR_data))
# print(type(interpreted_PTOR_data))













# raw_data = bytes([raw_data])
# print(raw_data)

# raw_data_1 = b'FF'
# raw_data_2 = b'\xFF'

# raw_data_1 = int.from_bytes(raw_data_1, byteorder='big')
# raw_data_2 = int.from_bytes(raw_data_2, byteorder='big')

# print(raw_data_1)
# print(raw_data_2)

# raw_data = binascii.hexlify(raw_data)
# print(int.from_bytes(raw_data[0:2], byteorder='big'))

# PTOR_data = [0x00 for _ in range(10)]
# print(f"PTOR_data: {PTOR_data}")

# def split_and_decode():
#     for i in range(len(PTOR_data)):
#         j = i*2
#         PTOR_data[i] = int.from_bytes(raw_data[j:j+2], byteorder='big')

#         # PTOR_data[i] = raw_data[j:(j+2)]
#         # PTOR_data[i] = int(PTOR_data[i], 16)
        

# split_and_decode()
# print(f'AFTER: {PTOR_data}')

# encodedRTOP_data = [0x00 for _ in range(10)]
# def merge_and_encode(encodedRTOP_data):
#     for i in range(len(PTOR_data)):
#         encodedRTOP_data[i] = (PTOR_data[i]).to_bytes(1, byteorder='big')

# merge_and_encode(encodedRTOP_data)
# print(f'To-SEND: {encodedRTOP_data}\n')

# print(type(encodedRTOP_data[1]))


# print(int.from_bytes(encodedRTOP_data[0], byteorder='big'))


# # print((25).to_bytes(1, byteorder='big'))
