'''Write a  Python program to check whether it follows the sequence given in the patterns array.
Pattern example:
For color1 = ["red", "green", "green"] and patterns = ["a", "b", "b"]
the output should be samePatterns(color1, patterns) = true;
For color2 = ["red", "green", "greenn"] and patterns = ["a", "b", "b"]
the output should be samePatterns (strings, color2) = false.'''

def samePatterns(color, patterns):
    if len(color) != len(patterns):
        return False
    
    mapping = {}  
    seen_patterns = set()  
    
    for c, p in zip(color, patterns):
        if c in mapping:
            if mapping[c] != p:
                return False
        else:
            if p in seen_patterns:
                return False
            mapping[c] = p
            seen_patterns.add(p)
    
    return True

color1 = ["red", "green", "green"]
patterns1 = ["a", "b", "b"]
print(samePatterns(color1, patterns1))  

color2 = ["red", "green", "greenn"]
patterns2 = ["a", "b", "b"]
print(samePatterns(color2, patterns2)) 