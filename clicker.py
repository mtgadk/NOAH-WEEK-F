import tkinter as tk

class ClickerGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Cookie Clicker")
        self.root.geometry("400x500")
        self.root.configure(bg="#2c3e50")

        # Game variables
        self.score = 0
        self.click_power = 1
        self.auto_clickers = 0
        self.upgrade_cost = 10
        self.auto_cost = 50

        # Score display
        self.score_label = tk.Label(
            root, text="Cookies: 0", font=("Arial", 24, "bold"), fg="#ecf0f1", bg="#2c3e50"
        )
        self.score_label.pack(pady=20)

        # Main clicker button
        self.click_button = tk.Button(
            root, text="🍪", font=("Arial", 60), command=self.click_cookie,
            bg="#f39c12", activebackground="#e67e22", bd=0, width=4, height=2
        )
        self.click_button.pack(pady=20)

        # Upgrade Click Power button
        self.upgrade_btn = tk.Button(
            root, text=f"Upgrade Click (+1) \nCost: {self.upgrade_cost} cookies",
            font=("Arial", 12), command=self.buy_upgrade, bg="#2980b9", fg="white", width=25
        )
        self.upgrade_btn.pack(pady=10)

        # Buy Auto-Clicker button
        self.auto_btn = tk.Button(
            root, text=f"Buy Auto-Clicker (+1/s) \nCost: {self.auto_cost} cookies",
            font=("Arial", 12), command=self.buy_auto, bg="#27ae60", fg="white", width=25
        )
        self.auto_btn.pack(pady=10)

        # Stats label
        self.stats_label = tk.Label(
            root, text="Click Power: 1  |  Auto-Clickers: 0",
            font=("Arial", 10), fg="#bdc3c7", bg="#2c3e50"
        )
        self.stats_label.pack(pady=20)

        # Start the background auto-clicker loop
        self.auto_click_loop()

    def update_ui(self):
        """Refreshes all text elements on the screen."""
        self.score_label.config(text=f"Cookies: {self.score}")
        self.upgrade_btn.config(text=f"Upgrade Click (+1) \nCost: {self.upgrade_cost} cookies")
        self.auto_btn.config(text=f"Buy Auto-Clicker (+1/s) \nCost: {self.auto_cost} cookies")
        self.stats_label.config(text=f"Click Power: {self.click_power}  |  Auto-Clickers: {self.auto_clickers}")

    def click_cookie(self):
        """Triggered when the big cookie is clicked."""
        self.score += self.click_power
        self.update_ui()

    def buy_upgrade(self):
        """Increases points gained per click."""
        if self.score >= self.upgrade_cost:
            self.score -= self.upgrade_cost
            self.click_power += 1
            self.upgrade_cost = int(self.upgrade_cost * 1.5)  # Scale cost
            self.update_ui()

    def buy_auto(self):
        """Adds an automated clicker that generates passive income."""
        if self.score >= self.auto_cost:
            self.score -= self.auto_cost
            self.auto_clickers += 1
            self.auto_cost = int(self.auto_cost * 1.7)  # Scale cost
            self.update_ui()

    def auto_click_loop(self):
        """Passively generates cookies every second based on auto-clickers owned."""
        if self.auto_clickers > 0:
            self.score += self.auto_clickers
            self.update_ui()
        # Run this function again after 1000ms (1 second)
        self.root.after(1000, self.auto_click_loop)

# Run the game
if __name__ == "__main__":
    window = tk.Tk()
    game = ClickerGame(window)
    window.mainloop()