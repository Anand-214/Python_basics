mystr = "Anand - +919028525438 uiew - +919456789021 wefwe - +914324567890"

import re
patt = re.compile(r'\d{10}')
matches = patt.finditer(mystr)
for match in matches:
	print(match)


