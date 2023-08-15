import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes
import clipboard
from ttkbootstrap import Style

class EncryptionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("RSA Key Generator and Encryption")

        self.private_key = None
        self.public_key = None

        self.style = Style(theme='vapor')
        self.create_widgets()

    def create_widgets(self):
        self.style.configure("TLabel", font=("Helvetica", 16, "bold"))

        ttk.Label(self.root, text="RSA Key Generator and Encryption").pack(pady=10)

        ttk.Button(self.root, text="Generate Key Pair", command=self.generate_key_pair).pack(pady=5)

        ttk.Label(self.root, text="Private Key:").pack(pady=5)
        self.private_key_text = tk.Text(self.root, height=8, width=60)
        self.private_key_text.pack()

        ttk.Button(self.root, text="Copy Private Key", command=self.copy_private_key).pack(pady=5)

        ttk.Label(self.root, text="Public Key:").pack(pady=5)
        self.public_key_text = tk.Text(self.root, height=8, width=60)
        self.public_key_text.pack()

        ttk.Button(self.root, text="Copy Public Key", command=self.copy_public_key).pack(pady=5)

        ttk.Label(self.root, text="Enter message to encrypt:").pack(pady=5)
        self.input_entry = ttk.Entry(self.root, width=60)
        self.input_entry.pack()

        ttk.Button(self.root, text="Encrypt", command=self.encrypt_data).pack(pady=5)

    def generate_key_pair(self):
        self.private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048,
            backend=default_backend()
        )
        self.public_key = self.private_key.public_key()

        private_key_pem = self.private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.TraditionalOpenSSL,
            encryption_algorithm=serialization.NoEncryption()
        )
        public_key_pem = self.public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )

        self.private_key_text.delete("1.0", tk.END)
        self.private_key_text.insert(tk.END, private_key_pem.decode())

        self.public_key_text.delete("1.0", tk.END)
        self.public_key_text.insert(tk.END, public_key_pem.decode())

    def copy_private_key(self):
        clipboard.copy(self.private_key_text.get("1.0", tk.END))
        messagebox.showinfo("Copy Successful", "Private key copied to clipboard.")

    def copy_public_key(self):
        clipboard.copy(self.public_key_text.get("1.0", tk.END))
        messagebox.showinfo("Copy Successful", "Public key copied to clipboard.")

    def encrypt_data(self):
        if not self.public_key:
            messagebox.showerror("Error", "Please generate a key pair first.")
            return

        try:
            data = self.input_entry.get().encode()
            encrypted_data = self.public_key.encrypt(
                data,
                padding.OAEP(
                    mgf=padding.MGF1(algorithm=hashes.SHA256()),
                    algorithm=hashes.SHA256(),
                    label=None
                )
            )
            messagebox.showinfo("Encryption Result", f"Encrypted Data: {encrypted_data}")
        except Exception as e:
            messagebox.showerror("Error", f"Encryption failed: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = EncryptionApp(root)
    root.mainloop()

