import tkinter as tk
from tkinter import messagebox

def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shifted = ord(char) + shift
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
            encrypted_text += chr(shifted)
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(encrypted_text, shift):
    decrypted_text = ""
    for char in encrypted_text:
        if char.isalpha():
            shifted = ord(char) - shift
            if char.islower():
                if shifted < ord('a'):
                    shifted += 26
            elif char.isupper():
                if shifted < ord('A'):
                    shifted += 26
            decrypted_text += chr(shifted)
        else:
            decrypted_text += char
    return decrypted_text

def encrypt_message():
    message = entry_message.get()
    shift = int(entry_shift.get())
    encrypted_message = encrypt(message, shift)
    messagebox.showinfo("Encrypted Message", encrypted_message)

def decrypt_message():
    message = entry_message.get()
    shift = int(entry_shift.get())
    decrypted_message = decrypt(message, shift)
    messagebox.showinfo("Decrypted Message", decrypted_message)

# Create main window
root = tk.Tk()
root.title("Caesar Cipher")

# Create message label and entry
label_message = tk.Label(root, text="Enter Message:")
label_message.grid(row=0, column=0, padx=5, pady=5)
entry_message = tk.Entry(root)
entry_message.grid(row=0, column=1, padx=5, pady=5)

# Create shift label and entry
label_shift = tk.Label(root, text="Enter Shift Value:")
label_shift.grid(row=1, column=0, padx=5, pady=5)
entry_shift = tk.Entry(root)
entry_shift.grid(row=1, column=1, padx=5, pady=5)

# Create buttons for encryption and decryption
button_encrypt = tk.Button(root, text="Encrypt", command=encrypt_message)
button_encrypt.grid(row=2, column=0, padx=5, pady=5)
button_decrypt = tk.Button(root, text="Decrypt", command=decrypt_message)
button_decrypt.grid(row=2, column=1, padx=5, pady=5)

root.mainloop()
