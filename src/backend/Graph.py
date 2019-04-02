import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.axes import Axes
import numpy as np
from matplotlib.figure import Figure


"""

"""
class Graph:


    def __init__(self, title, documentList):
        """

        """
        self._title = title
        self._Xs, self._Ys, self._Zs = self.__gatherData(documentList)


    def getTitle(self):
        """

        """
        return self._title

    def getFig(self):
        """

        """
        return self._fig

    def getAx(self):
        """

        """
        return self._ax


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


    def create3dGraph(self):
        """

        """
        fig = Figure()
        ax = Axes3D(fig)
        Cs = ['Red', 'Blue']
        Ls = ['Human Rights Journal Article', 'Intellectual Property Journal Article']
        for i in range(len(self._Xs)):
            ax.scatter(self._Xs[i], self._Ys[i], self._Zs[i], s=40, marker='o', c=Cs[i], label=Ls[i])

        fig.legend()
        ax.set_ylim(-1, 1)
        # ax.set_zlim(-1, 1)
        ax.set_xlabel("Date of Publication", fontsize='large', fontweight='bold')
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
        # fig.ylim(-1,1)
        # plt.show()
        self._ax = ax
        self._fig = fig


    def createIPHRgraph(self):
        """

        """
        fig = plt.figure()
        ax = plt.axes()
        Cs = ['Red', 'Blue']
        Ls = ['Human Rights Journal Article', 'Intellectual Property Journal Article']
        for i in range(len(self._Xs)):
            ax.scatter(self._Xs[i], self._Ys[i], s=40, marker='o', c=Cs[i], label=Ls[i])

        ax.spines['left'].set_position(('axes', 0.0))
        ax.spines['right'].set_color('none')
        ax.yaxis.tick_left()
        ax.spines['bottom'].set_position('zero')
        ax.spines['top'].set_color('none')
        ax.xaxis.tick_bottom()

        plt.legend()
        ax.set_ylim(-1, 1)
        ax.set_xlabel("Date of Publication", fontsize='large', fontweight='bold')
        ax.set_ylabel("HR-IP scale", fontsize='large', fontweight='bold')
        years = mdates.YearLocator()
        months = mdates.MonthLocator()
        yearsFmt = mdates.DateFormatter('%Y')
        ax.xaxis.set_major_locator(years)
        ax.xaxis.set_major_formatter(yearsFmt)
        ax.xaxis.set_minor_locator(months)
        ax.tick_params(axis='x', labelrotation=90, which='major', pad=0)
        ax.tick_params(axis='y', labelrotation=45, which='major', pad=0)
        ax.xaxis.labelpad = 23
        ax.yaxis.labelpad = 18
        ax.xaxis.label.set_color([0,0.733,0.839])
        ax.yaxis.label.set_color([0,0.733,0.839])
        self._ax = ax
        self._fig = fig


    def createUserCreatorGraph(self):
        """

        """
        fig = plt.figure()
        ax = plt.axes()
        Cs = ['Red', 'Blue']
        Ls = ['Human Rights Journal Article', 'Intellectual Property Journal Article']
        for i in range(len(self._Xs)):
            ax.scatter(self._Xs[i], self._Zs[i], s=40, marker='o', c=Cs[i], label=Ls[i])

        ax.spines['left'].set_position(('axes', 0.0))
        ax.spines['right'].set_color('none')
        ax.yaxis.tick_left()
        ax.spines['bottom'].set_position('zero')
        ax.spines['top'].set_color('none')
        ax.xaxis.tick_bottom()

        plt.legend()
        ax.set_ylim(-1, 1)
        ax.set_xlabel("Date of Publication", fontsize='large', fontweight='bold')
        ax.set_ylabel("HR-IP scale", fontsize='large', fontweight='bold')
        years = mdates.YearLocator()
        months = mdates.MonthLocator()
        yearsFmt = mdates.DateFormatter('%Y')
        ax.xaxis.set_major_locator(years)
        ax.xaxis.set_major_formatter(yearsFmt)
        ax.xaxis.set_minor_locator(months)
        ax.tick_params(axis='x', labelrotation=90, which='major', pad=0)
        ax.tick_params(axis='y', labelrotation=45, which='major', pad=0)
        ax.xaxis.labelpad = 23
        ax.yaxis.labelpad = 18
        ax.xaxis.label.set_color([0,0.733,0.839])
        ax.yaxis.label.set_color([0,0.733,0.839])
        # fig.ylim(-1,1)
        self._ax = ax
        self._fig = fig


    def createIPHRUserCreatorGraph(self):
        """

        """
        fig = plt.figure()
        ax = plt.axes()
        Cs = ['Red', 'Blue']
        Ls = ['Human Rights Journal Article', 'Intellectual Property Journal Article']
        for i in range(len(self._Xs)):
            ax.scatter(self._Ys[i], self._Zs[i], s=40, marker='o', c=Cs[i], label=Ls[i])

        ax.spines['left'].set_position(('zero'))
        ax.spines['right'].set_color('none')
        ax.yaxis.tick_left()
        ax.spines['bottom'].set_position('zero')
        ax.spines['top'].set_color('none')
        ax.xaxis.tick_bottom()

        plt.legend()
        # ax.set_ylim(-1, 1)
        ax.set_xlabel("HR-IP scale", fontsize='large', fontweight='bold')
        ax.set_ylabel("User-Creator scale", fontsize='large', fontweight='bold')
        years = mdates.YearLocator()
        months = mdates.MonthLocator()
        yearsFmt = mdates.DateFormatter('%Y')
        ax.tick_params(axis='x', labelrotation=45, which='major', pad=0)
        ax.tick_params(axis='y', labelrotation=45, which='major', pad=0)
        ax.xaxis.labelpad = 10
        ax.yaxis.labelpad = 10
        ax.xaxis.label.set_color([0,0.733,0.839])
        ax.yaxis.label.set_color([0,0.733,0.839])
        self._ax = ax
        self._fig = fig
