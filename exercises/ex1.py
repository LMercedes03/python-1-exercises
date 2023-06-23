def hello_world(times):
    num_times = int(times)  # Convert the string to an integer
    counter = 0  # Initialize counter at 0
    while counter < num_times:  # Iterate counter based on string input of times
        print("Hello World from Python!", end="\n")
        counter += 1
