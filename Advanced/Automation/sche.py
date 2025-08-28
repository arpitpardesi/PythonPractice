import schedule
import time

# Function definitions for scheduled tasks
def alarm():
   print("Time to restart the server   ")

def job():
   print("Starting daily tasks   ")

def meet():
   print('Weekly standup meeting   ')

# Schedule tasks
schedule.every(5).seconds.do(alarm)  # Run every 5 seconds
schedule.every().day.at("10:30").do(job)  # Run daily at 10:30 AM
schedule.every().monday.at("12:15").do(meet)  # Run every Monday at 12:15 PM

# Main loop to execute scheduled tasks
while True:
   schedule.run_pending()
   time.sleep(0.5)