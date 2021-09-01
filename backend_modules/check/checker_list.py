from backend_modules.content.save_info import WriteData


class CheckerParticipants(object):

    def __init__(self, log_file):
        self.log_file = log_file

    def init_list(self):
        list_info = []
        with open(self.log_file, "r") as log:
            raw_data = log.readlines()
            for raw in raw_data:
                work_row = raw.split(" ### ")
                if len(work_row) > 1:
                    if work_row[1] == "00":
                        list_info.append(work_row[2].replace("\n", ""))
        return list_info
