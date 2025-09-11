package aula04;
public class Index {
    public static void main(String[] args) {
        Banco conta1 = new Banco(01);
        conta1.abrirConta();
        conta1.depositar();
        conta1.sacar();
        conta1.fecharConta();

    }
}