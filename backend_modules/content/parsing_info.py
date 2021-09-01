class CreatorInfo(object):

    def create_output_data(self, input_data):
        return self._parsing_input(input_data)

    def _formatting_the_time_string(self, time_string):
        time_list = [float(i) for i in time_string.split(":")]
        time_list[2] = round(time_list[2], 1)
        if time_list[2] >= 60:
            time_list[2] = 0.0
            time_list[1] += 1
            if time_list[1] >= 60:
                time_list[1] = 0
                time_list[0] += 1
                if time_list[1] >= 24:
                    time_list[0] = 0
        return time_list

    @staticmethod
    def _correction_of_time(number):
        if number >= 10:
            return str(number)
        else:
            return "0" + str(number)


    def _parsing_input(self, input_data):
        """
        input_data: string
            format - BBBBxNNxHH:MM:SS.zhqxGGCR
            BBBB - number of sportsmen
            x - whitespace symbol
            NN - id chanel
            HH - hours
            MM - minutes
            SS - seconds
            zhq - tenths hundredths thousandths
            GG - number of group
            CR - close symbol
        :return:
        """
        try:
            number, chanel, time, group = input_data.split(" ")
            final_time = self._formatting_the_time_string(time)
            return "спортсмен, нагрудный номер {0}, прошёл отсечку {1} в {2}:{3}:{4}".format(
                number, chanel, self._correction_of_time(final_time[0]), self._correction_of_time(final_time[1]),
                self._correction_of_time(final_time[2])), group.split("[")[0]
        except ValueError:
            return "Value Error", None

