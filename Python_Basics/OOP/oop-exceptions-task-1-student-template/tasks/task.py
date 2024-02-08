class MissingPageError(Exception):
    pass


class SymbolWordMissingError(Exception):
    pass


class Pagination:

    def __init__(self, text, symbols_per_page):
        self.text = text
        self.symbols_per_page = symbols_per_page
        self.item_count = len([char for char in self.text if char != ''])
        self.page_count = self.calculate_page_count()

    def calculate_page_count(self):
        return -(-self.item_count // self.symbols_per_page)  # Ceiling division

    def count_items_on_page(self, page_number):
        if page_number >= self.page_count:
            raise MissingPageError("Invalid index. Page is missing")
        start_index = page_number * self.symbols_per_page
        end_index = min((page_number + 1) * self.symbols_per_page, self.item_count)
        return end_index - start_index

    def find_page(self, symbol_or_word):
        if symbol_or_word not in self.text:
            raise SymbolWordMissingError(f"'{symbol_or_word}' is missing on the pages")

        occurrences = [i for i in range(len(self.text)) if self.text.startswith(symbol_or_word, i)]
        pages_with_occurrences = set()

        for occurrence in occurrences:
            start_page = occurrence // self.symbols_per_page
            end_page = (occurrence + len(symbol_or_word) - 1) // self.symbols_per_page
            pages_with_occurrences.update(range(start_page, end_page + 1))

        return list(pages_with_occurrences)

    def display_page(self, page_number):
        if page_number >= self.page_count:
            raise MissingPageError("Invalid index. Page is missing")
        start_index = page_number * self.symbols_per_page
        end_index = min((page_number + 1) * self.symbols_per_page, self.item_count)
        return self.text[start_index:end_index]


# Example usage:
pages = Pagination('Your beautiful text', 5)
print(pages.page_count)
print(pages.item_count)

print(pages.count_items_on_page(0))
print(pages.count_items_on_page(3))

try:
    pages.count_items_on_page(4)
except Exception as e:
    print(e)

print(pages.find_page('Your'))  # Output: [0]
print(pages.find_page('e'))  # Output: [1, 3]
print(pages.find_page('beautiful'))

try:
    pages.find_page('great')
except Exception as e:
    print(e)

print(pages.display_page(0))  # Output: 'Your '
