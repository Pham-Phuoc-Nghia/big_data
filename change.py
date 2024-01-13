from mrjob.job import MRJob

class MyJob(MRJob):

    def mapper(self, _, line):
        try:
            country, cases, deaths, _, _ = line.split(',')
            yield country, (int(cases), int(deaths))
        except ValueError:
            # Xử lý lỗi cho các dòng không hợp lệ (không đủ 5 giá trị)
            pass

    def reducer(self, country, values):
        total_cases = sum(value[0] for value in values)
        total_deaths = sum(value[1] for value in values)
        yield country, (total_cases, total_deaths)

if __name__ == '__main__':
    MyJob.run()