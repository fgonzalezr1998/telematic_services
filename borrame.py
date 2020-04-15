import pytz

def main():
    for tz in pytz.all_timezones:
        print tz

if __name__ == "__main__":
    main()
