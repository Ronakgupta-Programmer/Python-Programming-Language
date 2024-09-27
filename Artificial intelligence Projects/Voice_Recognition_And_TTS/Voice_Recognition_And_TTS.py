import tkinter as tk
import speech_recognition as sr
import pyttsx3

# Initialize recognizer class (for recognizing the speech)
recognizer = sr.Recognizer()

# Initialize text-to-speech engine
tts_engine = pyttsx3.init()

# Get available voices from pyttsx3
voices = tts_engine.getProperty('voices')

# Function to set the selected voice
def set_voice(voice_index):
    selected_voice = voices[voice_index].id
    tts_engine.setProperty('voice', selected_voice)

# Function to convert speech to text
def speech_to_text():
    try:
        with sr.Microphone() as source:
            result_label.config(text="Adjusting for ambient noise... Please wait.")
            recognizer.adjust_for_ambient_noise(source)
            result_label.config(text="Listening...")

            # Listen for the user's input
            audio = recognizer.listen(source)

            # Use Google's speech recognition to convert audio to text
            result_label.config(text="Recognizing...")
            text = recognizer.recognize_google(audio)
            result_label.config(text=f"You said: {text}")
            return text

    except sr.UnknownValueError:
        result_label.config(text="Sorry, I did not understand that.")
        return None
    except sr.RequestError:
        result_label.config(text="Sorry, I could not request results from the speech recognition service.")
        return None

# Function to convert text to speech
def text_to_speech(text):
    tts_engine.say(text)
    tts_engine.runAndWait()

# Function to handle text-to-speech button
def handle_text_to_speech():
    user_input = input_text.get("1.0", tk.END).strip()
    if user_input:
        result_label.config(text=f"Speaking: {user_input}")
        text_to_speech(user_input)
    else:
        result_label.config(text="Please enter some text to speak.")

# Set up the GUI
def create_gui():
    # Create a main window
    root = tk.Tk()
    root.title("Speech to Text & Text to Speech")
    root.geometry("800x600")  # Increased size for larger window
    root.config(bg="#f0f0f0")

    # Create a label to show instructions
    instructions_label = tk.Label(root, text="Choose an action below:", font=("Arial", 18), bg="#f0f0f0")
    instructions_label.pack(pady=20)

    # Add a dropdown menu for selecting voice
    voice_label = tk.Label(root, text="Select Voice:", font=("Arial", 14), bg="#f0f0f0")
    voice_label.pack(pady=5)
    
    voice_var = tk.StringVar(root)
    voice_dropdown = tk.OptionMenu(root, voice_var, *[voice.name for voice in voices], command=lambda val: set_voice(voices.index(next(voice for voice in voices if voice.name == val))))
    voice_var.set(voices[0].name)  # Set default voice
    voice_dropdown.pack(pady=10)

    # Create a button to start speech-to-text
    stt_button = tk.Button(root, text="Speech to Text", command=speech_to_text, bg="#4CAF50", fg="white", font=("Arial", 16, "bold"), padx=10, pady=10, activebackground="#45a049")
    stt_button.pack(pady=10)

    # Create a text box to input text for text-to-speech
    global input_text
    input_text = tk.Text(root, height=6, width=50, font=("Arial", 14))  # Increased size
    input_text.pack(pady=10)

    # Create a button for text-to-speech
    tts_button = tk.Button(root, text="Text to Speech", command=handle_text_to_speech, bg="#2196F3", fg="white", font=("Arial", 16, "bold"), padx=10, pady=10, activebackground="#1e88e5")
    tts_button.pack(pady=10)

    # Create a label to display the result
    global result_label
    result_label = tk.Label(root, text="", wraplength=700, justify="center", bg="#f0f0f0", font=("Arial", 14))
    result_label.pack(pady=20)

    # Run the main loop
    root.mainloop()

# Run the GUI
if __name__ == "__main__":
    create_gui()
