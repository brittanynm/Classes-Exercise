"""Classes for melon orders."""
import random, datetime

class AbstractMelonOrder():

    def __init__(self, species, qty, country_type, tax):
        self.species = species
        self.qty = qty
        self.shipped = False
        self.order_type = country_type
        self.tax = tax
        #Throw melon error
        if qty > 100:
            raise TooManyMelonsError('No more than 100 melons!')

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True

    def get_total(self):
        """Calculate price, including tax."""

        base_price = self.get_base_price()

        if self.species == 'christmas':
            base_price *= 1.5

        total = (1 + self.tax) * self.qty * base_price

        if self.order_type == 'international' and self.qty < 10:
            total += 3
        
        return total

    def get_base_price(self):
        weekdays = [range(0, 5)]
        morning = [range(8, 12)]
        date_now = datetime.datetime.today()
        base_price = random.randint(5,9)
        if date_now.weekday() in weekdays and date_now.hour in morning:
            base_price += 4
        print(f'Day: {date_now.weekday()}') 
        print(f'Hour: {date_now.hour}')
        return base_price


class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""
    # country_type = 'domestic'

    def __init__(self, species, qty):
        """Initialize melon order attributes."""
        super().__init__(species, qty, 'domestic', 0.08)


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes."""
        super().__init__(species, qty, 'international', 0.17)
        self.country_code = country_code

    def get_country_code(self):
        """Return the country code."""

        return self.country_code


class GovernmentMelonOrder(AbstractMelonOrder):

    def __init__(self, species, qty):
        super().__init__(self, species, qty, 'government', 0)
        self.passed_inspection = False

    def mark_inspection(passed):
        if passed:
            self.passed_inspection = True

class TooManyMelonsError(ValueError):
    __module__ = ''

toomanymelons = many_melons = DomesticMelonOrder('cantaloupe', 101)