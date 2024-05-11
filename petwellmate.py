import tkinter as tk
from tkinter import messagebox, ttk, filedialog
from PIL import Image, ImageTk
from datetime import datetime
import openai

class PetWellMateApp:
    def __init__(self, master):
        self.master = master
        master.title("PetWellMate")
        master.geometry("800x600")
        master.configure(bg="#f0f0f0")
        
        # Title
        self.title_label = tk.Label(master, text="Welcome to PetWellMate", font=("Helvetica", 24, "bold"), bg="#ffffff")
        self.title_label.pack(pady=20)

        # Frame for buttons
        self.button_frame = tk.Frame(master, bg="#f0f0f0")
        self.button_frame.pack(pady=20)

        # Button style
        button_style = {"font": ("Helvetica", 14), "bg": "#4CAF50", "fg": "black", "bd": 0, "highlightthickness": 0, "activebackground": "#45a049", "relief": "flat"}

        # Health Monitoring Dashboard
        self.dashboard_button = tk.Button(self.button_frame, text="Health Monitoring Dashboard", command=self.open_dashboard, **button_style)
        self.dashboard_button.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

        # Symptom Checker and Health Recommendations
        self.symptom_checker_button = tk.Button(self.button_frame, text="Symptom Checker and Health Recommendations", command=self.open_symptom_checker, **button_style)
        self.symptom_checker_button.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

        # Nutritional Guidance and Diet Planning
        self.nutritional_guidance_button = tk.Button(self.button_frame, text="Nutritional Guidance and Diet Planning", command=self.open_nutritional_guidance, **button_style)
        self.nutritional_guidance_button.grid(row=2, column=0, padx=10, pady=10, sticky="ew")

        # Fitness and Exercise Planner
        self.fitness_planner_button = tk.Button(self.button_frame, text="Fitness and Exercise Planner", command=self.open_fitness_planner, **button_style)
        self.fitness_planner_button.grid(row=3, column=0, padx=10, pady=10, sticky="ew")

        # Digital Pet Profiles
        self.pet_profiles_button = tk.Button(self.button_frame, text="Digital Pet Profiles", command=self.open_pet_profiles, **button_style)
        self.pet_profiles_button.grid(row=4, column=0, padx=10, pady=10, sticky="ew")

        # Reminder Notifications
        self.reminder_notifications_button = tk.Button(self.button_frame, text="Reminder Notifications", command=self.open_reminder_notifications, **button_style)
        self.reminder_notifications_button.grid(row=5, column=0, padx=10, pady=10, sticky="ew")

        # Disease Awareness and Education Hub
        self.disease_awareness_button = tk.Button(self.button_frame, text="Disease Awareness and Education Hub", command=self.open_disease_awareness, **button_style)
        self.disease_awareness_button.grid(row=6, column=0, padx=10, pady=10, sticky="ew")
        
        # Chatbot
        self.chatbot_button = tk.Button(self.button_frame, text="Chatbot", command=self.open_chatbot, **button_style)
        self.chatbot_button.grid(row=7, column=0, padx=10, pady=10, sticky="ew")
        
        # Quit Button
        self.quit_button = tk.Button(master, text="Quit", command=self.quit_app, font=("Helvetica", 14), bg="#f44336", fg="white", bd=0, activebackground="#d32f2f", relief="flat")
        self.quit_button.pack(pady=20)

        # Load health records
        self.health_records = self.load_health_records()

        # Symptom Checker Data
        self.symptom_data = {
            "cat": {
                "Symptoms": ["Coughing", "Sneezing", "Vomiting", "Diarrhea", "Lethargy"],
                "Recommendations": "If your cat is showing these symptoms, it is recommended to consult a veterinarian for proper diagnosis and treatment."
            },
            "dog": {
                "Symptoms": ["Coughing", "Sneezing", "Vomiting", "Diarrhea", "Lethargy"],
                "Recommendations": "If your dog is showing these symptoms, it is recommended to consult a veterinarian for proper diagnosis and treatment."
            },
            "bird": {
                "Symptoms": ["Fluffed feathers", "Loss of appetite", "Decreased activity", "Sitting at bottom of cage"],
                "Recommendations": "If your bird is showing these symptoms, it is recommended to consult an avian veterinarian for proper diagnosis and treatment."
            }
        }
         # OpenAI API configuration
        openai.api_key = "sk-proj-REDMIqzss7l88kCO0QKWT3BlbkFJy2jUO9dOVkqypbc6712s"

    def open_chatbot(self):
        # Functionality for Chatbot
        chatbot_window = tk.Toplevel(self.master)
        chatbot_window.title("Chatbot")
        chatbot_window.geometry("600x400")
        chatbot_window.configure(bg="#f0f0f0")

        # Chat Display Section
        self.chat_display = tk.Text(chatbot_window, bg="white", fg="black", font=("Helvetica", 12), wrap=tk.WORD)
        self.chat_display.pack(expand=True, fill="both", padx=10, pady=10)

        # Chat Input Section
        self.chat_input = tk.Entry(chatbot_window, bg="white", fg="black", font=("Helvetica", 12))
        self.chat_input.pack(fill="x", padx=10, pady=10)

        # Send Button
        send_button = tk.Button(chatbot_window, text="Send", command=self.send_message, bg="#4CAF50", fg="white", font=("Helvetica", 12), relief="flat")
        send_button.pack(pady=10)

    def send_message(self):
        # Function to send user message to ChatGPT and get response
        user_message = self.chat_input.get().strip()
        if user_message:
            self.chat_display.configure(state="normal")
            self.chat_display.insert(tk.END, "You: " + user_message + "\n")
            self.chat_input.delete(0, tk.END)
            self.chat_display.see(tk.END)

            # Get response from ChatGPT
            try:
                response = openai.Completion.create(
                    engine="gpt-3.5-turbo-instruct",
                    prompt=user_message + "\n",
                    max_tokens=50
                )
                print("Response from API:", response)
                bot_message = response.choices[0].text.strip()
                print("Bot's response:", bot_message)
                self.chat_display.insert(tk.END, "Bot: " + bot_message + "\n")
            except Exception as e:
                print("Error:", e)
                self.chat_display.insert(tk.END, "Bot: I'm sorry, I couldn't understand that.\n")
            finally:
                self.chat_display.configure(state="disabled")
                self.chat_display.see(tk.END)

    def open_dashboard(self):
        # Functionality for Health Monitoring Dashboard
        dashboard_window = tk.Toplevel(self.master)
        dashboard_window.title("Health Monitoring Dashboard")
        dashboard_window.geometry("600x400")

        # Pet Information Section
        pet_info_frame = tk.Frame(dashboard_window, bg="#f0f0f0")
        pet_info_frame.pack(pady=20)

        pet_name_label = tk.Label(pet_info_frame, text="Pet's Name:", bg="#f0f0f0", fg="#333333")
        pet_name_label.grid(row=0, column=0, padx=10, pady=5)
        self.pet_name_entry = tk.Entry(pet_info_frame)
        self.pet_name_entry.grid(row=0, column=1, padx=10, pady=5)

        pet_breed_label = tk.Label(pet_info_frame, text="Breed:", bg="#f0f0f0", fg="#333333")
        pet_breed_label.grid(row=1, column=0, padx=10, pady=5)
        self.pet_breed_entry = tk.Entry(pet_info_frame)
        self.pet_breed_entry.grid(row=1, column=1, padx=10, pady=5)

        pet_age_label = tk.Label(pet_info_frame, text="Age:", bg="#f0f0f0", fg="#333333")
        pet_age_label.grid(row=2, column=0, padx=10, pady=5)
        self.pet_age_entry = tk.Entry(pet_info_frame)
        self.pet_age_entry.grid(row=2, column=1, padx=10, pady=5)

        pet_weight_label = tk.Label(pet_info_frame, text="Weight (kg):", bg="#f0f0f0", fg="#333333")
        pet_weight_label.grid(row=3, column=0, padx=10, pady=5)
        self.pet_weight_entry = tk.Entry(pet_info_frame)
        self.pet_weight_entry.grid(row=3, column=1, padx=10, pady=5)

        # Health History Section
        health_history_frame = tk.Frame(dashboard_window, bg="#f0f0f0")
        health_history_frame.pack(pady=20)

        # Health History Treeview
        self.health_tree = ttk.Treeview(health_history_frame, columns=("Date", "Category", "Details"), show="headings")
        self.health_tree.heading("Date", text="Date")
        self.health_tree.heading("Category", text="Category")
        self.health_tree.heading("Details", text="Details")
        self.health_tree.pack()

        # Load health records
        for record in self.health_records:
            self.health_tree.insert("", "end", values=record)

        # Add Health Record Section
        add_record_frame = tk.Frame(dashboard_window, bg="#f0f0f0")
        add_record_frame.pack(pady=20)

        add_record_label = tk.Label(add_record_frame, text="Add Health Record:", font=("Helvetica", 14, "bold"), bg="#f0f0f0", fg="#333333")
        add_record_label.grid(row=0, column=0, padx=10, pady=5, columnspan=2)

        record_date_label = tk.Label(add_record_frame, text="Date:", bg="#f0f0f0", fg="#333333")
        record_date_label.grid(row=1, column=0, padx=10, pady=5)
        self.record_date_entry = tk.Entry(add_record_frame)
        self.record_date_entry.grid(row=1, column=1, padx=10, pady=5)
        self.record_date_entry.insert(0, datetime.today().strftime('%Y-%m-%d'))

        record_category_label = tk.Label(add_record_frame, text="Category:", bg="#f0f0f0", fg="#333333")
        record_category_label.grid(row=2, column=0, padx=10, pady=5)
        self.record_category_entry = ttk.Combobox(add_record_frame, values=["Vaccination", "Medication", "Vet Visit"])
        self.record_category_entry.grid(row=2, column=1, padx=10, pady=5)

        record_details_label = tk.Label(add_record_frame, text="Details:", bg="#f0f0f0", fg="#333333")
        record_details_label.grid(row=3, column=0, padx=10, pady=5)
        self.record_details_entry = tk.Entry(add_record_frame)
        self.record_details_entry.grid(row=3, column=1, padx=10, pady=5)

        add_button = tk.Button(add_record_frame, text="Add Record", command=self.add_health_record, bg="#4CAF50", fg="white", font=("Helvetica", 12), relief="flat")
        add_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10, sticky="ew")

    def add_health_record(self):
        record_date = self.record_date_entry.get()
        record_category = self.record_category_entry.get()
        record_details = self.record_details_entry.get()

        if record_date and record_category and record_details:
            self.health_records.append((record_date, record_category, record_details))
            self.health_tree.insert("", "end", values=(record_date, record_category, record_details))
            self.record_date_entry.delete(0, 'end')
            self.record_details_entry.delete(0, 'end')
            self.save_health_records()
            messagebox.showinfo("Record Added", "Health record added successfully.")
        else:
            messagebox.showerror("Error", "Please fill all the fields.")

    def save_health_records(self):
        with open("health_records.txt", "w") as file:
            for record in self.health_records:
                file.write(",".join(record) + "\n")

    def load_health_records(self):
        try:
            with open("health_records.txt", "r") as file:
                records = [line.strip().split(",") for line in file.readlines()]
            return records
        except FileNotFoundError:
            return []

    def open_symptom_checker(self):
        # Functionality for Symptom Checker and Health Recommendations
        symptom_checker_window = tk.Toplevel(self.master)
        symptom_checker_window.title("Symptom Checker and Health Recommendations")
        symptom_checker_window.geometry("600x400")
        symptom_checker_window.configure(bg="#f0f0f0")

        # Symptom Input Section
        symptom_input_frame = tk.Frame(symptom_checker_window, bg="#f0f0f0")
        symptom_input_frame.pack(pady=20)

        symptom_label = tk.Label(symptom_input_frame, text="Enter Symptoms:", bg="#f0f0f0", fg="#333333", font=("Helvetica", 14))
        symptom_label.grid(row=0, column=0, padx=10, pady=5)
        self.symptom_entry = tk.Entry(symptom_input_frame, width=50)
        self.symptom_entry.grid(row=0, column=1, padx=10, pady=5)

        pet_type_label = tk.Label(symptom_input_frame, text="Select Pet Type:", bg="#f0f0f0", fg="#333333", font=("Helvetica", 14))
        pet_type_label.grid(row=1, column=0, padx=10, pady=5)
        self.pet_type_var = tk.StringVar()
        self.pet_type_var.set("cat")
        self.pet_type_dropdown = ttk.Combobox(symptom_input_frame, textvariable=self.pet_type_var, values=["cat", "dog", "bird"], font=("Helvetica", 12))
        self.pet_type_dropdown.grid(row=1, column=1, padx=10, pady=5)

        # Submit Button
        submit_button = tk.Button(symptom_input_frame, text="Submit", command=self.check_symptoms, bg="#4CAF50", fg="white", font=("Helvetica", 12), relief="flat")
        submit_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

    def check_symptoms(self):
        # Function to check symptoms and provide health recommendations
        symptoms = self.symptom_entry.get()
        pet_type = self.pet_type_var.get()

        if symptoms:
            if pet_type in self.symptom_data:
                recommendations = self.symptom_data[pet_type]["Recommendations"]
                messagebox.showinfo("Health Recommendations", recommendations)
            else:
                messagebox.showerror("Error", "Invalid pet type.")
            self.symptom_entry.delete(0, 'end')
        else:
            messagebox.showerror("Error", "Please enter your pet's symptoms.")

    def open_nutritional_guidance(self):
        # Functionality for Nutritional Guidance and Diet Planning
        nutritional_window = tk.Toplevel(self.master)
        nutritional_window.title("Nutritional Guidance and Diet Planning")
        nutritional_window.geometry("600x400")
        nutritional_window.configure(bg="#f0f0f0")

        # Pet Details Section
        pet_details_frame = tk.Frame(nutritional_window, bg="#f0f0f0")
        pet_details_frame.pack(pady=20)

        pet_age_label = tk.Label(pet_details_frame, text="Pet's Age (in years):", bg="#f0f0f0", fg="#333333", font=("Helvetica", 14))
        pet_age_label.grid(row=0, column=0, padx=10, pady=5)
        self.pet_age_var = tk.StringVar()
        self.pet_age_entry = tk.Entry(pet_details_frame, textvariable=self.pet_age_var, font=("Helvetica", 12))
        self.pet_age_entry.grid(row=0, column=1, padx=10, pady=5)

        pet_weight_label = tk.Label(pet_details_frame, text="Pet's Weight (in kg):", bg="#f0f0f0", fg="#333333", font=("Helvetica", 14))
        pet_weight_label.grid(row=1, column=0, padx=10, pady=5)
        self.pet_weight_var = tk.StringVar()
        self.pet_weight_entry = tk.Entry(pet_details_frame, textvariable=self.pet_weight_var, font=("Helvetica", 12))
        self.pet_weight_entry.grid(row=1, column=1, padx=10, pady=5)

        pet_activity_label = tk.Label(pet_details_frame, text="Pet's Activity Level:", bg="#f0f0f0", fg="#333333", font=("Helvetica", 14))
        pet_activity_label.grid(row=2, column=0, padx=10, pady=5)
        self.pet_activity_var = tk.StringVar()
        self.pet_activity_dropdown = ttk.Combobox(pet_details_frame, textvariable=self.pet_activity_var, values=["Low", "Moderate", "High"], font=("Helvetica", 12))
        self.pet_activity_dropdown.grid(row=2, column=1, padx=10, pady=5)

        # Calculate Button
        calculate_button = tk.Button(pet_details_frame, text="Calculate", command=self.calculate_diet, bg="#4CAF50", fg="white", font=("Helvetica", 12), relief="flat")
        calculate_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

    def calculate_diet(self):
        # Function to calculate daily caloric intake
        try:
            age = float(self.pet_age_var.get())
            weight = float(self.pet_weight_var.get())
            activity = self.pet_activity_var.get()

            if activity == "Low":
                factor = 95
            elif activity == "Moderate":
                factor = 132
            elif activity == "High":
                factor = 175

            daily_caloric_intake = (factor * weight) - (age * 2.5) + 100
            messagebox.showinfo("Daily Caloric Intake", f"Your pet requires {daily_caloric_intake:.2f} kcal per day.")
        except ValueError:
            messagebox.showerror("Error", "Please enter valid pet details.")

    def open_fitness_planner(self):
        # Functionality for Fitness and Exercise Planner
        fitness_window = tk.Toplevel(self.master)
        fitness_window.title("Fitness and Exercise Planner")
        fitness_window.geometry("600x400")
        fitness_window.configure(bg="#f0f0f0")

        # Exercise Entry Section
        exercise_entry_frame = tk.Frame(fitness_window, bg="#f0f0f0")
        exercise_entry_frame.pack(pady=20)

        exercise_label = tk.Label(exercise_entry_frame, text="Enter Exercise:", bg="#f0f0f0", fg="#333333", font=("Helvetica", 14))
        exercise_label.grid(row=0, column=0, padx=10, pady=5)

        self.exercise_var = tk.StringVar()
        self.exercise_entry = tk.Entry(exercise_entry_frame, textvariable=self.exercise_var, font=("Helvetica", 12))
        self.exercise_entry.grid(row=0, column=1, padx=10, pady=5)

        pet_type_label = tk.Label(exercise_entry_frame, text="Select Pet Type:", bg="#f0f0f0", fg="#333333", font=("Helvetica", 14))
        pet_type_label.grid(row=1, column=0, padx=10, pady=5)

        self.pet_type_var_exercise = tk.StringVar()
        self.pet_type_var_exercise.set("cat")
        self.pet_type_dropdown_exercise = ttk.Combobox(exercise_entry_frame, textvariable=self.pet_type_var_exercise, values=["cat", "dog", "bird"], font=("Helvetica", 12))
        self.pet_type_dropdown_exercise.grid(row=1, column=1, padx=10, pady=5)

        # Duration Entry
        duration_label = tk.Label(exercise_entry_frame, text="Duration (minutes):", bg="#f0f0f0", fg="#333333", font=("Helvetica", 14))
        duration_label.grid(row=2, column=0, padx=10, pady=5)

        self.duration_var = tk.StringVar()
        self.duration_entry = tk.Entry(exercise_entry_frame, textvariable=self.duration_var, font=("Helvetica", 12))
        self.duration_entry.grid(row=2, column=1, padx=10, pady=5)

        # Intensity Entry
        intensity_label = tk.Label(exercise_entry_frame, text="Intensity:", bg="#f0f0f0", fg="#333333", font=("Helvetica", 14))
        intensity_label.grid(row=3, column=0, padx=10, pady=5)

        self.intensity_var = tk.StringVar()
        self.intensity_var.set("Low")
        self.intensity_dropdown = ttk.Combobox(exercise_entry_frame, textvariable=self.intensity_var, values=["Low", "Moderate", "High"], font=("Helvetica", 12))
        self.intensity_dropdown.grid(row=3, column=1, padx=10, pady=5)

        # Weather Entry
        weather_label = tk.Label(exercise_entry_frame, text="Weather:", bg="#f0f0f0", fg="#333333", font=("Helvetica", 14))
        weather_label.grid(row=4, column=0, padx=10, pady=5)

        self.weather_var = tk.StringVar()
        self.weather_var.set("Sunny")
        self.weather_dropdown = ttk.Combobox(exercise_entry_frame, textvariable=self.weather_var, values=["Sunny", "Cloudy", "Rainy", "Snowy"], font=("Helvetica", 12))
        self.weather_dropdown.grid(row=4, column=1, padx=10, pady=5)

        # Terrain Entry
        terrain_label = tk.Label(exercise_entry_frame, text="Terrain:", bg="#f0f0f0", fg="#333333", font=("Helvetica", 14))
        terrain_label.grid(row=5, column=0, padx=10, pady=5)

        self.terrain_var = tk.StringVar()
        self.terrain_var.set("Flat")
        self.terrain_dropdown = ttk.Combobox(exercise_entry_frame, textvariable=self.terrain_var, values=["Flat", "Hilly", "Mountainous"], font=("Helvetica", 12))
        self.terrain_dropdown.grid(row=5, column=1, padx=10, pady=5)

        # Submit Button
        submit_button = tk.Button(exercise_entry_frame, text="Add Exercise", command=self.save_exercise, bg="#4CAF50", fg="white", font=("Helvetica", 12), relief="flat")
        submit_button.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

        # Exercise History Section
        exercise_history_frame = tk.Frame(fitness_window, bg="#f0f0f0")
        exercise_history_frame.pack(pady=20)

        exercise_history_label = tk.Label(exercise_history_frame, text="Exercise History:", bg="#f0f0f0", fg="#333333", font=("Helvetica", 14))
        exercise_history_label.grid(row=0, column=0, padx=10, pady=5)

        self.exercise_tree = ttk.Treeview(exercise_history_frame, columns=("Exercise", "Duration", "Intensity", "Weather", "Terrain"), show="headings")
        self.exercise_tree.heading("Exercise", text="Exercise")
        self.exercise_tree.heading("Duration", text="Duration")
        self.exercise_tree.heading("Intensity", text="Intensity")
        self.exercise_tree.heading("Weather", text="Weather")
        self.exercise_tree.heading("Terrain", text="Terrain")
        self.exercise_tree.pack()

        # Load exercise history
        self.load_exercise_history(fitness_window)

    def save_exercise(self):
        # Function to save exercise data
        exercise = self.exercise_var.get()
        pet_type = self.pet_type_var_exercise.get()
        duration = self.duration_var.get()
        intensity = self.intensity_var.get()
        weather = self.weather_var.get()
        terrain = self.terrain_var.get()

        if exercise and pet_type and duration and intensity and weather and terrain:
            with open(f"{pet_type}_fitness.txt", "a") as file:
               file.write(f"{exercise},{duration},{intensity},{weather},{terrain}\n")
            self.exercise_entry.delete(0, 'end')
            self.duration_entry.delete(0, 'end')
            self.exercise_tree.insert("", "end", values=(exercise, duration, intensity, weather, terrain))
            messagebox.showinfo("Exercise Added", "Exercise added successfully.")
        else:
              messagebox.showerror("Error", "Please fill all the fields.")

    def load_exercise_history(self, fitness_window):
        # Function to load exercise history
        pet_type = self.pet_type_var_exercise.get()
        try:
            with open(f"{pet_type}_fitness.txt", "r") as file:
                exercises = [line.strip().split(",") for line in file.readlines()]
            for exercise in exercises:
                self.exercise_tree.insert("", "end", values=exercise)
        except FileNotFoundError:
            pass


    def open_pet_profiles(self):
        # Functionality for Digital Pet Profiles
        pet_profiles_window = tk.Toplevel(self.master)
        pet_profiles_window.title("Digital Pet Profiles")
        pet_profiles_window.geometry("600x400")
        pet_profiles_window.configure(bg="#f0f0f0")

        # Upload Image Section
        upload_frame = tk.Frame(pet_profiles_window, bg="#f0f0f0")
        upload_frame.pack(pady=20)

        upload_label = tk.Label(upload_frame, text="Upload Image:", bg="#f0f0f0", fg="#333333", font=("Helvetica", 14))
        upload_label.grid(row=0, column=0, padx=10, pady=5)
        self.upload_button = tk.Button(upload_frame, text="Browse", command=self.upload_image, bg="#4CAF50", fg="white", font=("Helvetica", 12), relief="flat")
        self.upload_button.grid(row=0, column=1, padx=10, pady=5)

        # Pet Information Section
        pet_info_frame = tk.Frame(pet_profiles_window, bg="#f0f0f0")
        pet_info_frame.pack(pady=20)

        pet_name_label = tk.Label(pet_info_frame, text="Pet's Name:", bg="#f0f0f0", fg="#333333", font=("Helvetica", 14))
        pet_name_label.grid(row=0, column=0, padx=10, pady=5)
        self.pet_name_var = tk.StringVar()
        self.pet_name_entry = tk.Entry(pet_info_frame, textvariable=self.pet_name_var, font=("Helvetica", 12))
        self.pet_name_entry.grid(row=0, column=1, padx=10, pady=5)

        pet_breed_label = tk.Label(pet_info_frame, text="Breed:", bg="#f0f0f0", fg="#333333", font=("Helvetica", 14))
        pet_breed_label.grid(row=1, column=0, padx=10, pady=5)
        self.pet_breed_var = tk.StringVar()
        self.pet_breed_entry = tk.Entry(pet_info_frame, textvariable=self.pet_breed_var, font=("Helvetica", 12))
        self.pet_breed_entry.grid(row=1, column=1, padx=10, pady=5)

        pet_age_label = tk.Label(pet_info_frame, text="Age:", bg="#f0f0f0", fg="#333333", font=("Helvetica", 14))
        pet_age_label.grid(row=2, column=0, padx=10, pady=5)
        self.pet_age_var = tk.StringVar()
        self.pet_age_entry = tk.Entry(pet_info_frame, textvariable=self.pet_age_var, font=("Helvetica", 12))
        self.pet_age_entry.grid(row=2, column=1, padx=10, pady=5)

        pet_weight_label = tk.Label(pet_info_frame, text="Weight (kg):", bg="#f0f0f0", fg="#333333", font=("Helvetica", 14))
        pet_weight_label.grid(row=3, column=0, padx=10, pady=5)
        self.pet_weight_var = tk.StringVar()
        self.pet_weight_entry = tk.Entry(pet_info_frame, textvariable=self.pet_weight_var, font=("Helvetica", 12))
        self.pet_weight_entry.grid(row=3, column=1, padx=10, pady=5)

        # Save Button
        save_button = tk.Button(pet_info_frame, text="Save", command=self.save_pet_data, bg="#4CAF50", fg="white", font=("Helvetica", 12), relief="flat")
        save_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

    def upload_image(self):
        # Function to upload pet image
        file_path = filedialog.askopenfilename(title="Select Image", filetypes=(("Image Files", "*.png;*.jpg;*.jpeg"), ("All files", "*.*")))
        if file_path:
            self.image = Image.open(file_path)
            self.image = self.image.resize((150, 150))
            self.photo = ImageTk.PhotoImage(self.image)
            self.upload_button.config(text="Change Image")
            self.pet_image_label = tk.Label(self.master, image=self.photo)
            self.pet_image_label.image = self.photo
            self.pet_image_label.place(x=350, y=50)

    def save_pet_data(self):
        # Function to save pet data
        pet_name = self.pet_name_var.get()
        pet_breed = self.pet_breed_var.get()
        pet_age = self.pet_age_var.get()
        pet_weight = self.pet_weight_var.get()

        if pet_name and pet_breed and pet_age and pet_weight:
            with open("pet_data.txt", "w") as file:
                file.write(f"Name: {pet_name}\n")
                file.write(f"Breed: {pet_breed}\n")
                file.write(f"Age: {pet_age}\n")
                file.write(f"Weight: {pet_weight} kg\n")
            messagebox.showinfo("Pet Data Saved", "Pet data saved successfully.")
        else:
            messagebox.showerror("Error", "Please fill all the fields.")

    def open_reminder_notifications(self):
        # Functionality for Reminder Notifications
        reminder_window = tk.Toplevel(self.master)
        reminder_window.title("Reminder Notifications")
        reminder_window.geometry("800x600")
        reminder_window.configure(bg="#f0f0f0")

        # Header Frame
        header_frame = tk.Frame(reminder_window, bg="#4CAF50")
        header_frame.pack(fill="x")

        header_label = tk.Label(header_frame, text="Reminder Notifications", font=("Helvetica", 24, "bold"), bg="#4CAF50", fg="white")
        header_label.pack(pady=10)

        # Content Frame
        content_frame = tk.Frame(reminder_window, bg="#f0f0f0")
        content_frame.pack(pady=20)

        # Function to add custom reminder
        def add_custom_reminder():
            custom_window = tk.Toplevel(reminder_window)
            custom_window.title("Add Custom Reminder")
            custom_window.geometry("400x300")
            custom_window.configure(bg="#f0f0f0")

            # Function to save custom reminder
            def save_custom_reminder():
                title = title_entry.get()
                desc = desc_entry.get("1.0", tk.END)
                if title.strip() and desc.strip():
                    new_reminder_frame = tk.Frame(content_frame, bg="#ffffff", bd=1, relief="groove")
                    new_reminder_frame.grid(row=len(content_frame.winfo_children()), column=0, padx=10, pady=10, sticky="ew")

                    new_reminder_title = tk.Label(new_reminder_frame, text=title, font=("Helvetica", 18, "bold"), bg="#ffffff")
                    new_reminder_title.pack()

                    new_reminder_desc = tk.Label(new_reminder_frame, text=desc, font=("Helvetica", 14), bg="#ffffff")
                    new_reminder_desc.pack()

                    custom_window.destroy()

                else:
                    messagebox.showerror("Error", "Title and Description cannot be empty!")

            # Title Entry
            title_label = tk.Label(custom_window, text="Title:", font=("Helvetica", 12), bg="#f0f0f0")
            title_label.pack(pady=10)

            title_entry = tk.Entry(custom_window, font=("Helvetica", 12))
            title_entry.pack(pady=5)

            # Description Entry
            desc_label = tk.Label(custom_window, text="Description:", font=("Helvetica", 12), bg="#f0f0f0")
            desc_label.pack(pady=10)

            desc_entry = tk.Text(custom_window, font=("Helvetica", 12), height=5, width=30)
            desc_entry.pack(pady=5)

            # Save Button
            save_button = tk.Button(custom_window, text="Save", command=save_custom_reminder, font=("Helvetica", 14), bg="#4CAF50", fg="white", bd=0, activebackground="#45a049", relief="flat")
            save_button.pack(pady=10)

        # Add Custom Reminder Button
        custom_button = tk.Button(content_frame, text="Add Custom Reminder", command=add_custom_reminder, font=("Helvetica", 16), bg="#4CAF50", fg="white", bd=0, activebackground="#45a049", relief="flat")
        custom_button.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

        # Reminder 1
        reminder1_frame = tk.Frame(content_frame, bg="#ffffff", bd=1, relief="groove")
        reminder1_frame.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

        reminder1_title = tk.Label(reminder1_frame, text="Feeding Time", font=("Helvetica", 18, "bold"), bg="#ffffff")
        reminder1_title.pack()

        reminder1_desc = tk.Label(reminder1_frame, text="Don't forget to feed your pet at 8:00 AM and 6:00 PM", font=("Helvetica", 14), bg="#ffffff")
        reminder1_desc.pack()

        # Reminder 2
        reminder2_frame = tk.Frame(content_frame, bg="#ffffff", bd=1, relief="groove")
        reminder2_frame.grid(row=2, column=0, padx=10, pady=10, sticky="ew")

        reminder2_title = tk.Label(reminder2_frame, text="Walk Time", font=("Helvetica", 18, "bold"), bg="#ffffff")
        reminder2_title.pack()

        reminder2_desc = tk.Label(reminder2_frame, text="Take your dog for a walk at 7:00 AM and 7:00 PM", font=("Helvetica", 14), bg="#ffffff")
        reminder2_desc.pack()

        # Reminder 3
        reminder3_frame = tk.Frame(content_frame, bg="#ffffff", bd=1, relief="groove")
        reminder3_frame.grid(row=3, column=0, padx=10, pady=10, sticky="ew")

        reminder3_title = tk.Label(reminder3_frame, text="Medication Time", font=("Helvetica", 18, "bold"), bg="#ffffff")
        reminder3_title.pack()

        reminder3_desc = tk.Label(reminder3_frame, text="Give medication to your pet at 9:00 AM and 9:00 PM", font=("Helvetica", 14), bg="#ffffff")
        reminder3_desc.pack()

   

        # Close button
        close_button = tk.Button(reminder_window, text="Close", command=reminder_window.destroy, font=("Helvetica", 16), bg="#f44336", fg="white", bd=0, activebackground="#d32f2f", relief="flat")
        close_button.pack(pady=20)


    def open_disease_awareness(self):
        # Functionality for Disease Awareness and Education Hub
        disease_window = tk.Toplevel(self.master)
        disease_window.title("Disease Awareness and Education Hub")
        disease_window.geometry("600x400")
        disease_window.configure(bg="#f0f0f0")

        # Disease Information
        disease_info_frame = tk.Frame(disease_window, bg="#f0f0f0")
        disease_info_frame.pack(pady=20)

        disease_label = tk.Label(disease_info_frame, text="Select Disease:", bg="#f0f0f0", fg="#333333", font=("Helvetica", 14))
        disease_label.grid(row=0, column=0, padx=10, pady=5)
        self.disease_var = tk.StringVar()
        self.disease_dropdown = ttk.Combobox(disease_info_frame, textvariable=self.disease_var, values=["Heartworm", "Rabies", "Kennel Cough"], font=("Helvetica", 12))
        self.disease_dropdown.grid(row=0, column=1, padx=10, pady=5)

        # Disease Information Text
        disease_text_frame = tk.Frame(disease_window, bg="#f0f0f0")
        disease_text_frame.pack(pady=20)

        disease_text_label = tk.Label(disease_text_frame, text="Disease Information:", bg="#f0f0f0", fg="#333333", font=("Helvetica", 14))
        disease_text_label.grid(row=0, column=0, padx=10, pady=5)
        self.disease_text = tk.Text(disease_text_frame, width=60, height=10)
        self.disease_text.grid(row=1, column=0, padx=10, pady=5)

        # Submit Button
        submit_button = tk.Button(disease_text_frame, text="Show Info", command=self.show_disease_info, bg="#4CAF50", fg="white", font=("Helvetica", 12), relief="flat")
        submit_button.grid(row=2, column=0, padx=10, pady=10)

    def show_disease_info(self):
        # Function to display disease information
        disease = self.disease_var.get()
        if disease:
            if disease == "Heartworm":
                disease_info = "Heartworm is a serious and potentially fatal disease in pets, particularly in dogs. It is caused by foot-long worms (heartworms) that live in the heart, lungs, and associated blood vessels of affected pets, causing severe lung disease, heart failure, and damage to other organs in the body."
            elif disease == "Rabies":
                disease_info = "Rabies is a viral disease that causes inflammation of the brain in humans and other mammals. It is transmitted through the saliva of an infected animal, usually through a bite. Once symptoms of the disease develop, rabies is fatal."
            elif disease == "Kennel Cough":
                disease_info = "Kennel cough, also known as infectious tracheobronchitis, is a highly contagious respiratory disease in dogs. It is caused by a combination of bacteria and viruses, including canine parainfluenza virus and Bordetella bronchiseptica."
            self.disease_text.delete(1.0, tk.END)
            self.disease_text.insert(tk.END, disease_info)
        else:
            messagebox.showerror("Error", "Please select a disease.")

    def quit_app(self):
        self.master.destroy()

def main():
    root = tk.Tk()
    app = PetWellMateApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
