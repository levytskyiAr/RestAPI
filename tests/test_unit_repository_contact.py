import unittest
from unittest.mock import MagicMock, AsyncMock, Mock
from sqlalchemy.ext.asyncio import AsyncSession

from src.models.model import Contact, User
from src.dto.contact import ContactSchema, ContactUpdateSchema
from src.repository.contact import create_contact, get_contact, update_contact, delete_contact, get_contacts


class TestAsyncContact(unittest.IsolatedAsyncioTestCase):

    def setUp(self) -> None:
        self.user = User(id=1, username='test_user', password="qwerty", confirmed=True)
        self.session = AsyncMock(spec=AsyncSession)

    async def test_get_contacts(self):
        contacts = [Contact(id=1, name='test_name_1', last_name='test_l_name_1',email='test_email_1',phone='test_phone_1',birthday='test_birthday_1')]
        mocked_contact = Mock()
        mocked_contact.scalars.return_value.all.return_value = contacts
        self.session.execute.return_value = mocked_contact
        result = await get_contacts(self.session)
        self.assertEqual(result, contacts)

    async def test_get_contact(self):
        contact = [Contact(id=1, name='test_name_1', last_name='test_l_name_1',email='test_email_1',phone='test_phone_1',birthday='test_birthday_1', user=self.user)]
        mocked_contact = MagicMock()
        mocked_contact.scalar_one_or_none.return_value = contact
        self.session.execute.return_value = mocked_contact
        result = await get_contact(1, self.session)
        self.assertEqual(result, contact)