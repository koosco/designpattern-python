if __name__ == '__main__':
    from builder import Builder
    from concrete_builder1 import ConcreteBuilder1
    from director import Director

    director = Director()
    builder = ConcreteBuilder1()
    director.builder = builder

    print('Standard basic product: ')
    director.build_minimal_viable_product()
    builder.product.list_parts()

    print()

    print('Standard full featured product')
    director.build_full_featured_product()
    builder.product.list_parts()
