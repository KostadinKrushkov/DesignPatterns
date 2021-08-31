class DataAnalyzer:  # AbstractClass
    filename = None
    data = None
    analyzed_data = None

    def __init__(self, filename):
        self.filename = filename

    def extract_data(self):  # template method
        self.read_data()
        self.analyze_data()
        self.visualize_data()

    def read_data(self):
        raise NotImplemented()

    def analyze_data(self):
        raise NotImplemented()

    def visualize_data(self):
        if self.analyzed_data:
            print(self.analyzed_data)
        else:
            raise Exception("Data was not analyzed properly")


class PDFDataAnalyzer(DataAnalyzer):  # ConcreteClass1
    def read_data(self):
        # read data from pdf
        self.data = "Data read from pdf"

    def analyze_data(self):
        if not self.data:
            raise Exception("Data was not read properly")
        if type(self.data) == str:
            self.analyzed_data = "Data is of type string\n"
        else:
            self.analyzed_data = "Data could be anything but a string\n"


class CSVDataAnalyzer(DataAnalyzer):  # ConcreteClass2
    def read_data(self):
        # read data from pdf
        self.data = [
            ['First name', 'Last name', 'Age', 'Education'],
            ['Kostadin', 'Krushkov', '23', 'Bachelor\'s degree in engineering']
                    ]

    def analyze_data(self):
        self.analyzed_data = []
        if type(self.data) == list:
            if len(self.data) > 1:
                for i in range(1, len(self.data)):
                    self.analyzed_data.append(Person(*self.data[i]))

    def visualize_data(self):
        for person in self.analyzed_data:
            print(person)


class Person:
    first_name = None
    last_name = None
    age = None
    education = None

    def __init__(self, first_name, last_name, age, education):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.education = education

    def __repr__(self):
        return "{0} {1}, age {2}, has education {3}\n".format(self.first_name, self.last_name, self.age, self.education)


if __name__ == "__main__":
    filename = "some_file"
    pdf_analyzer = PDFDataAnalyzer(filename)
    csv_analyzer = CSVDataAnalyzer(filename)

    print("PDF data")
    pdf_analyzer.extract_data()

    print("CSV data")
    csv_analyzer.extract_data()
