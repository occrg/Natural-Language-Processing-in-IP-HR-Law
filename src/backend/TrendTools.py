import matplotlib.dates as mdates

from backend.Trend import Trend


"""

"""
class TrendTools:


    def arrangeIntoPoints(self, testDocuments):
        """

        """
        date_HR = []
        date_IP = []
        date = []
        hr_ip_HR = []
        hr_ip_IP = []
        hr_ip = []
        user_creator_HR = []
        user_creator_IP = []
        user_creator = []
        for document in testDocuments:
            try:
                if document.getClassInformation().getGt():
                    date_IP.append(mdates.date2num(document.getPDFmetadata().getDate()))
                    hr_ip_IP.append(document.getClassInformation().getIpRat() - document.getClassInformation().getHrRat())
                    user_creator_IP.append(document.getClassInformation().getCreatorRat() - document.getClassInformation().getUserRat())
                else:
                    date_HR.append(mdates.date2num(document.getPDFmetadata().getDate()))
                    hr_ip_HR.append(document.getClassInformation().getIpRat() - document.getClassInformation().getHrRat())
                    user_creator_HR.append(document.getClassInformation().getCreatorRat() - document.getClassInformation().getUserRat())
            except AttributeError as err:
                print(document.getFilename())
                print(err)
        date.append(date_HR)
        date.append(date_IP)
        hr_ip.append(hr_ip_HR)
        hr_ip.append(hr_ip_IP)
        user_creator.append(user_creator_HR)
        user_creator.append(user_creator_IP)
        return date, hr_ip, user_creator

    def generateTrends(self, date, hr_ip, user_creator):
        """

        """
        trends = []
        for i in range(len(date)):
            trends.append(Trend(i, "Intellectual Property",                  \
                "Human Rights", "HR-IP scale", "time", date[i], hr_ip[i]))
        for i in range(len(date)):
            trends.append(Trend(i, "Creator", "User", "User-Creator scale",  \
                "time", date[i], user_creator[i]))
        return trends
