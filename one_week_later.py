
# -----------------------------
# Global Constants
# -----------------------------
DAYS_IN_WEEK = 7

# Days in each month (no leap year handling)
FEB_DAYS = 28
LONG_MONTH_DAYS = 31  # Jan, Mar, May, Jul, Aug, Oct, Dec
SHORT_MONTH_DAYS = 30 # Apr, Jun, Sep, Nov

# Copy input values so we can keep originals for final output
def find_date_one_week_later(month, date):
    # Add 7 days
    day = date + DAYS_IN_WEEK
    # -----------------------------
    # Adjust for month boundaries
    # -----------------------------
    # February (28 days)
    if month == 2 and day > FEB_DAYS:
        month += 1
        day -= FEB_DAYS
    # Months with 31 days
    elif (month == 1 or month == 3 or month == 5 or
        month == 7 or month == 8 or month == 10 or
        month == 12) and day > LONG_MONTH_DAYS:
        month += 1
        day -= LONG_MONTH_DAYS
    # Months with 30 days
    elif day > SHORT_MONTH_DAYS:
        month += 1
        day -= SHORT_MONTH_DAYS

    # Wrap around past December
    if month > 12:
        month %= 12
    return month, day

def main():
    month = 0
    while month < 1 or month > 12:
        month = int(input("Month (1-12): "))
    day = 0
    while day < 1 or day > 31:
        day = int(input("Day (1-31): "))
    new_month, new_day = find_date_one_week_later(month, day)
    print("A week after " + str(month) + "/" + str(day) +
            " is " + str(new_month) + "/" + str(new_day))

if __name__ == "__main__":
    main()
