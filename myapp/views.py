from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContactForm
import numpy as np
import matplotlib.pyplot as plt
from io import StringIO
# Create your views here.

#def index(request):
#    form = ContactForm()
#    return render(request, 'pages/home.html', {'form': form})

def generate_mesh_M2(Nj, Ni):  # Nj, Ni: số điểm lưới
    # Kích thước vùng tính toán
    ly, lx = Nj/10, Ni/10

    # Tạo mảng 3 chiều để chứa tọa độ các điểm lưới
    points = np.zeros((Nj, Ni, 2))

    # tọa độ x tại các điểm lưới
    dx = lx / Ni
    x = np.linspace(0, lx, Ni)

    # tọa độ y của biên dưới
    y0 = np.zeros(Ni)

    # index i tương ứng vị trí x = 2, 4 trên biên dưới
    i2 = int(2. / dx)
    i4 = int(4. / dx)

    y0[i2:i4] = (x[i2:i4] - 2.) * np.tan(np.pi / 12)
    y0[i4:] = 2.0 * np.tan(np.pi / 12)

    # khoảng cách dy giữa hai điểm cùng cột
    dy = np.array([(ly - y) / (Nj - 1) for y in y0])

    # xác định tọa độ (x, y) của từng điểm
    for j in range(Nj):
        for i in range(Ni):
            points[j, i, 0] = x[i]
            points[j, i, 1] = y0[i] + j * dy[i]

    return points
def return_graph(Nj,Ni):
    #Nj, Ni = 41, 101
    #Nj=request.POST('w_h')
    #Ni = request.POST('w_l')
    points = generate_mesh_M2(Nj, Ni)
    fig = plt.figure()
    plt.plot(points[:, :, 0], points[:, :, 1], 'r+')

    imgdata= StringIO()
    fig.savefig(imgdata,format='svg')
    imgdata.seek(0)
    data=imgdata.getvalue()
    return data

def index(request):
    if request.method=='POST':
        Nj=int(request.POST['w_h'])*10+1
        Ni=int(request.POST['l_h'])*10+1

    else: Nj, Ni= 41,101
    graphic = return_graph(Nj,Ni)
    return render(request, 'pages/plot1.html', {'graphic':graphic})

