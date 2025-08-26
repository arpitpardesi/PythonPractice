import signal

def handle_sigint(signum, frame):
    print("SIGINT received! Cleaning up...")
    # Perform any necessary cleanup here
    exit(0)

signal.signal(signal.SIGINT, handle_sigint)

print("Press Ctrl+C to trigger SIGINT")
while True:
    pass