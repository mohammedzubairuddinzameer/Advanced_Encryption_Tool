from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto import Random
import os
from tkinter import *
from tkinter import filedialog, messagebox

# AES Encryption
def encrypt_file(key, filename):
    chunksize = 64 * 1024
    output_file = filename + ".enc"
    filesize = str(os.path.getsize(filename)).zfill(16)
    IV = Random.new().read(16)

    encryptor = AES.new(get_key(key), AES.MODE_CBC, IV)

    with open(filename, 'rb') as infile:
        with open(output_file, 'wb') as outfile:
            outfile.write(filesize.encode('utf-8'))
            outfile.write(IV)

            while True:
                chunk = infile.read(chunksize)
                if len(chunk) == 0:
                    break
                elif len(chunk) % 16 != 0:
                    chunk += b' ' * (16 - len(chunk) % 16)
                outfile.write(encryptor.encrypt(chunk))

# AES Decryption
def decrypt_file(key, filename):
    chunksize = 64 * 1024
    output_file = filename.replace(".enc", ".dec")

    with open(filename, 'rb') as infile:
        filesize = int(infile.read(16))
        IV = infile.read(16)

        decryptor = AES.new(get_key(key), AES.MODE_CBC, IV)

        with open(output_file, 'wb') as outfile:
            while True:
                chunk = infile.read(chunksize)
                if len(chunk) == 0:
                    break
                outfile.write(decryptor.decrypt(chunk))
            outfile.truncate(filesize)

# Generate 256-bit key
def get_key(password):
    hasher = SHA256.new(password.encode('utf-8'))
    return hasher.digest()

# File selection
def browse_file():
    filename = filedialog.askopenfilename()
    file_entry.delete(0, END)
    file_entry.insert(0, filename)

# Encrypt Button
def encrypt_action():
    key = password_entry.get()
    file_path = file_entry.get()
    if not key or not file_path:
        messagebox.showerror("Error", "Both file and password are required.")
        return
    encrypt_file(key, file_path)
    messagebox.showinfo("Success", "File encrypted successfully!")

# Decrypt Button
def decrypt_action():
    key = password_entry.get()
    file_path = file_entry.get()
    if not key or not file_path:
        messagebox.showerror("Error", "Both file and password are required.")
        return
    decrypt_file(key, file_path)
    messagebox.showinfo("Success", "File decrypted successfully!")

# GUI
root = Tk()
root.title("AES-256 Encryption Tool")
root.geometry("500x200")

Label(root, text="File Path:").pack()
file_entry = Entry(root, width=50)
file_entry.pack()

Button(root, text="Browse", command=browse_file).pack(pady=5)

Label(root, text="Password:").pack()
password_entry = Entry(root, show="*", width=50)
password_entry.pack()

Button(root, text="Encrypt", command=encrypt_action).pack(side=LEFT, padx=50, pady=20)
Button(root, text="Decrypt", command=decrypt_action).pack(side=RIGHT, padx=50, pady=20)

root.mainloop()
