# import os

# # Define the list of strings strs
# strs = ["flower", "flow", "flight"]

# def common_prefix(strs):
#     return os.path.commonprefix(strs)

# # Call the common_prefix function and print the result
# print(common_prefix(strs))

#Another method

strs = ["flower", "flow", "flight"]

def prefix(strs):
    longest_str = ""
    if not strs:
        return longest_str
    shortest_str = min(strs, key= len)
    for i in range(len(shortest_str)):
        if all([x.startswith(shortest_str[:i+1]) for x in strs]):
            longest_str = shortest_str[:i+1]
        else:
            break
    return longest_str
print(prefix(strs))