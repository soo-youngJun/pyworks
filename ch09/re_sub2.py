# 주민번호 뒷자리 *로 표시
import re

data = """
 kim 871212-1234567
 lee 951011-2345678
"""

p = re.compile("(\d{6})[-](\d)(\d{6})")
m = p.sub("\g<1>-\g<2>******", data)
print(m)