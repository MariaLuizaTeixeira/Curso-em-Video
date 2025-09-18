public class Teste {
public static void main(String[] args) {
    Cliente cliente1 = new Cliente("x", TipoCliente.PESSOA_FISICA, TipoPagamento.CREDITO);
    Cliente cliente2 = new Cliente("x", TipoCliente.PESSOA_JURIDICA, TipoPagamento.CREDITO);
    Cliente cliente3 = new Cliente("x", TipoCliente.PESSOA_FISICA, TipoPagamento.DEBITO);
    System.out.println(cliente1);
    System.out.println(cliente2);
    System.out.println(cliente3);

    System.out.println(TipoPagamento.DEBITO.cancularDesconto(100));
    System.out.println(TipoPagamento.CREDITO.cancularDesconto(100));

   // TipoCliente tipoCliente = TipoCliente.valuesOf("Pessoa Física");
}
}
