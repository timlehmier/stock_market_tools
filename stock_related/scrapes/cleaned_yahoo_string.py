txt = "388.55+2.99 (+0.78%)At close:  04:00PM EDT"

x = txt.split()
print(x)

# partitioning close pricing price from closing percentage + or -
close_price_raw = x[0]
close_price_positive = close_price_raw.partition('+')
close_price_negative = close_price_raw.partition('-')

# dropping percentage from close price
close_price_increase = close_price_positive[0]
close_price_decrease = close_price_negative[0]

# print relevant closing price
if close_price_increase < close_price_decrease:
    print(close_price_increase)
else:
    print(close_price_decrease)

# partitioning close percentage from close price
close_dollar_amount = x[0]
close_dollar_amount_increase_part = close_dollar_amount.partition('+')
close_dollar_amount_decrease_part = close_dollar_amount.partition('-')

# add back in the + or - to percentage increase or decrease
close_dollar_amount_increase = close_dollar_amount_increase_part[1] + close_dollar_amount_increase_part[2]
close_dollar_amount_decrease = close_dollar_amount_decrease_part[1] + close_dollar_amount_decrease_part[2]

# print relevant percentage
if close_dollar_amount_increase:
    print(close_dollar_amount_increase)
else:
    print(close_dollar_amount_decrease)


# separate out the unwanted characters in percentage change
closing_percentage_raw = x[1]
closing_percentage_part = closing_percentage_raw.partition('%')
closing_percentage_part_two = closing_percentage_part[0].partition('(')
closing_percentage_cleaned = closing_percentage_part_two[2]

print(closing_percentage_cleaned)