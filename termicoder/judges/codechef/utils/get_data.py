from datetime import datetime
from ....utils.logging import logger


def running_contests(self):
    r = self._request_api(self._make_url('contests'))
    data = r['result']['data']['content']
    contest_list = data['contestList']
    current_time = datetime.fromtimestamp(data['currentTime'])

    def check_current(contest):
        contest_time = datetime.strptime(
            contest['endDate'], '%Y-%m-%d %H:%M:%S')
        return contest_time >= current_time

    running = list(filter(check_current, contest_list))
    logger.debug("got running")

    return running
