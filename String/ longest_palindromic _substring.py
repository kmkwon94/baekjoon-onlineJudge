def expand(left : int, right : int) -> str:
    # 펠린드롬 판별 및 투포인터 확장
    # 슬라이딩 윈도우 범위를 받아서
    # 그 윈도우의 문자열이 펠린드롬인지 검사
    # 펠린드롬이라면 범위를 넓혀가면서 여전히 펠린드롬인지
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return s[left+1 : right]
        
    # 단어가 한개여서 그 자체로 펠린드롬인 경우, 전체를 뒤집었더니 전체가 펠린드롬이면 굳이 안돌아도 되니까
    if len(s) < 2 or s == s[::-1]:
        return s
        
    # 슬라이딩 윈도우 우측으로 이동
    result = ''
        
    for idx in range(len(s) - 1):
        result = max(result, expand(idx, idx),
                             expand(idx, idx + 1),
                             key = len)
    return result