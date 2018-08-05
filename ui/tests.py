import json
from datetime import datetime
from unittest.mock import Mock

import django
import os
from django.test import TestCase

os.environ['DJANGO_SETTINGS_MODULE'] = 'app.settings'
django.setup()
# Create your tests here.
from ui.models import Message
from ui.views import messages


class MessagesTest(TestCase):
    def setUp(self):
        Message.objects.all().delete()
        Message.objects.create(bearId='bear2',
                               message='I was here first',
                               timestamp=datetime(2018,8,5,12,13,14))

    def test_messages_with_post_adds_message_to_list(self):
        # Arrange
        request = Mock(method='POST',
                       body='{"bearId":"growling test bear",'
                            '"message":"i am a test"}')

        # Act
        messages(request)

        # Assert
        test_msg = Message.objects.get(bearId='growling test bear')
        self.assertEqual('i am a test', test_msg.message)

    def test_messages_with_get_returns_all_messages(self):
        # Arrange
        request = Mock(method='GET')

        # Act
        result = messages(request)

        # Assert
        json_content = json.loads(result.content)
        self.assertEqual('I was here first', json_content[0]['message'])
