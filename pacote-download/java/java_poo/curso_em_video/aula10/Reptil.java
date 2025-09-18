package aula10;
public class Reptil extends Animal{
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
        System.out.println("Ratejando.");
    }

    @Override
    public void alimentar() {
        System.out.println("Comedno vegetais.");
    }

    @Override
    public void emitirSom() {
        System.out.println("Som de réptil.");
    }
}
