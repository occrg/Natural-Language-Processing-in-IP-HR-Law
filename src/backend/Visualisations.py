import matplotlib.dates as mdates
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np


"""

"""
class Visualisations:


    def __init__(self, documentList):
        """

        """
        self.__visualisations = []
        Xs, Ys, Zs = self.__gatherData(documentList)
        self.__visualisations.append(self.__3dGraph(Xs, Ys, Zs))


    def __gatherData(self, documentList):
        """

        """
        XsHr = []
        XsIp = []
        Xs = []
        YsHr = []
        YsIp = []
        Ys = []
        ZsHr = []
        ZsIp = []
        Zs = []
        testDocuments = documentList.getTrainTestDocuments(1)
        for document in testDocuments:
            if document.getClassInformation().getGt():
                XsIp.append(mdates.date2num(document.getPDFmetadata().getDate()))
                YsIp.append(document.getClassInformation().getIpRat() - document.getClassInformation().getHrRat())
                ZsIp.append(document.getClassInformation().getCreatorRat() - document.getClassInformation().getUserRat())
            else:
                XsHr.append(mdates.date2num(document.getPDFmetadata().getDate()))
                YsHr.append(document.getClassInformation().getIpRat() - document.getClassInformation().getHrRat())
                ZsHr.append(document.getClassInformation().getCreatorRat() - document.getClassInformation().getUserRat())
        Xs.append(XsHr)
        Xs.append(XsIp)
        Ys.append(YsHr)
        Ys.append(YsIp)
        Zs.append(ZsHr)
        Zs.append(ZsIp)
        return Xs, Ys, Zs

    def __3dGraph(self, Xs, Ys, Zs):
        """

        """
        fig = plt.figure()
        ax = Axes3D(fig)
        Cs = ['Red', 'Blue']
        Ls = ['Human Rights', 'Intellectual Property']
        for i in range(len(Xs)):
            ax.scatter(Xs[i], Ys[i], Zs[i], s=40, marker='o', c=Cs[i], label=Ls[i])

        plt.legend()
        ax.set_ylim(-1, 1)
        # ax.set_zlim(-1, 1)
        ax.set_xlabel("Time", fontsize='large', fontweight='bold')
        ax.set_ylabel("HR-IP scale", fontsize='large', fontweight='bold')
        ax.set_zlabel("Creator-User scale", fontsize='large', fontweight='bold')
        years = mdates.YearLocator()
        months = mdates.MonthLocator()
        yearsFmt = mdates.DateFormatter('%Y')
        ax.xaxis.set_major_locator(years)
        ax.xaxis.set_major_formatter(yearsFmt)
        ax.xaxis.set_minor_locator(months)
        ax.tick_params(axis='x', labelrotation=90, which='major', pad=0)
        ax.tick_params(axis='y', labelrotation=45, which='major', pad=0)
        ax.tick_params(axis='z', labelrotation=45, which='major', pad=0)
        ax.xaxis.labelpad = 23
        ax.yaxis.labelpad = 18
        ax.zaxis.labelpad = 4
        ax.xaxis.label.set_color([0,0.733,0.839])
        ax.yaxis.label.set_color([0,0.733,0.839])
        ax.zaxis.label.set_color([0,0.733,0.839])
        plt.ylim(-1,1)
        # plt.show()
        return fig
