from etapa import Etapa

class EtapaFundacao(Etapa):
    """ Classe filha para etapas de fundação. Demonstra Herança. """
    def __init__(self, titulo, descricao, data_entrega, tipo_solo):
        super().__init__(titulo, descricao, data_entrega)
        self.tipo_solo = tipo_solo

    def exibir_detalhes(self):
        """
        POLIMORFISMO:
        Este método sobrescreve o 'exibir_detalhes' da classe-pai.
        """
        resp = self.responsavel.nome if self.responsavel else "Ninguém"
        print(f"\n  [ETAPA FUNDAÇÃO] {self.titulo} ({self.status})")
        print(f"    Tipo de Solo: {self.tipo_solo} | Responsável: {resp}")
        print(f"    Entrega: {self.data_entrega} | Descrição: {self.descricao}")

class EtapaAcabamento(Etapa):
    """ Outra classe filha para etapas de acabamento. """
    def __init__(self, titulo, descricao, data_entrega, material_principal):
        super().__init__(titulo, descricao, data_entrega)
        self.material_principal = material_principal

    def exibir_detalhes(self):
        """ POLIMORFISMO: Outra implementação do método. """
        resp = self.responsavel.nome if self.responsavel else "Ninguém"
        print(f"\n  [ETAPA ACABAMENTO] {self.titulo} ({self.status})")
        print(f"    Material: {self.material_principal} | Responsável: {resp}")
        print(f"    Entrega: {self.data_entrega} | Descrição: {self.descricao}")