import math
size="s" #s,m,l
add_pepparoni=True
extra_cheese=True

total_bill=0;
small_price=15;medium_price=20;large_price=25;
peparroni_small=2;peparroni_others=3;

if size=="s":
    total_bill==small_price
if size=="m":
    total_bill=medium_price
if size=="l":
    total_bill=large_price    
    
if add_pepparoni and size=='s':
    total_bill=total_bill+peparroni_small;
else:
    total_bill+=peparroni_others

