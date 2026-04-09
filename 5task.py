def is_isomorphic(s, t):
    if len(s) != len(t):
        return False

    map_s_t = {}
    map_t_s = {}

    for i in range(len(s)):
        if s[i] in map_s_t and map_s_t[s[i]] != t[i]:
            return False
        if t[i] in map_t_s and map_t_s[t[i]] != s[i]:
            return False

        map_s_t[s[i]] = t[i]
        map_t_s[t[i]] = s[i]

    return True


s = input()
t = input()
print(is_isomorphic(s, t))