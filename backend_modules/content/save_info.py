import datetime


class WriteData(object):

    @staticmethod
    def write_data_into_file(unsaved_data, group, path_file):
        with open(path_file, "a") as file_participants:
            file_participants.write("{0} ### {1} ### {2}\n".format(
                datetime.datetime.today().strftime("%Y-%m-%d-%H.%M.%S"), group, unsaved_data))
