package aula10;
public class Peixe extends Animal{
    // Atributos
    private char corEscama;

    // Getters e setters
    public char getCorEscama() {
        return corEscama;
    }

    public void setCorEscama(char corEscama) {
        this.corEscama = corEscama;
    }
    
    // Métodos
    @Override
    public void locomover() {
        System.out.println("Nadando.");
    }

    @Override
    public void alimentar() {
        System.out.println("Comendo substâncias.");
    }

    @Override
    public void emitirSom() {
        System.out.println("Peixe não faz som.");
    }

    public void soltarBolha() {
        System.out.println("Soltou uma bolha.");
    }
}
