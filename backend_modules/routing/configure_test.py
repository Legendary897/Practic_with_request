from flask import render_template, Blueprint
from backend_modules.content.parsing_info import CreatorInfo
from backend_modules.content.save_info import WriteData
from backend_modules.check.checker_list import CheckerParticipants

application_routing = Blueprint("application_routing", __name__)

log_file = "participants.txt"
list_data_to_view = CheckerParticipants(log_file).init_list()


@application_routing.route('/')
@application_routing.route('/index')
def index():
    return render_template('index.html')


@application_routing.route('/add_info/<info>', methods=['GET', 'POST'])
def add_info(info):
    data_to_view, group = CreatorInfo().create_output_data(info)
    if group is None:
        return "Fail"
    else:
        if group == "00":
            list_data_to_view.append(data_to_view)
        WriteData().write_data_into_file(data_to_view, group, log_file)
    return "Ok"


@application_routing.route('/get_info', methods=['GET', 'POST'])
def get_info():
    return {"data": list_data_to_view}
