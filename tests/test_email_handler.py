import pytest
from application import send_message, create_message



class TestCreateMessage:
    def test_create_message_basic(self):
        sender = "sender@example.com"
        to = "recipient@example.com"
        subject = "Test Subject"
        message_text = "This is a test message."
        
        result = create_message(sender, to, subject, message_text)
        
        assert isinstance(result, dict)
        assert 'raw' in result
        assert isinstance(result['raw'], str)
    
    def test_create_message_empty_fields(self):
        sender = ""
        to = ""
        subject = ""
        message_text = ""
        
        result = create_message(sender, to, subject, message_text)
        
        assert isinstance(result, dict)
        assert 'raw' in result
        assert isinstance(result['raw'], str)
    
    def test_create_message_special_characters(self):
        sender = "sender@example.com"
        to = "recipient@example.com"
        subject = "Test Subject with ñ and 漢字"
        message_text = "This is a test message with special characters: áéíóú 你好"
        
        result = create_message(sender, to, subject, message_text)
        
        assert isinstance(result, dict)
        assert 'raw' in result
        assert isinstance(result['raw'], str)
    
    def test_create_message_long_content(self):
        sender = "sender@example.com"
        to = "recipient@example.com"
        subject = "A" * 1000  # Very long subject
        message_text = "B" * 10000  # Very long message
        
        result = create_message(sender, to, subject, message_text)
        
        assert isinstance(result, dict)
        assert 'raw' in result
        assert isinstance(result['raw'], str)
    
    def test_create_message_multiple_recipients(self):
        sender = "sender@example.com"
        to = "recipient1@example.com, recipient2@example.com"
        subject = "Test Subject"
        message_text = "This is a test message."
        
        result = create_message(sender, to, subject, message_text)
        
        assert isinstance(result, dict)
        assert 'raw' in result
        assert isinstance(result['raw'], str)
