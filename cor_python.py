class ExpenseRequest:
    def __init__(self, amount, purpose):
        self.amount = amount
        self.purpose = purpose


class Handler:
    def __init__(self, successor=None):
        self.successor = successor

    def handle_request(self, request):
        if self.successor:
            self.successor.handle_request(request)


class TeamLeadHandler(Handler):
    MAX_LIMIT = 1000

    def handle_request(self, request):
        if request.amount <= self.MAX_LIMIT:
            print(f"Team Lead approved expense request for {request.purpose}")
        else:
            print(f"Team Lead cannot approve. Escalating to Manager.")
            super().handle_request(request)


class ManagerHandler(Handler):
    MAX_LIMIT = 5000

    def handle_request(self, request):
        if request.amount <= self.MAX_LIMIT:
            print(f"Manager approved expense request for {request.purpose}")
        else:
            print(f"Manager cannot approve. Escalating to Finance Manager.")
            super().handle_request(request)


class FinanceManagerHandler(Handler):
    MAX_LIMIT = 10000

    def handle_request(self, request):
        if request.amount <= self.MAX_LIMIT:
            print(f"Finance Manager approved expense request for {request.purpose}")
        else:
            print(f"Finance Manager cannot approve. Request denied.")


# Client code
if __name__ == "__main__":
    team_lead = TeamLeadHandler()
    manager = ManagerHandler()
    finance_manager = FinanceManagerHandler()

    team_lead.successor = manager
    manager.successor = finance_manager

    # Test with different expense requests
    expense_request_1 = ExpenseRequest(800, "Office supplies")
    expense_request_2 = ExpenseRequest(3500, "Business travel")
    expense_request_3 = ExpenseRequest(12000, "Equipment purchase")

    team_lead.handle_request(expense_request_1)
    print("------")
    team_lead.handle_request(expense_request_2)
    print("------")
    team_lead.handle_request(expense_request_3)
