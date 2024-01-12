class Solution:
    def get_sub_str_len(self, sub_str: str, ele: str) -> int:
        count = 0
        for ele_sub_str in sub_str:
            if ele == ele_sub_str:
                return count
            else:
                count = count + 1
        return count

    def lengthOfLongestSubstring(self, s: str) -> int:
        result = {}
        for index, ele in enumerate(s):
            sub_str = s[index + 1:]
            length = self.get_sub_str_len(sub_str, ele)
            result[ele] = length

        print(result)
        return 1


def length_of_longest_substring(s):
    # Create a dictionary to store the index of each character in the string
    char_index = {}

    # Initialize variables for the start of the substring and the maximum length
    start = 0
    max_length = 0

    for end in range(len(s)):
        character = s[end]

        # If the character is already in the substring, update the start index
        if character in char_index and char_index[character] >= start:
            start = char_index[character] + 1

        # Update the index of the current character in the dictionary
        char_index[character] = end

        # Update the maximum length if the current substring is longer
        max_length = max(max_length, end - start + 1)

    return max_length


# obj = Solution()
# obj.lengthOfLongestSubstring("abcabcbb")

print(length_of_longest_substring("abcabcbb"))
