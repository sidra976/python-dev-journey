import sqlite3  # Import the sqlite3 library for working with SQLite databases

# Connect to an SQLite database (creates the file if it doesn't exist)
conn = sqlite3.connect('youtube_videos.db')

# Create a cursor object which lets us run SQL commands
cursor = conn.cursor()

# Create a table named 'videos' if it doesn't already exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS videos (
               id INTEGER PRIMARY KEY,       -- Unique ID for each video
               name TEXT NOT NULL,           -- Video name (required)
               time TEXT NOT NULL            -- Video duration/time (required)
    )
''')

# Function to list all videos from the database
def list_videos():
    cursor.execute("SELECT * FROM videos")     # Fetch all records from the videos table
    for row in cursor.fetchall():              # Loop through each row in the result
        print(row)                             # Print the row (each video)

# Function to add a new video to the database
def add_video(name, time):
    cursor.execute("INSERT INTO videos (name, time) VALUES (?, ?)", (name, time))  # Insert name and time into table
    conn.commit()  # Save the changes to the database

# Function to update an existing video's name and time
def update_video(video_id, new_name, new_time):
    cursor.execute("UPDATE videos SET name = ?, time = ? WHERE id = ?", (new_name, new_time, video_id))  # Update by ID
    conn.commit()  # Save changes

# Function to delete a video by its ID
def delete_video(video_id):
    cursor.execute("DELETE FROM videos WHERE id = ?", (video_id,))  # Delete by ID (note: comma is required for single tuple)
    conn.commit()  # Save changes

# Main function to run the console-based YouTube video manager
def main():
    while True:  # Infinite loop until user chooses to exit
        print("\nYoutube manager app with DB")       # Menu heading
        print("1. List Videos")                      # Option to list
        print("2. Add Videos")                       # Option to add
        print("3. Update Videos")                    # Option to update
        print("4. Delete Videos")                    # Option to delete
        print("5. Exit app")                         # Option to exit

        choice = input('Enter your choice: ')        # Take user input

        if choice == '1':
            list_videos()                            # Call list function
        elif choice == '2':
            name = input("Enter the video name: ")   # Ask for video name
            time = input("Enter the video time: ")   # Ask for video duration
            add_video(name, time)                    # Call add function
        elif choice == '3':
            video_id = input("Enter video ID to update: ")   # Ask for ID
            name = input("Enter the video name: ")           # Ask for new name
            time = input("Enter the video time: ")           # Ask for new time
            update_video(video_id, name, time)               # Call update function
        elif choice == '4':
            video_id = input("Enter video ID to delete: ")   # Ask for ID to delete
            delete_video(video_id)                           # Call delete function
        elif choice == '5':
            break                                             # Exit the loop and app
        else:
            print("Invalid Choice ")                          # Invalid input handling
    
    conn.close()  # Close the database connection when exiting

# This ensures the main function runs only if the script is run directly
if __name__ == "__main__":
    main()
