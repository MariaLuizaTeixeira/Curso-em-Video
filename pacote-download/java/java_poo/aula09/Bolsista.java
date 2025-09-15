package aula09;
public class Bolsista extends Aluno {
    // Atributos
    private float bolsa;

    // Getters e setters
    public float getBolsa() {
        return bolsa;
    }

    public void setBolsa(float bolsa) {
        this.bolsa = bolsa;
    }

    // Métodos
    public void renovarBolsa() {
        System.out.println("Renovando bolsa de " + getNome());
    }

    @Override
    public void pagarMensalidade() {
        System.out.println(getNome() + " é bolsista! Pagamento facilitado.");
    }
}


