import tkinter as tk
import tkinter.scrolledtext as tkst
import csv

class VideoManager:
    def __init__(self, window):
        # Set up the main window
        window.geometry("850x500")
        window.title("Video Manager")

        # Video Number Input (for update and playlist)
        tk.Label(window, text="Enter Video Number:").grid(row=0, column=0, padx=10, pady=10)
        self.video_number_entry = tk.Entry(window, width=5)
        self.video_number_entry.grid(row=0, column=1, padx=10, pady=10)

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

        # Add Video Button
        add_video_button = tk.Button(window, text="Add Video", command=self.add_video)
        add_video_button.grid(row=0, column=2, padx=10, pady=10)

        # Update Video Button
        update_video_button = tk.Button(window, text="Update Video", command=self.update_video)
        update_video_button.grid(row=0, column=3, padx=10, pady=10)

        # Playlist Buttons
        play_playlist_button = tk.Button(window, text="Play Playlist", command=self.play_playlist)
        play_playlist_button.grid(row=4, column=0, padx=10, pady=10)

        reset_playlist_button = tk.Button(window, text="Reset Playlist", command=self.reset_playlist)
        reset_playlist_button.grid(row=4, column=1, padx=10, pady=10)

        # Scrolled Text Box for Video List
        self.video_list_text = tkst.ScrolledText(window, width=80, height=12, wrap="none")
        self.video_list_text.grid(row=5, column=0, columnspan=4, padx=10, pady=10)

        # Status Label
        self.status_label = tk.Label(window, text="", font=("Helvetica", 10))
        self.status_label.grid(row=6, column=0, columnspan=4, padx=10, pady=10)

        # File name for CSV storage
        self.csv_file = "videos.csv"

        # Load existing videos from CSV
        self.video_list = self.load_videos_from_csv()
        self.playlist = []

        # Refresh video list display
        self.refresh_video_list()

    def load_videos_from_csv(self):
        video_list = []
        try:
            with open(self.csv_file, mode='r', newline='') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    row['rating'] = float(row['rating'])  # Convert rating to float
                    row['play_count'] = int(row.get('play_count', 0))  # Convert play_count to int
                    video_list.append(row)
        except FileNotFoundError:
            # If the file doesn't exist, we start with an empty list
            self.status_label.configure(text="No previous data found. Starting fresh.", fg="blue")
        return video_list

    def save_videos_to_csv(self):
        with open(self.csv_file, mode='w', newline='') as file:
            fieldnames = ['number', 'name', 'director', 'rating', 'play_count']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(self.video_list)

    def add_video(self):
        video_number = self.video_number_entry.get()
        video_name = self.video_name_entry.get()
        director_name = self.director_name_entry.get()
        rating = self.rating_entry.get()

        # Check for valid input
        if video_number and video_name and director_name and rating:
            try:
                rating = float(rating)
                video_info = {"number": video_number, "name": video_name, "director": director_name, "rating": rating, "play_count": 0}
                self.video_list.append(video_info)
                self.status_label.configure(text=f"Video {video_number} added successfully!", fg="green")
                self.refresh_video_list()
                self.clear_inputs()
                self.save_videos_to_csv()  # Save to CSV after adding
            except ValueError:
                self.status_label.configure(text="Invalid rating. Please enter a numeric value.", fg="red")
        else:
            self.status_label.configure(text="All fields are required.", fg="red")

    def update_video(self):
        video_number = self.video_number_entry.get()
        video_name = self.video_name_entry.get()
        director_name = self.director_name_entry.get()
        rating = self.rating_entry.get()

        # Check for valid input
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
                        self.save_videos_to_csv()  # Save to CSV after updating
                        return
                
                self.status_label.configure(text=f"Video {video_number} not found.", fg="red")
            except ValueError:
                self.status_label.configure(text="Invalid rating. Please enter a numeric value.", fg="red")
        else:
            self.status_label.configure(text="All fields are required.", fg="red")

    def play_playlist(self):
        if self.playlist:
            for video in self.playlist:
                video['play_count'] += 1
            self.status_label.configure(text="Playlist played successfully!", fg="green")
            self.refresh_video_list()
            self.save_videos_to_csv()  # Save to CSV after playing playlist
        else:
            self.status_label.configure(text="Playlist is empty.", fg="red")

    def reset_playlist(self):
        self.playlist = []
        self.status_label.configure(text="Playlist reset successfully!", fg="green")

    def refresh_video_list(self):
        self.video_list_text.delete(1.0, tk.END)
        for video in self.video_list:
            video_info = (f"Video Number: {video['number']}, Name: {video['name']}, "
                          f"Director: {video['director']}, Rating: {video['rating']}, "
                          f"Play Count: {video.get('play_count', 0)}")
            self.video_list_text.insert(tk.END, video_info + "\n")

    def clear_inputs(self):
        self.video_number_entry.delete(0, tk.END)
        self.video_name_entry.delete(0, tk.END)
        self.director_name_entry.delete(0, tk.END)
        self.rating_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = VideoManager(root)
    root.mainloop()
