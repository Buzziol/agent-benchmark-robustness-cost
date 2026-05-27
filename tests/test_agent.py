from src.agent import RetailSupportAgent


def test_order_status_intent():
    agent = RetailSupportAgent()
    response = agent.answer("Quero saber o status do meu pedido.")
    assert response.intent == "order_status"


def test_refund_intent():
    agent = RetailSupportAgent()
    response = agent.answer("Quero reembolso do produto.")
    assert response.intent == "refund"


def test_change_address_intent():
    agent = RetailSupportAgent()
    response = agent.answer("Preciso alterar meu endereco.")
    assert response.intent == "change_address"


def test_unknown_intent():
    agent = RetailSupportAgent()
    response = agent.answer("Tenho uma duvida aleatoria.")
    assert response.intent == "unknown"
