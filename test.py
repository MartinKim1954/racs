# import binascii

# raw_data=b'FF'
# raw_data = int(raw_data, 16)
# print(raw_data) # 255

# raw_data = bytes([raw_data])
# print(raw_data)

raw_data_1 = b'FF'
raw_data_2 = b'\xFF'

print(type(raw_data_1))
print(type(raw_data_2))

raw_data_1 = int.from_bytes(raw_data_1, byteorder='big')
raw_data_2 = int.from_bytes(raw_data_2, byteorder='big')

print(raw_data_1)
print(raw_data_2)

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
