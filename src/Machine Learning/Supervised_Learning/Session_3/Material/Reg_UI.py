import tkinter as tk
from tkinter import messagebox
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class LinearRegressionGD:
    """Simple Linear Regression with Gradient Descent"""
    
    def __init__(self, learning_rate=0.00001, n_iters=1000):
        self.learning_rate = learning_rate
        self.n_iters = n_iters
        self.theta_0 = 0
        self.theta_1 = 0
        self.X_train = None
        self.y_train = None
        
    def fit(self, X, y):
        """Train the model"""
        self.X_train = X
        self.y_train = y
        self.theta_0 = 0
        self.theta_1 = 0
        
        for i in range(self.n_iters):
            y_pred = self.theta_1 * X + self.theta_0
            D_theta_0 = (2/len(X)) * np.sum(y_pred - y)
            D_theta_1 = (2/len(X)) * np.sum((y_pred - y) * X)
            self.theta_0 -= self.learning_rate * D_theta_0
            self.theta_1 -= self.learning_rate * D_theta_1
    
    def predict(self, X):
        """Make predictions"""
        return self.theta_1 * X + self.theta_0


class SalaryPredApp:
    def __init__(self, root):
        self.root = root
        self.root.title("DEPI Machine Learning Program")
        self.root.geometry("900x600")
        
        # Train the model with sample data
        self.train_model()
        
        # Create the UI
        self.create_widgets()
    
    def train_model(self):
        """Train the linear regression model with sample salary data"""
        # Sample data: Years of experience vs Salary (in thousands)
        self.X_data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        self.y_data = np.array([40, 45, 50, 55, 60, 65, 70, 75, 80, 85])
        
        # Create and train model
        self.model = LinearRegressionGD(learning_rate=0.001, n_iters=1000)
        self.model.fit(self.X_data, self.y_data)
    
    def create_widgets(self):
        # Header
        header = tk.Label(self.root,
                          text="DEPI-AI Diploma",
                          background="blue",
                          foreground="white",
                          font=("Arial", 28, "bold"))
        header.pack(fill=tk.X)
        
        # Sidebar
        sidebar = tk.Frame(self.root, background="lightgrey", width=150)
        sidebar.pack(fill=tk.Y, side=tk.LEFT)
        
        project_labels = ["Linear Regression", "Project2", "Project3",
                          "Project4", "Project5", "Project6",
                          "Project7", "Project8", "Project9"]
        
        for i, label in enumerate(project_labels):
            lbl = tk.Label(sidebar, text=label, bg="lightgrey", anchor="w",
                           padx=15, font=("Arial", 16))
            lbl.pack(fill=tk.X, padx=7, pady=7)
            
            # Highlight the first project
            if i == 0:
                lbl.config(bg="darkgrey", font=("Arial", 16, "bold"))
 
        # Main section
        main_frame = tk.Frame(self.root)
        main_frame.pack(pady=20, padx=20, fill=tk.BOTH, expand=True)
        
        # Title
        title = tk.Label(main_frame, text="Salary Prediction", font=("Arial", 24, "bold"))
        title.pack(pady=10)
        
        # Model info
        info_text = f"Model: y = {self.model.theta_1:.2f}x + {self.model.theta_0:.2f}"
        info_label = tk.Label(main_frame, text=info_text, font=("Arial", 12), fg="blue")
        info_label.pack()
 
        # Input section
        input_frame = tk.Frame(main_frame)
        input_frame.pack(pady=20)
        
        label = tk.Label(input_frame, text="Enter years of experience:", font=("Arial", 18))
        label.grid(row=0, column=0, padx=10)
        
        self.experience_entry = tk.Entry(input_frame, font=("Arial", 18), width=10)
        self.experience_entry.grid(row=0, column=1, padx=10)
        self.experience_entry.bind('<Return>', lambda e: self.predict_salary())
 
        # Buttons section
        button_frame = tk.Frame(main_frame)
        button_frame.pack(pady=10)
        
        execute_button = tk.Button(button_frame, text="Execute",
                                   command=self.predict_salary,
                                   bg="green", fg="white", 
                                   font=("Arial", 16, "bold"),
                                   width=12)
        execute_button.grid(row=0, column=0, padx=5)
        
        clear_button = tk.Button(button_frame, text="Clear",
                                command=self.clear_results,
                                bg="orange", fg="white", 
                                font=("Arial", 16, "bold"),
                                width=12)
        clear_button.grid(row=0, column=1, padx=5)
        
        show_graph_button = tk.Button(button_frame, text="Show Graph",
                                      command=self.show_graph,
                                      bg="blue", fg="white", 
                                      font=("Arial", 16, "bold"),
                                      width=12)
        show_graph_button.grid(row=0, column=2, padx=5)
 
        # Result label
        self.result_label = tk.Label(main_frame, text="", font=("Arial", 20, "bold"))
        self.result_label.pack(pady=20)
        
        # Additional info
        info_frame = tk.Frame(main_frame, bg="lightyellow", relief=tk.RIDGE, bd=2)
        info_frame.pack(pady=10, fill=tk.X)
        
        info_text = "ℹ️ This model predicts salary based on years of experience\n" \
                   "Training data: 1-10 years experience with salaries $40k-$85k"
        info = tk.Label(info_frame, text=info_text, font=("Arial", 10), 
                       bg="lightyellow", justify=tk.LEFT)
        info.pack(padx=10, pady=10)
    
    def predict_salary(self):
        """Predict salary based on years of experience"""
        try:
            # Get input value
            experience = float(self.experience_entry.get())
            
            # Validate input
            if experience < 0:
                messagebox.showerror("Invalid Input", "Please enter a positive number!")
                return
            
            if experience > 50:
                response = messagebox.askyesno("Warning", 
                                              "Experience > 50 years is outside training data.\n"
                                              "Prediction may be unreliable. Continue?")
                if not response:
                    return
            
            # Make prediction
            predicted_salary = self.model.predict(experience)
            
            # Display result
            result_text = f"Predicted Salary: ${predicted_salary:.2f}k\n" \
                         f"(${predicted_salary * 1000:,.0f} per year)"
            self.result_label.config(text=result_text, fg="green")
            
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid number!")
    
    def clear_results(self):
        """Clear the input and results"""
        self.experience_entry.delete(0, tk.END)
        self.result_label.config(text="")
    
    def show_graph(self):
        """Show the regression line and data points in a new window"""
        # Create new window
        graph_window = tk.Toplevel(self.root)
        graph_window.title("Salary Prediction Visualization")
        graph_window.geometry("800x600")
        
        # Create matplotlib figure
        fig, ax = plt.subplots(figsize=(10, 6))
        
        # Plot training data
        ax.scatter(self.X_data, self.y_data, color='red', s=100, 
                  label='Training Data', zorder=3)
        
        # Plot regression line
        x_line = np.linspace(0, 12, 100)
        y_line = self.model.predict(x_line)
        ax.plot(x_line, y_line, color='blue', linewidth=2, 
               label=f'Regression Line: y = {self.model.theta_1:.2f}x + {self.model.theta_0:.2f}')
        
        # If there's a prediction, show it
        if self.experience_entry.get():
            try:
                exp = float(self.experience_entry.get())
                pred = self.model.predict(exp)
                ax.scatter([exp], [pred], color='green', s=200, 
                          marker='*', label='Your Prediction', zorder=4)
            except:
                pass
        
        ax.set_xlabel('Years of Experience', fontsize=14)
        ax.set_ylabel('Salary (thousands $)', fontsize=14)
        ax.set_title('Salary vs Experience - Linear Regression', fontsize=16, fontweight='bold')
        ax.legend(fontsize=12)
        ax.grid(True, alpha=0.3)
        
        # Embed plot in tkinter window
        canvas = FigureCanvasTkAgg(fig, master=graph_window)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        
        # Close button
        close_btn = tk.Button(graph_window, text="Close", 
                             command=graph_window.destroy,
                             bg="red", fg="white", font=("Arial", 14))
        close_btn.pack(pady=10)


if __name__ == "__main__":  
    root = tk.Tk()
    app = SalaryPredApp(root)
    root.mainloop()