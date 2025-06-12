
def load_data(): #another method
    pass

def list_all_videos(videos):
     pass

def add_video(videos):
     pass

def update_video(videos):
     pass

def delete_video(videos):
     pass

def main():
    # Define the main function to control program execution.
    # All logic from initializing videos to handling user choices is placed here by cntrl + right sqaure bracket
    videos = load_data() #we will take the data from the file 

    while True:
        print("\n Youtube Manager | choose an option ")
        print("1. List all youtube videos ")
        print("2. Add a youtube video ")
        print("3. Update a youtube video details ")
        print("4. Delete a youtube video ")
        print("5. Exit the app ")
        choice = input("Enter your choice: ")

        match choice:
            case '1':
                list_all_videos(videos) 
            case '2':
                add_video(videos)        
            case '3':
                update_video(videos)      
            case '4': 
                delete_video(videos)       
            case '5':
                break
            case _:
                print("Invalid Choice")

# Entry point for the program
if __name__ ==  "__main__":
    main() 
