from django.test import TestCase
from .models import Menu, Booking


class MenuModelTest(TestCase):
    def test_menu_creation(self):
        menu = Menu.objects.create(name="Pizza", price=10.99)
        self.assertEqual(menu.name, "Pizza")
        self.assertEqual(menu.price, 10.99)


class BookingModelTest(TestCase):
    def test_booking_creation(self):
        booking = Booking.objects.create(
            customer_name="John Doe", table_number=5, booking_time="2024-11-07 19:00:00"
        )
        self.assertEqual(booking.customer_name, "John Doe")
