import tkinter as tk
import tkinter.scrolledtext as tkst

class UpdateVideos:
    def __init__(self, window):
        # Set up the main window
        window.geometry("750x350")
        window.title("Update Videos")

        # Update Video Button
        update_video_button = tk.Button(window, text="Update Video", command=self.update_video)
        update_video_button.grid(row=0, column=0, padx=10, pady=10)

        # Video Number Input
        tk.Label(window, text="Enter Video Number:").grid(row=0, column=1, padx=10, pady=10)
        self.video_number_entry = tk.Entry(window, width=5)
        self.video_number_entry.grid(row=0, column=2, padx=10, pady=10)

        # Video Name Input
        tk.Label(window, text="Video Name:").grid(row=1, column=0, padx=10, pady=10)
        self.video_name_entry = tk.Entry(window, width=30)
        self.video_name_entry.grid(row=1, column=1, columnspan=2, padx=10, pady=10)

        # Director Name Input
        tk.Label(window, text="Director Name:").grid(row=2, column=0, padx=10, pady=10)
        self.director_name_entry = tk.Entry(window, width=30)
        self.director_name_entry.grid(row=2, column=1, columnspan=2, padx=10, pady=10)

        # Rating Input
        tk.Label(window, text="Rating:").grid(row=3, column=0, padx=10, pady=10)
        self.rating_entry = tk.Entry(window, width=5)
        self.rating_entry.grid(row=3, column=1, padx=10, pady=10)

        # Scrolled Text Box for Video List
        self.video_list_text = tkst.ScrolledText(window, width=60, height=12, wrap="none")
        self.video_list_text.grid(row=4, column=0, columnspan=3, padx=10, pady=10)

        # Status Label
        self.status_label = tk.Label(window, text="", font=("Helvetica", 10))
        self.status_label.grid(row=5, column=0, columnspan=3, padx=10, pady=10)

        # List to store videos
        self.video_list = []  # Ideally, this should be passed to the class or loaded from a file

    def update_video(self):
        video_number = self.video_number_entry.get()
        video_name = self.video_name_entry.get()
        director_name = self.director_name_entry.get()
        rating = self.rating_entry.get()

        # Ensure all fields are filled
        if video_number and video_name and director_name and rating:
            try:
                rating = float(rating)
                
                # Find the video by number and update its details
                for video in self.video_list:
                    if video['number'] == video_number:
                        video['name'] = video_name
                        video['director'] = director_name
                        video['rating'] = rating
                        self.status_label.configure(text=f"Video {video_number} updated successfully!", fg="green")
                        self.refresh_video_list()
                        return
                
                # If video is not found
                self.status_label.configure(text=f"Video {video_number} not found.", fg="red")
            except ValueError:
                self.status_label.configure(text="Invalid rating. Please enter a numeric value.", fg="red")
        else:
            self.status_label.configure(text="All fields are required.", fg="red")

    def refresh_video_list(self):
        # Clear the text box and display the updated video list
        self.video_list_text.delete(1.0, tk.END)
        for video in self.video_list:
            video_info = (f"Video Number: {video['number']}, "
                          f"Name: {video['name']}, "
                          f"Director: {video['director']}, "
                          f"Rating: {video['rating']}")
            self.video_list_text.insert(tk.END, video_info + "\n")

if __name__ == "__main__":
    root = tk.Tk()
    app = UpdateVideos(root)
    
    # Example video list
    app.video_list = [
        {"number": "01", "name": "Inception", "director": "Christopher Nolan", "rating": 8.8},
        {"number": "02", "name": "The Matrix", "director": "Lana Wachowski, Lilly Wachowski", "rating": 8.7},
        {"number": "03", "name": "Interstellar", "director": "Christopher Nolan", "rating": 8.6},
    ]
    
    app.refresh_video_list()  # Display the initial video list
    root.mainloop()
