# Sky.ecommerce

## About the project
A training project - implementing e-shop core functionality

### Build with
* [![Python](https://img.shields.io/badge/Python%20IDLE-3776AB?logo=python&logoColor=fff)](https://python.org/)
* [![PyCharm](https://img.shields.io/badge/PyCharm-000?logo=pycharm&logoColor=fff)](https://www.jetbrains.com/pycharm/)

## Getting started
To clone the repository use the following links:

* with HTTPS:
```
    https://github.com/tray-46/Sky.pro-ecommerce.git
```

* with SSH:  
```
    git@github.com:tray-46/Sky.pro-ecommerce.git
```

To run the application, execute main.py module.

## Usage
Project has definition of classes:  
BaseProduct - abstract class for products;  
Product - class for representation of a product (subclass of BaseProduct);  
Smartphone - class for representation of a smartphone (subclass of Product);  
LawnGrass - class for representation of a lawn grass (subclass of Product);  

BaseProductsGroup - abstract class for products groups;  
Category - class for representation of a category of products (subclass of BaseProductsGroup);  
ShopOrder - class for representation of a shop order (subclass of BaseProductsGroup);  
ProductIterator - support class for iterating through Category object product list.  

PrintMixin - mixin class for printing object's class and parameters during creation  
ZeroQuantityProductError - custom exception for processing product additions

The following functions are implemented in the project:
1. function for creating and setting up logger:  
`get_logger`
2. function for loading data from JSON file  
`load_json`
3.  function for creating list of Product instances   
`create_products`
4. function for creating list of Category instances  
`create_categories`
5. function for loading categories data from JSON file, and creating list of Category objects  
`load_categories`
