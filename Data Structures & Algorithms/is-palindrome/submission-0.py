class Solution:
    def isPalindrome(self, s: str) -> bool:
        text = s.strip().lower()
        cleaned_text = re.sub(r'[^a-zA-Z0-9]', '', text)
        reversed_text=''
        for char in cleaned_text:
            reversed_text = char+reversed_text
        # print(cleaned_text)
        # print(reversed_text)
        return cleaned_text==reversed_text
            

        