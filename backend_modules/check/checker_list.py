from backend_modules.content.save_info import WriteData


class CheckerParticipants(object):

    def __init__(self, log_file):
        self.log_file = log_file
        self.list_data = []

    def init_list(self):
        list_info = []
        with open(self.log_file, "r") as log:
            raw_data = log.readlines()
            for raw in raw_data:
                work_row = raw.split(" ### ")
                self.list_data.append(work_row[2].replace("\n", ""))
                if len(work_row) > 1:
                    if work_row[1] == "00":
                        list_info.append(work_row[2].replace("\n", ""))
        return list_info

    def write_data_into_list(self, data, group):
        if self._check_list(self.list_data, data):
            self.list_data.append(data)
            WriteData().write_data_into_file(data, group, self.log_file)
            if group == "00":
                return data
            else:
                return None
        else:
            return None

    @staticmethod
    def _check_list(list_data, data):
        for i in list_data:
            if i == data:
                print(i, data)
                return False
        return True
