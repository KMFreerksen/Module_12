class County:
    """A Class to hold demographic data for each county in Iowa"""
    def __init__(self, rank, name, pci, mhi, mfi, pop, noh):
        self.rank = rank
        self.county = name
        self.per_capita_income = pci
        self.median_household_income = mhi
        self.median_family_income = mfi
        self.population = pop
        self.number_of_households = noh
