def binary_fingers(bin_string):
    fingers = ['Pinkie','Ring','Middle','Index','Thumb']
    padded = bin_string.zfill(5)
    return [name for bit, name in zip (padded, fingers) if bit == '1']