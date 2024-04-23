import ctypes
import os
import tkinter as tk
import psutil
import winreg
import sys
from PIL import Image, ImageTk


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


def scan_programs():
    global programs_found
    programs_found = []

    # Scan for programs in running processes
    running_processes = [p.name() for p in psutil.process_iter()]
    programs_to_check = ["njq8.exe", "njRAT.exe", "windows.exe","windows.exe.tmp", "ecc7c8c51c0850c1ec247c7fd3602f20.exe"]
    for program in programs_to_check:
        if program in running_processes:
            programs_found.append(program[:-4])

    # Check for files added by njRAT in specific locations
    root_files = ["njq8.exe", "njRAT.exe"]
    startup_folder = os.path.join(os.getenv("APPDATA"), "Microsoft", "Windows", "Start Menu", "Programs", "Startup")
    temp_folder = os.path.join(os.getenv("LOCALAPPDATA"), "Temp")

    for root_file in root_files:
        if os.path.exists(os.path.join("C:\\", root_file)):
            programs_found.append(root_file[:-4])
        if os.path.exists(os.path.join(startup_folder, root_file)):
            programs_found.append(root_file[:-4])
        if os.path.exists(os.path.join(temp_folder, root_file)):
            programs_found.append(root_file[:-4])

    # Display scan results
    if programs_found:
        result_label.place(relx=0.8, rely=0.6, anchor=tk.CENTER)
        result_label.config(text=f"Found: {', '.join(programs_found)} running!", fg="green",
                            font=("Helvetica", 15, "bold"))
        root.after(6000, remove_message)  # Remove the message after 6 seconds
    else:
        result_label.place(relx=0.8, rely=0.6, anchor=tk.CENTER)
        result_label.config(text="No programs found!", fg="red", font=("Helvetica", 15, "italic"))
        root.after(6000, remove_message)


def remove_programs():
    if not programs_found:
        result_label.config(text="Must scan first for running programs ", fg="red", font=("Helvetica", 15, "italic"))
        root.after(6000, remove_message)
        return

    # Remove njRAT processes
    for program in programs_found:
        try:
            for proc in psutil.process_iter():
                if proc.name() == f"{program}.exe":
                    proc.kill()
            result_label.config(text=f"Successfully removed {program} from running processes!", fg="blue",
                                font=("Helvetica", 16, "underline"))
            root.after(6000, remove_message)
        except Exception as e:
            print(f"Error while removing {program} from running processes: {e}")

    # Remove files added by njRAT
    root_files = ["njq8.exe", "njRAT.exe"]
    startup_folder = os.path.join(os.getenv("APPDATA"), "Microsoft", "Windows", "Start Menu", "Programs", "Startup")
    temp_folder = os.path.join(os.getenv("LOCALAPPDATA"), "Temp")

    for root_file in root_files:
        if os.path.exists(os.path.join("C:\\", root_file)):
            try:
                os.remove(os.path.join("C:\\", root_file))
                result_label.config(text=f"Successfully removed {root_file} from system root!", fg="blue",
                                    font=("Helvetica", 16, "underline"))
                root.after(6000, remove_message)
            except Exception as e:
                print(f"Error while removing {root_file} from system root: {e}")
        if os.path.exists(os.path.join(startup_folder, root_file)):
            try:
                os.remove(os.path.join(startup_folder, root_file))
                result_label.config(text=f"Successfully removed {root_file} from startup folder!", fg="blue",
                                    font=("Helvetica", 16, "underline"))
                root.after(6000, remove_message)
            except Exception as e:
                print(f"Error while removing {root_file} from startup folder: {e}")
        if os.path.exists(os.path.join(temp_folder, root_file)):
            try:
                os.remove(os.path.join(temp_folder, root_file))
                result_label.config(text=f"Successfully removed {root_file} from temp folder!", fg="blue",
                                    font=("Helvetica", 16, "underline"))
                root.after(6000, remove_message)
            except Exception as e:
                print(f"Error while removing {root_file} from temp folder: {e}")


def remove_message():
    result_label.config(text="")


# Check if script is running as administrator
if is_admin():
    # Create the main window
    root = tk.Tk()
    root.title("GREN Galactic Ranger Exterminator of njRAT")

    # Load the background image
    try:
        background_image = Image.open("Default_space_military_guy_remover_of_trojan_malware_across_th_1.png")
        image_width, image_height = background_image.size
        root.geometry(f"{image_width}x{image_height}")  # Set window size to match background image
        background_image = background_image.resize((image_width, image_height))
        background_photo = ImageTk.PhotoImage(background_image)
        background_label = tk.Label(root, image=background_photo)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)  # Stretch the label to cover the entire window
    except FileNotFoundError as e:
        print(f"Error while loading background image: {e}")

    # Create SCAN button
    scan_button = tk.Button(root, text="SCAN", command=scan_programs, font=("Helvetica", 17), bg="green", fg="white")
    scan_button.place(relx=0.8, rely=0.3, anchor=tk.CENTER)

    # Create REMOVE button (always present)
    remove_button_text = "REMOVE"
    remove_bg_color = "blue"
    remove_fg_color = "white"
    remove_button = tk.Button(root, text=remove_button_text, command=remove_programs, font=("Helvetica", 17),
                              bg=remove_bg_color, fg=remove_fg_color)
    remove_button.place(relx=0.8, rely=0.4, anchor=tk.CENTER)

    programs_found = []  # List to store programs found during scanning

    # Create a label to display the result of the actions
    result_label = tk.Label(root, text="", font=("Helvetica", 14), bg="white")

    # Run the main event loop
    root.mainloop()
else:
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
