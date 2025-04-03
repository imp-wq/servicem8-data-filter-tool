import logging
import tkinter as tk
from tkinter import messagebox
from fetch_data import FILE_PATH, SHEET_TITLE, run_oauth_flow, query_staff_uuid, query_jobs, write_jobs_to_excel
import logging

logging.basicConfig(level=logging.INFO)


class SheetWriterUI:
    def __init__(self, root):
        self.root = root
        self.root.title("PydanticAI Sheet Writer")

        # Create StringVars for binding
        self.file_path_var = tk.StringVar(value=FILE_PATH)
        self.sheet_title_var = tk.StringVar(value=SHEET_TITLE)

        self.build_ui()

    def build_ui(self):
        # File path input
        tk.Label(self.root, text="File Path:").grid(row=0, column=0, padx=10, pady=10, sticky="e")
        tk.Entry(self.root, textvariable=self.file_path_var, width=40).grid(row=0, column=1, padx=10, pady=10)

        # Sheet title input
        tk.Label(self.root, text="Sheet Title:").grid(row=1, column=0, padx=10, pady=10, sticky="e")
        tk.Entry(self.root, textvariable=self.sheet_title_var, width=40).grid(row=1, column=1, padx=10, pady=10)

        # Run button
        tk.Button(self.root, text="Run", command=self.on_run).grid(row=2, column=0, columnspan=2, pady=20)

    def on_run(self):
        file_path = self.file_path_var.get()
        sheet_title = self.sheet_title_var.get()

        if not file_path or not sheet_title:
            messagebox.showerror("Input Error", "Please fill in all fields.")
            return

        try:
            success = self.process_data(file_path, sheet_title)
            if success:
                messagebox.showinfo("Success", "Data written to sheet successfully!")
            else:
                messagebox.showwarning("Warning", "Process completed with issues.")
        except Exception as e:
            logging.error(e)
            messagebox.showerror("Error", str(e))

    def process_data(self, file_path, sheet_title):
        access_token = run_oauth_flow()

        logging.info(f"Processing file: {file_path} with sheet title: {sheet_title}")
        staff_uuid = query_staff_uuid(access_token)

        logging.info(f"Query staff uuid: {staff_uuid}")
        jobs = query_jobs(access_token, staff_uuid)
        write_jobs_to_excel(jobs, file_path, sheet_title)
        return True  # Simulate success


if __name__ == "__main__":
    root = tk.Tk()
    app = SheetWriterUI(root)
    root.mainloop()
