def isIsomorphic(s, t) -> bool:
    if len(s) != len(t):
        return False
    char_map_s = {}
    mapped_char = set()

    for i in range(len(s)):
        if s[i] not in char_map_s:
            # verify char in t is not already mapped to another char
            if t[i] in mapped_char:
                return False
            char_map_s[s[i]] = t[i]
            mapped_char.add(t[i])
        else:
            if char_map_s[s[i]] != t[i]:
                return False
    return True

print(isIsomorphic('baba', 'badc')) #false
print(isIsomorphic('paper', 'title')) #true
print(isIsomorphic('egg', 'add')) #true
print(isIsomorphic('foo', 'bar')) #false