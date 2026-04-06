"""test_product.py with tests for Product class"""

def test_product_init(product):
    assert product.name == "test_product"
    assert product.description == "test_product description"
    assert product.price == 321
    assert product.quantity == 123
