def is_leap(year):
    leap = False
    def divisible_by_100(year):
        return True if year%100==0 else False
    def divisible_by_400(year):
        return True if year%400==0 else False
    def divisible_by_4(year):
        return True if year%4==0 else False
    if (divisible_by_4(year) and divisible_by_100(year) and divisible_by_400(year)) or (divisible_by_4(year) and not divisible_by_100(year)) :
        leap = True
    # Write your logic here
    
    return leap

year = int(input())
print(is_leap(year))
