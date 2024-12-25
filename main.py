import example  # Импортируем скомпилированный модуль


class ExampleModule:
    @staticmethod
    def add(a: int, b: int) -> int:
        """sum a+b

        Args:
            a (int): a
            b (int): b

        Returns:
            int: sum
        """
        return example.add(a, b)


print(ExampleModule.add(5, 5))
