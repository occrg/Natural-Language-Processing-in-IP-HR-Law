import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.axes import Axes
from matplotlib.figure import Figure
import numpy as np
from scipy import stats

from backend.FilesIO import FilesIO


"""

"""
class Graph:


    def __init__(self, title, date, hr_ip, user_creator, trends,             \
        documentList):
        """

        """
        self._title = title
        self._trends = trends
        self._indexDict =                                                    \
            self.__compileIndexDict(documentList.getTrainTestDocuments(1))
        if title == '3D Graph':
            self.__create3dGraph(date, hr_ip, user_creator)
        elif title == 'IP-HR/Time':
            self.__createIPHRgraph(date, hr_ip, trends)
        elif title == 'User-Creator/Time':
            self.__createUserCreatorGraph(date, user_creator, trends)
        elif title == 'User-Creator/IP-HR':
            self.__createIPHRUserCreatorGraph(hr_ip, user_creator)
        documentList.addGraph(self)


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

    def getAnnot(self):
        """

        """
        return self._annot

    def getTrends(self):
        """

        """
        return self._trends

    def __create3dGraph(self, Xs, Ys, Zs):
        """

        """
        fig = Figure()
        ax = Axes3D(fig)
        Cs = ['r', 'b']
        Ls = ['Human Rights Journal Article', 'Intellectual Property Journal Article']
        for i in range(len(Xs)):
            ax.scatter(Xs[i], Ys[i], Zs[i], s=40, marker='o', c=Cs[i], label=Ls[i])

        fig.legend()

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

        self._ax = ax
        self._fig = fig


    def __createIPHRgraph(self, Xs, Ys, trends):
        """

        """
        fig = plt.figure()
        ax = plt.axes()
        Cs = ['r', 'b']
        Ls = ['Human Rights Journal Article', 'Intellectual Property Journal Article']
        self._scs = []
        for i in range(len(Xs)):
            sc = ax.scatter(Xs[i], Ys[i], s=40, marker='o', c=Cs[i], label=Ls[i])
            ax.plot(trends[i].getX(), trends[i].getY(), '-%s' % Cs[i])
            self._scs.append(sc)

        self._annot = ax.annotate("", xy=(0,0), xytext=(10,10),textcoords="offset points",
                            bbox=dict(boxstyle="round", alpha=0.9,edgecolor=[0,0.733,0.839], fc="w"),
                            arrowprops=dict(arrowstyle="->"))
        self._annot.set_visible(False)



        ax.spines['left'].set_position(('axes', 0.0))
        ax.spines['right'].set_color('none')
        ax.yaxis.tick_left()
        ax.spines['bottom'].set_position('zero')
        ax.spines['top'].set_color('none')
        ax.xaxis.tick_bottom()

        plt.legend()

        ax.set_xlabel("Date of Publication", fontsize='large', fontweight='bold')
        ax.set_ylabel("IP-HR Scale", fontsize='large', fontweight='bold')
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


    def __createUserCreatorGraph(self, Xs, Ys, trends):
        """

        """
        fig = plt.figure()
        ax = plt.axes()
        Cs = ['r', 'b']
        Ls = ['Human Rights Journal Article', 'Intellectual Property Journal Article']

        self._scs = []
        for i in range(len(Xs)):
            sc = ax.scatter(Xs[i], Ys[i], s=40, marker='o', c=Cs[i], label=Ls[i])
            ax.plot(trends[i].getX(), trends[i].getY(), '-%s' % Cs[i])
            self._scs.append(sc)

        self._annot = ax.annotate("", xy=(0,0), xytext=(10,10),textcoords="offset points",
                            bbox=dict(boxstyle="round", alpha=0.9,edgecolor=[0,0.733,0.839], fc="w"),
                            arrowprops=dict(arrowstyle="->"))
        self._annot.set_visible(False)

        ax.spines['left'].set_position(('axes', 0.0))
        ax.spines['right'].set_color('none')
        ax.yaxis.tick_left()
        ax.spines['bottom'].set_position('zero')
        ax.spines['top'].set_color('none')
        ax.xaxis.tick_bottom()

        plt.legend()
        ax.set_xlabel("Date of Publication", fontsize='large', fontweight='bold')
        ax.set_ylabel("User-Creator Scale", fontsize='large', fontweight='bold')
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


    def __createIPHRUserCreatorGraph(self, Xs, Ys):
        """

        """
        fig = plt.figure()
        ax = plt.axes()
        Cs = ['r', 'b']
        Ls = ['Human Rights Journal Article', 'Intellectual Property Journal Article']

        self._scs = []
        for i in range(len(Xs)):
            sc = ax.scatter(Xs[i], Ys[i], s=40, marker='o', c=Cs[i], label=Ls[i])
            self._scs.append(sc)

        self._annot = ax.annotate("", xy=(0,0), xytext=(10,10),textcoords="offset points",
                            bbox=dict(boxstyle="round", alpha=0.9,edgecolor=[0,0.733,0.839], fc="w"),
                            arrowprops=dict(arrowstyle="->"))
        self._annot.set_visible(False)

        ax.spines['left'].set_position(('zero'))
        ax.spines['right'].set_color('none')
        ax.yaxis.tick_left()
        ax.spines['bottom'].set_position('zero')
        ax.spines['top'].set_color('none')
        ax.xaxis.tick_bottom()

        plt.legend()
        ax.set_xlabel("IP-HR Scale", fontsize='large', fontweight='bold')
        ax.set_ylabel("User-Creator Scale", fontsize='large', fontweight='bold')
        ax.tick_params(axis='x', labelrotation=45, which='major', pad=0)
        ax.tick_params(axis='y', labelrotation=45, which='major', pad=0)
        ax.xaxis.labelpad = 10
        ax.yaxis.labelpad = 10
        ax.xaxis.label.set_color([0,0.733,0.839])
        ax.yaxis.label.set_color([0,0.733,0.839])
        self._ax = ax
        self._fig = fig


    def hover(self, event, canvas):
        """

        """
        vis = self._annot.get_visible()
        if event.inaxes == self._ax:
            for sc in self._scs:
                cont, ind = sc.contains(event)
                if cont:
                    self.__update_annot(sc, ind)
                    self._annot.set_visible(True)
                    canvas.draw_idle()
                else:
                    if vis:
                        self._annot.set_visible(False)
                        canvas.draw_idle()

    def __update_annot(self, sc, ind):
        """

        """
        pos = sc.get_offsets()[ind["ind"][0]]
        document = self._testDocuments[self._indexDict[tuple(pos)]]
        documentData = document.getPDFmetadata()
        self._annot.xy = pos
        text = "Title: {}\nJournal: {}\nDate: {}\nFilename: {}".format(                     \
            documentData.getTitle(),                                         \
            documentData.getJournal(),
            documentData.getDate(),
            document.getFilename())
        self._annot.set_text(text)


    def __compileIndexDict(self, testDocuments):
        """

        """
        indexDict = {}
        for c, document in enumerate(testDocuments):
            classInfo = document.getClassInformation()
            hr_ip = classInfo.getIpRat() - classInfo.getHrRat()
            user_creator = classInfo.getCreatorRat() - classInfo.getUserRat()
            date = mdates.date2num(document.getPDFmetadata().getDate())
            indexDict[(date, hr_ip, user_creator)] = c
            indexDict[(date, hr_ip)] = c
            indexDict[(date, user_creator)] = c
            indexDict[(hr_ip, user_creator)] = c
        return indexDict
