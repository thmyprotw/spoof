import tkinter
import tkinter.messagebox
import webbrowser

def main():
    flag = True

    def change_label_text():        # 修改標籤上的文字
        nonlocal flag               # nonlocal 區域變數
        flag = not flag
        color, msg = ('red', '吳揚升')\
            if flag else ('blue', '露ㄋㄋ')
        label.config(text = msg, fg = color)

    def confirm_to_quit():          # 確認退出
        if tkinter.messagebox.askokcancel('溫馨提示', '确定要把吳揚升退出人生嗎'):
            top.quit()
            urL='https://drive.google.com/file/d/1EVcYWOzKNYWaxTpLfkvg863dFoEmz1aO/view?usp=sharing'
            webbrowser.get('windows-default').open_new(urL)
            print("你被吳揚升中毒了!!!")
    top = tkinter.Tk()              # 創建視窗
    top.geometry('240x160')         # 視窗大小
    top.title('吳揚升露ㄋㄋ')              # 視窗標題
    # 創建標籤並添加到視窗
    label = tkinter.Label(top, text = '吳揚升露ㄋㄋ', font = 'Arial -32', fg = 'red')
    # pack() 函數用來對主控制元件裡面的小控制元件來進行佈局分佈
    label.pack(expand = 1)         
    # Frame 是螢幕上的一快矩形區域，多是用來作為容器（container）布局。
    panel = tkinter.Frame(top)      
    # 創建按鈕物件,指定添加到哪個容器中,透過 command 參數绑定調用函數
    button1 = tkinter.Button(panel, text = '吳揚升露ㄋㄋ', command = change_label_text)
    button1.pack(side = 'left')     
    button2 = tkinter.Button(panel, text = '吳揚升退出人生', command = confirm_to_quit)
    button2.pack(side = 'right')    
    panel.pack(side = 'bottom')     
    # 主程式循環
    tkinter.mainloop()

if __name__ == '__main__':
    main()