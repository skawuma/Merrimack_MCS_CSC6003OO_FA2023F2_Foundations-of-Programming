class Account:
    """
    Base class for a bank account.

    Attributes:
    - account_number: str
        The account number associated with the account.
    - balance: float
        The current balance of the account.

    Methods:
    - deposit(amount: float) -> None:
        Deposits the specified amount into the account.
    - withdraw(amount: float) -> None:
        Withdraws the specified amount from the account.
    - calculate_interest() -> float:
        Calculates the interest earned on the account.
    """

    def __init__(self, account_number: str, balance: float = 0.0):
        """
        Constructor to instantiate the Account class.

        Parameters:
        - account_number: str
            The account number associated with the account.
        - balance: float, optional (default: 0.0)
            The initial balance of the account.
        """

        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount: float) -> None:
        """
        Deposits the specified amount into the account.

        Parameters:
        - amount: float
            The amount to be deposited.

        Returns:
        - None
        """

        self.balance += amount

    def withdraw(self, amount: float) -> None:
        """
        Withdraws the specified amount from the account.

        Parameters:
        - amount: float
            The amount to be withdrawn.

        Returns:
        - None

        Raises:
        - ValueError:
            Raises an error if the withdrawal amount exceeds the account balance.
        """

        if amount > self.balance:
            raise ValueError("Insufficient balance.")
        self.balance -= amount

    def calculate_interest(self) -> float:
        """
        Calculates the interest earned on the account.

        Returns:
        - float:
            The interest earned on the account.
        """

        # Placeholder implementation, can be overridden in subclasses
        return 0.0


class SavingsAccount(Account):
    """
    Subclass of Account representing a savings account.

    Methods:
    - calculate_interest() -> float:
        Calculates the interest earned on the savings account.

    Attributes:
    - interest_rate: float
        The interest rate for the savings account.
    """

    def __init__(self, account_number: str, balance: float = 0.0, interest_rate: float = 0.0):
        """
        Constructor to instantiate the SavingsAccount class.

        Parameters:
        - account_number: str
            The account number associated with the account.
        - balance: float, optional (default: 0.0)
            The initial balance of the account.
        - interest_rate: float, optional (default: 0.0)
            The interest rate for the savings account.
        """

        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

    def calculate_interest(self) -> float:
        """
        Calculates the interest earned on the savings account.

        Returns:
        - float:
            The interest earned on the savings account.
        """

        return self.balance * self.interest_rate


class CheckingAccount(Account):
    """
    Subclass of Account representing a checking account.

    Attributes:
    - transaction_fee: float
        The transaction fee for the checking account.
    """

    def __init__(self, account_number: str, balance: float = 0.0, transaction_fee: float = 0.0):
        """
        Constructor to instantiate the CheckingAccount class.

        Parameters:
        - account_number: str
            The account number associated with the account.
        - balance: float, optional (default: 0.0)
            The initial balance of the account.
        - transaction_fee: float, optional (default: 0.0)
            The transaction fee for the checking account.
        """

        super().__init__(account_number, balance)
        self.transaction_fee = transaction_fee

    def withdraw(self, amount: float) -> None:
        """
        Withdraws the specified amount from the checking account.

        Parameters:
        - amount: float
            The amount to be withdrawn.

        Returns:
        - None

        Raises:
        - ValueError:
            Raises an error if the withdrawal amount exceeds the account balance plus the transaction fee.
        """

        if amount > self.balance + self.transaction_fee:
            raise ValueError("Insufficient balance.")
        self.balance -= amount + self.transaction_fee