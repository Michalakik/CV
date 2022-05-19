import matplotlib.pyplot as plt
from quicksort_mediana import *
from merge_sort import *
from quicksort_random import *
from tkinter import *
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)

sys.setrecursionlimit(5000)

def printList(arr):
    for i in range(len(arr)):
        print(arr[i], end="\n")
    print()


# x = [10, 100, 500, 1000, 5000, 10000, 25000, 50000, 75000, 100000, 150000, 200000]  # wielkosc danych
x = [10, 100, 1000]  # dane probne


def fill_table(a, b):
    data = []  # tablica z danymi
    for i in x:
        data.append([])
        for j in range(i):
            data[len(data) - 1].append(random.randint(a, b))
    return data


dane1 = fill_table(-5000, 5000)
dane2 = fill_table(-10000, 10000)
dane3 = fill_table(-100000, 100000)


def time(arr):
    time_median = []
    for i in range(len(arr)):
        time_median.append(check_time(arr[i]))

    time_merge = []
    for i in range(len(arr)):
        time_merge.append(check_time_merge(arr[i]))

    time_random = []
    for i in range(len(arr)):
        time_random.append(check_time_random(arr[i]))

    return time_median, time_random, time_merge


time1 = time(dane1)
time2 = time(dane2)
time3 = time(dane3)


def plotting(time_table):
    fig, ax = plt.subplots()  # figura z pojedynczymi osiami
    fig.set_size_inches(18.5, 10.5, forward=TRUE)
    plt.title("Porównanie czasu wykonywania quicksortów i mergesorta")
    plt.ylabel("czas(sekundy)")
    plt.xlabel("ilość danych")
    plt.plot(x, time_table[1], 'or', label="random")
    plt.plot(x, time_table[0], 'oy', label="median")
    plt.plot(x, time_table[2], 'o', label="merge")
    plt.legend()

    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.draw()

    canvas.get_tk_widget().pack()

    toolbar = NavigationToolbar2Tk(canvas, window)
    toolbar.update()

    canvas.get_tk_widget().pack()


def plot():
    plotting(time1)


def plot2():
    plotting(time2)


def plot3():
    plotting(time3)


def restart():
    global window
    try:
        if (0 == 0):
            window.destroy()
    finally:
        window = Tk()
        frame = Frame(window)
        frame.pack()

        window.title('Plotting in Tkinter')

        window.geometry("700x700")

        plot_button = Button(master=frame, command=plot, height=2, width=20, text="od -5000 do 5000")
        plot_button2 = Button(master=frame, command=plot2, height=2, width=20, text="od -10000 do 10000")
        plot_button3 = Button(master=frame, command=plot3, height=2, width=20, text="od -100000 do 100000")
        button_clear = Button(master=frame, command=restart, height=2, width=20, text="WYCZYŚĆ")

        plot_button.pack(side=LEFT)
        plot_button2.pack(side=LEFT)
        plot_button3.pack(side=LEFT)
        button_clear.pack(side=LEFT)

        window.mainloop()


def main():
    global window
    window = Tk()
    window.minsize(700, 700)
    frame = Frame(window)
    frame.pack()

    window.title('Plotting in Tkinter')

    window.geometry("700x700")

    plot_button = Button(master=frame, command=plot, height=2, width=20, text="od -5000 do 5000")
    plot_button2 = Button(master=frame, command=plot2, height=2, width=20, text="od -10000 do 10000")
    plot_button3 = Button(master=frame, command=plot3, height=2, width=20, text="od -100000 do 100000")
    button_clear = Button(master=frame, command=restart, height=2, width=20, text="WYCZYŚĆ")

    plot_button.pack(side=LEFT)
    plot_button2.pack(side=LEFT)
    plot_button3.pack(side=LEFT)
    button_clear.pack(side=LEFT)

    window.mainloop()


main()