leap_year = int(raw_input())
if (leap_year % 4) == 0:
   if (leap_year % 100) == 0:
       if (leap_year % 400) == 0:
           print "yes"
       else:
           print "no"
   else:
       print "yes"
else:
   print "no"
