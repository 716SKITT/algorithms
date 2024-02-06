import matplotlib.pyplot as plt


def main():
    x_dot = [0, 1, 2, 3, 4]
    y_dot = [0, 3, 1, 5, 2]
    plt.plot(x_dot, y_dot)
    plt.xlim(xmin=-1, xmax=10)
    plt.ylim(ymin=-1, ymax=6)
    plt.title('Образец')
    plt.xlabel('X ось')
    plt.ylabel('Y ось')
    plt.grid(True)
    plt.show()


# main()

def bar():
    left_edges = [0, 10, 20, 30, 40]
    heights = [100, 200, 300, 400, 500]
    plt.bar(left_edges, heights, 10, color=('r', 'g', 'b', 'm', 'k'))
    plt.title('Тест')
    plt.xlabel('X Сторона')
    plt.ylabel('Y Сторона')
    plt.xticks([5, 15, 25, 35, 45], ['2013', '2014', '2015', '2016', '2017'])
    plt.yticks([0, 100, 200, 300, 400, 500], ['$0m', '$1m', '$2m', '$3m', '$4m', '$5m',])
    plt.show()


# bar()

def pie():
    sales = [20, 60, 80, 40]
    slice_labels = ['I квартал', 'II квартал', 'III квартал', 'IV квартал']
    plt.pie(sales, labels=slice_labels)
    plt.show()


# pie()


