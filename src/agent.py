from dataclasses import dataclass


@dataclass
class AgentResponse:
    intent: str
    action: str
    message: str
    turns: int
    estimated_tokens: int


class RetailSupportAgent:
    """
    Agente simples de atendimento para varejo.

    O objetivo nao e substituir um LLM real, mas criar um prototipo minimo
    para avaliar comportamento, robustez e custo estimado em cenarios controlados.
    """

    def answer(self, user_message: str) -> AgentResponse:
        text = user_message.lower()
        estimated_tokens = self._estimate_tokens(user_message)

        if any(word in text for word in ["status", "rastreio", "entrega", "pedido", "atraso", "encomenda", "chegou"]):
            return AgentResponse(
                intent="order_status",
                action="check_order_status",
                message="Consultei o pedido e retornei o status de entrega.",
                turns=1,
                estimated_tokens=estimated_tokens + 45,
            )

        if any(word in text for word in ["reembolso", "devolver", "dinheiro", "cancelar", "defeito", "quebrado", "troca"]):
            return AgentResponse(
                intent="refund",
                action="start_refund_process",
                message="Iniciei o fluxo de reembolso conforme a politica da loja.",
                turns=2,
                estimated_tokens=estimated_tokens + 70,
            )

        if any(word in text for word in ["endereco", "endereço", "mudar", "alterar", "local", "onde", "entregar"]):
            return AgentResponse(
                intent="change_address",
                action="update_delivery_address",
                message="Solicitei os dados necessarios para alterar o endereco de entrega.",
                turns=2,
                estimated_tokens=estimated_tokens + 65,
            )

        return AgentResponse(
            intent="unknown",
            action="ask_clarification",
            message="Nao entendi completamente a solicitacao. Poderia fornecer mais detalhes?",
            turns=3,
            estimated_tokens=estimated_tokens + 55,
        )

    @staticmethod
    def _estimate_tokens(text: str) -> int:
        return max(1, len(text) // 4)
