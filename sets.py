#Sets
daily_pints = {1,2,3}
print(type(daily_pints))
print(daily_pints)
# In below there is only once write there is no duplicate
daily_pints_logs = {1,59,6,4,5,4,5,2,4,54,5}
print(daily_pints_logs)
 
Suprit_daily_pints_logs = {55,46,64,984,88,8464,88,8,8,4,4}
print(Suprit_daily_pints_logs)
# In below all unique valus b/w tham
print(daily_pints_logs | Suprit_daily_pints_logs) 
# Common values b/w them
print(daily_pints_logs & Suprit_daily_pints_logs)
# Dose n't match 
print(daily_pints_logs - Suprit_daily_pints_logs)
#the value is present in one or other but not both
print(daily_pints_logs ^ Suprit_daily_pints_logs)
