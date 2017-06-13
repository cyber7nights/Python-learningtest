# -*- coding: utf-8 -*-

import base64

def safe_base64_decode(s):
    if int(len(s)) % 4 == 0:
        return base64.urlsafe_b64decode(s)
    else:
        a = 4 - int(len(s)) % 4
        while a > 0:
            s=s+b'='#此处等号应该用byte
            a = a - 1
        return base64.urlsafe_b64decode(s)
# 测试:
assert b'abcd' == safe_base64_decode(b'YWJjZA=='), safe_base64_decode('YWJjZA==')
assert b'abcd' == safe_base64_decode(b'YWJjZA'), safe_base64_decode('YWJjZA')
print('Pass')

#base64编码补‘=’，是因为最后一个字符二进制位每增加2个0，就要增加一个‘=’号。代表的意义是最后一个字符缺少的二进制位。而恰好这种不足二进制位的做法，让base64编码呈现出4的倍数。
#所以，‘=’符号并不是补足base64要满足4的倍数才出现的，而是因为补足最后一位编码时，发生的巧合。
#当文本多出1 byte文本时，其中二进制位只有8bit，base64编码用一个表示不全，需要在二进制位补足4个‘0’，凑齐12bit的二进制位，用2个base64编码来表示。所以，每补足两个0，base64用一个‘=’表示。而多出来1 byte的文本，则需要补足4四个零后的2个base64来编码。加上代表补足4个‘0’的两个‘=’，刚好又变成了4的倍数。
#同样，多出来2个 byte 文本时二进制位16bit。需要3个base64编码18个bit来表示。则需要补足2个‘0’，用1个‘=’表示补足的2个‘0’。3个base64编码，加一个‘=’，又恰好是4的倍数。
#综上，base64编码永远呈现4的倍数，其原因是补足二进制位所造成的。