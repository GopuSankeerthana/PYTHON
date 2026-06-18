s = input().strip()
period = s[-2:]       
hh = int(s[:2])        
mm = s[3:5]
ss = s[6:8]
if period == "AM":
    if hh == 12:
        hh = 0
else:  
    if hh != 12:
        hh += 12
print(f"{hh:02d}:{mm}:{ss}") 