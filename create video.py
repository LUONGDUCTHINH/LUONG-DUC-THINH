import tkinter as tk
import tkinter.scrolledtext as tkst

class CreateVideoList:
    def __init__(self, window):
        # Set window dimensions and title
        window.geometry("750x350")
        window.title("Create Video List")

        # Video Name Input
        tk.Label(window, text="Video Name:").grid(row=0, column=0, padx=10, pady=10)
        self.video_name_entry = tk.Entry(window, width=30)
        self.video_name_entry.grid(row=0, column=1, padx=10, pady=10)

        # Director Name Input
        tk.Label(window, text="Director Name:").grid(row=1, column=0, padx=10, pady=10)
        self.director_name_entry = tk.Entry(window, width=30)
        self.director_name_entry.grid(row=1, column=1, padx=10, pady=10)

        # Rating Input
        tk.Label(window, text="Rating:").grid(row=2, column=0, padx=10, pady=10)
        self.rating_entry = tk.Entry(window, width=30)
        self.rating_entry.grid(row=2, column=1, padx=10, pady=10)

        # Add Video Button
        add_video_button = tk.Button(window, text="Add Video", command=self.add_video)
        add_video_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

        # Scrolled Text Box for Video List
        self.video_list_text = tkst.ScrolledText(window, width=60, height=12, wrap="none")
        self.video_list_text.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

        # Status Label
        self.status_label = tk.Label(window, text="", font=("Helvetica", 10))
        self.status_label.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

        # List to store videos
        self.video_list = []

    def add_video(self):
        video_name = self.video_name_entry.get()
        director_name = self.director_name_entry.get()
        rating = self.rating_entry.get()

        # Ensure all fields are filled
        if video_name and director_name and rating:
            try:
                # Convert rating to a float and validate
                rating = float(rating)
                video_info = f"Video Name: {video_name}, Director: {director_name}, Rating: {rating}"
                
                # Add video to the list and update the text area
                self.video_list.append(video_info)
                self.video_list_text.insert(tk.END, video_info + "\n")
                
                # Update status and clear input fields
                self.status_label.configure(text="Video added successfully!", fg="green")
                self.clear_inputs()
            except ValueError:
                self.status_label.configure(text="Invalid rating. Please enter a number.", fg="red")
        else:
            self.status_label.configure(text="All fields are required.", fg="red")

    def clear_inputs(self):
        self.video_name_entry.delete(0, tk.END)
        self.director_name_entry.delete(0, tk.END)
        self.rating_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = CreateVideoList(root)
    root.mainloop()
