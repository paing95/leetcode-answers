"""
68. Text Justification
https://leetcode.com/problems/text-justification/description/?envType=study-plan-v2&envId=top-interview-150

Words to fill up to maxWidth on a sentence.
Must include at least one space between each word.
Conditions:
1. Except from last sentence, words need to be center aligned.
That means extra spaces to be allocated between each space.
2. There can be a scenario when one word takes most of the
maxWidth and it is with trailing spaces. Cos next word won't fit.
3. On last sentence, it needs to be left aligned.
"""

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        # output
        res = []
        # current sentence, length of all words in current sentence
        line, length = [], 0
        # index i for a while loop
        i = 0
        while i < len(words):
            check = length + len(line) + len(words[i]) > maxWidth
            # one word case for center-aligned
            if check and len(line) == 1:
                # since length is len(all words in line)
                # spaces we need to put can be counted that way
                all_spaces = maxWidth - length
                # since line has only one element
                res.append(line[0] + (" " * all_spaces))
                # reset cos we already added to result
                line, length = [], 0
            # normal center-aligned
            elif check and len(line) > 1:
                # since length is len(all words in line)
                # spaces we need to put can be counted that way
                all_spaces = maxWidth - length
                # calculate space needed for each word
                # last element to be excluded cos we are appending spaces
                each_space = all_spaces // (len(line) - 1)
                # special case if spaces cannot be shared evenly
                remainder = all_spaces % (len(line) - 1)
                
                for j in range(len(line) - 1):
                    line[j] += " " * each_space
                    if remainder:
                        line[j] += " "
                        remainder -= 1
                
                res.append("".join(line))
                # reset cos we already added to result
                line, length = [], 0

            line.append(words[i])
            length += len(words[i])
            i += 1
        
        # for the last row
        # since length of last row will not exceed maxWidth
        line = " ".join(line)
        all_spaces = maxWidth - len(line)
        line += all_spaces * " "
        res.append(line)

        return res