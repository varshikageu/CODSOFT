import tkinter as tk
from tkinter import messagebox, ttk
from recommender import Recommender

class RecommendationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🎬 Movie Recommendation System")
        self.root.geometry("600x450")
        self.root.resizable(False, False)
        self.root.configure(bg="#f8f9fa")

        # Load recommender
        self.recommender = Recommender(data_path="data/movies.csv")

        # Heading
        heading = tk.Label(
            root,
            text="Movie Recommendation System",
            font=("Segoe UI", 18, "bold"),
            fg="#333",
            bg="#f8f9fa"
        )
        heading.pack(pady=20)

        # Entry field
        entry_frame = tk.Frame(root, bg="#f8f9fa")
        entry_frame.pack(pady=10)

        tk.Label(entry_frame, text="Enter a movie you like:", bg="#f8f9fa", font=("Segoe UI", 11)).pack(side="left", padx=5)
        self.movie_entry = ttk.Entry(entry_frame, width=40)
        self.movie_entry.pack(side="left", padx=5)

        # Recommend button
        recommend_btn = ttk.Button(root, text="Get Recommendations", command=self.get_recommendations)
        recommend_btn.pack(pady=10)

        # Results box
        self.result_box = tk.Listbox(root, width=60, height=10, font=("Segoe UI", 11))
        self.result_box.pack(pady=15)

        # Exit button
        exit_btn = ttk.Button(root, text="Exit", command=root.quit)
        exit_btn.pack(pady=10)

    def get_recommendations(self):
        movie_name = self.movie_entry.get().strip()
        if not movie_name:
            messagebox.showwarning("Input Error", "Please enter a movie name.")
            return

        self.result_box.delete(0, tk.END)
        recommendations = self.recommender.recommend(movie_name)

        if isinstance(recommendations, str):
            messagebox.showerror("Not Found", recommendations)
        else:
            self.result_box.insert(tk.END, "You might also like:")
            for rec in recommendations:
                self.result_box.insert(tk.END, f"🎬 {rec}")

# Run GUI
if __name__ == "__main__":
    root = tk.Tk()
    app = RecommendationApp(root)
    root.mainloop()
