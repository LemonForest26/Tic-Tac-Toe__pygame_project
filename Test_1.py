import time

#Setting time count
# while True:
#     start = time.ctime()
#     print(start)
#     time.sleep(1)

#Show timer passed in seconds
# while True:
#     start = time.ctime(time.time() - time.mktime(time.strptime(start, "%a %b %d %H:%M:%S %Y")))
#     print(start)
#     time.sleep(1)


def count_up_timer():
    seconds = 0  # Initialize the timer to 0 seconds

    while True:
        # Convert seconds into minutes and seconds
        minutes = seconds // 60
        remaining_seconds = seconds % 60

        # Format the time in MM:SS format
        formatted_time = f"{minutes:02}:{remaining_seconds:02}"
        
        # Print the timer value
        print(formatted_time, end='\r')

        # Wait for 1 second
        time.sleep(1)

        # Increment the seconds
        seconds += 1

# Start the timer
count_up_timer()
