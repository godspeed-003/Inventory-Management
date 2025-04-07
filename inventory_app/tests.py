from django.test import TestCase
from .inventory import InventoryManager

class InventoryManagerTests(TestCase):
    def setUp(self):
        self.manager = InventoryManager()
        self.manager.add_product(1, 'Test Product', 10, 5.0)

    def test_add_product(self):
        result = self.manager.add_product(2, 'Another Product', 5, 10.0)
        self.assertTrue(result)
        self.assertIn(2, self.manager.products)

    def test_add_duplicate_product(self):
        result = self.manager.add_product(1, 'Duplicate Product', 5, 10.0)
        self.assertFalse(result)

    def test_update_quantity(self):
        result = self.manager.update_quantity(1, 20)
        self.assertTrue(result)
        self.assertEqual(self.manager.get_product(1).quantity, 20)

    def test_update_nonexistent_product(self):
        result = self.manager.update_quantity(999, 10)
        self.assertFalse(result)

    def test_remove_product(self):
        result = self.manager.remove_product(1)
        self.assertTrue(result)
        self.assertNotIn(1, self.manager.products)

    def test_remove_nonexistent_product(self):
        result = self.manager.remove_product(999)
        self.assertFalse(result)

    def test_list_products(self):
        products = self.manager.list_products()
        self.assertEqual(len(products), 1)
        self.assertEqual(products[0]['id'], 1)

    def test_get_total_inventory_value(self):
        total_value = self.manager.get_total_inventory_value()
        self.assertEqual(total_value, 50.0)  # 10 quantity * 5.0 price