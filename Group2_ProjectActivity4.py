import requests
import tkinter as tk
from tkinter import messagebox

def get_public_ip(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        data = response.json()
        return data.get("ip", "Unknown")
    except requests.RequestException as e:
        return str(e)

def display_ip_info():
    ipv4 = get_public_ip("https://api.ipify.org?format=json")
    ipv6 = get_public_ip("https://api64.ipify.org?format=json")

    ipv4_label.config(text=f"Public IPv4 Address: {ipv4}")
    ipv6_label.config(text=f"Public IPv6 Address: {ipv6}")

# GUI setup
root = tk.Tk()
root.title("Public IP Information")
root.configure(bg="#ADD8E6")  # Light Blue background

ipv4_label = tk.Label(root, text="Public IPv4 Address: ", bg="#ADD8E6")
ipv4_label.pack(pady=10)

ipv6_label = tk.Label(root, text="Public IPv6 Address: ", bg="#ADD8E6")
ipv6_label.pack(pady=10)

refresh_button = tk.Button(root, text="Refresh", command=display_ip_info, bg="#87CEEB")  # Sky Blue button
refresh_button.pack(pady=20)

exit_button = tk.Button(root, text="Exit", command=root.destroy, bg="#87CEEB")  # Sky Blue button
exit_button.pack(pady=10)

# Run the application
display_ip_info()  # Display IP information on startup
root.mainloop()
