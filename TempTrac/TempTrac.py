"""A project to practice array use.
  Initialize an array,
  Get and store value from user input for 7 days,
  Calculate average temperature,
  Find highest and lowest temperature
"""
import statistics 

def main():
    # Initialize array
    temp_array = []

    # Use range function to iterate over values and store in array using append
    # Ask for the user to input data
    for i in range (7):
        forecast = float(input(f"Enter forecast for past seven days {i + 1}: "))
        temp_array.append(forecast)
        
    
    # Find average of temp for the week

    # Using mean from statistics
    average_stats = statistics.mean(temp_array)
    print(f"Average temp Stats:: {average_stats:.2f}")

    # Using sum and length
    average_sl = sum(temp_array) / len(temp_array)
    print(f"Average temp SL: {average_sl:.2f}")

    # Find highest and lowest Temp

    # Use max function to find highest temp
    print(f"Max temp for week: {max(temp_array):.2f}")

    # Use min function to find lowest temp
    print(f"Min temp for week: {min(temp_array):.2f}")
    
if __name__ == "__main__":
    main()


