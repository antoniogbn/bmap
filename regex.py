import re

p = re.compile(r'mT.{1,36}')
line = "mM      040     'Sweep Increment= 040mN      069     'System Type    = 069mO      002     'Gyro Type      = 002mP      072     'Polang Type    = 072mQ      029     '24v Polang Offset= 029mR      090     '24v Polang Scale= 090mS      003     'mT      232     'AZ Limit 1     = 1000mU      010     'mV      140     'AZ Limit 2     = 2700mW      002     'Polang Tx Type = 002mY      000     'mZ      000     'AZ Limit3      = 0000m[      000     'm\      000     'AZ Limit4      = 0000m]      000     '"
m = p.findall(line)

print(m)