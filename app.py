class Bank:
    """
    A class representing a bank with a class variable for its name
    and a class method to change that name.
    """
    bank_name = "Default National Bank"  # Class variable

    def __init__(self, branch_id):
        """
        Initializes a Bank instance with a branch ID.

        Args:
            branch_id (str): The unique identifier for the bank branch.
        """
        self.branch_id = branch_id

    @classmethod
    def change_bank_name(cls, new_name):
        """
        Class method to change the bank's name.
        This change will be reflected across all instances.

        Args:
            cls: Refers to the class itself (Bank in this case).
            new_name (str): The new name for the bank.
        """
        cls.bank_name = new_name
        print(f"\nBank name has been changed to: {cls.bank_name}")

    def display_branch_info(self):
        """
        Displays the branch ID and the current bank name.
        """
        print(f"Branch ID: {self.branch_id}, Bank Name: {Bank.bank_name}")

# Create instances of the Bank class
branch1 = Bank("B101")
branch2 = Bank("B202")
branch3 = Bank("B303")

print("--- Initial Bank Information ---")
branch1.display_branch_info()
branch2.display_branch_info()
branch3.display_branch_info()

# Change the bank name using the class method
Bank.change_bank_name("Global Financial Holdings")

print("\n--- Bank Information After Name Change ---")
# Show that the change affects all instances
branch1.display_branch_info()
branch2.display_branch_info()
branch3.display_branch_info()

# Create a new instance after the name change
branch4 = Bank("B404")
print("\n--- New Instance After Name Change ---")
branch4.display_branch_info()