def compress_string(string):
    compressed = []  # Stores the compressed representation
    count = 1  # Initialize the count of consecutive characters to 1
    for i in range(1, len(string)):
        if string[i] == string[i - 1]:
            count += 1  # Increment the count if the current character is the same as the previous character
        else:
            compressed.append(string[i - 1])  # Append the previous character
            compressed.append(str(count))  # Append its count
            count = 1  # Reset the count to 1 for the new character
 # Add the last character and its count to the compressed list
    compressed.append(string[-1])
    compressed.append(str(count))
    compressed_string = ''.join(compressed)  # Join the compressed list into a string
    # Check if the compressed string is shorter than the original string
    if len(compressed_string) < len(string):
        return compressed_string  # Return the compressed string if it is shorter
    else:
        return string  # Return the original string if the compressed string is not shorter

def compress_string_twice(string):
    compressed = compress_string(string)  # Compress the string once using the compress_string function
    return compress_string(compressed)  # Compress the result again

def decompress_string_twice(string):
    decompressed = decompress_string(string)  # Decompress the string once using the decompress_string function
    return decompress_string(decompressed)  # Decompress the result again

def decompress_string(string):
    decompressed = []  # Stores the decompressed representation
    i = 0
    while i < len(string):
        char = string[i]
        i += 1
        count = ""  # Initialize an empty count string
        while i < len(string) and string[i].isdigit():
            count += string[i]  # Append digits to the count string
            i += 1
        if count:
            decompressed.append(char * int(count))  # Repeat the character by the count value
        else:
            decompressed.append(char)  # If no count value, simply append the character
    return ''.join(decompressed)  # Join the decompressed list into a string
input_string = input("Enter a string: ")
compressed_once = compress_string(input_string)  # Compress the input string once
print("Compressed once:", compressed_once)
compressed_twice = compress_string_twice(input_string)  # Compress the input string twice
print("Compressed twice:", compressed_twice)
decompressed_twice = decompress_string_twice(compressed_twice)  # Decompress the doubly compressed string
print("Decompressed twice:", decompressed_twice)
