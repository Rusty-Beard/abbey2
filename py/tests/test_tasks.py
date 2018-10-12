import unittest
from unittest.mock import patch
import ctl.tasks
from app import app


class TasksViewTestCase(unittest.TestCase):
    @patch('ctl.tasks.flask')
    @patch('dao.utils.mysql')
    def test_connect_to_database(self, mysql_connector, flask):
        with app.app_context():
            mysql_connector.connect().cursor().fetchone.return_value = None
            ctl.tasks.task_view('')
            self.assertTrue(flask.abort.called)


if __name__ == '__main__':
    unittest.main()
