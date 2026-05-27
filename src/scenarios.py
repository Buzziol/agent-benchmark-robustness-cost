SCENARIOS = [
    {
        "id": "S01",
        "message": "Quero saber o status do meu pedido 1234.",
        "expected_intent": "order_status",
        "type": "normal",
    },
    {
        "id": "S02",
        "message": "Meu produto nao chegou ainda, consegue ver o rastreio?",
        "expected_intent": "order_status",
        "type": "normal",
    },
    {
        "id": "S03",
        "message": "Comprei errado e quero meu dinheiro de volta.",
        "expected_intent": "refund",
        "type": "normal",
    },
    {
        "id": "S04",
        "message": "Preciso devolver o produto porque veio com defeito.",
        "expected_intent": "refund",
        "type": "normal",
    },
    {
        "id": "S05",
        "message": "Coloquei o endereco errado na compra.",
        "expected_intent": "change_address",
        "type": "normal",
    },
    {
        "id": "S06",
        "message": "Tem como mudar onde vai ser entregue?",
        "expected_intent": "change_address",
        "type": "ambiguous",
    },
    {
        "id": "S07",
        "message": "O negocio la da compra, queria resolver isso.",
        "expected_intent": "unknown",
        "type": "ambiguous",
    },
    {
        "id": "S08",
        "message": "Meu pedido sumiu, quero cancelar ou saber se chega.",
        "expected_intent": "order_status",
        "type": "ambiguous",
    },
]
