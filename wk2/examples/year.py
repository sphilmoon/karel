YEAR = 365
DAY = 24
HOUR = 60
MIN = 60

def main():
    one_year_sec = MIN * HOUR * DAY * YEAR
    print("1 year in seconds is", f"{one_year_sec:,d}", "sec!")

if __name__ == "__main__":
    main()