import tkinter as tk
from tftpy import TftpClient
from tkinter import filedialog
from tkinter import messagebox

# 定義選擇資料夾路徑的函數
def choose_save_path():
    save_path = filedialog.askdirectory()
    if save_path:
        save_path_entry.delete(0, tk.END)
        save_path_entry.insert(0, save_path)

# 定義下載檔案的函數
def download_file():
    # 取得IP地址和檔案名
    ip_address = ip_entry.get()
    file_name = file_name_entry.get()
    save_path = save_path_entry.get()
    # 建立TFTPClient物件
    client = TftpClient(ip_address, 69)
    # 從TFTP伺服器下載檔案
    client.download(file_name, f'{save_path}/{file_name}')
    # 顯示下載完成通知視窗
    messagebox.showinfo('下載完成', '檔案已成功下載')


# 建立Tkinter視窗
root = tk.Tk()
root.title("TFTP Client")

# 建立IP地址標籤和文字方塊
ip_label = tk.Label(root, text="IP Address:")
ip_entry = tk.Entry(root)

# 建立檔案名標籤和文字方塊
file_name_label = tk.Label(root, text="File Name:")
file_name_entry = tk.Entry(root)

# 建立儲存路徑標籤和文字方塊
save_path_label = tk.Label(root, text="Save Path:")
save_path_entry = tk.Entry(root)
choose_path_button = tk.Button(root, text="選擇路徑", command=choose_save_path)

# 建立下載按鈕
download_button = tk.Button(root, text="Download", command=download_file)

# 將標籤、文字方塊和按鈕放置在視窗上
ip_label.grid(row=0, column=0)
ip_entry.grid(row=0, column=1)
file_name_label.grid(row=1, column=0)
file_name_entry.grid(row=1, column=1)
save_path_label.grid(row=2, column=0)
save_path_entry.grid(row=2, column=1)
choose_path_button.grid(row=2, column=2)
download_button.grid(row=3, columnspan=3)

# 將視窗顯示在螢幕上
root.mainloop()